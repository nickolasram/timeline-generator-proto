from datetime import datetime
from timeline_landmark import Landmark, Size, Relationship
from timeline_person import Person
from timeline_era import Era
from timeline_image import Image
from timeline_link import Link

color_pj = '#B2C063'
pre_jazz_image = Image('https://www.messynessychic.com/wp-content/uploads/2022/01/scott-AJM-1999-20-284-001.jpg')
pre_jazz = Era(title='Before Jazz', active_start=datetime(1878, 1, 1), display_date=False,
               images=[pre_jazz_image],
               color=color_pj, intro='Jazz was born from the synthesis of many musical traditions ranging from Classical music '
                                     'to slave work songs, from western african music to the relatively new genre of ragtime, and much more.')

n_o_music_scene = Landmark(color=color_pj, size=Size.LARGE, date=datetime(1878, 1, 2),
                           title='New Orleans Music Scene Pre-Jazz', display_date=False)

gospel_desc = 'Chastized as the devil’s music, jazz may have even deeper ties with the house of God. “You heard the pastors in the Baptist churches,” explained ' \
              'Paul Barbarin, one of the finest of the early New Orleans jazz drummers,' \
              '“they were singing rhythm. More so than a jazz band.” “Those Baptist' \
              'rhythms were similar to the jazz rhythms,” concurred Crescent City banjoist' \
              'Johnny St. Cyr, “and the singing was very much on the blues side.” Kid' \
              'Ory, the most famous of the New Orleans trombonists, claimed Bolden' \
              'drew inspiration from the church, not the nightlife of Storyville: “Bolden' \
              'got most of his tunes from the Holy Roller Church, the Baptist church on' \
              'Jackson Avenue and Franklin. I know that he used to go to that church, but' \
              'not for religion. He went there to get ideas on music.”'

gospel = Landmark(color=color_pj, title='gospel', size=Size.SMALL, date=datetime(1878, 1, 3),
                  display_date=False, description=gospel_desc)

bb_img = Image('https://thumbnailer.digitalnz.org/?resize=664%3E&src=https%3A%2F%2Fndhadeliver.natlib.govt.nz%2FNLNZStreamGate%2Fget%3Fdps_pid%3DIE212927')

bb_desc = 'Drummer Baby Dodds recalled the instrumentation for the marching brass bands:' \
          '"There was a traditional line-up for the New Orleans parades. The ' \
          'trombones were always first. Behind the trombones would be the ' \
          'heavy instruments, like bass, tubas and baritones. Then behind them ' \
          'were the altos, two or three alto horns, and behind them were the ' \
          'clarinets. It was very good if there were two. Usually it was only one, ' \
          'an E flat. Then behind the clarinets would come the trumpets, always ' \
          'two or three, and they came next. Bringing up the rear would come the ' \
          'drums, only two, a bass drum and a snare drum. That was for balance. ' \
          'For funeral marches the snare drum is muffled by pulling the snares ' \
          'off. When the snares are off it’s the same as a tom-tom. But you don’t ' \
          'muffle drums with parades, or going back from the cemetery. At most ' \
          'there were eleven or twelve men in the whole brass band." Sometimes the same instrumentation ' \
          'would be employed for dances, but in many instances a smaller subset of these musicans, often joined by ' \
          'string players, would be used. The repertoire of these bands was remarkably ' \
          'varied. In addition to concert and march music, the ensembles also knew a range of quadrilles, polkas, ' \
          'schottisches, mazurkas, two-steps, and other popular dance styles. As the ragtime craze ' \
          'swept the country around the turn of the century, syncopated pieces became more and more frequently ' \
          'played by these bands, a shift that was accompanied by increased interest in “ragging” more traditional ' \
          'compositions. This blurring of musical genres was, as we shall see, central to the creation of jazz music.'

brass_bands = Landmark(color=color_pj, title='brass bands', size=Size.SMALL, date=datetime(1878, 1, 4),
                       display_date=False, images=[bb_img], description=bb_desc)


ragtime = Landmark(color=color_pj, title='ragtime', size=Size.SMALL, date=datetime(1878, 1, 5),
                       display_date=False)

classical_desc = 'The influence of this highbrow, European musical tradition was' \
                 'especially strong within the local black Creole culture.'

classical = Landmark(color=color_pj, title='classical', size=Size.SMALL, date=datetime(1878, 1, 6),
                       display_date=False, intro='European concert music, opera, and drama', description=classical_desc)

string_bands = Landmark(color=color_pj, title='String ensembles', size=Size.SMALL, date=datetime(1878, 1, 7),
                        display_date=False, intro='Ensembles hired to play at clubs, parties, and other social events')

blues = Landmark(color=color_pj, title='The Blues', size=Size.SMALL, date=datetime(1878, 1, 8),
                 display_date=False)

excelsior = Landmark(color=color_pj, title='Excelsior Brass Bands', size=Size.SMALL, date=datetime(1879, 1, 1),
                     intro='one of the best known brass bands')
excelsior.landmark_end_date = datetime(1931, 1, 1)

onward = Landmark(color=color_pj, title='Onward Brass Bands', size=Size.SMALL, date=datetime(1886, 1, 1),
                  intro='one of the best known brass bands')
onward.landmark_end_date = datetime(1930, 1, 1)

color_noj = '#7c45b9'

noj_img = Image('https://cdn.britannica.com/80/205980-050-190E3A67/Buddy-Bolden-Band-New-Orleans-Jimmie-Johnson-1905.jpg',
                'Buddy Bolden Band, New Orleans, c. 1905: (back row from left to right) Jimmie Johnson, Buddy Bolden, '
                'Brock Mumford, and Willie Cornish and (front row from left to right) Frank Lewis and Willie Warner.')

new_orleans_jazz = Era(active_start=datetime(1889, 1, 1), end_year=datetime(1927, 1, 1), color=color_noj,
                       title='New Orleans Jazz', images=[noj_img])

new_orleans_img = Image('https://cdn.britannica.com/92/64492-050-C5D590BE.jpg')
new_orleans = Landmark(size=Size.SMALL, color=color_noj, title='New Orleans', display_date=False,
                       date=datetime(1889, 1, 2), images=[new_orleans_img])

storyville_desc = 'A red-light district in New Orleans that existed for a scant twenty years' \
                  'usually considered the birthplace of jazz. Though ' \
                  'close investigation of the facts casts more than a few doubts on this history.' \
                  'Donald Marquis, a leading expert on New Orleans jazz who painstakingly researched the life of Buddy' \
                  'Bolden—commonly credited with being the first jazz musician— was' \
                  'forced to conclude that Bolden “did not play in the brothels. None of the' \
                  'musicians who were interviewed remembered playing with a band in a' \
                  'whorehouse, nor did they know of anyone who had.”'

storyville = Landmark(size=Size.SMALL, title='StoryVille',
                      intro='The birthplace of Jazz?', date=datetime(1897, 7, 6),
                      description=storyville_desc, color=color_noj
                      )
storyville.landmark_end_date = datetime(1917, 11, 12)

buddy_desc = 'Buddy Bolden, often cited as the first jazz musician, may well be the most mysterious figure in the ' \
             'annals of New Orleans music. No recordings survive of this seminal figure—despite the rumored existence ' \
             'of a cylinder recording from the turn of the century—and no mention of his music appeared in print until ' \
             '1933, two years after his death, and some three decades after Bolden contributed to the revolutionary ' \
             'birth of a new style of American music. Bolden would have been exposed to music not only at various social ' \
             'events, but also at church and in school—in fact, two of John Robichaux’s ' \
             'musicians taught at the Fisk School for Boys, which Bolden likely attended. At some point in ' \
             'the mid-1890s, Bolden began playing the cornet, initially taking lessons from a neighbor, and ' \
             'was soon supplementing his income as a plasterer with earnings from performing. ' \
             'At this remove, it is hard to evaluate how much formal training Bolden enjoyed. Members of the Robichaux ' \
             'band dismissed Bolden’s group as a bunch of “routineers,” by which they meant fakers.' \
             ' Yet Bolden listed himself as a “music teacher” in the local directory. Unlike many New Orleans horn ' \
             'players, Bolden’s initiation into the public music life of the city came not through the brass ' \
             'bands that figured prominently in the local social life, but instead as a member of the string ' \
             'ensembles that entertained at dances and parties. Bolden’s single biggest contribution to jazz may have' \
             ' been his focus on the blues. “On those old, slow, lowdown blues, he had a moan in his cornet that' \
             ' went right through you,” trombonist Bill Matthews recalled, “just like you were in church or something.”' \
             'Bolden was likely incorporating the blues sensibility and structure into his music around this same time.' \
             'Certainly Bolden, even if he did not invent jazz, had mastered the recipe for it, which combined the rhythms ' \
             'of ragtime, the bent notes and chord patterns of the blues, and an instrumentation drawn from New Orleans ' \
             'brass bands and string ensembles. As we have seen, the syncopated rhythms of ragtime' \
             ' spread into the mainstream of American culture before the the blues became well known, ' \
             'and Bolden can hardly take credit for this aspect of African American music, ' \
             'although it certainly served as another key ingredient in his work. ' \
             'Yet his instistence on marrying these syncopations to the blues, in an era ' \
             'when the latter idiom existed only on the fringes of the music world, was ' \
             'a brash move, and no doubt a key reason why he captured the attention of' \
             ' his contemporaries and the later chroniclers of New Orleans jazz.'

bolden_img = Image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Buddy_Bolden_001.png/800px-Buddy_Bolden_001.png',
                   'Bolden c.1905')
buddy_bolden = Person(size=Size.LARGE, title='Buddy Bolden',
                      intro='the father of jazz', birthday=datetime(1877, 9, 6), deathday=datetime(1931, 11, 4),
                      active_start=datetime(1890, 1, 1), active_end=datetime(1907, 1, 1), color=color_noj,
                      images=[bolden_img],
                      description=buddy_desc
                      )
buddy_bolden.key_points = ['Often cited as the first jazz musician',
                           'Synthesized music styles such as gospel, the blues, and popular string ensemble music',
                           'Born in New Orleans']
buddy_bolden.sources = ['The History Of Jazz ( Ted Gioia)',
                          'https://en.wikipedia.org/wiki/Buddy_Bolden']


oejf_desc = 'Although Bolden has been typically heralded as the progenitor of jazz, such simplistic lineages ignore the' \
            ' broader musical ferment taking place in turn-of-the-century New Orleans. Many musicians—mostly black, ' \
            'but also Creole and white— were experimenting with the syncopations of ragtime and the blues' \
            ' tonality and applying these rhythmic and melodic devices to a wide range of compositions. At first, ' \
            'improvisational techniques were probably used merely to ornament composed melodies, but at some point ' \
            'these elaborations must have evolved into more free-form solos. What began as ' \
            'experimentation eventually led to formalized practice. Reconstructing these events with ' \
            'any precision is all but impossible—a terminology for describing this music would not ' \
            'exist for quite some time, and the first recordings of this new style would not be made for at least twenty' \
            ' years. Whether Bolden was the decisive figure or merely one among many to spur this transformation remains' \
            ' a matter for speculation. In any event, all our research indicates that sometime around the' \
            ' end of the nineteenth century, a growing body of musicians in New Orleans were playing a type of music' \
            ' that, with benefit of hindsight, can only be described as jazz. ' \
            'A number of uptown cornetists built on the foundations that Bolden and others had created, including Bunk' \
            ' Johnson, Joe “King” Oliver, Mutt Carey, and later, Louis Armstrong, the greatest of the New Orleans ' \
            'trumpeters. But jazz quickly leaped over the racial barriers that divided New Orleans in the ' \
            'early 1900s. Musicians who were early practitioners of this new idiom also included Creoles' \
            ' Sidney Bechet, Jelly Roll Morton, Kid Ory, and Freddie Keppard, as well as white' \
            ' players Papa Jack Laine, Emmett Hardy, Sharkey Bonano, and Nick LaRocca.' \
            ' By the 1920s, when the first recordings of a wide range of New Orleans jazz ensembles' \
            ' were made, the ethnic mix of the local bands was almost as diverse as the city’s population. These ' \
            'recordings featured, in addition to the major black and Creole players, such ensembles as' \
            ' Johnny Bayersdorffer’s Jazzola Novelty Orchestra, a solid New Orleans jazz band composed' \
            ' of musicians of central and southern European ancestry; Russ Papalia’s' \
            ' orchestra, another jazz unit, this one primarily comprising Italian Americans; and ' \
            'the New Orleans Owls, which included in its ranks, among others, clarinetist Pinky Vidacovich, pianist ' \
            'Sigfre Christensen, trombonist Frank Netto, banjoist Rene Gelpi, and tuba player Dan LeBlanc—a lineup whose' \
            ' lineage spanned much of Europe. Certainly jazz remained primarily an African American contribution to the ' \
            'city’s— and, eventually, the nation’s—culture; but like all such contributions, once given,' \
            ' it no longer remained the exclusive property of the giver. Instead, destined to become part' \
            ' of the broader cultural gene pool, it was taken up with enthusiasm by musicians of all colors,' \
            ' all nationalities.'

other_early_jazz_figures = Landmark(size=Size.MEDIUM, title='other early jazz figures', description=oejf_desc,
                                    color=color_noj, display_date=False, date=datetime(1890, 1, 2),
                                    intro='Bunk Johnson, Joe Oliver, Louis Armstrong and more')

