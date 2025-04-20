from timeline_landmark import Landmark
from datetime import datetime
import bisect
import math
import numpy
from timeline_year import Year
import json


class Timeline:
    def __init__(self):
        self.start: datetime = datetime(4000, 1, 1)
        self.end: datetime = datetime(1, 1, 1)
        self.landmarks = []
        self.smallest_gap = 1000
        self.gradient = 1000
        self.range = 0
        self.timeline = []
        self.outlier_threshold = 3
        self.negative_outliers = []
        self.positive_outliers = []
        self.column_tracker = 1

    def __str__(self):
        return_string = f'start: {self.start.strftime("%Y %b")}, end: {self.end.strftime("%Y %b")}\n' \
                        f'range: {self.range} years. smallest gap: {self.smallest_gap}.'
        for date in self.timeline:
            return_string += f"\n {date.strftime('%Y %b')}"
        return_string += f'\ngradient: {self.gradient}'
        return return_string

    def update_start_end(self, date):
        if self.start > date:
            self.start = date
        if self.end < date:
            self.end = date

    def update_gap(self, index):
        date = self.landmarks[index].date
        lower_gap = 1000000
        upper_gap = 1000000
        lower_neighbor = index - 1
        upper_neighbor = index + 1
        while lower_neighbor >= 0:
            if self.landmarks[lower_neighbor].date.year == date.year:
                lower_neighbor -= 1
            else:
                lower_gap = date.year - self.landmarks[lower_neighbor].date.year
                break
        while upper_neighbor < len(self.landmarks):
            if self.landmarks[upper_neighbor].date.year == date.year:
                upper_neighbor += 1
            else:
                upper_gap = self.landmarks[upper_neighbor].date.year - date.year
                break
        local_smallest_gap = min(lower_gap, upper_gap)
        self.smallest_gap = min(self.smallest_gap, local_smallest_gap)

    def update_range(self):
        self.range = self.end.year - self.start.year

    def update_gradient(self):
        self.gradient = math.gcd(self.range, self.smallest_gap)

    def add_landmark(self, landmark):
        insertion_index = bisect.bisect(self.landmarks, landmark)
        self.landmarks.insert(insertion_index, landmark)
        self.update_start_end(landmark.date)
        if len(self.landmarks) == 0:
            self.gradient = 1
        else:
            self.update_gap(insertion_index)
            self.update_range()
            self.update_gradient()

    def detach_negative_outliers(self, mean, std):
        outlier = True
        while outlier:
            landmark = self.landmarks[0]
            x = landmark.date
            z_score = (x.year - mean) / std
            landmark.z_score = -1 * round(z_score)
            if z_score <= -self.outlier_threshold:
                self.negative_outliers.append(self.landmarks.pop(0))
            else:
                outlier = False

    def detach_positive_outliers(self, mean, std):
        outlier = True
        while outlier:
            landmark = self.landmarks[-1]
            x = landmark.date
            z_score = (x.year - mean) / std
            landmark.z_score = round(z_score)
            if z_score >= self.outlier_threshold:
                self.positive_outliers.insert(0, self.landmarks.pop(-1))
            else:
                outlier = False

    def detach_outliers(self):
        mean = numpy.mean([x.date.year for x in self.landmarks])
        std = round(numpy.std([x.date.year for x in self.landmarks]), 0)
        self.detach_negative_outliers(mean, std)
        self.detach_positive_outliers(mean, std)

    def generate_span(self, start_year, real_year, distance, real_distance, z_score_difference):
        coefficient = 1
        cumulative_value = 1
        max_value = 2 + z_score_difference
        while cumulative_value > 0:
            if cumulative_value == max_value:
                new_year = Year(year=start_year + cumulative_value * self.gradient,
                             end_year=start_year + distance - cumulative_value * self.gradient,
                             placeholder=True, span=True)
                new_year.x_coordinate = self.column_tracker
                self.column_tracker += 3
                new_year.real_year = real_year + cumulative_value * self.gradient
                new_year.real_end_year = real_year + real_distance - cumulative_value * self.gradient
                self.timeline.append(new_year)
                coefficient = -1
            else:
                if coefficient > 0:
                    new_year = Year(year=start_year + cumulative_value * self.gradient, placeholder=True)
                    new_year.x_coordinate = self.column_tracker
                    self.column_tracker += 1
                    new_year.real_year = real_year + cumulative_value * self.gradient
                    self.timeline.append(new_year)
                else:
                    new_year = Year(year=start_year + distance - cumulative_value * self.gradient, placeholder=True)
                    new_year.real_year = real_year + real_distance - cumulative_value * self.gradient
                    new_year.x_coordinate = self.column_tracker
                    self.column_tracker += 1
                    self.timeline.append(new_year)
            cumulative_value += coefficient

    def re_evaluate_outliers(self):
        # negative outliers
        for i in range(len(self.negative_outliers)-1, -1, -1):
            landmark = self.negative_outliers[i]
            if i == len(self.negative_outliers)-1:
                following_year = self.landmarks[0].date.year
            else:
                following_year = self.negative_outliers[i+1].real_date.year
            distance = following_year - landmark.real_date.year
            if distance < 7:
                if i == len(self.negative_outliers)-1:
                    new_year = following_year - distance
                else:
                    new_year = self.negative_outliers[i+1].date.year - distance
                landmark.date = datetime(new_year, landmark.date.month, landmark.date.day)
            else:
                if i == len(self.negative_outliers)-1:
                    new_year = following_year - 8 - landmark.z_score - math.floor(abs(landmark.z_score)/2)
                else:
                    new_year = self.negative_outliers[i+1].date.year - 8 - landmark.z_score - math.floor(abs(landmark.z_score)/2)
                landmark.date = datetime(new_year, landmark.date.month, landmark.date.day)
        # positive outliers
        for i in range(len(self.positive_outliers)):
            landmark = self.positive_outliers[i]
            if i == 0:
                previous_year = self.landmarks[-1].date.year
            else:
                previous_year = self.positive_outliers[i-1].real_date.year
            distance = landmark.real_date.year - previous_year
            if distance < 7:
                if i == 0:
                    new_year = previous_year + distance
                else:
                    new_year = self.positive_outliers[i-1].date.year + distance
                landmark.date = datetime(new_year, landmark.date.month, landmark.date.day)
            else:
                if i == 0:
                    new_year = previous_year + 8 + landmark.z_score + math.floor(landmark.z_score/2)
                else:
                    new_year = self.positive_outliers[i-1].date.year + 8 + landmark.z_score
                landmark.date = datetime(new_year, landmark.date.month, landmark.date.day)

    def generate_timeline(self):
        self.detach_outliers()
        self.re_evaluate_outliers()
        self.update_gradient()
        self.landmarks = self.negative_outliers + self.landmarks + self.positive_outliers
        if len(self.landmarks) == 0:
            self.timeline = ['empty']
        elif len(self.timeline) == 1:
            only_date = self.landmarks[0].date
            only_year = Year(year=only_date.year, landmarks=[])
            only_year.real_year = self.landmarks[0].real_date.year
            only_year.x_coordinate = 1
            only_year.set_landmarks([self.landmarks[0]])
            self.timeline = [only_year]
        else:
            first_landmark: Landmark = self.landmarks[0]
            first_landmark.group_relationships()
            first_year = Year(year=first_landmark.date.year, landmarks=[first_landmark])
            first_year.real_year = first_landmark.real_date.year
            first_year.x_coordinate = self.column_tracker
            self.timeline = [first_year]
            timeline_index = 0
            for i in range(len(self.landmarks[1:])):
                landmark = self.landmarks[1:][i]
                landmark.group_relationships()
                distance = (landmark.date.year - self.timeline[timeline_index].year)
                if distance == 0:
                    self.timeline[timeline_index].landmarks.append(landmark)
                else:
                    self.timeline[timeline_index].generate_year_grid()
                    self.column_tracker += self.timeline[timeline_index].rightmost_column + 1
                    if 0 < distance <= 1 * self.gradient:
                        new_year = Year(year=landmark.date.year, landmarks=[landmark])
                        new_year.x_coordinate = self.column_tracker
                        new_year.real_year = landmark.real_date.year
                        self.timeline.append(new_year)
                        timeline_index += 1
                    elif 1 * self.gradient < distance <= 5 * self.gradient:
                        for j in range(1, distance, self.gradient):
                            if self.timeline[timeline_index].year + self.gradient >= landmark.date.year:
                                break
                            new_year = Year(year=self.timeline[timeline_index].year + self.gradient, placeholder=True)
                            new_year.x_coordinate = self.column_tracker
                            self.column_tracker += 1
                            new_year.real_year = self.timeline[timeline_index].real_year + self.gradient
                            self.timeline.append(new_year)
                            timeline_index += 1
                        new_year = Year(year=landmark.date.year, landmarks=[landmark])
                        new_year.x_coordinate = self.column_tracker
                        new_year.real_year = landmark.real_date.year
                        self.timeline.append(new_year)
                        timeline_index += 1
                    else:
                        if i == 0:
                            z_score_difference = abs(self.landmarks[0].z_score - landmark.z_score)
                        else:
                            z_score_difference = abs(landmark.z_score - self.landmarks[1:][i-1].z_score)
                        real_distance = landmark.real_date.year - self.timeline[timeline_index].real_year
                        self.generate_span(self.timeline[timeline_index].year, self.timeline[timeline_index].real_year,
                                        distance, real_distance, z_score_difference)
                        new_year = Year(year=landmark.date.year, landmarks=[landmark])
                        new_year.x_coordinate = self.column_tracker
                        new_year.real_year = landmark.real_date.year
                        self.timeline.append(new_year)
                        timeline_index += 4 + (z_score_difference*2)
                if i == len(self.landmarks[1:])-1:
                    self.timeline[timeline_index].generate_year_grid()
    
    def set_landmarks(self, landmarks):
        for landmark in landmarks:
            self.add_landmark(landmark)
        self.generate_timeline()

    def dump_data(self):
        landmark_dict = {
            'landmarks': []
        }
        for landmark in self.landmarks:
            landmark_dict['landmarks'].append(landmark.to_dict())
        # with open('F:\School and Work\jazz-time\data.json', 'w') as outfile:
        with open('/home/nickolasram/Coding/timeline-web/data.json', 'w') as outfile:
            json.dump(landmark_dict, outfile, indent=4)