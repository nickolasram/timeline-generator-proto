from timeline import Timeline
from initial_data import landmarks, nola_jazz_landmarks
from initial_data_2 import landmarks_2
from initial_data6 import landmarks_6, presentation_2
from timeline_presentation import Presentation


if __name__ == "__main__":
    x = Timeline()
    x.title = 'The History of Jazz'
    x.authors = ['Site Developer',
                 'Ted Goia']
    x.citations = ['The History of Jazz by Ted Goia',
                   'Wikipedia',
                   'SyncopatedTimes.com']
    x.note = 'This timeline covers some aspects of the history of jazz. It is an example of a more complicated' \
             'and full timeline. This text here is an example of a desctriptive timeline note.'
    x.set_landmarks(landmarks)
    nola_presentation = Presentation('NOLA Jazz')
    nola_presentation.set_landmarks(nola_jazz_landmarks)
    nola_presentation_dict = nola_presentation.to_dict()
    x.presentations.append(nola_presentation_dict)
    x.presentations_summary.append(nola_presentation_dict['meta'])

    y = Timeline()
    y.title = 'The Scientific Revolution'
    y.authors = ['Student Handouts, Inc']
    y.citations = ['https://www.studenthandouts.com/00/201007/10.01-Scientific-Revolution-PowerPoint-Presentation.pdf']
    y.set_landmarks(landmarks_2)

    z = Timeline()
    z.title = 'The Scientific Revolution 2'
    z.authors = ['Student Handouts, Inc']
    z.citations = ['https://www.studenthandouts.com/00/201007/10.01-Scientific-Revolution-PowerPoint-Presentation.pdf']
    z.set_landmarks(landmarks_6)
    class_presentation = Presentation('European History 2')
    class_presentation.set_landmarks(presentation_2)
    class_presentation_dict = class_presentation.to_dict()
    z.presentations.append(class_presentation_dict)
    z.presentations_summary.append(class_presentation_dict['meta'])

    z.dump_data([x, y, z])