eagle_desc='The Eagle Band was an American jazz band during the Ragtime and Early Jazz periods, stationed in New Orleans' \
           ', Louisiana. The instrumentation of the band was clarinet, drums, trombone, trumpet, guitar, and' \
           ' string bass, with one person on an instrument. The band was originally known as The Buddy Bolden Band,' \
           ' under the direction of Buddy Bolden from 1895–1906. On September 3, 1906, while playing in the Labor Day' \
           ' parade with his band, Buddy Bolden suffered a memorable breakdown, which included staggering out of ' \
           'marching formation and screaming. He was removed from the parade ranks and would permanently resign from the band' \
           '. After the resignation of Bolden, Frankie Dusen would be the one to lead the band, and change the name' \
           ' from The Buddy Bolden Band, to the Eagle Band, named after the Eagle Saloon on the corner of Perdido' \
           ' and Rampart Streets. The band maintained the popularity it had as The Buddy Bolden Band and primarily ' \
           'performed the same repertoire as before. Similar to the Hard Bop combo, Art Blakey and The Jazz' \
           ' Messengers, which would emerge in decades to come, The Eagle Band would serve as a stepping-stone' \
           ' for many prominent Hot Jazz players during the Early Jazz period. The Eagle Band was known as a very ' \
           'authentic, poignant band known for its ability to play slow gut-wrenching blues.'
eagle_img = Image('https://upload.wikimedia.org/wikipedia/commons/3/3e/Eagle_Band_1916_New_Orleans.jpg')
eagle_band = Landmark(size=Size.SMALL, title='The Eagle Band', intro="Buddy Bolden's band during the early jazz era",
                      date=datetime(1895, 1, 1), images=[eagle_img], color=color_noj, description=eagle_desc)
eagle_band.landmark_end_date = datetime(1929, 1, 1)

lsb_link = Link('https://www.youtube.com/watch?v=xPbLtSZc2-I&ab_channel=mrblindfreddy9999', 'Youtube Link')

lsb_desc='some twenty years transpired between Bolden’s glory days and the release of the first jazz recordings. ' \
         'Nor do these first commercial discs simplify the historian’s task. If anything, the ' \
         'opposite is true: the history of recorded jazz was initiated with an event that ' \
         'remains to this day clouded in controversy. And, as with so many of the ' \
         'loaded issues in the story of the music, the question of race lies at the core of the dispute. ' \
         'In an ironic and incongruous twist of fate, the Original ' \
         'Dixieland Jazz Band (ODJB), an ensemble consisting of white musicians, ' \
         'was the first to make commercial recordings of this distinctly African ' \
         'American music. Raised in New Orleans, these five instrumentalists—' \
         'leader and cornetist Nick LaRocca, clarinetist Larry Shields, trombonist ' \
         'Eddie Edwards, drummer Tony Sbarbaro, and pianist Henry Ragas—joined ' \
         'forces and performed in Chicago in 1916, then opened in New York in ' \
         'January 1917. During an engagement at Reisenweber’s Restaurant, the ' \
         'group attracted large audiences with its novel and spirited music, and ' \
         'spurred the interest of East Coast recording companies. Columbia was the ' \
         'first to record the band, but hesitated to release the sides because of the ' \
         'unconventional and ostensibly vulgar nature of the music. Soon after, the ' \
         'Victor label overcame such scruples, and a second session produced a major ' \
         'commercial success in “Livery Stable Blues.”'
lsb_img=Image('https://upload.wikimedia.org/wikipedia/commons/d/d2/Livery-stable.jpg')
livery_stable_blues = Landmark(title='Livery Stable Blues', color=color_noj, size=Size.MEDIUM, links=[lsb_link],
                               date=datetime(1917, 1, 1), intro='the first recorded jazz song', images=[lsb_img],
                               description=lsb_desc)

odjb_desc = 'The Original Dixieland Jass Band (ODJB) was a Dixieland jazz band ' \
            'that made the first jazz recordings in early 1917. Their "Livery Stable Blues"' \
            ' became the first jazz record ever issued. The group composed and recorded many jazz standards' \
            ', the most famous being "Tiger Rag". In late 1917, the spelling of the band\'s' \
            ' name was changed to Original Dixieland Jazz Band.' \
            'ODJB billed itself as "the Creators of Jazz". It was the first band to' \
            ' record jazz commercially and to have hit recordings in the genre. Band leader and' \
            ' cornetist Nick LaRocca argued that ODJB deserved recognition as the first band to' \
            ' record jazz commercially and the first band to establish jazz as a musical idiom or genre.'
odjb_image=Image('https://upload.wikimedia.org/wikipedia/commons/9/94/Tigerag.jpg')
odjb = Landmark(color=color_noj, title='Original Dixieland Jass Band', date=datetime(1916, 1, 1),
                description=odjb_desc, size=Size.SMALL, images=[odjb_image])
odjb.landmark_end_date = datetime(1926, 1, 1)

jelly_roll_desc = 'Jelly Roll Morton, the greatest of the New Orleans jazz composers, also ' \
                  'generated controversy by his claims to have invented the music. Indeed, ' \
                  'Morton was known to exaggerate about many things, so much so that he ' \
                  'has acquired the persona of a blustering loudmouth in most historical ' \
                  'accounts. However, a careful study of Morton’s firsthand recollections, ' \
                  'preserved by Alan Lomax in a series of taped interviews and performances ' \
                  'for the Library of Congress, reveals that this often maligned figure could ' \
                  'be, when the occasion warranted, one of the most thoughtful and accurate ' \
                  'sources of information on early jazz. Morton’s apprenticeship in the music business took' \
                  'place largely in the bordellos of Storyville (although Morton worked mainly ' \
                  'in the white bordellos where few other jazz players could follow). Rather ' \
                  'than regretting the low-life associations of the District, Morton luxuriated in ' \
                  'the company of pimps, prostitutes, murderers, gamblers, pool sharks, and ' \
                  'dealers and hustlers of various sorts, and at times could rely on a few of ' \
                  'these trades himself. At some point in the early 1900s—Morton claimed ' \
                  '1902, although this seems too early, given his birthdate—he began working ' \
                  'as a musician in Storyville. His great-grandmother expelled him from home ' \
                  'when she learned of his activities in the District, and before long Morton ' \
                  'started on the peripatetic freelancing that would occupy most of his life. His ' \
                  'early travels brought him to Memphis, New York, Chicago, St. Louis, ' \
                  'Detroit, Tulsa, Houston, and other locales. By 1917, Morton had traveled ' \
                  'farther west, visiting California, Canada, Alaska, and Mexico.' \
                  'when he returned to Chicago around 1923, Morton was well prepared to draw on his ' \
                  'considerable talents for self-promotion in building a musical career. ' \
                  'Certainly the time was ripe. The Jazz Age had begun in earnest, and Morton ' \
                  'looked to capitalize on the public’s insatiable demand for this new style of music.' \
                  'Morton’s Chicago years, which lasted until 1926, constitute the most ' \
                  'prolific musical period of his career. He made over one hundred recordings ' \
                  'or piano rolls of his compositions, published a steady stream of pieces, and ' \
                  'formed his most famous ensemble, the Red Hot Peppers. This band, which ' \
                  'recorded in both Chicago and New York during the remaining years of the ' \
                  'decade, achieved a level of collective artistry that few New Orleans groups ' \
                  'ever matched, and none surpassed. Nor would Morton’s preeminence as a ' \
                  'jazz composer—“the world’s greatest hot tune writer” was how his business ' \
                  'card modestly described it—be seriously challenged until Duke Ellington ' \
                  'pushed the limits of creativity even further in the following decade. But, ' \
                  'above all, in its mastery of ensemble interaction—so essential to the New ' \
                  'Orleans aesthetic—this band remains the paragon to this day. ' \
                  'Jelly Roll continued to record frequently during the remainder of the 1920s. ' \
                  'The members of his band changed regularly, but, regardless of the ' \
                  'sidemen or the evolving musical tastes of the American public, Morton’s ' \
                  'ensembles were at their best when working within the aesthetic constraints ' \
                  'of the classic New Orleans idiom. Noteworthy Morton recordings from the ' \
                  '1920s include an invigorating 1927 trio session with clarinetist Johnny ' \
                  'Dodds and drummer Baby Dodds, a tantalizing 1924 duet date with King ' \
                  'Oliver, and Morton’s 1923 work with the New Orleans Rhythm Kings.'
jelly_roll_img = Image('https://upload.wikimedia.org/wikipedia/commons/3/35/MortonBricktopRowCropMortonFace.jpg',
                       'Morton in 1918')
jelly_roll = Person(title='Jelly Roll Morton', birthday=datetime(1890, 9, 20), deathday=datetime(1941, 7, 10),
                    active_start=datetime(1904, 1, 1), active_end=datetime(1941, 7, 10), size=Size.LARGE,
                    images=[jelly_roll_img], color=color_noj, intro="the world's greatest hot tune writer",
                    description=jelly_roll_desc)

bb_blues_desc="Though no recording of Buddy Bolden's music exists, " \
              "Jelly Roll Morton immortalized the most mythical of New Orleans jazz pioneers" \
              " by covering Bolden's signature song, \"Funky Butt\" with" \
              " his composition that he titled, \"I Thought i Heard Buddy Bolden Say.\" " \
              "He recorded it twice in 1939, first for RCA Bluebird with a band that" \
              " included New Orleanians Sidney Bechet, Albert Nicholas, " \
              "Wellman Braud, and Zutty Singleton. Four months later, on December" \
              " 16, 1939, he recorded the tune as \"Buddy Bolden's Blues\" " \
              "on a solo session for General Records. It was later released in an album by Commodore."
bb_blues_link = Link('https://www.youtube.com/watch?v=qSFr1S0z6dA&ab_channel=cdbpdx', 'Youtube link')
bb_blues = Landmark(size=Size.SMALL, color=color_noj, title="Buddy Bolden's Blues",
                    date=datetime(1939, 12, 16), links=[bb_blues_link], description=bb_blues_desc)

color_jazz_age = '#9b1818'

jazz_age_intro = 'Revolutions, whether in arts or matters of state, create a new world only ' \
                 'by sacrificing the old. With jazz, it is no different. To be sure, Louis ' \
                 'Armstrong, who closed the book on the dynastic tradition in New Orleans ' \
                 'jazz—putting an end to its colorful lineage of Kings Bolden, Keppard, and ' \
                 'Oliver—stands out as an unlikely regicide. Armstrong always spoke with ' \
                 'deference, bordering on awe, of his musical roots, and with especial ' \
                 'devotion of his mentor Joe Oliver. Yet the evidence of the grooves does not ' \
                 'lie: the superiority of Armstrong’s musicianship, the unsurpassed linear ' \
                 'momentum of his improvised lines, could serve only to make Oliver, ' \
                 'Morton, Bolden, and the whole New Orleans ensemble tradition look passé, ' \
                 'a horse-and-buggy cantering by Henry Ford’s assembly line. The New ' \
                 'Orleans pioneers exit stage left; Armstrong on trumpet enters stage right' \
                 'heralding the new Age of the Soloist.'
jazz_age_desc = 'Or so it seems in retrospect. But the ebb and flow of any history seldom ' \
                'match the rigid categories and sharp delineations we apply after the fact. In ' \
                'actuality, the revolution initiated by Armstrong took place in fits and starts, ' \
                'and with little fanfare at the time. After Armstrong’s departure from King ' \
                'Oliver’s Creole Jazz Band, over a year would pass before he would record ' \
                'as a leader. And even when those famous recordings were planned—the ' \
                'classic “Hot Fives”—the record company considered enlisting a betterknown ' \
                'leader to front the band. Most accounts stress that Armstrong’s ' \
                'talents may have been neglected by the general public, but were amply ' \
                'recognized by the musical community—“his playing was revered by ' \
                'countless jazz musicians,” runs a typical commentary—but even this claim ' \
                'is suspect. Fletcher Henderson, Armstrong’s first major employer after' \
                ' Oliver, made the trumpeter accept a cut in pay to join his band. Many ' \
                'accounts suggest that Henderson, in fact, preferred the playing of cornetist ' \
                'Joe Smith, and that Armstrong was hired only because Smith was unavailable.' \
                ' Armstrong may not have taken New York, or even the Henderson band, ' \
                'by storm, but slowly and steadily he exerted his influence on the musical ' \
                'community. Brass players were the first to feel the heat of Armstong’s ' \
                'rising star; but, as with Charlie Parker’s innovations twenty years later, ' \
                'Armstrong’s contributions eventually spread to every instrument in the ' \
                'band. Don Redman’s arrangements, Coleman Hawkins’s saxophone work— one by one, the converts were won.'
jazz_age_img = Image('https://cdn.thecollector.com/wp-content/uploads/2022/03/ma-rainey-jazz-age-band-photo-1924-1925.jpg?width=1200&quality=55',
                     'Gertrude Ma Rainey and her Georgia Jazz Band in Chicago in 1923. Bridgeman Images')
gatsby_img = Image('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/The_Great_Gatsby_Cover_1925_Retouched.jpg/500px-The_Great_Gatsby_Cover_1925_Retouched.jpg',
                   'The Great Gatsby, Fitzgerald. Fitzgerald explores the major developments of the Roaring Twenties, including the Jazz Age.')
jazz_age = Era(active_start=datetime(1920, 1, 1), end_year=datetime(1929, 1, 1), color=color_jazz_age,
               title='The Jazz Age', images=[jazz_age_img, gatsby_img], intro=jazz_age_intro, description=jazz_age_desc)

chicago_img = Image('https://cdn.britannica.com/51/64751-050-24A999CB.jpg')
chicago = Landmark(color=color_noj, title='Chicago', size=Size.SMALL, date=datetime(1910, 1, 2), display_date=False,
                   images=[chicago_img])

new_york_img = Image('https://cdn.britannica.com/89/64489-004-8CE3B4B5.jpg')
new_york = Landmark(color=color_jazz_age, title='New York', size=Size.SMALL, date=datetime(1920, 1, 3), display_date=False,
                    images=[new_york_img])

