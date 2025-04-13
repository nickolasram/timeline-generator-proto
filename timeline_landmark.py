import bisect
import math
import datetime
from enum import Enum

class Size(Enum):
    SMALL = {"x": 3, "y": 3}
    MEDIUM = {"x": 5, "y": 5}
    LARGE = {"x": 7, "y": 7}
    ERA = {"x": 5, "y": 12}

class Landmark:
    def __init__(self, size, title='', date=datetime.datetime(1900, 1, 1), display_date=True, image=0, color='#888888',
                 description=False):
        self.title = title
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
        self.image = image
        self.color = color
        # for general landmarks that don't necessarily have a date
        self.display_date = display_date
        self.description = description

    def __str__(self):
        return f"Landmark for {self.real_date}"

    def print_self(self):
        print(f"{self.size} landmark for {self.real_date.year}")
    
    def grid_placement(self):
        return f"column: {self.x_coordinate}, row: {self.y_coordinate}"

    def __lt__(self, other):
        return self.date < other.date

    def add_relationship(self, other):
        if other.real_date > self.real_date:
            bisect.insort(self.future_relationships, Relationship(other))
        else:
            bisect.insort(self.past_relationships, Relationship(other))

    def set_relationships(self, others):
        for other in others:
            self.add_relationship(other)

    def future_lump(self):
        self.f_rel_groups = [Relationship_Group(0, 150)]

    def past_lump(self):
        self.p_rel_groups = [Relationship_Group(180, 330)]

    def group_relationships(self):
        frg_index = 0
        ceiling = 0
        baseline = 0
        if len(self.future_relationships) > 0:
            future_relationships_first_year = self.future_relationships[0].other.real_date.year
            future_relationships_last_year = self.future_relationships[-1].other.real_date.year
            future_relationships_range = future_relationships_last_year - future_relationships_first_year
            if future_relationships_range == 0:
                future_relationships_range = 1
            for relationship in self.future_relationships:
                relationship_year = relationship.other.real_date.year
                distance = relationship_year - future_relationships_first_year
                distance_percentage = distance / future_relationships_range
                angle = math.floor(distance_percentage * 130)
                relationship.angle = angle
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
        if len(self.past_relationships) > 0:
            past_relationships_first_year = self.past_relationships[0].other.real_date.year
            past_relationships_last_year = self.past_relationships[0].other.real_date.year
            past_relationships_range = past_relationships_last_year - past_relationships_first_year
            if past_relationships_range == 0:
                past_relationships_range = 1
            for relationship in self.past_relationships:
                relationship_year = relationship.other.real_date.year
                distance = relationship_year - past_relationships_first_year
                distance_percentage = distance / past_relationships_range
                angle = math.floor(distance_percentage * 130)
                relationship.angle = angle + 180
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
        self.group_relationships()
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
        basic_dict = {
            'row': f"row-start-{self.y_coordinate} row-end-{self.y_coordinate+self.size.value['y']}",
            'column': f"col-start-{self.x_coordinate} col-end-{self.x_coordinate+self.size.value['x']}",
            'era': self.size == Size.ERA,
            'title': self.title,
            'year': self.real_date.year,
            'month': self.real_date.month,
            'day': self.real_date.day,
            'display_date': self.display_date,
            'relationshipAngles': relationship_groups,
            'size': self.size.value["x"],
            'bg_color': f"bg-[{self.color}7F]",
            'border_color': f"border-[{self.color}]"
        }
        if self.image:
            basic_dict["image"] = f"bg-[url(../public/images/{self.image})]"
        if self.description:
            basic_dict["description"] =  self.description
        return basic_dict    


class Relationship:
    def __init__(self, other):
        self.other = other
        self.angle = 0

    def __eq__(self, other):
        return self.angle == other.angle

    def __lt__(self, other):
        return self.angle < other.angle


class Relationship_Group:
    def __init__(self, angle, end_angle):
        self.angle = angle
        self.end_angle = end_angle