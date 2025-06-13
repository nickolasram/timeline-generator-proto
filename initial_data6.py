from datetime import datetime
from timeline_landmark import Landmark, Size, Relationship
from timeline_image import Image
from timeline_era import Era
from timeline_link import Link

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
copernicus_img = Image('https://cdn.britannica.com/83/74283-050-B94F541D.jpg')
heliocentric_img = Image('https://images.saymedia-content.com/.image/t_share/MTc2Mjg5MTg3NzkwNTk1MjYy/scientifis-revolutions-nicolaus-copernicus.jpg',
                         'Heliocentric model of the universe')
copernicus = Landmark(title='Nicolas Copernicus', size=Size.MEDIUM, date=copernicus_bday, images=[copernicus_img, heliocentric_img])
copernicus.key_points = ['Book, On the Revolutions of the Heavenly Spheres',
                         'Heliocentric theory: Sun is the center of the universe',
                         'Earth revolves around the sun']
copernicus.landmark_end_date = copernicus_dday

brahe_desc = 'A Danish astronomer of the Renaissance, known for his comprehensive and unprecedentedly accurate ' \
             'astronomical observations. He was known during his lifetime as an astronomer, astrologer, and alchemist. ' \
             'He was the last major astronomer before the invention of the telescope. Tycho Brahe has also been ' \
             'described as the greatest pre-telescopic astronomer. In 1572, Tycho noticed a completely new star that was' \
             ' brighter than any star or planet. Astonished by the existence of a star that ought not to have' \
             ' been there, he devoted himself to the creation of ever more accurate instruments of measurement over ' \
             'the next fifteen years (1576–1591). King Frederick II granted Tycho an estate on the island of Hven and' \
             ' the money to build Uraniborg, the first large observatory in Christian Europe. He later worked' \
             ' underground at Stjerneborg, where he realised that his instruments in Uraniborg were not sufficiently ' \
             'steady. His unprecedented research program both turned astronomy into the first modern science and also' \
             ' helped launch the Scientific Revolution.'
brahe_intro = 'the greatest pre-telescopic astronomer'
brahe_bday = datetime(1546, 1, 1)
brahe_dday = datetime(1601, 1, 1)
brahe_img = Image('https://cdn.britannica.com/77/83677-050-D0958F1A/Tycho-Brahe.jpg')
ptolemaic_img = Image('https://study.com/cimages/multimages/16/ptolemaic_system_psf7999927724135214065.png',
                      'The Ptolemaic system')
tycho_brahe = Landmark(title='Tycho Brahe', date=brahe_bday, size=Size.MEDIUM, images=[brahe_img, ptolemaic_img],
                       description=brahe_desc, intro=brahe_intro)
tycho_brahe.key_points = [' Danish royal astrologer',
                          'Follower of Ptolemaic system',
                          'Observed and mapped over 700 stars in a 20-year period']
tycho_brahe.landmark_end_date = brahe_dday

bacon_bday = datetime(1561, 1, 1)
bacon_dday = datetime(1626, 1, 1)
bacon_desc = 'Bacon has been called the father of empiricism. He argued for the possibility of scientific knowledge ' \
             'based only upon inductive reasoning and careful observation of events in nature. He believed that ' \
             'science could be achieved by the use of a sceptical and methodical approach whereby scientists aim to ' \
             'avoid misleading themselves. Although his most specific proposals about such a method, the Baconian ' \
             'method, did not have long-lasting influence, the general idea of the importance and possibility of a ' \
             'sceptical methodology makes Bacon one of the later founders of the scientific method. His portion of' \
             ' the method based in scepticism was a new rhetorical and theoretical framework for science, whose' \
             ' practical details are still central to debates on science and methodology. He is famous for' \
             ' his role in the scientific revolution, promoting scientific experimentation as a way of glorifying' \
             ' God and fulfilling scripture.'
bacon_img = Image('https://images.fineartamerica.com/images-medium-large/1618-francis-bacon-portrait-philosopher-paul-d-stewart.jpg')
scientific_img = Image('https://www.australianenvironmentaleducation.com.au/wp-content/uploads/2020/07/Scientific-Method.jpg',
                       'the scientific method')
