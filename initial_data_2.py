from datetime import datetime
from timeline_landmark import Landmark, Size, Relationship
from timeline_image import Image
from timeline_era import Era


color_s_r_era = '#c9dddd'
sre_key_points = [
    'Beginning of modern Science',
    'Scientific method: Depends upon logic, observation, and reason rather than faith',
    'Created the technologies and techniques that built the modern world',
    'Created paradigm of our solar system'
]
sre_img = Image('https://hti.osu.edu/sites/default/files/styles/100/public/copernicus.jpg?itok=5rBQa7ua')
s_r_era = Era(title='The Scientific Revolution', active_start=datetime(1472, 1, 1), end_year=datetime(1687, 1, 1),
              images=[sre_img], color=color_s_r_era, intro='1500-1700s', display_date=False)
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

bacon_bday = datetime(1561, 1, 1)
bacon_dday = datetime(1626, 1, 1)
francis_bacon = Landmark(title='Sire Francis Bacon', date=bacon_bday, size=Size.MEDIUM)
francis_bacon.landmark_end_date = bacon_dday
francis_bacon.key_points=['Preferred inductive reasoning and facts over theory',
                          'Invented the scientific method']

galileo_bday = datetime(1564, 1, 1)
galileo_dday = datetime(1642, 1, 1)
gg_img = Image('https://img2.rtve.es/im/6811327/?w=900')
galileo_galilei = Landmark(title='Galileo Galilei', date=galileo_bday, size=Size.LARGE, images=[gg_img])
galileo_galilei.landmark_end_date = galileo_dday
galileo_galilei.key_points = ['"I recant"',
                              'Invented the telescope, pendulum clock, thermometer, water pump, and sector',
                              'Discovered speed of acceleration for gravity']

kepler_bday = datetime(1571, 1, 1)
kepler_dday = datetime(1630, 1, 1)
johann_kepler = Landmark(title='Johannes Kepler', size=Size.MEDIUM, date=kepler_bday)
johann_kepler.landmark_end_date = kepler_dday
johann_kepler.key_points = ["Brahe's student for 20 years",
                            'Living during 30 years of war',
                            "Loved the planets and made it his life's work to explain the motion of planets",
                            'Invented Three Laws of Planetary Motion']

descartes_bday = datetime(1595, 1, 1)
descartes_dday = datetime(1650, 1, 1)
rene_descartes = Landmark(title='Renee Descartes', date=descartes_bday, size=Size.MEDIUM)
rene_descartes.landmark_end_date = descartes_dday
rene_descartes.key_points = ['Deductive Logic',
                             'Deduced the existence of God',
                             'Invented Cartesian geometry (xy axis)',
                             '"I think therefore I am"']

newton_bday = datetime(1642, 1, 1)
newton_dday = datetime(1727, 1, 1)
isaac_newton = Landmark(date=newton_bday, size=Size.LARGE, title='Sir Isaac Newton')
isaac_newton.landmark_end_date = newton_dday
isaac_newton.key_points = ['The Principia',
                           'Tied up the loose ends of Kepler and Galileo',
                           'Three Laws of Motion',
                           'Defined gravity and its laws',
                           'Invented optics and calculus']

rise_of_community = Landmark(title='Rise of the Scientific Community', date=datetime(1642, 1, 2), display_date=False,
                             size=Size.LARGE)
rise_of_community.key_points = ['Developed the modern scientific method',
                                'Universe ordered according to natural laws',
                                'Discovered that scientific laws can be discovered by human reason',
                                'Took the role of a deity or god out of the study of the universe',
                                'Mechanical views of the universe',
                                'Deistic view of God']

landmarks_2 = [s_r_era, epist, tycho_brahe, copernicus, francis_bacon, galileo_galilei, johann_kepler, rene_descartes,
               isaac_newton, rise_of_community]