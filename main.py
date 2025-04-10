from datetime import datetime
from timeline_landmark import Landmark
from timeline import Timeline
from enum import Enum


def test_timeline():
    a = Landmark(0, datetime(1954, 2, 12))
    b = Landmark(0, datetime(1944, 5, 20))
    c = Landmark(0, datetime(1969, 7, 18))
    d = Landmark(0, datetime(1954, 3, 12))
    e = Landmark(0, datetime(1974, 3, 12))
    f = Landmark(0, datetime(1972, 7, 18))
    g = Landmark(0, datetime(1981, 3, 12))
    h = Landmark(0, datetime(1989, 3, 12))
    i = Landmark(0, datetime(1990, 3, 12))
    j = Landmark(0, datetime(1970, 2, 12))
    k = Landmark(0, datetime(1970, 2, 12))
    l = Landmark(0, datetime(1995, 2, 12))
    m = Landmark(0, datetime(1969, 7, 18))
    n = Landmark(0, datetime(1954, 3, 10))
    o = Landmark(0, datetime(1, 3, 12))
    p = Landmark(0, datetime(1963, 3, 12))
    q = Landmark(0, datetime(1981, 3, 12))
    r = Landmark(0, datetime(1955, 3, 12))
    landmarks = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r]
    x = Timeline()
    for landmark in landmarks:
        x.add_landmark(landmark)
    x.generate_timeline()
    for entry in x.timeline:
        print(entry)


class Size(Enum):
    SMALL = {"x": 3, "y": 3}
    MEDIUM = {"x": 5, "y": 5}
    LARGE = {"x": 7, "y": 7}
    ERA = {"x": 5, "y": 12}


class MainLandmark:
    def __init__(self, size: Size):
        self.upper_limit = 0
        self.lower_limit = 12
        self.size = size


class Year:
    def __init__(self):
        self.final_list = []
        self.default_cell = [3, 5, 7]
        for i in range(12):
            self.final_list.append([self.default_cell])
        self.column_count = 1
        self.leftmost_available_column = 0

    def define_list(self, size):
        if size == 3:
            return [
                [[5, 7, 8], [7, 8, 8], [5, 7, 8]],
                [[7, 8, 8], [8, 8, 8], [7, 8, 8]],
                [[5, 7, 8], [7, 8, 8], [5, 7, 8]]
            ]
        if size == 5:
            return [
                [[3, 7, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [3, 7, 8]],
                [[7, 8, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [7, 8, 8]],
                [[8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8]],
                [[7, 8, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [7, 8, 8]],
                [[3, 7, 8], [7, 8, 8], [8, 8, 8], [7, 8, 8], [3, 7, 8]]
            ]
        if size == 7:
            return [
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

    def add_landmark(self, landmark: MainLandmark):
        # IF CASE FOR ADDING AN ERA

        self.column_count += landmark.size.value["x"] - (1 if self.column_count == 1 else 0)
        for row in self.final_list:
            while len(row) < self.column_count:
                row.append(self.default_cell)
        column_index = self.leftmost_available_column
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
        if row_index != 0:
            lower_space = True
            while row_index + landmark_size < 12 and lower_space:
                for i in range(column_index, terminal_column):
                    if landmark_size not in self.final_list[row_index + landmark_size ][i]:
                        lower_space = False
                        break
                if lower_space:
                    row_index += 1

        self.adjust_cell_values(row_index, column_index, landmark_size)
        self.leftmost_available_column = int(column_index + (landmark_size / 2 - 0.5))
        print(f"{column_index}, {row_index}")
        print(self.leftmost_available_column)
    '''keep track of rightmost for easy placement of eras. remove unnecessary columns'''

    def print_grid(self):
        for row in self.final_list:
            print(row)

if __name__ == "__main__":
    test_year = Year()
    test_landmark = MainLandmark(Size.LARGE)
    test_year.add_landmark(test_landmark)
    test_landmark2 = MainLandmark(Size.SMALL)
    test_year.add_landmark(test_landmark2)
    test_year.add_landmark(test_landmark2)
    test_landmark3 = MainLandmark(Size.MEDIUM)
    test_year.add_landmark(test_landmark3)
    test_year.add_landmark(test_landmark2)
    test_year.print_grid()