sidewalk_desc = 'This number was recorded in Chicago at the Webster Hotel on September 21st 1926 with George Mitchell ' \
                'cornet, Kid Ory trombone, Barney Bigard, Omer Simeon, and Darnell Howard clarinets, Ferd "Jelly Roll"' \
                ' Morton piano & speech, Johnny St Cyr guitar & speech, John Lindsay bass, Andrew Hilaire drums, ' \
                'and Marty Bloom sound effects.' \
                'Morton’s 1926 recording of his “Sidewalk Blues” testifies to the results ' \
                'achieved by this single-mindedness. The piece begins with a roll call, a tenbar ' \
                'introduction in which each major instrument is summoned to order: ' \
                'piano, trombone, cornet, and clarinet. This leads directly into a twelve-bar ' \
                'cornet melody statement over blues harmonies supported by a stop-time ' \
                'vamp. Stop-time techniques such as this—here the band propels the soloist ' \
                'with sharp accents on beats two and four—were a trademark of Morton’s ' \
                'music, invariably used for a brief spell to add variety to the accompaniment. ' \
                'A second twelve-bar melody follows, this time employing the interlocking ' \
                'trombone-cornet-clarinet counterpoint style, which is the calling card of ' \
                'classic New Orleans jazz. The piece then returns to the opening twelve-bar' \
                ' melody, but with the clarinet taking the lead this time. A four-bar interlude ' \
                'segues into a new thirty-two-bar melody played by cornet, trombone, and ' \
                'clarinet (interrupted briefly at bar sixteen by a car horn, a typical Morton' \
                ' novelty twist) that abandons the blues form and sensibility in favor of a ' \
                'plaintive parlor song style. This thirty-two-bar melody is repeated, but now ' \
                'played in an arrangement for three clarinets. In the context of the New ' \
                'Orleans style, this was a startling device. Morton brought two extra ' \
                'clarinetists to the session, letting them sit idly by most of the day, merely ' \
                'requiring their presence at certain key junctures of the performances such as ' \
                'this interlude. This change of instrumentation in midsong, so rare in other ' \
                'jazz recordings of the period, is representative of Morton’s penchant to pull ' \
                'out some surprising sound at unexpected places in his music. This ' \
                'understated clarinet section changes direction dramatically in the final eight ' \
                'bars, with the return of the energetic New Orleans–style counterpoint. A ' \
                'five-bar tag closes this whirlwind three-and-a-half-minute performance. In a ' \
                'compact form, Morton has covered a world of sounds.'
sidewalk_img = Image('https://ia902301.us.archive.org/1/items/edison-51897_01_11361/cusb_ed_51897_01_11361_0b.jpg?cnt=0')
sidewalk = Landmark(size=Size.SMALL, title='Sidewalk Blues', color=color_noj, date=datetime(1926, 9, 21),
                    description=sidewalk_desc, images=[sidewalk_img])

rhp_img = Image('https://64parishes.org/wp-content/uploads/2013/03/3077.jpg',
                '1926, Illinois, Chicago, Jelly Roll Morton and His Red Hot Peppers, L-R: Omer Simeon, Andrew Hilaire, John Lindsay, Jelly Roll Morton (seated in front), Johnny St. Cyr, Kid Ory, George Mitchell. (Photo by Michael Ochs Archive)')
red_hot_peppers = Landmark(size=Size.MEDIUM, date=datetime(1926, 1, 1), color=color_noj, title='Red Hot Peppers',
                           images=[rhp_img])
red_hot_peppers.landmark_end_date = datetime(1930, 1, 1)

diaspora_desc = 'One of the supreme ironies of the history of New Orleans jazz is that so ' \
                'much of it took place in Chicago. By the early 1920s, the center of the jazz ' \
                'world had clearly shifted northward. New Orleans musicians continued to ' \
                'dominate the idiom, but they were now operating far afield from their ' \
                'native soil. Well before the middle of the decade, a large cadre of major ' \
                'New Orleans jazz musicians were making their reputations in other locales' \
                '—Jelly Roll Morton left New Orleans around 1908; Freddie Keppard ' \
                'departed in 1914 (if not earlier); Sidney Bechet in 1916, Jimmie Noone in ' \
                '1917, King Oliver in 1918, Kid Ory in 1919, Johnny Dodds around that ' \
                'same time, Baby Dodds in 1921, and Louis Armstrong in 1922. These ' \
                'moves may have begun as brief stints on the road, but in the end proved all ' \
                'but permanent. The vast majority of the New Orleans diaspora never ' \
                'returned to their home state except for brief visits.' \
                'This exodus was anything but a purely musical phenomenon. Between ' \
                'the years 1916 and 1919, a half-million African Americans left the South ' \
                'for more tolerant communities in the North, with almost one million more ' \
                'following in their wake in the 1920s. This vast population shift, which has ' \
                'since come to be known as the Great Migration, encompassed the whole ' \
                'range of black society, from doctors and lawyers to musicians and ' \
                'ministers, from teachers and merchants to artisans and manual laborers. ' \
                'Musicians moved north for the same reasons that motivated other groups: ' \
                'the search for a better life, for greater opportunities to work, to support a ' \
                'family, to enjoy a modicum of personal freedom—options that were much ' \
                'harder for an African American to pursue in the segregated South. As a ' \
                'result, in a host of major cities—Chicago, New York, Cleveland, Detroit, ' \
                'Philadelphia—the black population more than tripled between 1910 and 1930.'
diaspora = Landmark(size=Size.MEDIUM, color=color_noj, title='The New Orleans Diaspora',
                    date=datetime(1910, 1, 1), display_date=False, description=diaspora_desc)

louis_desc = 'Over the next several years, his ' \
             'playing graced a number of celebrated bands, including Kid Ory’s group ' \
             '(where he replaced Oliver, after the latter’s departure to Chicago), ' \
             'clarinetist Sam Dutrey’s Silver Leaf Band, Fate Marable’s riverboat' \
             ' ensemble, and Papa Celestin’s Tuxedo Brass Band. By the time Oliver sent ' \
             'for the young cornetist, Armstrong may have been unknown to jazz fans in ' \
             'Chicago; however, musicians in New Orleans were already taking note of ' \
             'this up-and-coming player.'
louis_img = Image('https://ids.si.edu/ids/deliveryService?max_w=800&id=NPG-NPG_94_43Armstrong-000002')
louis_armstrong = Person(color=color_noj, size=Size.LARGE, title='Louis Armstrong', birthday=datetime(1901, 8, 4),
                         deathday=datetime(1971, 6, 6), active_start=datetime(1918, 1, 1), active_end=datetime(1971, 1, 1),
                         images=[louis_img], description=louis_desc)

king_oliver_img = Image('https://upload.wikimedia.org/wikipedia/commons/5/52/King_Oliver_%281915_portrait%29.jpg')
king_oliver = Person(color=color_noj, size=Size.LARGE, title='Joe "King" Oliver', birthday=datetime(1881, 12, 19),
                     deathday=datetime(1938, 4, 10), active_start=datetime(1907, 1, 1), active_end=datetime(1937, 1, 1),
                     images=[king_oliver_img])

king_band_desc = 'In the year 1921 Oliver took a group of musicians to California for a short stint, ' \
                 'this group would become the foundation of what would later be renamed as King Oliver’s Creole Jazz ' \
                 'Band.In 1922 Oliver returned to Chicago with his group which featured both Johnny and Warren Dodds ' \
                 '(clarinet & drums), Honore Dutrey (trombone), William Jones (bass) and pianist Lillian Hardin,' \
                 ' who later married Louis Armstrong, becoming his second wife. In this same year, Oliver sent' \
                 ' via telegram for Louis Armstrong to join him in his new band as his second cornet.'
king_oliver_band = Landmark(title="King Oliver's Creole Jazz Band", color=color_noj, date=datetime(1921, 1, 1),
                            size=Size.MEDIUM, description=king_band_desc)



kid_ory_img = Image('https://upload.wikimedia.org/wikipedia/commons/5/50/Kidory.png')
kid_ory = Person(color=color_noj, size=Size.LARGE, title='Kid Ory', birthday=datetime(1886, 12, 25),
                 deathday=datetime(1973, 1, 23), active_start=datetime(1910, 1, 1), active_end=datetime(1966, 1, 1),
                 images=[kid_ory_img])

ory_band_desc = 'Ory moved his six-piece band to New Orleans in 1910. Ory had one of the best-known bands in New' \
               ' Orleans in the 1910s, hiring many of the great jazz musicians of the city, including the cornetists' \
               ' Joe "King" Oliver, Mutt Carey, and Louis Armstrong, who joined the band in 1919;' \
               ' and the clarinetists Johnny Dodds and Jimmie Noone. This iteration of his band existed (with the' \
               'occasional member joing or leaving) until 1919 when Ory moved to Los Angeles and formed a new ensemble.'
kid_ory_band = Landmark(color=color_noj, size=Size.MEDIUM, title="Kid Ory's Band",
                        date=datetime(1910, 1, 1), description=ory_band_desc)
kid_ory_band.landmark_end_date=datetime(1919, 1, 1)

sidney_bechet_desc = 'Bechet played the most prominent role in developing the clarinet as a ' \
                     'mature solo voice in jazz. Other performers, no doubt, also contributed—' \
                     ' hear, for instance, Leon Roppolo’s underappreciated recordings with the ' \
                     'New Orleans Rhythm Kings that gave notice of the instrument’s potential as ' \
                     'early as 1922—yet Bechet’s role was especially influential in pointing the ' \
                     'way toward a more melodic, linear conception of the horn, and drawing on ' \
                     'a more expansive palette of sounds. Much like King Oliver, Bechet ' \
                     'developed a voicelike quality to his playing, and exhibited a rare sensitivity ' \
                     'to the potential of timbre and phrasing. These skills allowed him to stand ' \
                     'out as a premier soloist, yet—unlike Armstrong—Bechet felt equally at ' \
                     'home submerging his melody lines in the larger ensemble.'
sidney_bechet_img = Image('https://upload.wikimedia.org/wikipedia/commons/c/c9/Bechet.gif')
sidney_bechet = Person(size=Size.LARGE, birthday=datetime(1897, 5, 14),
                       deathday=datetime(1959, 5, 14), active_start=datetime(1908, 1, 1),
                       active_end=datetime(1957, 1, 1), color=color_noj,
                       images=[sidney_bechet_img], intro='Armstrong’s stiffest challenge',
                       title='Sidney Bechet', description=sidney_bechet_desc)


clarence_five_desc = "a studio band only, formed after the success of King Oliver's recordings in order" \
                " to explore the market for blues-oriented music. Armstrong’s stiffest challenge during" \
                " these months leading up to the Hot Five recordings came in a " \
                "different setting. As a sideman in the Clarence Williams Blue Five, Armstrong " \
                "faced off with Sidney Bechet—“the only man who,” in the words of critic" \
                " Gary Giddins, “for a short while, seemed [Armstrong’s] equal as an " \
                "improviser during those transitional years.”"
clarence_five = Landmark(size=Size.MEDIUM, color=color_jazz_age, title="Clarence Williams' Blue Five",
                         date=datetime(1924, 1, 1), description=clarence_five_desc)

armstrong_migrates = Landmark(size=Size.NODE, title='Armstrong migrates to Chicago', date=datetime(1919, 1, 1), color=color_noj)
bechet_migrates = Landmark(size=Size.NODE, title='Bechet migrates to Europe', date=datetime(1919, 1, 2), color=color_noj)

early_every_morn_img = Image('https://images.genius.com/c28f10c94ebc48c7a0f9a09c9ac4d62a.996x1000x1.jpg')
early_every_morn_desc = 'This difference in temperament between the two great New Orleans ' \
                                'players is evident in their December 1924 pairing on “Early Every Morn,” ' \
                                'where they ostensibly support vocalist Alberta Hunter. Bechet’s soprano ' \
                                'work, with its mixture of high held notes and diving phrases into the lower ' \
                                'register, blends well with the group and provides ample space for ' \
                                'Armstrong’s countermelodies. Armstrong, in contrast, assumes a more ' \
                                'assertive posture and belts out a flamboyant coda to the performance, one ' \
                                'that tends to eclipse Hunter and the rest of the band. Such exhibitions of ' \
                                'technique were not Bechet’s forte. Yet he too could indulge in ' \
                                'grandstanding when the situation so warranted. On another collaboration ' \
                                'from the period, “Texas Moaner Blues,” Armstrong again takes center stage ' \
                                'with a brief burst of double time in his feature break, but Bechet is not to be' \
                                'outdone in this encounter. He lets loose a swarming cannonade of angular ' \
                                'phrases, less fluid than the cornetist’s, but clearly signaling a determination ' \
                                'to match any contender note for note, even the great Louis Armstrong. And ' \
                                'this time Bechet steals the show with a bluesy coda.'
early_every_morn = Landmark(size=Size.SMALL, title='Early Every Morn', date=datetime(1924, 12, 22),
                            description=early_every_morn_desc, color=color_noj, images=[early_every_morn_img])

