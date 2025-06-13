class Image:
    def __init__(self, image,  description=False, alt='timeline image'):
        self.image = image
        self.description = description
        self.alt = alt

    def to_dict(self):
        return {
            'image': self.image,
            'description': self.description,
            'alt': self.alt
        }