francis_bacon = Landmark(title='Sire Francis Bacon', date=bacon_bday, size=Size.MEDIUM, description=bacon_desc,
                         images=[bacon_img, scientific_img])
francis_bacon.landmark_end_date = bacon_dday
francis_bacon.key_points = ['Preferred inductive reasoning and facts over theory',
                           'Invented the scientific method']

galileo_bday = datetime(1564, 1, 1)
galileo_dday = datetime(1642, 1, 1)
gg_img = Image('https://img2.rtve.es/im/6811327/?w=900')
gg_desc = 'Galileo di Vincenzo Bonaiuti de\' Galilei (15 February 1564 – 8 January 1642), commonly referred to as ' \
          'Galileo Galilei or mononymously as Galileo, was an Italian astronomer, physicist and engineer, sometimes ' \
          'described as a polymath. He was born in the city of Pisa, then part of the Duchy of Florence. Galileo has ' \
          'been called the father of observational astronomy, modern-era classical physics, the scientific method, and' \
          ' modern science. Galileo studied speed and velocity, gravity and free fall, the principle of relativity, ' \
          'inertia, projectile motion and also worked in applied science and technology, describing the properties of' \
          ' the pendulum and "hydrostatic balances". He was one of the earliest Renaissance developers of the ' \
          'thermoscope and the inventor of various military compasses. With an improved telescope he built, he' \
          ' observed the stars of the Milky Way, the phases of Venus, the four largest satellites of Jupiter, ' \
          'Saturn\'s rings, lunar craters and sunspots. He also built an early microscope. Galileo\'s championing of ' \
          'Copernican heliocentrism was met with opposition from within the Catholic Church and from some astronomers. ' \
          'The matter was investigated by the Roman Inquisition in 1615, which concluded that his opinions contradicted ' \
          'accepted Biblical interpretations. Galileo later defended his views in Dialogue' \
          ' Concerning the Two Chief World Systems (1632), which appeared to attack and ridicule Pope Urban VIII, ' \
          'thus alienating both the Pope and the Jesuits, who had both strongly supported Galileo up until this ' \
          'point. He was tried by the Inquisition, found "vehemently suspect of heresy", and forced to recant. He ' \
          'spent the rest of his life under house arrest. During this time, he wrote Two New Sciences (1638), ' \
          'primarily concerning kinematics and the strength of materials.'


inventions_img = Image('https://image.slidesharecdn.com/galileogalilei-130815003250-phpapp02/95/galileo-galilei-13-638.jpg?cb=1376526830')
galileo_galilei = Landmark(title='Galileo Galilei', date=galileo_bday, size=Size.LARGE, images=[gg_img, inventions_img],
                           description=gg_desc)
galileo_galilei.landmark_end_date = galileo_dday
galileo_galilei.key_points = ['"I recant"',
                              'Invented the telescope, pendulum clock, thermometer, water pump, and sector',
                              'Discovered speed of acceleration for gravity']
galileo_galilei.files = [Link('https://www.edb.gov.hk/attachment/en/curriculum-development/kla/eng-edu/famous_scientists/Common/files/Reading_2_Galileo_Galilei.pdf', 'Galileo\'s Life Worksheet')]

kepler_bday = datetime(1571, 1, 1)
kepler_dday = datetime(1630, 1, 1)
kepler_img = Image('https://www.thefamouspeople.com/profiles/images/johannes-kepler-2.jpg')
planetary_motion_img = Image('https://www.shutterstock.com/image-vector/set-three-keplers-laws-planetary-260nw-2250613515.jpg',
                             "Kepler's 3 laws of planetary motion")
kepler_desc = 'Johannes Kepler (27 December 1571 – 15 November 1630) was a German astronomer, mathematician, ' \
              'astrologer, natural philosopher and writer on music. He is a key figure in the 17th-century Scientific' \
              ' Revolution, best known for his laws of planetary motion, and his books Astronomia nova,' \
              ' Harmonice Mundi, and Epitome Astronomiae Copernicanae, influencing among others Isaac Newton, providing' \
              ' one of the foundations for his theory of universal gravitation. The variety and impact of his work made' \
              ' Kepler one of the founders and fathers of modern astronomy, the scientific method, natural and modern' \
              ' science. He has been described as the "father of science fiction" for his novel Somnium.'
