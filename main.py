from timeline import Timeline
from initial_data import landmarks
from initial_data_2 import landmarks_2


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

    y = Timeline()
    y.title = 'The Scientific Revolution'
    y.authors = ['Student Handouts, Inc']
    y.citations = ['https://www.studenthandouts.com/00/201007/10.01-Scientific-Revolution-PowerPoint-Presentation.pdf']
    y.set_landmarks(landmarks_2)

    y.dump_data([x, y])