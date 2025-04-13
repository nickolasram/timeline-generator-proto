from timeline_landmark import Landmark
import datetime

class Person(Landmark):
    def __init__(self, size, title='',
                 active_start=datetime.datetime(1900, 1, 1), active_end=datetime.datetime(2100, 1, 1),
                 birthday=datetime.datetime(1900, 1, 1), deathday=datetime.datetime(2100, 1, 1), image=0,
                 display_date=True, color='#888888', description=False):
        super().__init__(size, title, active_start, display_date, image, color=color, description=description)
        self.active_end = active_end
        self.birthday = birthday
        self.deathday = deathday

    def to_dict(self):
        basic_dict = super().to_dict()
        basic_dict["a_e_year"] = self.active_end.year
        basic_dict["a_e_month"] = self.active_end.month
        basic_dict["a_e_day"] = self.active_end.day
        basic_dict["birthyear"] = self.birthday.year
        basic_dict["birthmonth"] = self.birthday.month
        basic_dict["birthday"] = self.birthday.day
        basic_dict["deathyear"] = self.deathday.year
        basic_dict["deathmonth"] = self.deathday.month
        basic_dict["deathday"] = self.deathday.day
        return(basic_dict)