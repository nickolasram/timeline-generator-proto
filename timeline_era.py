from timeline_landmark import Landmark, Size
import datetime

class Era(Landmark):
    def __init__(self, title='',
                 active_start=datetime.datetime(1900, 1, 1), end_year =datetime.datetime(2100, 1, 1),
                 image=0, display_date=True, color='#888888', description=False):
        super().__init__(Size.ERA, title, active_start, display_date=display_date, image=image, color=color, description=description)
        self.end_year = end_year

    def to_dict(self):
        basic_dict = super().to_dict()
        basic_dict["end_date"] = self.end_year.year
        return(basic_dict)