bix_img = Image('https://cdn.britannica.com/98/6398-004-DE3BE588/Bix-Beiderbecke.jpg?w=300')
bix_desc = 'Beiderbecke’s first major band, the Wolverines, brought together a group ' \
           'of like-minded instrumentalists. These all but unknown young jazz devotees ' \
           'took their inspiration primarily from the performances of the New Orleans ' \
           'Rhythm Kings. During that band’s engagement at Friar’s Inn, members of ' \
           'Bix’s circle were frequently in attendance: listening, learning, sometimes ' \
           'sitting in with the group. A chance to put this education into practice came ' \
           'in October 1923, when clarinetist Jimmy Hartwell succeeded in obtaining ' \
           'regular employment for the Wolverines at the Stockton Club, located ' \
           'seventeen miles north of Cincinnati. Performances here and at other venues ' \
           'in the area gave the musicians ample opportunity to refine their craft and ' \
           'develop an enthusiastic local following; but greater fame would have been ' \
           'inconceivable this far distant from the major music capitals of America had ' \
           'not the Wolverines secured an opportunity to spend a day recording at the ' \
           'Gennett recording studio in Richmond, Indiana, some 125 miles away from ' \
           'Cincinnati. This was a turning point, not only in documenting the band’s ' \
           'progress to date, but also in reinforcing the confidence of this group of ' \
           'novices to the music industry. “No amount of words could adequately ' \
           'describe the excitement and utter amazement of that first recording, played ' \
           'back to us for correction of positions around the recording horns,” recalled ' \
           'George Johnson, tenorist with the group. “I doubt if any of us realized until ' \
           'that moment how different in style and how dissimilar in effect our results ' \
           'were from the music of the Friar’s band that had thrilled us all so, barely ' \
           'months before.” Beiderbecke’s debut recordings with the Wolverines only hint at the ' \
           'potential of the young cornetist. His solos, for all their poise, are ' \
           'melodically simple by comparison with the work he would create over the ' \
           'next several years. Evidence of Beiderbecke’s sensitivity to altered tones is ' \
           'apparent—hear his use of flatted fifths and ninths in his work on “Riverboat ' \
           'Shuffle”—but one also notes the relaxed delivery, so characteristic of Bix’s ' \
           'phrasing. Above all, the expressive, at times haunting, tone of ' \
           'Beiderbecke’s cornet demands our attention. Bix may not have mastered the ' \
           'dirty, rough-edged sound of a King Oliver, a style vastly influential at this ' \
           'stage in the history of jazz; nor do his solos burst forth with the unbridled ' \
           'energy that Armstrong would soon bring to the music. But they sing in a ' \
           'way that was unique in the context of mid-1920s jazz. Not so much played, ' \
           'they sound as though lofted gently from the bell of the horn, left to float in a stream of warm air. ' \
           'These halcyon days, which lasted from the middle of the decade to the ' \
           'stock market crash of 1929, witnessed much of Beiderbecke’s greatest ' \
           'work. But this period also encompassed an exceptional flourishing of ' \
           'improvised music on a much wider scale, one that music historians have ' \
           'come to designate simply as Chicago jazz. Beiderbecke’s contributions, as ' \
           'great as they are, were just one facet of this new sound, this new style.'
bix_beiderbecke = Person(size=Size.LARGE, title='Bix Beiderebecke', birthday=datetime(1903, 2, 10),
                         deathday=datetime(1931, 8, 6), active_start=datetime(1920, 1, 2), active_end=datetime(1931, 8, 6),
                         color=color_jazz_age, images=[bix_img])

bix_death = Landmark(size=Size.NODE, title='Bix beiderbecke passes away', date=datetime(1931, 8, 6), color=color_jazz_age)

chicago_jazz_desc = 'Like the New Orleans tradition that preceded it, and the Swing Era offerings that ' \
                    'followed it, Chicago jazz was not just the music of a time and place, but ' \
                    'also a timeless style of performance—and for its exponents, very much a ' \
                    'way of life—one that continues to reverberate to this day in the work of ' \
                    'countless Dixieland and traditional jazz bands around the world. For many ' \
                    'listeners, the Chicago style remains nothing less than the quintessential sound of jazz. ' \
                    'Further, the association of the so-called Chicago style of music with its ' \
                    'leading figure, Bix Beiderbecke, is also rather puzzling: Bix played little in ' \
                    'Chicago—if anything, his residencies in New York stand out as the decisive ' \
                    'interludes in his musical career. (Then again, when dealing with the topsyturvy ' \
                    'subject of jazz geography, be prepared for the strangest ' \
                    'contradictions: just as much of the history of New Orleans jazz took place ' \
                    'in Chicago, so did the sounds of Chicago jazz eventually find their most ' \
                    'hospitable home in New York.) The further stereotype that associates early ' \
                    'Chicago jazz almost solely with white musicians is equally off mark: as we ' \
                    'have already seen, the finest African American musicians from New ' \
                    'Orleans and elsewhere—Armstrong, Hines, Morton, Oliver, Noone, Dodds ' \
                    '—had already gravitated to Chicago by the mid-1920s. William Howland ' \
                    'Kenney, in his study of the biographies of fifty-five black musicians ' \
                    'associated with Chicago jazz during the 1920s, determined that nearly half ' \
                    'came from New Orleans, and a similar percentage arrived during or just ' \
                    'following World War I.14 Black jazz, white jazz, hot jazz, sweet jazz, New ' \
                    'Orleans jazz, Dixieland jazz: no matter what you call it or how you define ' \
                    'it, it all became part of Chicago jazz during these formative years. ' \
                    'The similarities between the music of the white Chicagoans and their ' \
                    'New Orleans models have often been noted—frequently by the Chicagoans ' \
                    'themselves. But close listening reveals subtle gradations of difference. A ' \
                    'certain restless energy begins to reverberate in the music. Counterpoint ' \
                    'lines no longer weave together, as in the earlier New Orleans style, but ' \
                    'often battle for supremacy. The specific roles filled by the New Orleans ' \
                    'front line are modified. The tailgate trombone tradition, with its use of ' \
                    'portamentos (or slurs) to link harmony notes, is less evident among the ' \
                    'Chicago players; and, at times, the trombone is totally absent, replaced by ' \
                    'the tenor sax, which takes on a more linear and overtly melodic role... ' \
                    'Perhaps the most obvious shift ' \
                    'came in the repertoire of the local jazz bands. During the decade of the ' \
                    '1920s, popular songs and thirty-two-bar forms were increasingly used by ' \
                    'Chicago jazz musicians, while blues and multitheme ragtime structures, so ' \
                    'central to the New Orleans tradition, became less common. This move does ' \
                    'not seem to have been driven by aesthetic considerations—it is hardly ' \
                    'mentioned by the players themselves in the many memoirs and interviews ' \
                    'from the period—but came about gradually as a response to the changing demands of audiences.' \
                    ' The blues recording craze of the early 1920s had ' \
                    'already subsided by the time Chicago jazz took off in full force, while the ' \
                    'ragtime explosion of the turn of the century was only a distant memory. In ' \
                    'this new world of mass marketing, jazz as a category of entertainment came ' \
                    'to occupy a wider and wider orbit, encompassing a broad spectrum of performance styles.'
chicago_jazz_intro = 'For many listeners, the quintessential sound of jazz.'
chicago_jazz = Landmark(size=Size.LARGE, title='Chicago Jazz', display_date=False, date=datetime(1923, 1, 1),
                        color=color_jazz_age, description=chicago_jazz_desc, intro=chicago_jazz_intro)

blues_fall = Landmark(size=Size.NODE, date=datetime(1922, 1, 1), title='The blues recording craze of the early 1920s subsides',
                      color=color_jazz_age)

clarinetitis_desc = 'By Benny Goodman. An example of the influence of the various nonjazz musical tradtiions that the ' \
                    'multiethnic Chicagoans brought with them to their Jazz making.The minor key melodies on clarinetitis' \
                    'convey more than a hint of klezmer.'
clarinetitis_img = Image('https://www.popsike.pics/pix/20180819/232896269336.jpg')
clarinetitis_link = Link('https://www.youtube.com/watch?v=1bFOB59cT5E&ab_channel=AtticusJazz', 'Youtube Link')
clarinetitis = Landmark(size=Size.SMALL, title='Clarinetitis', date=datetime(1928, 6, 13), images=[clarinetitis_img],
                        description=clarinetitis_desc, links=[clarinetitis_link], color=color_jazz_age)

thats_a_plenty_desc = 'By Benny Goodman. An example of the influence of the various nonjazz musical tradtiions that the ' \
                      'multiethnic Chicagoans brought with them to their Jazz making.The minor key melodies on ' \
                      '"That\'s a Plenty" convey more than a hint of klezmer.'
thats_a_plenty_link = Link('https://www.youtube.com/watch?v=saiY6YwsQKg&ab_channel=JonathanHolmes', 'Youtube Link')
thats_a_plenty_img = Image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.WkAk-5cxaeoenj52Plzk-AHaHa%26pid%3DApi&f=1&ipt=757c4470ef58718daa9289da473321cd90a7d046ee38a86135963f0150fb41d5')
thats_a_plenty = Landmark(size=Size.SMALL, title="That's a Plenty", date=datetime(1928, 6, 13),
                          description=thats_a_plenty_desc, links=[thats_a_plenty_link], images=[thats_a_plenty_img],
                          color=color_jazz_age)

liza_img = Image('https://ia801200.us.archive.org/22/items/78_liza_mckenzie-condons-chicagoans-mckenzie-condon-rubin_gbia3021815b/78_liza_mckenzie-condons-chicagoans-mckenzie-condon-rubin_gbia3021815b_itemimage.jpg?cnt=0')
liza_desc = 'By Red McKenzie And Condon\'s Chicagoans. Frank Teschemacher\'s use of 6/4 in his clarinet intro to' \
            '"Liza" is an example of the common fascination with contemporary classical music this generation\'s jazzmen' \
            'evidently had.'
liza_link = Link('https://www.youtube.com/watch?v=bApevgxvO7s&ab_channel=SwingBluesJazz78RPM', 'Youtube Link')
liza = Landmark(size=Size.SMALL, date=datetime(1927, 12, 16), description=liza_desc, links=[liza_link],
                images=[liza_img], color=color_jazz_age, title='Liza')

tram_desc = 'For a time in the 1920s, saxophonist Frank Trumbauer enjoyed an ' \
            'influence and reputation that even surpassed that of his frequent ' \
            'collaborator Bix Beiderbecke. Beiderbecke eventually came to take center ' \
            'stage in accounts of this body of music, yet this posthumous transformation ' \
            'should not blind us to Trumbauer’s compelling achievements. Two years ' \
            'older than the cornetist, Tram (as he came to be known) was born in ' \
            'Carbondale, Illinois, on May 30, 1901. Musical studies began early for him ' \
            '—like Beiderbecke, he showed signs of being a child prodigy—but his ' \
            'career as a professional saxophonist started late, not taking off in earnest ' \
            'until he completed a stint in the military. After joining forces in 1925, the ' \
            'two musicians became a package deal for bandleaders. They entered the ' \
            'Goldkette band at virtually the same time—Trumbauer later claimed that ' \
            'Beiderbecke’s employment was a condition he set for taking the gig—and ' \
            'moved to the Whiteman band in tandem, starting at the same Indianapolis ' \
            'performance. The duo also worked together in a St. Louis-based band, as ' \
            'well as served an overlapping and all-too-brief stint in an exceptional allstar ' \
            'group that also featured Joe Venuti, Eddie Lang, and Adrian Rollini. ... ' \
            'Even in their chosen profession, the two went different ' \
            'ways: Beiderbecke, the unschooled player, was devoted to music, and one ' \
            'can hardly imagine him pursuing any other livelihood; while Trumbauer, ' \
            'although the more formally trained of the two—his proficiency extended to ' \
            'the piano, trombone, cornet, violin, bassoon, and flute, with the saxophone ' \
            'being something of an afterthought—betrayed an ambivalent commitment ' \
            'to the jazz life; he later served as a test pilot in World War II and eventually ' \
            'abandoned music for aeronautics. But perhaps most decisive were their ' \
            'differences not in vocation but in avocation: outside music, Beiderbecke’s ' \
            'fatal passion was for alcohol, the forbidden fermented fruit of Prohibition, ' \
            'while Trumbauer drank little, and after a gig promptly returned home to his ' \
            'wife and child—with the result that he outlived his younger collaborator by a full quarter-century.'
tram_img = Image('https://upload.wikimedia.org/wikipedia/en/c/cf/Trumbauerfrankie20.jpg')
tram = Person(title='Frankie "Tram" Trumbauer', size=Size.MEDIUM, color=color_jazz_age, birthday=datetime(1901, 5, 30),
              deathday=datetime(1956, 6, 11), active_start=datetime(1923, 1, 2), active_end=datetime(1939, 1, 1),
              images=[tram_img])

tram_bix_desc = 'After joining forces in 1925, the two musicians became a package deal for bandleaders. ' \
                'They entered the Goldkette band at virtually the same time—Trumbauer later claimed that ' \
                'Beiderbecke’s employment was a condition he set for taking the gig—and ' \
                'moved to the Whiteman band in tandem, starting at the same Indianapolis ' \
                'performance. The duo also worked together in a St. Louis-based band, as ' \
                'well as served an overlapping and all-too-brief stint in an exceptional allstar ' \
                'group that also featured Joe Venuti, Eddie Lang, and Adrian Rollini.'
tram_bix = Landmark(size=Size.SMALL, title='The Bix-Tram collaboration', date=datetime(1925, 1, 2),
                    description=tram_bix_desc, color=color_jazz_age)
tram_bix_whiteman = Landmark(size=Size.NODE, title='Bix and Tram move to the Whiteman Band', date=datetime(1927, 1, 3),
                             color=color_jazz_age)

tram_bix_1927_desc = 'Beiderbecke and Trumbauer reached their peak on heartfelt performances ' \
                     'such as “Singin’ the Blues” and “I’m Comin’ Virginia,” both recorded in ' \
                     '1927, which went a long way toward establishing the ballad tradition in jazz.' \
                     ' True, earlier hot musicians had often played slow blues, but the ' \
                     'ambiance of such performances was much different from the purer, more ' \
                     'fragile melodicism of these inspired BeiderbeckeTrumbauer collaborations. ' \
                     'It was almost as if, before these sides, the hot and the sweet were thought to ' \
                     'be mutually exclusive, not to be joined, except in some fanciful chimera not ' \
                     'found in reality. But far from being opposites, these two currents, the lyric ' \
                     'and the intense, blend seamlessly on these late vintages of the Jazz Age. ' \
                     'Especially on “I’m Comin’ Virginia,” the 2/4 bounce so prevalent on most ' \
                     'earlier jazz recordings gives way to a smooth 4/4 ballad tempo, helped ' \
                     'along admirably by Eddie Lang’s subtle guitar textures. Yet the ' \
                     'achievements of the rhythm section are overshadowed by the pungent solos ' \
                     'by Beiderbecke and Trumbauer, with their artful balance of emotion and ' \
                     'logic. Above all, the essence of Beiderbecke’s conception of jazz stands out ' \
                     'in relief on these performances; the substitution chords implicit in his solos' \
                     '—superimposed diminished chords, augmented chords, dominant ninth ' \
                     'chords—are incorporated with such ease that it is easy to overlook the hard ' \
                     'harmonic edge to Bix’s melodicism. Instead, the technical aspects are ' \
                     'submerged in the free play of his musical creativity.'
