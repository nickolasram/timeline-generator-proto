import bisect
import math
import datetime
from enum import Enum

class Landmark_Size(Enum):
    SMALL = 3
    MEDIUM = 5
    LARGE = 7
    ERA = 5

class Landmark:
    def __init__(self, size, date=datetime.datetime(1900, 1, 1)):
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.relationships: list[Relationship] = []
        self.size = size
        self.left_column = 0
        self.top_row = 0
        self.f_rel_groups = []
        self.p_rel_groups = []
        self.future_relationships = []
        self.past_relationships = []
        self.date = date
        self.z_score = 0
        self.real_date = self.date

    def __str__(self):
        return f"Landmark for {self.real_date}"
        # return f"landmark: {self.size} ({self.x_coordinate}, {self.y_coordinate}) " \
        #        f"left-column: {self.left_column} top-row: {self.top_row}"

    def toString(self):
        return f"Landmark for {self.real_date}"

    def __lt__(self, other):
        return self.date < other.date

    def add_relationship(self, angle):
        if angle < 151:
            bisect.insort(self.future_relationships, Relationship(angle))
        else:
            bisect.insort(self.past_relationships, Relationship(angle))

    def future_lump(self):
        self.f_rel_groups = [Relationship_Group(0, 150)]

    def past_lump(self):
        self.p_rel_groups = [Relationship_Group(180, 330)]

    def group_relationships(self):
        frg_index = 0
        ceiling = 0
        baseline = 0
        for relationship in self.future_relationships:
            if len(self.f_rel_groups) == 0:
                self.f_rel_groups.append(Relationship_Group(relationship.angle, relationship.angle + 20))
                ceiling = relationship.angle + 20
            else:
                if baseline > 130 or ceiling > 127.5:
                    self.future_lump()
                    break
                if relationship.angle <= self.f_rel_groups[frg_index].end_angle:
                    self.f_rel_groups[frg_index].end_angle += 10
                    ceiling += 10
                else:
                    baseline = max(ceiling+2.5, relationship.angle)
                    ceiling = baseline + 20
                    self.f_rel_groups.append(Relationship_Group(baseline, ceiling))
                    frg_index += 1
        prg_index = 0
        ceiling = 0
        baseline = 0
        for relationship in self.past_relationships:
            if len(self.p_rel_groups) == 0:
                self.p_rel_groups.append(Relationship_Group(relationship.angle, relationship.angle + 20))
                ceiling = relationship.angle + 20
            else:
                if baseline > 310 or ceiling > 307.5:
                    self.past_lump()
                    break
                if relationship.angle <= self.p_rel_groups[prg_index].end_angle:
                    self.p_rel_groups[prg_index].end_angle += 10
                    ceiling += 10
                else:
                    baseline = max(ceiling + 2.5, relationship.angle)
                    ceiling = baseline + 20
                    self.p_rel_groups.append(Relationship_Group(baseline, ceiling))
                    prg_index += 1

    def find_point_on_circle(self, angle):
        radians = angle * (math.pi / 180)
        x = math.sin(radians)
        y = -math.cos(radians)
        return f"{math.ceil(x * 100)} {math.ceil(y * 100)}"

    def to_dict(self):
        relationship_groups = []
        for r_g in self.f_rel_groups:
            relationship_groups.append({
                'startpoint': self.find_point_on_circle(r_g.angle),
                'endpoint': self.find_point_on_circle(r_g.end_angle),
            })
        for r_g in self.p_rel_groups:
            relationship_groups.append({
                'startpoint': self.find_point_on_circle(r_g.angle),
                'endpoint': self.find_point_on_circle(r_g.end_angle),
            })
        return {
            'x': self.x_coordinate,
            'y': self.y_coordinate,
            'row': f"row-start-{self.top_row} row-end-{self.top_row+self.size}",
            'column': f"col-start-{self.left_column} col-end-{self.left_column+self.size}",
            'size': self.size,
            'relationshipAngles': relationship_groups
        }


class Relationship:
    def __init__(self, angle):
        self.angle = angle

    def __eq__(self, other):
        return self.angle == other.angle

    def __lt__(self, other):
        return self.angle < other.angle


class Relationship_Group:
    def __init__(self, angle, end_angle):
        self.angle = angle
        self.end_angle = end_angle