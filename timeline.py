from timeline_landmark import Landmark, Size
from timeline_presentation import Presentation
from bisect import bisect_left, bisect_right
from datetime import datetime
import bisect
import math
import numpy
from timeline_year import Year
import json
import uuid


class YearIndex:
    def __init__(self, percentage, year):
        self.percentage = percentage
        self.year = year

    def __lt__(self, other):
        return self.percentage < other.percentage
    
class Thread:
    def __init__(self, landmark: Landmark):
        self.landmark = landmark
        self.id = landmark.id
        self.x = landmark.x_coordinate
        self.y = landmark.y_coordinate
    

    def generate_dict(self):
        base_x = self.landmark.x_coordinate + (math.floor(self.landmark.size.value['x']/2))
        base_y = self.landmark.y_coordinate + (math.floor(self.landmark.size.value['x']/2))
        min_x = base_x
        min_y = base_y
        max_x = base_x
        max_y = base_y
        related = self.landmark.relationships
        for relationship in related:
            nudge = math.floor(relationship.other.size.value['x']/2)
            related_x = relationship.other.x_coordinate + nudge
            related_y = relationship.other.y_coordinate + nudge
            if related_x < min_x:
                min_x = related_x
            if related_x > max_x:
                max_x = related_x
            if related_y < min_y:
                min_y = related_y
            if related_y > max_y:
                max_y = related_y
        vb_width = (max_x - min_x + 1)*10
        vb_height = (max_y - min_y + 1)*10
        x_nudge = 1 - min_x
        y_nudge = 1 - min_y
        if min_x == base_x:
            line_start = f'{(min_x + x_nudge) * 10 - 5} {(base_y + y_nudge) * 10 - 5}'
        else:
            line_start = f'{(min_x + x_nudge) * 10 + 5} {(base_y + y_nudge) * 10 - 5}'
        if max_x == base_x:
            line_end = f'{(max_x + x_nudge) * 10 - 5} {(base_y + y_nudge) * 10 - 5}'
        else:
            line_end = f'{(max_x + x_nudge) * 10 - 15} {(base_y + y_nudge) * 10 - 5}'
        # landmark_timeline = f'M{line_start}L{line_end}'

        # def defineCurve(provided_x, provided_y):
        #     if provided_y > base_y:
        #         curve_modifier = 40
        #         bezier_modifier = 10
        #     else:
        #         curve_modifier = -20
        #         bezier_modifier = 0
        #     if provided_x > base_x:
        #         curve_start = f'{(provided_x + x_nudge) * 10 - 5} {(base_y + y_nudge) * 10 - 5}'
        #     else:
        #         curve_start = f'{(provided_x + x_nudge) * 10 + 15} {(base_y + y_nudge) * 10 - 5}'
        #     curve_end_bezier_x = (provided_x + x_nudge)*10 + 5
        #     curve_start_bezier_x = curve_end_bezier_x
        #     curve_end_x = curve_end_bezier_x
        #     curve_end_y = provided_y * 10
        #     curve_start_bezier_y = base_y * 10 - 20 + bezier_modifier
        #     curve_end_bezier_y = curve_start_bezier_y + curve_modifier - 10
        #     return f'M{curve_start}C{curve_start_bezier_x} {curve_start_bezier_y} {curve_end_bezier_x} {curve_end_bezier_y} {curve_end_x} {curve_end_y}'
        landmark_timeline = ''
        for relationship in self.landmark.relationships:
        #     landmark_timeline += defineCurve(relationship.other.x_coordinate, relationship.other.y_coordinate)
            other_x_center = relationship.other.x_coordinate + (math.floor(relationship.other.size.value['x']/2))
            other_y_center = relationship.other.y_coordinate + (math.floor(relationship.other.size.value['x']/2))
            ll = 0
            if self.landmark.size.value['x'] == 3:
                ll = 6
            if self.landmark.size.value['x'] == 5:
                ll = 14
            if self.landmark.size.value['x'] == 7:
                ll = 21
            if other_x_center < base_x:
                ll = -6
            line_start = f'{(base_x + x_nudge) * 10 +ll} {(base_y + y_nudge) * 10 - 5}'
            line_end = f'{(other_x_center + x_nudge) * 10 - 5} {(other_y_center + y_nudge) * 10 - 5}'    
            landmark_timeline += f'M{line_start}L{line_end}'
        thread_as_dict = {
            'id': self.id,
            'className': f'col-start-{min_x} row-start-{min_y} col-end-{max_x+1} row-end-{max_y+1}',
            'viewbox': f'0 0 {vb_width} {vb_height}',
            'path': landmark_timeline,
            'color': self.landmark.color
        }
        return thread_as_dict


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
        self.title = 'Title'
        self.note = False
        self.citations = False
        self.authors = False
        self.id = str(uuid.uuid4())[:8] + str(uuid.uuid4())[:8]
        self.presentations = []
        self.presentations_summary = []

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
            # first_landmark.group_relationships(first_landmark.size.value['x'])
            first_year = Year(year=first_landmark.date.year, landmarks=[first_landmark])
            first_year.real_year = first_landmark.real_date.year
            first_year.x_coordinate = self.column_tracker
            self.timeline = [first_year]
            timeline_index = 0
            for i in range(len(self.landmarks[1:])):
                landmark = self.landmarks[1:][i]
                # landmark.group_relationships(landmark.size.value['x'])
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

    def to_dict(self):
        timeline_dict = {
            'meta': {
                'timelineTitle': self.title,
                'citations': self.citations,
                'note': self.note,
                'authors': self.authors,
                'id': self.id,
                'landmarkCount': len(self.landmarks),
                'columns': self.timeline[-1].rightmost_column + self.column_tracker,
                'svgColumns': f'col-end-{self.timeline[-1].rightmost_column + self.column_tracker + 1}'
            },
            'landmarks': [],
            'circles': [],
            'threads': [],
            'years': [],
            'yearsIndex': {},
            'presentations': self.presentations,
            'presentationsSummary': self.presentations_summary
        }
        default_presentation = Presentation()
        default_presentation.set_landmarks(self.landmarks)
        default_presentation_dict = default_presentation.to_dict()
        timeline_dict['presentations'].append(default_presentation_dict)
        timeline_dict['presentationsSummary'].append(default_presentation_dict['meta'])
        for landmark in self.landmarks:
            timeline_dict['landmarks'].append(landmark.to_dict())
            if landmark.size is not Size.ERA:
                center_x = (landmark.x_coordinate + math.floor(landmark.size.value['x']/2)) * 10
                center_y = ((landmark.y_coordinate + math.floor(landmark.size.value['x']/2)) * 10) - 5
                ll = 0
                if landmark.size.value['x'] == 3:
                    ll = 6
                if landmark.size.value['x'] == 5:
                    ll = 14
                if landmark.size.value['x'] == 7:
                    ll = 21
                right_circle_x = center_x + ll + 1
                left_circle_x = center_x - ll - 11
                timeline_dict['circles'].append({'xCoordinate': right_circle_x, 'yCoordinate': center_y})
                timeline_dict['circles'].append({'xCoordinate': left_circle_x, 'yCoordinate': center_y})
            if len(landmark.relationships) > 0:
                new_thread = Thread(landmark)
                timeline_dict['threads'].append(new_thread.generate_dict())
        timeline_distance = self.timeline[-1].x_coordinate + self.timeline[-1].rightmost_column
        years_percentages = []
        for year in self.timeline:
            if not year.placeholder:
                percentage = math.floor((year.x_coordinate / timeline_distance) * 100)
                year.percentage_across = percentage
                years_percentages.append(YearIndex(percentage, year.year))
            timeline_dict['years'].append(year.to_dict())
        years_index = {}
        for i in range(101):
            temp_year_index = YearIndex(i, None)
            pos = min(bisect_left(years_percentages, temp_year_index), len(years_percentages)-1)
            years_index[i] = years_percentages[pos].year
        timeline_dict['yearsIndex'] = years_index
        return timeline_dict

    def dump_data(self, timelines=False):
        if not timelines:
            timelines = [self]
        final_dict = {}
        for timeline in timelines:
            final_dict[timeline.id] = timeline.to_dict()
        # with open('F:\School and Work\jazz-time\data.json', 'w') as outfile:
        with open('/home/nickolasram/Coding/timeline-web/data.json', 'w') as outfile:
            json.dump(final_dict, outfile, indent=4)