tram_bix_1927_link = Link('https://www.youtube.com/watch?v=tyzw7CH692w&ab_channel=HeinzBecker', 'Singin\' the Blues Youtube Link')
tram_bix_1927_link_2 = Link('https://www.youtube.com/watch?v=oW7YYt0F-K4&ab_channel=warholsoup100', "I'm Coming Virginia Youtube")
tram_bix_1927_img = Image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FvYqALyYDnTc%2Fhqdefault.jpg&f=1&nofb=1&ipt=e19610821a97d20b401c68efc74680fc109033b8dd16a1b7bbfbe52d5d7d5c05')
tram_bix_1927 = Landmark(size=Size.SMALL, title="Singin' the Blues and I'm Coming Virginia",
                         date=datetime(1927, 2, 4), links=[tram_bix_1927_link, tram_bix_1927_link_2], description=tram_bix_1927_desc,
                         color=color_jazz_age, images=[tram_bix_1927_img])

goldkette_orchestra_desc = 'In addition to Bix and Tram, the ' \
                           'Goldkette group also featured, at one time or another, Joe Venuti, Eddie ' \
                           'Lang, the Dorsey Brothers, Red Nichols, Miff Mole, Don Murray, Steve ' \
                           'Brown, and arranger Bill Challis—an impressive lineup by any standard. ' \
                           'Goldkette’s modest ambitions—primarily aimed, it seems, at producing ' \
                           'inoffensive commercial music—were what limited his achievements, not ' \
                           'any lack of firepower on the bandstand. The Goldkette orchestra was ' \
                           'clearly capable of playing at a much higher level than its recordings ' \
                           'indicate. How else can we explain Rex Stewart’s account of a 1926 battle of ' \
                           'the bands between Fletcher Henderson’s group (in which Stewart served as ' \
                           'cornetist) with Goldkette’s orchestra? “This proved to be a most humiliating ' \
                           'experience for us, since, after all, we were supposed to be the world’s ' \
                           'greatest dance orchestra,” Stewart later wrote. “The facts were that we ' \
                           'simply could not compete with Jean Goldkette’s Victor Recording ' \
                           'Orchestra. Their arrangements were too imaginative, their rhythm too ' \
                           'strong.” “Fletcher was the King up there, had Hawk and all them guys and ' \
                           'Goldkette’s band washed them away,” adds Sonny Greer. “Man, that was ' \
                           'the sensation of New York. … Goldkette’s band was something else.” The ' \
                           'surviving recordings contain only hints—in an occasional choice solo or ' \
                           'well-arranged ensemble part—of what Stewart describes as “the first ' \
                           'original white swing band in history.” ' \
                           'Bix and Tram were far from the only famous jazz buddies recruited into ' \
                           'the Goldkette band. Two innovative string soloists, guitarist Eddie Lang and' \
                           'violinist Joe Venuti, were added for recording sessions, and stand out as the' \
                           ' premier players on their instruments from the early days of jazz.' \
                           ' Eventually the core of jazz soloists on the Goldkette roster—Bix, Tram, ' \
                           'Lang, Venuti—made the move to the more successful Paul Whiteman ' \
                           'orchestra, a group that, if anything, presents later listeners with an enigma ' \
                           'even more puzzling than Goldkette’s.'
goldkette_orchestra = Landmark(title='Jean Goldkette’s Victor Recording Orchestra', date=datetime(1924, 1, 2),
                               size=Size.MEDIUM, color=color_jazz_age, description=goldkette_orchestra_desc)
goldkette_orchestra.landmark_end_date = datetime(1927, 1, 1)

eddie_lang_img = Image('https://media.snl.no/media/243463/standard_eddie-lang.jpg')
eddie_lang = Person(intro='the father of jazz guitar', birthday=datetime(1902, 10, 25), deathday=datetime(1933, 3, 26),
                    active_start=datetime(1918, 1, 2), active_end=datetime(1933, 1, 1), color=color_jazz_age,
                    size=Size.MEDIUM, title='Eddie Lang', images=[eddie_lang_img])

joe_venuti_img = Image('https://2.bp.blogspot.com/-um_mT3iEaw8/V6CBasN_bHI/AAAAAAAAEWY/dHpBiuMOcuoVDrK9OjljsSg-nlthWoSDACLcB/s1600/j%2Bvenuti%2Bsmiling.jpg')
joe_venuti = Person(intro='the father of jazz violin', birthday=datetime(1903, 9, 16), deathday=datetime(1978, 8, 14),
                    active_start=datetime(1924, 1, 3), active_end=datetime(1978, 1, 1), color=color_jazz_age,
                    size=Size.MEDIUM, title='Joe Venuti', images=[joe_venuti_img])

stringing_img = Image('https://i.ytimg.com/vi/eEdGLoj0ILE/hqdefault.jpg?sqp=-oaymwEmCOADEOgC8quKqQMa8AEB-AH-BIAC4AOKAgwIABABGEAgTihlMA8=&rs=AOn4CLBf08rJfQslQEd4G00I8-_J0qezwg')
stringing_link = Link('https://www.youtube.com/watch?v=eEdGLoj0ILE&ab_channel=cdbpdx', 'Youtube Link')
stringing_desc = 'Their 1926 duet, “Stringing the Blues,” not only ' \
                 'showcases their deep rapport and the ease of their playing, but is also a ' \
                 'landmark in defining the role of guitar and violin in the jazz idiom ' \
                 '(anticipating the celebrated later work of the Quintette of the Hot Club of ' \
                 'France). Later collaborations, such as “Running Ragged” from October ' \
                 '1929 and “The Wild Dog” from October 1930, document the pair’s ' \
                 'progress in expanding the jazz vocabulary on their instruments. These ' \
                 'seminal recordings went a long way toward forging a chamber music style of jazz combo playing.'
stringing = Landmark(size=Size.SMALL, color=color_jazz_age, title='Stringing the Blues', description=stringing_desc,
                     links=[stringing_link], date=datetime(1926, 11, 8), images=[stringing_img])

whiteman_orchestra_img = Image('https://syncopatedtimes.com/wp-content/uploads/2020/04/Paul-Whiteman-and-his-Orchestra.jpg')
whiteman_orchestra_desc = 'Whiteman, who was originally a violinist, conducted a 40-piece U.S. Navy band in 1917–18' \
                          ' and then developed a hotel orchestra in California, which he took to New York City in 1920. ' \
                          'He hired the best white jazz players, but he allowed little room for improvisation in his' \
                          ' arrangements and greatly simplified jazz rhythms. He was successful as a cocomposer of' \
                          ' popular songs during the 1920s and led his orchestra in Broadway musicals.' \
                          ' Paul Whiteman greatly enriched American music by commissioning George Gershwin to write ' \
                          'Rhapsody In Blue which became his orchestra’s signature tune. He also “discovered” Bing ' \
                          'Crosby and featured him in Paul Whiteman’s Rhythm Boys, and gave the career of Hoagy ' \
                          'Carmichael a boost, by recording several of Hoagy’s songs early in his career. Jazz singer' \
                          ' Mildred Bailey also rose to fame in the orchestra in the 1930s.' \
                          'If there is such a thing as the “King of Jazz” the title belongs to Louis Armstrong, ' \
                          'although that may not have been clear to most people in the 1920s. ' \
                          'Whiteman is also criticized for not hiring African-American musicians to' \
                          ' play in his band, but this argument ignores the commercial realities of the period. ' \
                          'Paul Whiteman commissioned Duke Ellington to write for his modern music series, ' \
                          'recorded with Paul Robeson and Billie Holiday, and hired Don Redman as an arranger in the ' \
                          '1930s and was generally held in high regards as a person by musicians both Black and White.'
whiteman_orchestra = Landmark(size=Size.MEDIUM, title='Paul Whiteman Orchestra', color=color_jazz_age,
                              description=whiteman_orchestra_desc, date=datetime(1920, 1, 4), images=[whiteman_orchestra_img])

whiteman_poach = Landmark(size=Size.NODE, title='Whiteman hires most of Goldkette\'s better players',
                          date=datetime(1927, 1, 2), color=color_jazz_age)

two_harlems_desc = 'Harlem in the late 1920s was a society precariously balanced between ' \
                   'two extremes. The Harlem Renaissance...But another Harlem coexisted alongside this one, ' \
                   'reflecting a crueler reality and a less promising future....Harlem was becoming a slum...' \
                   'Jazz was very much a part of this second Harlem—more at home here ' \
                   'than in the “other” Harlem of high culture and higher aspirations. ' \
                   'True, the Harlem Renaissance created an ideology, a cultural context for jazz. But the ' \
                   'Harlem of rent parties and underground economies created music. Even ' \
                   'before the onset of the Great Depression, the rent party had become ' \
                   'established as an accepted way of paying for the high cost of lodging.' \
                   'Flyers might be circulated up to a month in advance, advertising which ' \
                   'entertainers would be performing. Admission on the night of the party ' \
                   'might cost anywhere between twenty-five cents and a dollar. The money ' \
                   'would pay for both the cost of the party and the next month’s rent. “They ' \
                   'would crowd a hundred or more people into a seven room railroad flat, and ' \
                   'the walls would bulge,” recalled Willie “The Lion” Smith, one of the ' \
                   'greatest of the Harlem pianists. “Some of the parties spread to the halls and ' \
                   'all over the building.” The piano was often the battleground between these two visions of black ' \
                   'artistic achievement. It is not going too far to suggest that the piano was to ' \
                   'Harlem what brass bands had been to New Orleans. The instrument ' \
                   'represented conflicting possibilities—a pathway for assimilating traditional ' \
                   'highbrow culture, a calling card of lowbrow nightlife, a symbol of middleclass ' \
                   'prosperity, or, quite simply, a means of making a living. But, with the ' \
                   'benefit of hindsight, we tend to view the piano in Harlem of the late 1920s ' \
                   'and early 1930s as the center of a new type of music--harlem stride.'
two_harlems = Landmark(size=Size.MEDIUM, title='The Two Harlems', date=datetime(1928, 2, 2), display_date=False,
                       description=two_harlems_desc, color=color_jazz_age)

harlem_stride_desc = 'Harlem stride piano, as it has come to be known, stood as a bridge between the ragtime idiom of' \
                     'the turn of the century and the new jazz piano styles that were in the process of evolution. ' \
                     'Between 1900 and 1914, around one hundred New York companies were ' \
                     'involved in publishing ragtime sheet music. Yet commercial interests and ' \
                     'artistic values coexisted uneasily in Tin Pan Alley, with scores of mediocre ' \
                     'rag songs—most of them bearing little resemblance to the classic ragtime ' \
                     'music of Scott Joplin, James Scott, and Joseph Lamb—overshadowing the ' \
                     'more sophisticated compositions of the masters. Stride piano players were ' \
                     'well aware of the gulf between highbrow and lowbrow that Joplin—perhaps ' \
                     'foolishly, perhaps wisely—had refused to recognize back in 1915; and ' \
                     'though they sometimes tried to bridge it, they never forgot the importance ' \
                     'of their roots in popular music. Understanding that music required an ' \
                     'audience, preferably a large one, they mastered a wide range of novelty ' \
                     'devices and popular effects. At times the superficial glitter could outshine ' \
                     'the jazz content— “When I began my work, jazz was a stunt,” was Duke ' \
                     'Ellington’s later critique of some of this music11—but the slick ' \
                     'professionalism of the Harlem stride style also served to expand the ' \
                     'audience for African American music in the face of discrimination from the ' \
                     'cultural elite, both within and without the black community, and despite a ' \
                     'severe economic downturn. For better or worse, the stride players did not ' \
                     'shy away from being entertainers. Indeed, the most famous of them, Fats ' \
                     'Waller, displayed a knack for captivating audiences unsurpassed by any jazz ' \
                     'musician, past or present, with the possible exception of Louis Armstrong. ... ' \
                     ''
harlem_stride = Landmark(size=Size.LARGE, title='Harlem Stride', date=datetime(1928, 2, 3), display_date=False,
                         description=harlem_stride_desc, color=color_jazz_age)

james_p_johnson_desc = 'Johnson’s own music epitomized this approach; it represents a critical ' \
                       'link between the ragtime of Joplin and the jazz of Waller and Tatum. His' \
                       ' early efforts remain true to the rag style, with his composition “Carolina ' \
                       'Shout” gaining particular favor among his peers. The work was widely ' \
                       'imitated by other players even before the sheet music was published, and ' \
                       'eventually replaced the “Maple Leaf Rag” as the ultimate test piece for ' \
                       'aspiring rag pianists. Johnson’s works may have lacked the melodic ' \
                       'inspiration and compositional balance that characterized Joplin’s pieces, but ' \
                       'he made up for it in the sheer breadth of his musical aspirations. His ' \
                       'popular songs were great successes, with “If I Could Be with You (One ' \
                       'Hour Tonight),” “Old Fashioned Love,” and “Charleston” reaching a mass ' \
                       'audience that was only vaguely familiar with the composer’s jazz ' \
                       'credentials. Yet Johnson also attacked the citadels of concert music... ' \
                       'Even when he kept true to the stride idiom, Johnson was an inveterate ' \
                       'experimenter who was willing to look outside the jazz and rag idiom for ' \
                       'techniques he could apply to his compositions. These devices included ' \
                       'classical interpolations (his repertoire included hot versions of the William ' \
                       'Tell Overture and Peer Gynt), counterpoint exercises using national ' \
                       'anthems (the final theme of his “Imitators’ Rag” mixes “Dixie” in the right ' \
                       'hand with the “Star-Spangled Banner” in the left), and much else besides. In ' \
                       'later years, Johnson even adapted to the demands of jazz-combo work, ' \
                       'recording with the Blue Note Jazzmen and on a number of sides by ' \
                       'prominent Chicago players. There may have been greater jazz musicians ' \
                       'than James P. Johnson, but few artists of his day sensed so clearly the latent ' \
                       'potential of African American music or worked so vigorously to bring it into reality.'