johann_kepler = Landmark(title='Johannes Kepler', size=Size.MEDIUM, date=kepler_bday,
                         images=[kepler_img, planetary_motion_img], description=kepler_desc)
johann_kepler.landmark_end_date = kepler_dday
johann_kepler.key_points = ["Brahe's student for 20 years",
                            'Living during 30 years of war',
                            "Loved the planets and made it his life's work to explain the motion of planets",
                            'Invented Three Laws of Planetary Motion']

descartes_bday = datetime(1595, 1, 1)
descartes_dday = datetime(1650, 1, 1)
descartes_img = Image('https://images.saymedia-content.com/.image/t_share/MTk2NzE5ODAxMjE5OTQ5NTg2/key-concepts-of-the-philosophy-of-ren-descartes.jpg')
cartesian_img = Image('https://www.media4math.com/sites/default/files/library_asset/images/Definition--CoordinateSystems--CartesianCoordinateSystem.png',
                      'the cartesian system')
decartes_desc = 'René Descartes (31 March 1596 – 11 February 1650) was a French philosopher, scientist, and' \
                ' mathematician, widely considered a seminal figure in the emergence of modern philosophy and science.'
rene_descartes = Landmark(title='Renee Descartes', date=descartes_bday, size=Size.MEDIUM, description=decartes_desc,
                          images=[descartes_img, cartesian_img])
rene_descartes.landmark_end_date = descartes_dday
rene_descartes.key_points = ['Deductive Logic',
                             'Deduced the existence of God',
                             'Invented Cartesian geometry (xy axis)',
                             '"I think therefore I am"']

newton_bday = datetime(1642, 1, 1)
newton_dday = datetime(1727, 1, 1)
newton_img = Image('https://www.thefamouspeople.com/profiles/images/isaac-newton-25.jpg')
gravity_img = Image('https://forceinphysics.com/wp-content/uploads/2021/01/What-is-gravitational-force-in-physics.png',
                    'Newton realized gravity is a force given off by everything like electromagnetism')
motion_img = Image('https://image-static.collegedunia.com/public/image/a943f0e049da48f9b7b7126cf6f706f0.png')
optics_img = Image('https://images.fineartamerica.com/images-medium-large-5/newtons-optics-science-photo-library.jpg',
                   'Newton studying optics')
calculus_img = Image('https://image.slidesharecdn.com/basicsofcalculus-150407154114-conversion-gate01/95/basics-of-calculus-6-638.jpg?cb=1428421302')
newton_desc = 'Sir Isaac Newton (January 25 December 1643 – 31 March 20 March 1727) was an English polymath active as a' \
              ' mathematician, physicist, astronomer, alchemist, theologian, and author. Newton was a key figure in' \
              ' the Scientific Revolution and the Enlightenment that followed. His book Philosophiæ Naturalis' \
              ' Principia Mathematica (Mathematical Principles of Natural Philosophy), first published in 1687,' \
              ' achieved the first great unification in physics and established classical mechanics. Newton also' \
              ' made seminal contributions to optics, and shares credit with German mathematician Gottfried Wilhelm' \
              ' Leibniz for formulating infinitesimal calculus, though he developed calculus years before Leibniz.' \
              ' Newton contributed to and refined the scientific method, and his work is considered the most ' \
              'influential in bringing forth modern science.'
isaac_newton = Landmark(date=newton_bday, size=Size.LARGE, title='Sir Isaac Newton', description=newton_desc,
                        images=[newton_img, motion_img, gravity_img, calculus_img])
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


heavenly_revolution = Landmark(size=Size.NODE, title='Copernicus publishes "On the Revolution of the Heavenly Spheres"',
                               date=datetime(1543, 1, 1))
heavenly_revolution.set_relationships([Relationship(copernicus)])

