import bisect
import math
import datetime
from enum import Enum
import uuid

class Size(Enum):
    SMALL = {"x": 3, "y": 3}
    MEDIUM = {"x": 5, "y": 5}
    LARGE = {"x": 7, "y": 7}
    ERA = {"x": 5, "y": 12}


class Relationship:
    def __init__(self, other, title=False):
        self.other = other
        self.angle = 0
        self.title = title
        self.target_id = other.id
        if self.title is False:
            self.title = self.other.title[:8]

    def __eq__(self, other):
        return self.other.date == other.other.date

    def __lt__(self, other):
        return self.other.date < other.other.date

    def __str__(self):
        return self.title


class Relationship_Group:
    def __init__(self, angle, end_angle):
        self.angle = angle
        self.end_angle = end_angle
        self.relationships = []


class Landmark:
    def __init__(self, size, title='', date=datetime.datetime(1900, 1, 1), display_date=True, image=False, color='#888888',
                 description=False, intro=False):
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
        self.id = str(uuid.uuid4())[:8] + str(uuid.uuid4())[:8]
        self.person = False
        self.intro = intro
        self.era = False

    def __str__(self):
        return f"Landmark for {self.real_date}. {self.title}"

    def print_self(self):
        print(f"{self.size} landmark for {self.real_date.year}")
    
    def grid_placement(self):
        return f"column: {self.x_coordinate}, row: {self.y_coordinate}"

    def __lt__(self, other):
        return self.date < other.date

    def add_relationship(self, other):
        if other.real_date > self.real_date:
            bisect.insort_right(self.future_relationships, Relationship(other=other))
        else:
            bisect.insort_right(self.past_relationships, Relationship(other=other))

    def set_relationships(self, others):
        for other in others:
            self.add_relationship(other)

    def future_lump(self):
        self.f_rel_groups = [Relationship_Group(0, 150)]
        self.f_rel_groups[0].relationships = self.future_relationships

    def past_lump(self):
        self.p_rel_groups = [Relationship_Group(180, 330)]
        self.p_rel_groups[0].relationships = self.past_relationships

    def group_relationships(self):
        frg_index = 0
        ceiling = 0
        baseline = 0
        if len(self.future_relationships) >= 6:
            self.future_lump()
        elif len(self.future_relationships) > 0:
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
                    self.f_rel_groups[0].relationships.append(relationship)
                    ceiling = relationship.angle + 20
                else:
                    if baseline > 130 or ceiling > 127.5:
                        self.future_lump()
                        break
                    if relationship.angle <= self.f_rel_groups[frg_index].end_angle:
                        self.f_rel_groups[frg_index].end_angle += 10
                        self.f_rel_groups[frg_index].relationships.append(relationship)
                        ceiling += 10
                    else:
                        baseline = max(ceiling+2.5, relationship.angle)
                        ceiling = baseline + 20
                        self.f_rel_groups.append(Relationship_Group(baseline, ceiling))
                        self.f_rel_groups[-1].relationships.append(relationship)
                        frg_index += 1
        prg_index = 0
        ceiling = 0
        baseline = 0
        if len(self.past_relationships) >= 6:
            self.past_lump()
        elif len(self.past_relationships) > 0:
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
                    self.p_rel_groups[0].relationships.append(relationship)
                    ceiling = relationship.angle + 20
                else:
                    if baseline > 310 or ceiling > 307.5:
                        self.past_lump()
                        break
                    if relationship.angle <= self.p_rel_groups[prg_index].end_angle:
                        self.p_rel_groups[prg_index].end_angle += 10
                        self.p_rel_groups[prg_index].relationships.append(relationship)
                        ceiling += 10
                    else:
                        baseline = max(ceiling + 2.5, relationship.angle)
                        ceiling = baseline + 20
                        self.p_rel_groups.append(Relationship_Group(baseline, ceiling))
                        self.p_rel_groups[-1].relationships.append(relationship)
                        prg_index += 1

    def find_point_on_circle(self, angle):
        radians = angle * (math.pi / 180)
        x = math.sin(radians)
        y = -math.cos(radians)
        return f"{math.ceil(x * 100)} {math.ceil(y * 100)}"

    def find_rel_title_point(self, start_angle, end_angle, index, denominator, future):
        angular_adjustment = start_angle
        denominator = min(denominator, 7)
        numerator = index+1
        if not future:
            numerator = denominator - numerator
        position = numerator / denominator
        range = end_angle - start_angle
        base_angle = round(position * range)
        angle = base_angle + angular_adjustment + 15
        radians = angle * (math.pi / 180)
        x = math.sin(radians)
        y = -math.cos(radians)
        return math.ceil(x * 110), math.ceil(y * 110)

    def relationships_to_dict(self, group: Relationship_Group, future):
        relationship_list = []
        denominator = len(group.relationships) + 1
        for i in range(len(group.relationships)):
            relationship = group.relationships[i]
            title_location = self.find_rel_title_point(
                group.angle, group.end_angle, i, denominator, future
            )
            relationship_dict = {
                'title': relationship.title + f"{i}",
                'x': title_location[0],
                'y': title_location[1],
                'dx': 0 if future else -15,
                'dy': 0 if title_location[1] < 0 else 4,
                'targetId': relationship.target_id,
                'date': relationship.other.date.year
            }
            relationship_list.append(relationship_dict)
        return relationship_list

    def to_dict(self):
        relationship_groups = []
        for r_g in self.f_rel_groups:
            relationship_groups.append({
                'startPoint': self.find_point_on_circle(r_g.angle),
                'endPoint': self.find_point_on_circle(r_g.end_angle),
                'relationships': self.relationships_to_dict(r_g, True)
            })
        for r_g in self.p_rel_groups:
            relationship_groups.append({
                'startPoint': self.find_point_on_circle(r_g.angle),
                'endPoint': self.find_point_on_circle(r_g.end_angle),
                'relationships': self.relationships_to_dict(r_g, False)
            })
        basic_dict = {
            'row': f"row-start-{self.y_coordinate} row-end-{self.y_coordinate+self.size.value['y']}",
            'column': f"col-start-{self.x_coordinate} col-end-{self.x_coordinate+self.size.value['x']}",
            'era': self.size == Size.ERA,
            'title': self.title,
            'year': self.real_date.year,
            'month': self.real_date.month,
            'day': self.real_date.day,
            'displayDate': self.display_date,
            'size': self.size.value["x"],
            'bgColor': f"bg-[{self.color}7F]",
            'borderColor': f"border-[{self.color}]",
            'id': self.id,
            'person': self.person,
            'intro': self.intro,
            'image': self.image,
            'bgImage': self.image
        }
        if self.image:
            basic_dict["bgImage"] = f"bg-[url({self.image})]"
        if self.description:
            basic_dict["description"] = self.description
        if len(relationship_groups) > 0:
            basic_dict["relationshipGroups"] = relationship_groups
        return basic_dict    
