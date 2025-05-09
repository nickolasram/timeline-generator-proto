from datetime import datetime
from timeline_landmark import Landmark, Size, Relationship
from timeline_person import Person
from timeline_era import Era


color_s_r_era = '#c9dddd'
sre_key_points = [
    'Beginning of modern Science',
    'Scientific method: Depends upon logic, observation, and reason rather than faith',
    'Created the technologies and techniques that built the modern world',
    'Created paradigm of our solar system'
]
sre_img = 'https://hti.osu.edu/sites/default/files/styles/100/public/copernicus.jpg?itok=5rBQa7ua'
s_r_era = Era(title='The Scientific Revolution', active_start=datetime(1472, 1, 1), end_year=datetime(1687, 1, 1),
              image=sre_img, color=color_s_r_era, intro='1500-1700s', display_date=False)
s_r_era.key_points = sre_key_points

epist = Landmark(size=Size.LARGE, color=color_s_r_era, title='Revolution in Epistemology and Philosophy',
                 date=datetime(1472, 1, 2), display_date=False)
epist.key_points = ['Universities formed',
                    'Rediscovery of classical science',
                    'Leading figures include Bacon, Brahe, Copernicus, Descartes, Galileo, Kepler, and Newton'
                    ]

copernicus_bday = datetime(1473, 1, 1)
copernicus_dday = datetime(1543, 1, 1)
copernicus = Landmark(title='Nicolas Copernicus', size=Size.MEDIUM, date=copernicus_bday)
copernicus.key_points = ['Book, On the Revolutions of the Heavenly Spheres',
                         'Heliocentric theory: Sun is the center of the universe',
                         'Earth revolves around the sun']
copernicus.landmark_end_date = copernicus_dday

brahe_bday = datetime(1546, 1, 1)
brahe_dday = datetime(1601, 1, 1)
tycho_brahe = Landmark(title='Tycho Brahe', date=brahe_bday, size=Size.MEDIUM)
tycho_brahe.key_points = [' Danish royal astrologer',
                          'Follower of Ptolemaic system',
                          'Observed and mapped over 700 stars in a 20-year period']
tycho_brahe.landmark_end_date = brahe_dday


landmarks_2 = [s_r_era, epist, tycho_brahe, copernicus]