james_p_johnson_img = Image('https://syncopatedtimes.com/wp-content/uploads/2019/10/James-P-Johnson-1920s.jpg')
james_p_johnson = Person(size=Size.LARGE, title='James P Johnson', color=color_jazz_age,
                         birthday=datetime(1894, 2, 1), deathday=datetime(1955, 11, 12), active_start=datetime(1912, 1, 1),
                         active_end=datetime(1955, 1, 1), description=james_p_johnson_desc, images=[james_p_johnson_img])

cutting_contests_desc = 'Under the inspiration of Johnson and others, the world of stride piano ' \
                        'developed a macho, competitive ethos that has since come to permeate the ' \
                        'jazz world as a whole. This overlay of artistry and combat remains an ' \
                        'important—and often overlooked— tradition in African American culture. ' \
                        'Duke Ellington, recalling his own schooling in the Harlem stride piano ' \
                        'tradition, explained: “Anybody who had a reputation as a piano player had ' \
                        'to prove it right there and then by sitting down to the piano and displaying ' \
                        'his artistic wares.” In later years, the cutting contest—a jam session in ' \
                        'which outplaying the other participants (“cutting” them, in jazz jargon)— ' \
                        'became an important part of jazz pedagogy and practice, and the most ' \
                        'crucial rite of passage for a young player. Its overtones now hover over ' \
                        'even the friendliest of jazz encounters. In an age in which other art forms ' \
                        'have come to eschew demonstrations of virtuosity, the jazz world continues ' \
                        'to embrace one-upmanship and displays of technique as an integral part of ' \
                        'its culture. To a great extent, the hothouse environment of Harlem helped to ' \
                        'produce this new image of the jazz musician as half artist, half warrior.'
cutting_contests = Landmark(size=Size.MEDIUM, title='cutting contests', description=cutting_contests_desc,
                            date=datetime(1929, 1, 1), display_date=False, color=color_jazz_age)

fats_waller_desc = 'Yet Thomas “Fats” Waller did more than any of these players to bring the ' \
                   'Harlem style to the attention of the broader American public.'
fats_waller_img = Image('https://hips.hearstapps.com/hmg-prod/images/gettyimages-514974526-copy.jpg?resize=1200:*')
fats_waller = Person(size=Size.LARGE, color=color_jazz_age, title='Thomas "Fats" Waller',
                     birthday=datetime(1904, 5, 21), deathday=datetime(1943, 12, 15),
                     active_start=datetime(1918, 3, 1), active_end=datetime(1943, 12, 15),
                     description=fats_waller_desc, images=[fats_waller_img])

aint_misbehavin_img = Image('https://i.ytimg.com/vi/WTUxw6ioyJU/hqdefault.jpg')
aint_misbehavin_link = Link('https://www.youtube.com/watch?v=o1TIHXBzFHU&ab_channel=JGCHistory', 'Youtube Link')
aint_misbehavin = Landmark(size=Size.SMALL, date=datetime(1929, 7, 9), color=color_jazz_age, title="Ain't Misbehavin'",
                           images=[aint_misbehavin_img], links=[aint_misbehavin_link])

honeysuckle_img= Image('https://i.ytimg.com/vi/H0VwiHDxRIw/maxresdefault.jpg')
honeysuckle = Landmark(size=Size.SMALL, title='Honeysuckle Rose', date=datetime(1929, 2, 2), color=color_jazz_age,
                       links=[Link('https://www.youtube.com/watch?v=-F6n_12c9bo&ab_channel=DanielGraham', 'Youtube Link')], images=[honeysuckle_img])

squeeze_me_desc = 'A 1925 jazz standard composed by Fats Waller. It was based on an old blues song called "The Boy' \
                  ' in the Boat". The lyrics were credited to publisher Clarence Williams, although Andy Razaf has ' \
                  'claimed to have actually written the lyrics.'
squeeze_me_link = Link('https://www.youtube.com/watch?v=cgCetEpAqcw&ab_channel=DominikFeri', 'Youtube Link')
squeeze_me_img = Image('https://ia800600.us.archive.org/27/items/mbid-b73281a8-e794-4ed9-95d6-f0567ef51085/mbid-b73281a8-e794-4ed9-95d6-f0567ef51085-35811676337.jpg')
squeeze_me = Landmark(size=Size.SMALL, date=datetime(1925, 4, 4), title='Squeeze Me', color=color_jazz_age,
                      links=[squeeze_me_link], description=squeeze_me_desc, images=[squeeze_me_img])

boogie_woogie_desc = 'A genre of blues music that became popular during the late 1920s, but ' \
                     'already developed in African-American communities since the 1870s. This ' \
                     'musical idiom combined insistent left-hand patterns based on blues chord ' \
                     'progressions with syncopated melody lines or block chords in the right ' \
                     'hand. The style demanded exceptional hand independence and a sure sense ' \
                     'of time from the performer. The style achieved its highest pitch as unaccompanied keyboard ' \
                     'music, although it was not uncommon for pianists to perform together in ' \
                     'duos and trios, as on “Boogie Woogie Prayer” recorded by Meade Lux ' \
                     'Lewis, Albert Ammons, and Pete Johnson. The leading practitioners ' \
                     'occasionally tried their dextrous hands at other keyboard styles, but, for the ' \
                     'most part, boogie-woogie remained a fringe music, lingering in the ' \
                     'interstices between blues and jazz.'
boogie_woogie = Landmark(size=Size.SMALL, title='Boogie-woogie', color=color_jazz_age, date=datetime(1925, 5, 1),
                         display_date=False, description=boogie_woogie_desc)

art_tatum_img = Image('https://media.npr.org/assets/img/2012/01/31/art-tatum_vert-88dab16cc37c5e7c479ff7e39d57ae98a99d7a01-s1100-c50.jpg')
art_tatum_desc = 'Historians of early twentieth-century piano styles—Harlem stride, boogie-woogie, ' \
                 'and other strands of jazz and popular keyboard music—face their greatest' \
                 ' challenge in trying to place the genrecrossing ' \
                 'and genre-busting artist Art Tatum, whose work from the early ' \
                 '1930s through the mid-1950s seemed to set its own rules and follow its own ' \
                 'evolutionary schemas. He stands out as the greatest virtuoso in the Harlem ' \
                 'stride piano tradition—and also demonstrated his mastery, on many ' \
                 'occasions, of boogie-woogie—yet he also did much more; as such, he ' \
                 'remains a complex and controversial figure, one difficult to situate with any ' \
                 'real precision in the stylistic pigeonholes commonly used in histories of ' \
                 'modern American music. One invariably ends up reaching for the oldest ' \
                 'cliché of them all: simply asserting that Tatum was “ahead of his time.” Yet ' \
                 'it is equally valid to see Tatum as obsessed with the achievements of the ' \
                 'past, not just in jazz but also in classical music, given the bravura Lisztian ' \
                 'aspects of his playing. And though some might suggest that Art Tatum represented' \
                 ' the finest flowering of the Harlem stride tradition, in point of fact, he rang its' \
                 ' death knell. In developing his mature style, Tatum all but exhausted' \
                 ' the possibilities of stride, forcing later piano modernists—Monk, Powell,' \
                 ' Tristano, Brubeck, Evans, and others—to veer off into far different directions' \
                 ' in an attempt to work their way outside the massive shadow of this' \
                 ' imposing figure. Because of this, much of the musical vocabulary ' \
                 'developed by Tatum remains unassimilated by later jazz pianists.' \
                 ' Long after the phraseology of such later jazz masters as Charlie Parker and' \
                 ' John Coltrane has been widely imitated and mastered, Tatum’s legacy' \
                 ' still sits in probate, waiting for a new generation of pianists to lay claim to its many riches.'
art_tatum = Person(size=Size.MEDIUM, birthday=datetime(1909, 10, 13), deathday=datetime(1956, 11, 5),
                   active_start=datetime(1925, 6, 6), active_end=datetime(1956, 10, 10),
                   title='Art Tatum', images=[art_tatum_img], color=color_jazz_age, description=art_tatum_desc)

big_bands_desc = 'The emergence of the big band idiom, with its subtle interweaving of ' \
                 'four sections— saxophone, trumpet, trombone, and rhythm—may seem, ' \
                 'with the benefit of hindsight, an inevitable development in the evolution of ' \
                 'jazz music. Was it not some law of aesthetic Darwinism that forced the ' \
                 'rough-and-ready small combos of early jazz to give way to the more robust ' \
                 'and polished orchestras of Ellington and Goodman? Not really. The ' \
                 'connecting line between the roots of jazz and the later big band sound is far ' \
                 'from direct or clear. During the so-called Jazz Age, most of the music’s key ' \
                 'exponents focused their creative energy on soloing not bandleading, on ' \
                 'improvisation not orchestration, on an interplay between individual ' \
                 'instruments not between sections. The move to a more compositionally ' \
                 'oriented idiom of dance music, under the rubric of big band jazz, was ' \
                 'anything but smooth or obvious at the time. Commercial pressures, rather ' \
                 'than artistic prerogatives, stand out as the spur that forced many early jazz ' \
                 'players (including Armstrong, Beiderbecke, and Hines) to embrace the big ' \
                 'band idiom. But even in the new setting, they remained improvisers, first ' \
                 'and foremost, not orchestrators or composers. A different body of ' \
                 'individuals, with different talents and inclinations—Don Redman, Fletcher ' \
                 'Henderson, Duke Ellington, Ferde Grofé, Benny Carter, Bill Challis, Art ' \
                 'Hickman, and others— would be required to decipher the artistic ' \
                 'implications in this shift in the public’s taste, to comprehend it as a ' \
                 'guidepost pointing to a truly revolutionary, rather than evolutionary, change ' \
                 'in the sound of American band music.'
big_bands = Landmark(size=Size.LARGE, title='The Big Band', color=color_jazz_age, date=datetime(1921, 8, 8),
                     display_date=False, description=big_bands_desc)

fletcher_henderson_desc = 'Fletcher Henderson, who helped define the emerging jazz big band sound ' \
                          'in the 1920s, also drew inspiration not just from New Orleans and Chicago ' \
                          'jazz, but even more from these currents of popular music and dance that ' \
                          'were sweeping New York in those years. Ethel Waters, in a telling anecdote,' \
                          ' described how she had to force Henderson to listen to player piano rolls so ' \
                          'that he could understand how to accompany her properly on a blues ' \
                          'recording. Henderson was a quick study and eventually made extensive use ' \
                          'of the blues in his music, but initially it was the ethos of the ballrooms, of ' \
                          'Tin Pan Alley, of Broadway and vaudeville, as well as of the rag bands of ' \
                          'the Northeast that set the context for his dramatic reconstruction of the ' \
                          'American jazz orchestra. In truth, by both temperament and training, ' \
                          'Henderson was an unlikely jazz innovator.'
fletcher_henderson_img = Image('https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Fletcher_Henderson_%281943_publicity_photo%29.jpg/500px-Fletcher_Henderson_%281943_publicity_photo%29.jpg')
fletcher_henderson = Person(size=Size.MEDIUM, title='Fletcher Henderson', color=color_jazz_age,
                            birthday=datetime(1897, 12, 18), deathday=datetime(1952, 12, 29),
                            active_start=datetime(1921, 7, 7), active_end=datetime(1950, 2, 2),
                            description=fletcher_henderson_desc, images=[fletcher_henderson_img])

fletcher_orchestra_desc = 'When Harry Pace left the company to start Black Swan Records, he took Henderson ' \
                          'with him to be musical director, a job which lasted from 1921 until 1923....' \
                          'Henderson\'s activities up to the end of 1923 were mainly recording dates for' \
                          ' Black Swan and other labels.[4] His band at this point was only a pick-up unit for' \
                          ' recordings, not a regular working band. In January 1924, the recording band became' \
                          ' the house band at the Club Alabam at 216 W. 44th St.[4] Despite many erroneous ' \
                          'publications indicating otherwise, this 1924 band was Henderson\'s first working band.' \
                          'In July 1924, the band began a brief engagement at the Roseland Ballroom. Although only' \
                          ' meant to stay for a few months,[4] the band was brought back for the autumn season.' \
                          ' Henderson called on Armstrong for a second time to join the band. On October 13, 1924,' \
                          ' history was made when Henderson\'s band began their re-engagement at Roseland,' \
                          ' with Armstrong now in the orchestra. The band quickly became known as the best ' \
                          'African American band in New York. By late 1924, the arrangements by Don Redman ' \
                          'were featuring more solo work. Even with Redman and Hawkins on board, the earliest' \
                          ' recordings of Henderson’s band are lackluster. The arrangements are simple, sticking ' \
                          'close to the model set by King Oliver (whose influence looms large on ' \
                          'these sides) and the other New Orleans pioneers, while the improvised ' \
                          'sections of the music are often repetitive and unimaginative, with only an ' \
                          'occasional phrase or hot break to indicate the potential of the band’s ' \
                          'soloists. But in the months following Henderson’s opening at the Club ' \
                          'Alabam, a number of changes can be heard: the band adds more players; its ' \
                          'sound gets denser and more complex; the performances become tighter and ' \
                          'more focused. The group still has not abandoned its allegiance to formulas ' \
                          'associated with New Orleans jazz, especially in terms of rhythmic ' \
                          'conception and solo construction, but already the barest indications of a ' \
                          'different paradigm—more arranged, more harmonically sophisticated—can ' \
                          'be heard in incipient form. And even the lingering influence of the New ' \
                          'Orleans style was not without its value in this new setting—a perspicacious ' \
                          'listener can hear the later battling exchanges of sections in a jazz big band ' \
                          'anticipated in the dueling counterpoint of individual horns in the traditional ' \
                          'jazz of Oliver and other Crescent City pioneers. ' \
                          'More than any other event, Henderson’s hiring of Louis Armstrong in ' \
                          '1924 served as a catalyst in accelerating the band’s evolution. Comparisons ' \
                          'of Armstrong’s solo work with Hawkins’s on performances from 1924 and ' \
                          '1925 such as “Money Blues,” “Go ‘Long Mule,” “How Come You Do Me ' \
                          'Like You Do?,” or “Carolina Stomp” show how much the cornetist had to ' \
                          'teach—and, equally, how much the saxophonist still had to learn. In this ' \
                          'setting, Hawkins gradually softened the rough edges of his phrasing and ' \
                          'smoothed out the rhythmic flow of his playing.'
