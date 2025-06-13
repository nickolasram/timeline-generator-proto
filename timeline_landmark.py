import bisect
import math
import datetime
from enum import Enum
import uuid

class Size(Enum):
    NODE = {"x": 1, "y": 1}
    SMALL = {"x": 3, "y": 3}
    MEDIUM = {"x": 5, "y": 5}
    LARGE = {"x": 7, "y": 7}
    ERA = {"x": 5, "y": 12}


class Relationship:
    def __init__(self, other, context=False):
        self.other = other
        self.angle = 0
        self.title = other.title
        self.target_id = other.id
        self.context = context

    def __eq__(self, other):
        return self.other.date == other.other.date

    def __lt__(self, other):
        return self.other.date < other.other.date

    def __str__(self):
        return self.title


class Relationship_Group:
    def __init__(self, angle, end_angle, size):
        self.angle = angle
        self.end_angle = end_angle
        self.relationships = []
        self.size = size


class Landmark:
    def __init__(self, size, title='', date=datetime.datetime(1900, 1, 1), display_date=True, images=None, color='#888888',
                 description=False, intro=False, links=False):
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
        self.landmark_end_date = False
        self.z_score = 0
        self.real_date = self.date
        self.images = images
        self.color = color
        # for general landmarks that don't necessarily have a date
        self.display_date = display_date
        self.description = description
        self.id = str(uuid.uuid4())[:8] + str(uuid.uuid4())[:8]
        self.person = False
        self.intro = intro
        self.era = False
        self.links = links
        self.key_points = False
        self.presentations = []
        self.sources = False
        self.files = False

    def __str__(self):
        return f"Landmark for {self.real_date}. {self.title}"

    def print_self(self):
        print(f"{self.size} landmark for {self.real_date.year}")
    
    def grid_placement(self):
        return f"column: {self.x_coordinate}, row: {self.y_coordinate}"

    def __lt__(self, other):
        return self.date < other.date

    def add_relationship(self, other:Relationship):
        if other.other.real_date > self.real_date:
            bisect.insort_right(self.future_relationships, other)
        else:
            bisect.insort_right(self.past_relationships, other)

    def set_relationships(self, others):
        for other in others:
            self.add_relationship(other)

    def future_lump(self, size):
        self.f_rel_groups = [Relationship_Group(0, 150, size)]
        self.f_rel_groups[0].relationships = self.future_relationships

    def past_lump(self, size):
        self.p_rel_groups = [Relationship_Group(180, 330, size)]
        self.p_rel_groups[0].relationships = self.past_relationships

    def group_relationships(self, size):
        frg_index = 0
        ceiling = 0
        baseline = 0
        if len(self.future_relationships) >= 6:
            self.future_lump(size)
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
                    self.f_rel_groups.append(Relationship_Group(relationship.angle, relationship.angle + 20, size))
                    # this index might be -1
                    self.f_rel_groups[0].relationships.append(relationship)
                    ceiling = relationship.angle + 20
                else:
                    if baseline > 130 or ceiling > 127.5:
                        self.future_lump(size)
                        break
                    if relationship.angle <= self.f_rel_groups[frg_index].end_angle:
                        self.f_rel_groups[frg_index].end_angle += 15
                        self.f_rel_groups[frg_index].relationships.append(relationship)
                        ceiling += 15
                    else:
                        baseline = max(ceiling+2.5, relationship.angle)
                        ceiling = baseline + 20
                        self.f_rel_groups.append(Relationship_Group(baseline, ceiling, size))
                        self.f_rel_groups[-1].relationships.append(relationship)
                        frg_index += 1
        prg_index = 0
        ceiling = 0
        baseline = 0
        if len(self.past_relationships) >= 6:
            self.past_lump(size)
        elif len(self.past_relationships) > 0:
            past_relationships_first_year = self.past_relationships[0].other.real_date.year
            past_relationships_last_year = self.past_relationships[-1].other.real_date.year
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
                    self.p_rel_groups.append(Relationship_Group(relationship.angle, relationship.angle + 20, size))
                    self.p_rel_groups[0].relationships.append(relationship)
                    ceiling = relationship.angle + 20
                else:
                    if baseline > 310 or ceiling > 307.5:
                        self.past_lump(size)
                        break
                    if relationship.angle <= self.p_rel_groups[prg_index].end_angle:
                        self.p_rel_groups[prg_index].end_angle += 15
                        self.p_rel_groups[prg_index].relationships.append(relationship)
                        ceiling += 15
                    else:
                        baseline = max(ceiling + 2.5, relationship.angle)
                        ceiling = baseline + 20
                        self.p_rel_groups.append(Relationship_Group(baseline, ceiling, size))
                        self.p_rel_groups[-1].relationships.append(relationship)
                        prg_index += 1


    def find_point_on_circle(self, angle, future):
        radians = angle * (math.pi / 180)
        x = math.sin(radians)
        y = -math.cos(radians)
        if not future:
            y *= -1
            if angle > 270:
                y -= .01
        return [math.ceil(x * 100), math.ceil(y * 100)]

    def find_rel_title_point(self, start_angle, end_angle, index, list_length, future, lm_size):
        denominator = list_length + 1
        pivot = (list_length - 1) / 2
        nudge_factor = index - pivot
        # ones that need to move up (index below pivot) need to move farther? than ones that need to move down
        position_compensation = 0
        if index < pivot:
            position_compensation = -3
        # if index > pivot:
        #     position_compensation = -1
        nudge_coefficient = ((34/list_length) - lm_size) + position_compensation
        if not future:
            nudge_factor *= -1
        if lm_size == 7:
            nudge_factor = 0
        nudge_amount = nudge_factor * nudge_coefficient
        angular_adjustment = start_angle
        titles_shown = 5
        if self.size.value['x'] == 5:
            titles_shown = 6
        if self.size.value['x'] == 7:
            titles_shown = 7
        denominator = min(denominator, titles_shown)
        numerator = index+1
        if not future:
            numerator = denominator - numerator
        position = numerator / denominator
        range = end_angle - start_angle
        base_angle = round(position * range)
        angle = base_angle + angular_adjustment + 15 + nudge_amount
        radians = angle * (math.pi / 180)
        x = math.sin(radians)
        y = -math.cos(radians)
        if not future:
            y *= -1
        return math.ceil(x * 110), math.ceil(y * 110)

    def relationships_to_dict(self, group: Relationship_Group, future):
        relationship_list = []
        for i in range(len(group.relationships)):
            relationship = group.relationships[i]
            title_location = self.find_rel_title_point(
                group.angle, group.end_angle, i, len(group.relationships), future, group.size
            )
            relationship_dict = {
                'title': relationship.title,
                'x': title_location[0],
                'y': title_location[1],
                # 'dx': 0,
                'dy': 0 if title_location[1] < 0 else 4,
                'textAnchor': 'start' if future else 'end',
                'targetId': relationship.target_id,
                'date': relationship.other.date.year,
                'context': relationship.context,
                'color': relationship.other.color,
                'displayDate': relationship.other.display_date
            }
            relationship_list.append(relationship_dict)
        return relationship_list

    def to_dict(self):
        relationship_groups = []
        for r_g in self.p_rel_groups:
            relationship_groups.append({
                'startPoint': self.find_point_on_circle(r_g.angle, False),
                'endPoint': self.find_point_on_circle(r_g.end_angle, False),
                'relationships': self.relationships_to_dict(r_g, False),
                'future': False
            })
        for r_g in self.f_rel_groups:
            relationship_groups.append({
                'startPoint': self.find_point_on_circle(r_g.angle, True),
                'endPoint': self.find_point_on_circle(r_g.end_angle, True),
                'relationships': self.relationships_to_dict(r_g, True),
                'future': True
            })
        relative_time_position = [-1, -1]
        passed = False
        if len(relationship_groups)>0:
            for i in range(len(relationship_groups)):
                if passed:
                    break
                for j in range(len(relationship_groups[i]['relationships'])):
                    if (relationship_groups[i]['relationships'][j]['date'] >= self.real_date.year) and not passed:
                        relative_time_position = [i, j]
                        passed = True
                        break

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
            'images': self.images,
            'bgImage': self.images,
            'links': self.links,
            'color': self.color,
            'keyPoints': self.key_points,
            'presentations': self.presentations,
            'relativeTimePosition': relative_time_position,
            'endDate': self.landmark_end_date,
            'files': self.files
        }
        if self.files:
            basic_dict["files"] = [x.to_dict() for x in self.files]
        if self.links:
            basic_dict["links"] = [x.to_dict() for x in self.links]
        if self.landmark_end_date:
            basic_dict["endDate"] = self.landmark_end_date.year
        if self.images:
            basic_dict["images"] = [x.to_dict() for x in self.images]
            basic_dict["bgImage"] = f"bg-[url({self.images[0].image})]"
        if self.description:
            basic_dict["description"] = self.description
        if self.sources:
            basic_dict["sources"] = self.sources
        if len(relationship_groups) > 0:
            basic_dict["relationshipGroups"] = relationship_groups
        return basic_dict    
