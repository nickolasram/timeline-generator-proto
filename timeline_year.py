from timeline_landmark import Landmark, Size
import random

class Year:
    def __init__(self, placeholder=False, landmarks=[],
                 year=0, end_year=0, span=False, width=0):
        self.landmarks = []
        self.final_list = []
        self.default_cell = [1, 3, 5, 7]
        self.column_count = 1
        self.leftmost_available_column = 0
        self.rightmost_column = 0
        self.x_coordinate = 0
        self.placeholder = placeholder
        self.landmarks = landmarks
        self.year = year
        self.end_year = end_year
        self.span = span
        self.width = width
        self.real_year = self.year
        self.real_end_year = 0
        self.percentage_across = 0

    def __str__(self):
        return f"{self.year} - {self.end_year}. {self.placeholder}"
    
    def to_dict(self):
        display_year = False
        for landmark in self.landmarks:
            if landmark.display_date:
                display_year = self.year
                break
        if not display_year and self.placeholder:
            display_year = self.year
        if not display_year:
            display_year = ''
        first_era = False
        if not self.placeholder:
            first_era = self.landmarks[0].era
        return {
            'year': self.year,
            'endYear': self.end_year,
            'placeholder': self.placeholder,
            'hoverContent': f"hover:before:content-['{display_year}']",
            'setContent': f"before:content-['{display_year}']",
            'span': self.span,
            'firstId': False if len(self.landmarks) == 0 else self.landmarks[0].id,
            'percentageAcross': self.percentage_across,
            'bgYearColumn': f"col-start-{self.x_coordinate} col-end-{self.x_coordinate+3}",
            'bgYearDisplay': display_year,
            'firstEra': first_era
        }

    def define_list(self, size):
        if size == 1:
            return [[1]]
        if size == 3:
            return [
                # [[1, 5, 7, 8], [7, 8, 8], [1, 5, 7, 8]],
                # [[7, 8, 8], [8, 8, 8], [7, 8, 8]],
                # [[1, 5, 7, 8], [7, 8, 8], [1, 5, 7, 8]]
                [[5, 7, 8], [7, 8, 8], [5, 7, 8]],
                [[7, 8, 8], [8, 8, 8], [7, 8, 8]],
                [[5, 7, 8], [7, 8, 8], [5, 7, 8]]
            ]
        if size == 5:
            return [
                # [[1, 3, 7, 8], [1, 7, 8, 8], [1, 8, 8, 8], [1, 7, 8, 8], [1, 3, 7, 8]],
                # [[1, 7, 8, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [1, 7, 8, 8]],
                # [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                # [[1, 7, 8, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [1, 7, 8, 8]],
                # [[1, 3, 7, 8], [1, 7, 8, 8], [1, 8, 8, 8], [1, 7, 8, 8], [1, 3, 7, 8]]
                [[3, 7, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [3, 7, 8]],
                [[7, 8, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [7, 8, 8]],
                [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                [[7, 8, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [7, 8, 8]],
                [[3, 7, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [3, 7, 8]]
            ]
        if size == 7:
            return [
                # [[1, 3, 5, 8], [1, 3, 5, 8], [8, 8, 8], [1, 8, 8, 8], [8, 8, 8], [1, 3, 5, 8], [1, 3, 5, 8]],
                # [[1, 3, 5, 8], [5, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [5, 8, 8], [1, 3, 5, 8]],
                # [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                # [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                # [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                # [[1, 3, 5, 8], [5, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [5, 8, 8], [1, 3, 5, 8]],
                # [[1, 3, 5, 8], [1, 3, 5, 8], [8, 8, 8], [1, 8, 8, 8], [8, 8, 8], [1, 3, 5, 8], [1, 3, 5, 8]]
                [[3, 5, 8], [3, 5, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [3, 5, 8], [3, 5, 8]],
                [[3, 5, 8], [5, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [5, 8, 8], [3, 5, 8]],
                [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                [[3, 5, 8], [5, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [5, 8, 8], [3, 5, 8]],
                [[3, 5, 8], [3, 5, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [3, 5, 8], [3, 5, 8]]
            ]

    def adjust_cell_values(self, row, column, size):
        replacement_values_list = self.define_list(size)
        for i in range(row, row+size):
            for j in range(column, column+size):
                self.final_list[i][j] = replacement_values_list[i - row][j - column]
    
    def remove_excess_columns(self):
        for i in range(len(self.final_list)):
            self.final_list[i] = self.final_list[i][:self.rightmost_column+1]

    def evaluate_lower_row(self, row_index, landmark_size, column_index, terminal_column):
        lower_space = True
        while row_index + landmark_size < 12 and lower_space:
            random_chance = random.randint(1, 10)
            if random_chance > 6:
                break
            for i in range(column_index, terminal_column):
                if landmark_size not in self.final_list[row_index + landmark_size][i]:
                    lower_space = False
                    break
            if lower_space:
                row_index += 1
        return row_index

    def place_landmark(self, landmark: Landmark):
        self.column_count += landmark.size.value["x"] - (1 if self.column_count == 1 else 0)
        if landmark.size.value["x"] == 1:
            self.column_count += 1
        for row in self.final_list:
            while len(row) < self.column_count:
                row.append(self.default_cell)
        # IF LANDMARK IS AN ERA
        if landmark.size == Size.ERA:
            column_index = self.rightmost_column + (1 if self.rightmost_column != 0 else 0)
            row_index = 0
            self.leftmost_available_column = column_index + 5
            self.rightmost_column = column_index + 4
            landmark.x_coordinate = column_index + self.x_coordinate
            landmark.y_coordinate = row_index + 1
            return
        column_index = self.leftmost_available_column
        if landmark.size.value["x"] == 1:
            column_index += 1
        landmark_size = landmark.size.value["x"]
        streak = 0
        row_index = 0
        terminal_column = column_index + landmark_size
        while streak < landmark_size:
            if row_index > 12 - landmark_size:
                column_index += 1
                row_index = 0
            escape = 0
            for i in range(landmark_size):
                for j in range(column_index, terminal_column):
                    if landmark_size not in self.final_list[row_index+i][j]:
                        row_index += 1
                        streak = 0
                        escape = 1
                        break
                    streak += 1
                if escape == 1:
                    escape = 0
                    break
        row_index = self.evaluate_lower_row(row_index, landmark_size, column_index, terminal_column)
        self.adjust_cell_values(row_index, column_index, landmark_size)
        landmark.x_coordinate = column_index + self.x_coordinate
        landmark.y_coordinate = row_index + 1
        self.leftmost_available_column = int(column_index + (landmark_size / 2 - 0.5))
        if landmark_size == 1:
            self.leftmost_available_column += 1
        self.rightmost_column = max(column_index + landmark_size - 1, self.rightmost_column)
        self.remove_excess_columns()

    def generate_year_grid(self):
        for i in range(12):
            self.final_list.append([self.default_cell])
        for landmark in self.landmarks:
            self.place_landmark(landmark)
        if self.landmarks[-1].size.value["x"] == 1:
            self.rightmost_column += 1
    
    def set_landmarks(self, landmarks):
        self.landmarks = landmarks
        self.generate_year_grid()

    def print_grid(self):
        for row in self.final_list:
            print(row)

    def landmarks_placement(self):
        for landmark in self.landmarks:
            print(landmark.grid_placement())