fletcher_orchestra_img = Image('https://upload.wikimedia.org/wikipedia/commons/9/9d/FletcherHendersonOrchestra1925.jpg')
fletcher_orchestra = Landmark(size=Size.MEDIUM, color=color_jazz_age, images=[fletcher_orchestra_img],
                              display_date=False, date=datetime(1923, 1, 4), title='Fletcher Henderson Orchestra')

fletcher_hawkins = Landmark(size=Size.NODE, title='Hawkins starts playing with Henderson\'s orchestra',
                            color=color_jazz_age, date=datetime(1923, 10, 13))


coleman_hawkins_desc = 'Hawkins learned piano at age five and took up cello two years later. For ' \
                       'his ninth birthday he received a saxophone, and by age twelve he was ' \
                       'playing at school dances. In 1921, Hawkins went on the road with singer ' \
                       'Mamie Smith, who one year earlier had achieved a huge success with ' \
                       '“Crazy Blues,” a million-selling hit that initiated the craze for race records. ' \
                       'Smith provided Hawkins with a number of opportunities: to perform in ' \
                       'front of large crowds, to initiate his recording career (in May 1922), and to ' \
                       'come to New York. But by the summer of 1923, Hawkins had left Smith ' \
                       'and was recording with Henderson. While Redman did much of his work ' \
                       'behind the scenes, crafting the band’s arrangements, Hawkins stood out on ' \
                       'the bandstand as the group’s featured soloist, usually on tenor saxophone, ' \
                       'but sometimes playing clarinet, C-melody saxophone, baritone saxophone, ' \
                       'or bass saxophone. ' \
                       'Today the saxophone is not only an accepted and popular band ' \
                       'instrument, but to many listeners represents the quintessential sound of jazz. ' \
                       'This was far from the case during the years in which Hawkins mastered his ' \
                       'craft. The saxophone family was still in its infancy, virtually unknown in ' \
                       'the symphonic world, and relegated primarily to military bands. But' \
                       ' the intrinsic advantages of his most famous instrument—it was easy to ' \
                       'learn, forgiving in its tone production, and relatively inexpensive to make ' \
                       'with its simple metal body attached to a conventional clarinet-type ' \
                       'mouthpiece—proved decisive in the long run. By the early years of the ' \
                       'twentieth century, the saxophone had established itself as an important ' \
                       'instrumental voice, first in military bands and later in popular and jazz ' \
                       'ensembles. The only thing lacking was a tradition and an accepted body of playing techniques. ' \
                       'This was provided, in large part, by Hawkins. Even so, at the start of ' \
                       'Hawkins’s career the saxophone had yet to match the role of the cornet or ' \
                       'clarinet as an important jazz solo voice. Years later, many devotees of New ' \
                       'Orleans style would grumble that the death knell for “pure” jazz was ' \
                       'sounded when the saxophonists took over the music.'
coleman_hawkins_img = Image('https://cdn.allsolos.com/images/soloist/202.jpg')
coleman_hawkins = Person(size=Size.MEDIUM, color=color_jazz_age, title='Coleman Hawkins',
                         birthday=datetime(1904, 11, 21), deathday=datetime(1969, 5, 19),
                         active_start=datetime(1921, 5, 5), active_end=datetime(1967, 5, 19), images=[coleman_hawkins_img])

fletcher_armstrong = Landmark(size=Size.NODE, title='Armstrong starts playing with Henderson\'s orchestra',
                              color=color_jazz_age, date=datetime(1924, 10, 13))

money_blues_img = Image('https://i.ytimg.com/vi/tW0EJVHp3CU/maxresdefault.jpg')
money_blues_link = Link('https://www.youtube.com/watch?v=tW0EJVHp3CU&ab_channel=AtticusJazz', 'Youtube Link')
money_blues = Landmark(size=Size.SMALL, date=datetime(1925, 5, 12), images=[money_blues_img], links=[money_blues_link],
                       color=color_jazz_age, title='Money Blues')

go_long_mule_link = Link('https://www.youtube.com/watch?v=bWQGI9MjDPU&ab_channel=HeinzBecker')
go_long_mule_img = Image('https://i.ytimg.com/vi/2nBN8-BBFOc/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AGUA4AC0AWKAgwIABABGGUgYChVMA8=&rs=AOn4CLCC8Wkm5ToKfWrtDonddLpUpF8a6Q')
go_long_mule = Landmark(size=Size.SMALL, color=color_jazz_age, title='Go \'Long Mule',
                        date=datetime(1924, 10, 7), links=[go_long_mule_link], images=[go_long_mule_img])

redman_leaves = Landmark(size=Size.NODE, date=datetime(1927, 3, 3), title='Redman leaves the Henderson Orchestra',
                         color=color_jazz_age)

duke_ellington_img = Image('https://www.kennedy-center.org/globalassets/education/resources-for-educators/classroom-resources/artsedge/artists/ellington-duke.jpg')
duke_ellington = Person(size=Size.LARGE, title='Duke Ellington', color=color_jazz_age,
                        birthday=datetime(1899, 4, 29), deathday=datetime(1974, 5, 24),
                        active_start=datetime(1917, 2, 2), active_end=datetime(1974, 5, 24),
                        images=[duke_ellington_img])

duke_cotton_orchestra_desc = 'Although Ellington had previously expanded his group for recordings, ' \
                             'the Club Kentucky engagement had supported only a sextet. Now required ' \
                             'to front a much larger band, Ellington again displayed his unerring knack ' \
                             'for finding the right individual ingredients for the complex new sounds he ' \
                             'was in the process of concocting. In this defining moment, when he was on ' \
                             'the cusp of stardom, Ellington brought in a core group of players who ' \
                             'would stay with him for years—in some instances, for decades—and help ' \
                             'him create more than a passing style, but in essence serve as building ' \
                             'blocks for their employer’s lifelong vocation as a composer and bandleader.... ' \
                             'It is especially illuminating to compare Ellington’s big band ' \
                             'charts from the late 1920s with Don Redman’s efforts for Henderson and ' \
                             'other bands. Redman’s writing is packed full with musical activity—calland- ' \
                             'responses, breaks, dense section work, repeated rhythmic figures, and ' \
                             'other devices. Ellington’s arrangements are much sparser, more focused, ' \
                             'less frenetic. This clarity and balance stood out whether Ellington was ' \
                             'writing mood pieces (“Black Beauty,” “Misty Morning”), his so-called ' \
                             'jungle pieces (“The Mooche”), or even standard blues (“Beggar Blues,” ' \
                             '“The Blues with a Feeling”); while, with a few exceptions, even the showy ' \
                             'up-tempo numbers maintain a cohesive musical identity. An atomistic, ' \
                             'stream-of-consciousness compilation of devices, along the lines of what ' \
                             'Redman attempted in his “Whiteman Stomp” had no place in Duke’s holistic music.... ' \
                             'Duke’s ascendancy during the Cotton Club years enabled him not only to ' \
                             'weather the onset of the Great Depression, but even to flourish at a time ' \
                             'when most bandleaders needed to retrench. Ellington’s group was one of ' \
                             'the most widely recorded jazz ensembles of the period, while regular radio ' \
                             'broadcasts further expanded his audience.'
duke_cotton_orchestra = Landmark(title='Duke and the Cotton Club Orchestra', size=Size.LARGE,
                                 date=datetime(1927, 12, 4), color=color_jazz_age)

color_swing_era = '#26cdf0'

swing_era_desc = 'The onset of the Great Depression had a chilling effect on the jazz ' \
                 'world, as it did on the whole entertainment industry. Record sales in the ' \
                 'United States had surpassed one hundred million in 1927, but by 1932 only ' \
                 'six million were sold....Thousands of them changed careers—membership in the' \
                 ' musicians’ union declined by almost one-third between 1928 and 1934—or else remained chronically ' \
                 'underemployed. Greater and lesser talents suffered alike. ' \
                 '...their careers spiraled downward in tandem with the nation’s industrial output.' \
                 'The end of Prohibition in 1933 transformed many speakeasies into ' \
                 'legitimate nightclubs, but the change was hardly a positive one for most ' \
                 'jazz players. Not only alcohol but the whole ethos and ambiance of jazz ' \
                 'culture were demystified in the process. Both could now be easily ' \
                 'consumed at home: alcohol legally purchased at the liquor store, jazz ' \
                 'carried into the household over the airwaves. This was progress of sorts. Yet ' \
                 'the harsh math of this new equation did not bode well for musicians: a ' \
                 'single band could now entertain countless listeners through the magic of radio...' \
                 'Even so, the American music industry during these years was a tinderbox waiting for the ' \
                 'spark that would set it off. The rise of network radio, much more than the ' \
                 'earlier spread of record players, transformed the general public into passive ' \
                 'receptors of entertainment chosen by a few arbiters of taste. The results ' \
                 'were now all but inevitable. The mechanisms of stardom were set in place ' \
                 'in the music world. All that was needed was the right star.'
swing_era_intro = 'There was a time, from 1933–1947, when teenagers and young adults danced ' \
                  'to jazz-orientated bands. When jazz orchestras dominated pop charts and when' \
                  ' influential clarinettists were household names. This was the swing era.'
prohibition_img = Image('https://cdn.thecollector.com/wp-content/uploads/2022/03/frank-scherschel-men-women-celebrate-end-prohibition-1933.jpg?width=995&quality=55')
swing_era_img = Image('https://4.bp.blogspot.com/-v1pd5GIwLUI/Wk8nN6DOPRI/AAAAAAABMzI/gotamcaSuAkSiMsRZEwoYoacQ_GzlHoNgCLcBGAs/s1600/Vintage%2BLindy%2BHop%2B%25281%2529.jpg')
swing_ellington_img=Image('https://www.kaufmanmusiccenter.org/images/uploads/events/_medium/Duke_Ellington_1200x1200.jpg', 'Duke Ellington')
swing_era = Era(title='The Swing Era', active_start=datetime(1933, 1, 1), end_year=datetime(1947, 1, 1),
                images=[swing_era_img, prohibition_img, swing_ellington_img], color=color_swing_era, description=swing_era_desc, intro=swing_era_intro)

benny_goodman_img = Image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Benny_Goodman_1942.jpg/500px-Benny_Goodman_1942.jpg')
benny_goodman = Person(size=Size.LARGE, color=color_swing_era, title='Benny Goodman',
                       birthday=datetime(1909, 5, 30), deathday=datetime(1986, 6, 13),
                       active_start=datetime(1926, 2, 2), active_end=datetime(1986, 6, 13),
                       images=[benny_goodman_img], intro='The King of Swing')

dorsey_marie_link = Link('https://www.youtube.com/watch?v=XgR0g6WKvgk&ab_channel=AlexSuzano', 'Youtube Link')
dorsey_marie_img = Image('https://i.ytimg.com/vi/hDuZW6ygrFI/hqdefault.jpg')
dorsey_marie = Landmark(size=Size.SMALL, title='Marie', date=datetime(1937, 1, 29), color=color_swing_era,
                        images=[dorsey_marie_img], links=[dorsey_marie_link])

tommy_dorsey_orchestra = Landmark(size=Size.MEDIUM, title='The Tommy Dorsey Orchestra', color=color_swing_era,
                                  date=datetime(1935, 1, 1))

dorsey_sy = Landmark(size=Size.NODE, title='Sy Oliver joins the Tommy Dorsey Orchestra', date=datetime(1939, 2, 2),
                     color=color_swing_era)

n_o_music_scene_relationships = [Relationship(gospel),
                                 Relationship(brass_bands),
                                 Relationship(ragtime),
                                 Relationship(classical),
                                 Relationship(string_bands),
                                 Relationship(blues)]
n_o_music_scene.set_relationships(n_o_music_scene_relationships)
brass_bands_relationships = [Relationship(n_o_music_scene),
                             Relationship(excelsior, 'Excelsior--a prominent NOLA brass bands'),
                             Relationship(onward, 'Onward--a prominent NOLA brass bands')]
brass_bands.set_relationships(brass_bands_relationships)
classical.set_relationships([Relationship(n_o_music_scene)])
string_bands.set_relationships([Relationship(n_o_music_scene)])
blues.set_relationships([Relationship(n_o_music_scene),
                         Relationship(buddy_bolden, 'A major influence on Buddy Bolden')])
