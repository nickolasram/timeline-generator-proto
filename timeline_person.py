from timeline_landmark import Landmark
import datetime


class Person(Landmark):
    def __init__(self, size, title='',
                 active_start=datetime.datetime(1900, 1, 1), active_end=datetime.datetime(2100, 1, 1),
                 birthday=datetime.datetime(1900, 1, 1), deathday=datetime.datetime(2100, 1, 1), image=0,
                 display_date=True, color='#888888', description=False, intro=False):
        super().__init__(size, title, active_start, display_date, image, color=color, description=description,
                         intro=intro)
        self.active_end = active_end
        self.birthday = birthday
        self.deathday = deathday
        self.person = True

    def to_dict(self):
        basic_dict = super().to_dict()
        basic_dict["activeEndYear"] = self.active_end.year
        basic_dict["activeEndMonth"] = self.active_end.month
        basic_dict["activeEndDay"] = self.active_end.day
        basic_dict["birthYear"] = self.birthday.year
        basic_dict["birthMonth"] = self.birthday.month
        basic_dict["birthDay"] = self.birthday.day
        basic_dict["deathYear"] = self.deathday.year
        basic_dict["deathMonth"] = self.deathday.month
        basic_dict["deathDay"] = self.deathday.day
        return basic_dict
