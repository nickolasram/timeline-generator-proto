from timeline_landmark import Size
import uuid

class Presentation:
    def __init__(self, title='default'):
        self.title = title
        self.landmarkIDs = []
        self.id = str(uuid.uuid4())[:8] + str(uuid.uuid4())[:8]

    def add_landmarkID(self, landmark):
        self.landmarkIDs.append(landmark.id)
        landmark.presentations.append({
            'title': self.title,
            'index': len(self.landmarkIDs) - 1
        })

    def set_landmarks(self, landmarks):
        for landmark in landmarks:
            if landmark.size is not Size.NODE:
                self.add_landmarkID(landmark)

    def to_dict(self):
        return {
            'meta': {
                'title': self.title,
                'highIndex': len(self.landmarkIDs) - 1,
                'firstLandmarkID': self.landmarkIDs[0],
                'id': self.id
            },
            'landmarkIDs': self.landmarkIDs
        }