ragtime_relationship = [Relationship(n_o_music_scene)]
ragtime.set_relationships(ragtime_relationship)
excelsior.set_relationships([Relationship(brass_bands)])
onward.set_relationships([Relationship(brass_bands)])
gospel_relationships = [Relationship(n_o_music_scene),
                        Relationship(buddy_bolden, 'A major influence on Buddy Bolden')]
gospel.set_relationships(gospel_relationships)
buddy_bolden_relationships = [Relationship(gospel, 'Majorly influenced by gospel'),
                              Relationship(string_bands, 'Was a professional string ensemblist'),
                              Relationship(eagle_band),
                              Relationship(bb_blues),
                              Relationship(blues, 'Majorly influenced by the blues')]
buddy_bolden.set_relationships(buddy_bolden_relationships)
eagle_band.set_relationships([Relationship(buddy_bolden, 'founded by Buddy Bolden')])
odjb.set_relationships([Relationship(livery_stable_blues)])
livery_stable_blues.set_relationships([Relationship(odjb)])
jelly_roll_relationships = [Relationship(bb_blues, 'composed Buddy Bolden\'s Blues'),
                            Relationship(storyville, 'Started his career in Storyville'),
                            Relationship(chicago, 'Spent years of his career in Chicago'),
                            Relationship(new_york, 'Spent years of his career in New York'),
                            Relationship(sidewalk),
                            Relationship(red_hot_peppers, 'Founded the Red Hot Peppers')]
jelly_roll.set_relationships(jelly_roll_relationships)
bb_blues.set_relationships([Relationship(jelly_roll, 'composed by Jelly Roll Morton'),
                            Relationship(buddy_bolden, 'A recomposition Bolden\'s song, "Funky Butt"')])
storyville.set_relationships([Relationship(jelly_roll, 'Where Morton got his start'),
                              Relationship(new_orleans)])
chicago.set_relationships([Relationship(jelly_roll)])
new_york.set_relationships([Relationship(jelly_roll)])
sidewalk.set_relationships([Relationship(jelly_roll),
                            Relationship(chicago, 'Recorded in Chicago')])
red_hot_peppers.set_relationships([Relationship(jelly_roll),
                                   Relationship(chicago),
                                   Relationship(sidewalk)])
diaspora.set_relationships([Relationship(chicago)])
new_orleans_relationships = [Relationship(buddy_bolden),
                             Relationship(louis_armstrong),
                             Relationship(jelly_roll),
                             Relationship(king_oliver),
                             Relationship(kid_ory),
                             Relationship(sidney_bechet)]
new_orleans.set_relationships(new_orleans_relationships)
kid_ory_band_relationships = [Relationship(king_oliver, 'Featured King Oliver at one point'),
                              Relationship(kid_ory),
                              Relationship(louis_armstrong, 'Featured Louis Armstrong at one point')]
kid_ory_band.set_relationships(kid_ory_band_relationships)
king_oliver_relationships = [Relationship(new_orleans, 'Born in NOLA'),
                             Relationship(louis_armstrong, 'Mentored Louis Armstrong'),
                             Relationship(chicago),
                             Relationship(kid_ory_band, 'played in Kid Ory\'s Band')]
king_oliver.set_relationships(king_oliver_relationships)
louis_relationships = [Relationship(new_orleans, 'Born in NOLA'),
                       Relationship(chicago, "Migrated to play in Oliver's band"),
                       Relationship(kid_ory_band, 'Replaced King Oliver in Kid Ory\'s Band'),
                       Relationship(king_oliver_band, 'Recruited by King Oliver to play in 1922'),
                       Relationship(king_oliver, "Mentored by King Oliver"),
                       Relationship(fletcher_orchestra)]
kid_ory_relationships = [Relationship(new_orleans, 'Moved to NOLA at age 21'),
                         Relationship(chicago),
                         Relationship(kid_ory_band)]
kid_ory.set_relationships(kid_ory_relationships)
louis_armstrong.set_relationships(louis_relationships)
king_oliver_band_relationships = [Relationship(louis_armstrong),
                                  Relationship(king_oliver),
                                  Relationship(chicago)
                                  ]
king_oliver_band.set_relationships(king_oliver_band_relationships)
clarence_five_relationships = [Relationship(louis_armstrong),
                               Relationship(sidney_bechet)]
clarence_five.set_relationships(clarence_five_relationships)
sidney_bechet_relationships = [Relationship(clarence_five),
                               Relationship(new_orleans, 'Born in NOLA')]
sidney_bechet.set_relationships(sidney_bechet_relationships)
armstrong_migrates_relationships = [Relationship(louis_armstrong),
                                    Relationship(chicago)]
armstrong_migrates.set_relationships(armstrong_migrates_relationships)
bechet_migrates_relationships = [Relationship(sidney_bechet)]
bechet_migrates.set_relationships(bechet_migrates_relationships)
early_every_morn_relationship = [Relationship(louis_armstrong),
                                 Relationship(sidney_bechet)]
early_every_morn.set_relationships(early_every_morn_relationship)
bix_death_relationships = [Relationship(bix_beiderbecke)]
bix_death.set_relationships(bix_death_relationships)
bix_relationships = [Relationship(chicago_jazz, 'The new sound\'s leading figure'),
                     Relationship(tram_bix)]
bix_beiderbecke.set_relationships(bix_relationships)
chicago_jazz_relationships = [Relationship(bix_beiderbecke)]
chicago_jazz.set_relationships(chicago_jazz_relationships)
blues_fall_relationships = [Relationship(chicago_jazz)]
blues_fall.set_relationships(blues_fall_relationships)
clarinetitis_relationships = [Relationship(chicago_jazz)]
clarinetitis.set_relationships(clarinetitis_relationships)
thats_a_plenty_relationships = [Relationship(chicago_jazz)]
thats_a_plenty.set_relationships(thats_a_plenty_relationships)
liza_relationships = [Relationship(chicago_jazz)]
liza.set_relationships(liza_relationships)
tram_relationships = [Relationship(tram_bix)]
tram.set_relationships(tram_relationships)
tram_bix_relationships = [Relationship(bix_beiderbecke),
                          Relationship(tram),
                          Relationship(goldkette_orchestra, 'where Tram and Bix started working together')]
tram_bix.set_relationships(tram_bix_relationships)
tram_bix_whiteman_rel = [Relationship(tram),
                         Relationship(bix_beiderbecke),
                         Relationship(tram_bix),
                         Relationship(whiteman_poach)]
tram_bix_whiteman.set_relationships(tram_bix_whiteman_rel),
tram_bix_1927_relationship = [Relationship(tram),
                              Relationship(bix_beiderbecke),
                              Relationship(tram_bix)]
tram_bix_1927.set_relationships(tram_bix_1927_relationship)
goldkette_orchestra_relationships = [Relationship(tram_bix, 'where Tram and Bix started working together'),
                                     Relationship(tram),
                                     Relationship(bix_beiderbecke),
                                     Relationship(eddie_lang),
                                     Relationship(joe_venuti),
                                     Relationship(whiteman_orchestra, 'many players left to join Whiteman')]
goldkette_orchestra.set_relationships(goldkette_orchestra_relationships)
eddie_lang_relationships = [Relationship(goldkette_orchestra),
                            Relationship(joe_venuti, 'childhood friend and, later, coworker'),
                            Relationship(stringing)]
eddie_lang.set_relationships(eddie_lang_relationships)
joe_venuti_relationships = [Relationship(goldkette_orchestra),
                            Relationship(eddie_lang, 'childhood friend and, later, coworker'),
                            Relationship(stringing)]
joe_venuti.set_relationships(joe_venuti_relationships),
stringing_relationship = [Relationship(joe_venuti),
                          Relationship(eddie_lang)]
stringing.set_relationships(stringing_relationship)
whiteman_orchestra_rel = [Relationship(tram),
                          Relationship(bix_beiderbecke),
                          Relationship(eddie_lang),
                          Relationship(joe_venuti),
                          Relationship(goldkette_orchestra, 'hired many of their players')]
whiteman_orchestra.set_relationships(whiteman_orchestra_rel)
whiteman_poach_rel = [Relationship(whiteman_orchestra),
                      Relationship(goldkette_orchestra),
                      Relationship(bix_beiderbecke),
                      Relationship(eddie_lang),
                      Relationship(tram),
                      Relationship(joe_venuti)]
whiteman_poach.set_relationships(whiteman_poach_rel)
harlem_stride_relationships = [Relationship(two_harlems),
                               Relationship(ragtime)]
harlem_stride.set_relationships(harlem_stride_relationships)
james_p_johnson_relationships = [Relationship(ragtime, 'his work was link between ragtime and stride'),
                                 Relationship(harlem_stride, 'his work was link between ragtime and stride')]
james_p_johnson.set_relationships(james_p_johnson_relationships)
cutting_contests_relationships = [Relationship(harlem_stride)]
cutting_contests.set_relationships(cutting_contests_relationships)
fats_waller_relationships = [Relationship(harlem_stride)]
fats_waller.set_relationships(fats_waller_relationships)
aint_misbehavin_relationships = [Relationship(fats_waller),
                                 Relationship(harlem_stride)]
aint_misbehavin.set_relationships(aint_misbehavin_relationships)
honeysuckle_relationships = [Relationship(fats_waller),
                             Relationship(harlem_stride)]
honeysuckle.set_relationships(honeysuckle_relationships)
squeeze_me_relationships = [Relationship(fats_waller),
                            Relationship(harlem_stride)]
squeeze_me.set_relationships(squeeze_me_relationships)
art_tatum_relationships = [Relationship(fats_waller, 'major influence'),
                           Relationship(james_p_johnson, 'major influence'),
                           Relationship(boogie_woogie, 'a notable artist of the genre'),
                           Relationship(harlem_stride, 'perhaps the greatest virtuoso of stride')]
art_tatum.set_relationships(art_tatum_relationships)
big_bands_relationships = [Relationship(fletcher_henderson, 'majorly defined by')]
big_bands.set_relationships(big_bands_relationships)
fletcher_henderson_relationships = [Relationship(big_bands, 'helped define the genre'),
                                    ]
fletcher_henderson.set_relationships(fletcher_henderson_relationships)
fletcher_armstrong_relationships = [Relationship(fletcher_henderson),
                                    Relationship(fletcher_orchestra),
                                    Relationship(louis_armstrong)]
fletcher_armstrong.set_relationships(fletcher_armstrong_relationships)
fletcher_orchestra_relationships = [Relationship(fletcher_henderson),
                                    Relationship(louis_armstrong),
                                    Relationship(fletcher_armstrong),
                                    Relationship(coleman_hawkins)]
fletcher_orchestra.set_relationships(fletcher_orchestra_relationships)
fletcher_hawkins_relationships = [Relationship(fletcher_henderson),
                                  Relationship(fletcher_orchestra),
                                  Relationship(coleman_hawkins)]
fletcher_hawkins.set_relationships(fletcher_hawkins_relationships)
coleman_hawkins_relationships = [Relationship(fletcher_orchestra)]
coleman_hawkins.set_relationships(coleman_hawkins_relationships)
money_blues_relationships = [Relationship(fletcher_orchestra),
                             Relationship(coleman_hawkins),
                             Relationship(louis_armstrong)]
money_blues.set_relationships(money_blues_relationships)
go_long_mule_relationships = [Relationship(fletcher_orchestra),
                             Relationship(coleman_hawkins),
                             Relationship(louis_armstrong)]
go_long_mule.set_relationships(go_long_mule_relationships)
redman_leaves.set_relationships([Relationship(fletcher_orchestra)])
duke_ellington_relationships = [Relationship(duke_cotton_orchestra)]
duke_ellington.set_relationships(duke_ellington_relationships)
duke_cotton_orchestra_rel = [Relationship(duke_ellington)]
duke_cotton_orchestra.set_relationships(duke_cotton_orchestra_rel)
dorsey_sy.set_relationships([Relationship(tommy_dorsey_orchestra)])
dorsey_marie.set_relationships([Relationship(tommy_dorsey_orchestra)])
tommy_dorsey_orchestra.set_relationships([Relationship(dorsey_marie)])


landmarks = [
    pre_jazz, n_o_music_scene, brass_bands, classical, blues, string_bands, excelsior, onward, ragtime, gospel,
    new_orleans_jazz, storyville, buddy_bolden, other_early_jazz_figures, eagle_band, livery_stable_blues, odjb,
    jelly_roll, bb_blues, jazz_age, new_orleans, chicago, new_york, sidewalk, red_hot_peppers,
    diaspora, louis_armstrong, king_oliver, kid_ory, kid_ory_band, king_oliver_band,
    sidney_bechet, clarence_five, armstrong_migrates, bechet_migrates, early_every_morn, bix_beiderbecke,
    bix_death, chicago_jazz, blues_fall, thats_a_plenty, clarinetitis, liza, tram, tram_bix, tram_bix_whiteman,
    tram_bix_1927, goldkette_orchestra, eddie_lang, joe_venuti, stringing, whiteman_orchestra, whiteman_poach,
    harlem_stride, two_harlems, james_p_johnson, cutting_contests, fats_waller, aint_misbehavin, honeysuckle,
    squeeze_me, boogie_woogie, art_tatum, big_bands, fletcher_henderson, fletcher_orchestra, fletcher_armstrong,
    fletcher_hawkins, coleman_hawkins, money_blues, go_long_mule, redman_leaves, duke_ellington, duke_cotton_orchestra,
    swing_era, benny_goodman, dorsey_marie, tommy_dorsey_orchestra, dorsey_sy
    # gatsby, prohibition
]

nola_jazz_landmarks = [new_orleans_jazz, buddy_bolden, storyville, jelly_roll,
                       king_oliver, sidney_bechet, diaspora, kid_ory, livery_stable_blues,
                       louis_armstrong]

# Los Angeles landmark

# goldkitee landmark

# Paul Whiteman the self-ascribed King of Jazz