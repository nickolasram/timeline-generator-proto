from datetime import datetime
from timeline_landmark import Landmark, Size
from timeline_person import Person
from timeline_era import Era

a = Era('The Kansas City Era', datetime(1954, 1, 1), datetime(1955, 1, 1))

b = Landmark(Size.LARGE, 'Swing', datetime(1944, 5, 20), color='#B2C063')

c = Person(Size.SMALL, 'Thelonius Monk', 
             datetime(1969, 7, 18), datetime(1999, 8, 10),
             datetime(1953, 4, 8), datetime(1999, 8, 13))

d = Person(Size.MEDIUM, 'Buddy Bolden', 
             datetime(1954, 3, 12), datetime(1980, 8, 10),
             datetime(1933, 4, 8), datetime(1999, 8, 13))

e = Era('The Smooth Jazz Era', datetime(1974, 3, 12), datetime(1989, 4, 20))

f = Landmark(Size.LARGE, 'Benny Hillson Trio', datetime(1972, 7, 18))

g = Landmark(Size.SMALL, 'A Brighter Shade of Blue', datetime(1981, 3, 12))

h_desc = f"Miles Dewey Davis III was an American jazz trumpeter, bandleader, and composer. He is among the most influential and acclaimed figures in the history of jazz and 20th-century music. Davis adopted a variety of musical directions in a roughly five-decade career that kept him at the forefront of many major stylistic developments in jazz. Born into an upper-middle-class family in Alton, Illinois, and raised in East St. Louis, Davis started on the trumpet in his early teens. He left to study at Juilliard in New York City, before dropping out and making his professional debut as a member of saxophonist Charlie Parker's bebop quintet from 1944 to 1948. Shortly after, he recorded the Birth of the Cool sessions for Capitol Records, which were instrumental to the development of cool jazz."

h = Person(Size.SMALL, 'Miles Davis', 
           datetime(1944, 3, 12), datetime(1999, 8, 10),
            datetime(1926, 4, 8), datetime(2000, 10, 23),
            image='miles-davis.jpg', color='#B2C063', description=h_desc)

i = Landmark(Size.SMALL, 'Bitch\'s Brew', datetime(1990, 3, 12))

j = Person(Size.MEDIUM, 'Duke Ellington', 
           datetime(1970, 2, 12), datetime(2002, 8, 10),
             datetime(1954, 4, 8), datetime(2003, 8, 13))

k = Person(Size.MEDIUM, 'Marlena Shaw', 
           datetime(1971, 2, 12), datetime(1999, 8, 10),
             datetime(1943, 4, 8), datetime(1999, 8, 13))

l = Landmark(Size.MEDIUM, 'Blanket Fort', datetime(1995, 2, 12))

m = Person(Size.SMALL, 'Art Farmer', 
           datetime(1969, 7, 18), datetime(1989, 8, 10),
             datetime(1953, 4, 8), datetime(2009, 8, 13)) 

n = Landmark(Size.SMALL, 'The Strange', datetime(1954, 3, 10))

o = Landmark(Size.SMALL, 'The Blues', datetime(1936, 3, 12), color='#B2C063')

p = Person(Size.LARGE, 'CannonBall Adderly', 
           datetime(1963, 3, 12), datetime(1997, 8, 10),
             datetime(1931, 4, 8), datetime(1997, 8, 13))

q = Era('The Jazz Fusion Era', datetime(1981, 3, 12), datetime(1997, 5, 15))

r = Person(Size.LARGE, 'Paul Bufano', 
           datetime(1955, 3, 12), datetime(1999, 8, 10),
             datetime(1953, 4, 8), datetime(1999, 8, 13))

s = Era('Before Jazz', datetime(1936, 1, 1), datetime(1944, 1, 1), 
             image='brass-band.jpg', display_date=False, color='#B2C063')

b_relationships = [o, c, l]
b.set_relationships(b_relationships)
landmarks = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]