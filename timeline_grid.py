from timeline_landmark import Landmark
import random
import json

# Eventually, the x position will be determined by date. For testing we'll place each consecutively.

class Grid:
    # minimum xCoordinate = 1
    # yCoordinate range for angle calculation: -1 to -12
    # row range for CSS 1 - 12
    def __init__(self):
        # landmark count
        self.lm_count = 0
        # xCoordinate/column of leftmost column of the next landmark
        self.column = 1
        # vertical position for each new landmark. Incrememnts by ??? each new landmark until a landmark can't
        # be placed any lower then returns to ???
        self.vert = 0
        self.landmarks: list[Landmark] = []
        # Establish small landmark size variable here. can determine large landmark size and adjustments based on that
        self.small_size = 3
        self.medium_size = self.small_size + 2
        self.large_size = self.medium_size + 2


    def oscillate(self, size):
        if size == 7:
            y = random.randint(4, 6)
        elif size == 5:
            y = random.randint(3, 6)
        else:
            y = random.randint(2, 6)
        if len(self.landmarks) % 2 != 0:
            if size == 7:
                y += 3
            elif size == 5:
                y += 4
            else:
                y += 5
        return y


    def add_landmark(self, size):
        new_landmark = Landmark(size)
        column = self.column
        new_landmark.left_column = column
        if size == 3:
            new_landmark.x_coordinate = column + self.small_size // 2
        elif size == 5:
            new_landmark.x_coordinate = column + self.medium_size // 2
        else:
            new_landmark.x_coordinate = column + self.large_size // 2
        new_landmark.y_coordinate = -self.oscillate(size)
        if size == 7:
            self.column += self.large_size
            new_landmark.top_row = (-new_landmark.y_coordinate) - 3
        elif size == 5:
            self.column += self.medium_size
            new_landmark.top_row = (-new_landmark.y_coordinate) - 2
        else:
            self.column += self.small_size
            new_landmark.top_row = (-new_landmark.y_coordinate) - 1
        self.landmarks.append(new_landmark)


    def generate_relationships(self):
        for landmark in self.landmarks:
            for i in range(random.randint(0, 6)):
                landmark.add_relationship(random.randint(0, 130))
            for i in range(random.randint(0, 6)):
                landmark.add_relationship(random.randint(180, 310))


    def print_relationships(self):
        for i in range(len(self.landmarks)):
            print(
                f"landmark {i} ({self.landmarks[i].x_coordinate}, "
                f"{self.landmarks[i].y_coordinate}) has {len(self.landmarks[i].relationships)} relationships:"
            )
            for j in range(len(self.landmarks[i].relationships)):
                print(
                    f"landmark at point ({self.landmarks[i].relationships[j].other.x_coordinate}, "
                    f"{self.landmarks[i].relationships[j].other.y_coordinate}). "
                    f"{self.landmarks[i].relationships[j].relationship_angle} degrees."
                )


    def dump_data(self):
        landmark_dict = {
            'landmarks': []
        }
        for landmark in self.landmarks:
            landmark.group_relationships()
            landmark_dict['landmarks'].append(landmark.to_dict())
        with open('F:\School and Work\jazz-time\data.json', 'w') as outfile:
            json.dump(landmark_dict, outfile)


    # def decluster_angles(self):