telescope_desc = 'Perhaps based only on descriptions of the first practical telescope which Hans Lippershey tried' \
                 ' to patent in the Netherlands in 1608, Galileo, in the following year, made a telescope with about 3×' \
                 ' magnification. He later made improved versions with up to about 30× magnification. With a Galilean' \
                 ' telescope, the observer could see magnified, upright images on the Earth—it was what is' \
                 ' commonly known as a terrestrial telescope or a spyglass. He could also use it to observe the sky; ' \
                 'for a time he was one of those who could construct telescopes good enough for that purpose. On ' \
                 '25 August 1609, he demonstrated one of his early telescopes, with a magnification of about 8× or 9×, ' \
                 'to Venetian lawmakers. His telescopes were also a profitable sideline for Galileo, who sold them to ' \
                 'merchants who found them useful both at sea and as items of trade. He published his initial telescopic' \
                 ' astronomical observations in March 1610 in a brief treatise entitled Sidereus Nuncius (Starry Messenger).'
telescope = Landmark(size=Size.SMALL, date=datetime(1610, 1, 1), title='Starry Messenger', description=telescope_desc)
telescope.set_relationships([Relationship(galileo_galilei)])
telescope.key_points=['Galileo\'s initial treatise on his style of telescopes']


affair_start = Landmark(date=datetime(1610, 1, 2), title='The Galileo affair begins', size=Size.NODE)
affair_end_description = 'The Galileo affair began around 1610, and culminated with the trial and condemnation of ' \
                         'Galileo Galilei by the Roman Catholic Inquisition in 1633. Galileo was prosecuted for ' \
                         'holding as true the doctrine of heliocentrism, the astronomical model in which the Earth ' \
                         'and planets revolve around the Sun at the centre of the universe. In 1610, Galileo published ' \
                         'his Sidereus Nuncius (Starry Messenger), describing the observations that he had made with' \
                         ' his new, much stronger telescope, amongst them, the Galilean moons of Jupiter. With' \
                         ' these observations and additional observations that followed, such as the phases of Venus, ' \
                         'he promoted the heliocentric theory of Nicolaus Copernicus published in De revolutionibus ' \
                         'orbium coelestium in 1543. Galileo\'s opinions were met with opposition within the Catholic ' \
                         'Church, and in 1616 the Inquisition declared heliocentrism to be "formally heretical". ' \
                         'Galileo went on to propose a theory of tides in 1616, and of comets in 1619; he argued that' \
                         ' the tides were evidence for the motion of the Earth. In 1632, Galileo published his ' \
                         'Dialogue Concerning the Two Chief World Systems, which defended heliocentrism, and was ' \
                         'immensely popular. Responding to mounting controversy over theology, astronomy and' \
                         ' philosophy, the Roman Inquisition tried Galileo in 1633, found him "vehemently suspect of' \
                         ' heresy", and sentenced him to house arrest where he remained until his death in 1642.' \
                         ' At that point, heliocentric books were banned and Galileo was ordered to abstain from ' \
                         'holding, teaching or defending heliocentric ideas after the trial.'
affair_end = Landmark(date=datetime(1633, 1, 1), title='"I recant"', size=Size.SMALL, description=affair_end_description,
                      intro='The Galileo Affair')

copernicus.set_relationships([Relationship(galileo_galilei, 'Reinforced heliocentric model')])
affair_start.set_relationships([Relationship(galileo_galilei),
                                Relationship(affair_end),
                                Relationship(telescope)
                                ])
affair_end.set_relationships([Relationship(affair_start),
                              Relationship(telescope, 'spurned controversy'),
                              Relationship(galileo_galilei)])
brahe_relationships = [Relationship(johann_kepler, "Kepler's teacher")]
tycho_brahe.set_relationships(brahe_relationships)
kepler_relationships = [Relationship(tycho_brahe, "Brahe's Student")]
johann_kepler.set_relationships(kepler_relationships)
galileo_galilei_relationships = [Relationship(affair_end, 'The Galileo Affair'),
                                 Relationship(telescope)]
galileo_galilei.set_relationships(galileo_galilei_relationships)
telescope_relationships=[Relationship(copernicus, 'Reinforced the Heliocentric model'),
                         ]
telescope.set_relationships(telescope_relationships)

landmarks_6 = [s_r_era, epist, tycho_brahe, copernicus, francis_bacon, galileo_galilei, johann_kepler, rene_descartes,
               isaac_newton, rise_of_community, heavenly_revolution, telescope, affair_start, affair_end]

presentation_2 = [s_r_era, epist, tycho_brahe, copernicus, francis_bacon, galileo_galilei, johann_kepler, rene_descartes,
                  isaac_newton, rise_of_community]