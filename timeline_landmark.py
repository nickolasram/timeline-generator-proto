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
        self.title = other.title
        self.target_id = other.id
        self.context = context

    def __eq__(self, other):
        return self.other.date == other.other.date

    def __lt__(self, other):
        return self.other.date < other.other.date

    def __str__(self):
        return self.title
    
    def to_dict(self):
        d = {
            'title': self.title,
            'targetId': self.target_id,
            'context': self.context
        }
        return d


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
        bisect.insort_right(self.relationships, other)

    def set_relationships(self, others):
        for other in others:
            self.add_relationship(other)

    def to_dict(self):
        relative_time_position = [-1, -1]
        passed = False
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
            'files': self.files,
            'relationships': [x.to_dict() for x in self.relationships]
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
        return basic_dict    
