from datetime import datetime
from timeline_landmark import Landmark, Size
from timeline_person import Person
from timeline_era import Era

a_intro = f'The swing era (also frequently referred to as the big band era) was the period when big band swing music' \
         f' was the most popular music in the United States, especially for teenagers. Though this was its most popular' \
         f' period, the music had actually been around since the late 1920s and early 1930s, being played by black bands' \
         f' led by such artists as Duke Ellington, Jimmie Lunceford, Bennie Moten, Cab Calloway, Earl Hines, and' \
         f' Fletcher Henderson, and white bands from the 1920s led by the likes of Jean Goldkette, Russ Morgan and ' \
         f'Isham Jones.'

a = Era('The Swing Era', datetime(1954, 1, 1), datetime(1980, 1, 1),
        image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.kaufmanmusiccenter.org%2Fimages%2Fuploads%2Fevents%2F_medium%2FDuke_Ellington_1200x1200.jpg&f=1&nofb=1&ipt=bc440045f73dd7efb2f8bb046b5ac2224d89863badfb27969762347bccbc8e7d',
        color='#7c45b9', intro=a_intro)

b = Landmark(Size.LARGE, 'Swing', datetime(1944, 5, 20), color='#B2C063',
             image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.britannica.com%2F73%2F201073-050-7A256B9D%2Fbig-band-jazz-greats-Duke-Ellington-Otto.jpg&f=1&nofb=1&ipt=c8d1d3373a623cb1193a5472cedfab18fcbba7b73c165611827fdbc582e70ece')

c = Person(Size.SMALL, 'Thelonius Monk', 
             datetime(1969, 7, 18), datetime(1999, 8, 10),
             datetime(1953, 4, 8), datetime(1999, 8, 13), color='#7c45b9')

d = Person(Size.MEDIUM, 'Buddy Bolden', 
             datetime(1954, 3, 12), datetime(1980, 8, 10),
             datetime(1933, 4, 8), datetime(1999, 8, 13), color='#7c45b9')

e_intro = 'Having evolved out of the music of marching bands and ragtime, much of the music heard in this earlier ' \
         'period of jazz has similar instrumentation (drums, trumpets, trombone, sax etc) and feel. Also the ' \
         'influence of Afro Latin rhythms from places such as Cuba can be heard (from music as far back as the 1880\'s).' \
         ' The tresillo rhythm is heavily used in the New Orleans Jazz of this time and can be directly linked to the' \
         ' music of the Caribbean. Dixieland bands played rag style music but also incorporated collective and solo' \
         ' improvisation within their performances which was something that hadn\'t been done before in traditional ' \
         'marching,ragtime or vaudeville bands. In Chicago, a different more soulful and vocal oriented jazz developed ' \
         'with artists such as Louis Armstrong, who played trumpet and popularized the use of scat singing. During the ' \
         '1920s and prohibition, Jazz existed in the darker parts of society in brothels and speakeasies and was ' \
         'heavily racially segregated. Some notable artists of this time are Jellyroll Morton, Louis Armstrong and ' \
         'Buddy Bolden.'

e = Era('The Smooth Jazz Era', datetime(1974, 3, 12), datetime(1990, 4, 20),
        image='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F4.bp.blogspot.com%2F-hXo9FERfTQo%2FUp0rxgpNsNI%2FAAAAAAAAogQ%2FPnrQeETkXOE%2Fs1600%2Fbobby_caldwell_cd-front.jpg&f=1&nofb=1&ipt=f165614561dbd65da3c0bc14c728cf1dd474bf6e43cac1426ede5d452c52090c',
        color='#459db9', intro=e_intro)

f = Landmark(Size.LARGE, 'Benny Hillson Trio', datetime(1972, 7, 18), color='#7c45b9', intro='Benny\'s Band')

g = Landmark(Size.SMALL, 'A Brighter Shade of Blue', datetime(1981, 3, 12), color='#459db9')

h_desc = f"Miles Dewey Davis III was an American jazz trumpeter, bandleader, and composer. He is among the most " \
         f"influential and acclaimed figures in the history of jazz and 20th-century music. Davis adopted a variety of " \
         f"musical directions in a roughly five-decade career that kept him at the forefront of many major stylistic" \
         f" developments in jazz. Born into an upper-middle-class family in Alton, Illinois, and raised in East St. " \
         f"Louis, Davis started on the trumpet in his early teens. He left to study at Juilliard in New York City, " \
         f"before dropping out and making his professional debut as a member of saxophonist Charlie Parker's bebop " \
         f"quintet from 1944 to 1948. Shortly after, he recorded the Birth of the Cool sessions for Capitol Records, " \
         f"which were instrumental to the development of cool jazz."

h = Person(Size.SMALL, 'Miles Davis', 
           datetime(1944, 3, 12), datetime(1999, 8, 10),
           datetime(1926, 4, 8), datetime(2000, 10, 23),
           image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.needsomefun.net%2Fwp-content%2Fuploads%2F2016%2F07%2FMiles-Davis-1.jpeg&f=1&nofb=1&ipt=4f727e39bd7fda300428619d48cb6f4bc1e1d145948cb5bc061613c9b53747dd',
           color='#B2C063', description=h_desc)

i = Landmark(Size.SMALL, 'Bitch\'s Brew', datetime(1990, 3, 12), color='#459db9')

j = Landmark(Size.MEDIUM, 'Duke Ellington Band Duke Ellington Band Duke Ellington Band Duke Ellington Band Duke Ellington Band',
           datetime(1970, 2, 12), color='#7c45b9')

k = Person(Size.MEDIUM, 'Marlena Shaw Marlena Shaw Marlena Shaw Marlena Shaw Marlena Shaw Marlena Shaw Marlena Shaw',
           datetime(1971, 2, 12), datetime(1999, 8, 10),
             datetime(1943, 4, 8), datetime(1999, 8, 13), color='#7c45b9')

l = Landmark(Size.MEDIUM, 'Blanket Fort', datetime(1995, 2, 12), color='#9b1818')

m = Person(Size.SMALL, 'Art Farmer', 
           datetime(1969, 7, 18), datetime(1989, 8, 10),
             datetime(1953, 4, 8), datetime(2009, 8, 13), color='#7c45b9')

n = Landmark(Size.SMALL, 'The Strange Strange Strange Strange Strange Strange Strange', datetime(1954, 3, 10), color='#7c45b9')

o = Landmark(Size.SMALL, 'The Blues', datetime(1936, 3, 12), color='#B2C063', display_date=False,
             image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fprojetoitaca.com.br%2Fwp-content%2Fuploads%2F2020%2F12%2FRobert-Johnson.jpg&f=1&nofb=1&ipt=7dad8bfc3686d1fde77ea0a53bb2f2a5619d62d78db108ae93d2f3c1f72487ed')

p = Person(Size.LARGE, 'CannonBall Adderly', 
           datetime(1963, 3, 12), datetime(1997, 8, 10),
             datetime(1931, 4, 8), datetime(1997, 8, 13), color='#7c45b9')

q_intro = f"Jazz fusion (also known as jazz rock, jazz-rock fusion, or simply fusion) is a popular music genre that " \
          f"developed in the late 1960s when musicians combined jazz harmony and improvisation with rock music, funk, " \
          f"and rhythm and blues. Electric guitars, amplifiers, and keyboards that were popular in rock began to be " \
          f"used by jazz musicians, particularly those who had grown up listening to rock and roll."

q = Era('The Jazz Fusion Era', datetime(1981, 3, 12), datetime(1997, 5, 15),
        image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.spin.com%2Ffiles%2F2019%2F09%2FGettyImages-84843312-1569691641.jpg&f=1&nofb=1&ipt=3e82a0b24fae8f0d6c940038dbf661e4f8877b07d5e2f5d13ee1432a03fad84f',
        color='#9b1818', intro=q_intro)

r = Person(Size.LARGE, 'Paul Bufano Paul Bufano Paul Bufano Paul Bufano Paul Bufano',
           datetime(1955, 3, 12), datetime(1999, 8, 10),
           datetime(1953, 4, 8), datetime(1999, 8, 13), color='#7c45b9',
           image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fy.yarn.co%2F46d3497c-75ea-4b52-9e87-883593080a3b_screenshot.jpg&f=1&nofb=1&ipt=ba1b9e2e60eb2900d145a84e0ff1aaace10fff78917d70e0bb651ff3838b0538')

s_intro = 'Pre-jazz is the time before the recognition of jazz as an individual music art form and is perhaps ' \
                'the most important. It was during this time that the musical and cultural influences blended together ' \
                'to create jazz. No records were kept and recording studios and devices were not available, the history' \
                ' of pre-jazz is still mostly unknown. The social and cultural influences appeared to come from all ' \
                'directions. The African musical traditions that continued as a part of the slave culture and these ' \
                'traditions were superimposed on the dominant white musical culture.'

s = Era('Before Jazz', datetime(1936, 1, 1), datetime(1944, 1, 1), 
        image='https://www.messynessychic.com/wp-content/uploads/2022/01/scott-AJM-1999-20-284-001.jpg',
        display_date=False, color='#B2C063', intro=s_intro)

t = Landmark(Size.SMALL, 'A Darker Shade of Blue', datetime(1980, 3, 12), color='#7c45b9')

u_intro = f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus aliquam et elit nec" \
          f" condimentum. Morbi sit amet felis dolor. Vestibulum molestie eleifend iaculis. " \
          f"Ut augue augue, varius id aliquet ac, vehicula sit amet purus. Nullam quis ex dictum purus " \
          f"fringilla pretium in in justo. Cras nec metus ligula. Aenean nec luctus lorem, sit amet aliquet " \
          f"ligula. Pellentesque vestibulum vitae neque ultricies gravida. Nam faucibus blandit lectus, eu " \
          f"lobortis tellus fringilla sit amet. Duis auctor cursus est, nec eleifend lacus ullamcorper" \
          f" vel. In varius congue lorem, vitae maximus mi faucibus a. Pellentesque efficitur pellentesque " \
          f"magna in pulvinar. Morbi viverra ultrices sapien, quis placerat diam tincidunt non."

u = Landmark(Size.LARGE,
             'Title 1',
             datetime(1950, 7, 12),
             color='#B2C063',
             intro=u_intro,
             image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpbs.twimg.com%2Fprofile_images%2F428316729220276224%2FEdBZ2Kgp.jpeg&f=1&nofb=1&ipt=6088c5a2c1f1f40bbf88c24c95a37af5d7982fda497d01780314cfdc9d2432fb'
             )

v_intro = 'son of Miles Davis'

v = Person(Size.LARGE, 'Miles Davis jr.',
           active_start=datetime(1984, 3, 12), active_end=datetime(1999, 8, 10),
           birthday=datetime(1956, 4, 8), deathday=datetime(2020, 10, 23),
           color='#7c45b9', intro=v_intro)

w = Person(Size.LARGE, 'Miles Davis III',
           active_start=datetime(1994, 3, 12), active_end=datetime(1999, 8, 10),
           birthday=datetime(1990, 4, 8), deathday=datetime(2040, 10, 23),
           color='#9b1818', intro=u_intro)

x = Landmark(Size.LARGE, 'Paul Bufano Paul Bufano Paul Bufano Paul Bufano Paul Bufano',
             datetime(1955, 3, 12), color='#7c45b9')

y = Landmark(Size.LARGE, 'Paul Bufano Paul Bufano Paul Bufano Paul Bufano Paul Bufano',
             datetime(1970, 3, 12), color='#7c45b9', intro='A short intro for Paul')

z = Landmark(Size.LARGE, 'Paul Bufano Paul Bufano Paul Bufano Paul Bufano Paul Bufano',
             datetime(1944, 3, 12), color='#B2C063', intro=u_intro, image='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fy.yarn.co%2F46d3497c-75ea-4b52-9e87-883593080a3b_screenshot.jpg&f=1&nofb=1&ipt=ba1b9e2e60eb2900d145a84e0ff1aaace10fff78917d70e0bb651ff3838b0538')

aa = Person(Size.LARGE, 'Paul Bufano Paul Bufano Paul Bufano Paul Bufano Paul Bufano',
            datetime(1998, 3, 12), datetime(1999, 8, 10),
            datetime(1953, 4, 8), datetime(1999, 8, 13), color='#9b1818', intro='Paul B')

ab = Person(Size.MEDIUM, 'Paul Bufano Paul Bufano Paul Bufano Paul Bufano Paul Bufano',
            datetime(1970, 3, 12), datetime(1999, 8, 10),
            datetime(1953, 4, 8), datetime(1999, 8, 13), color='#7c45b9', intro=u_intro)

# b_relationships = [o, c, l]
# b.set_relationships(b_relationships)
landmarks = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab]
