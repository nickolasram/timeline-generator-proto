class Link:
    def __init__(self, link, display=False):
        self.link = link
        self.display = display
        if display is False:
            self.display = self.link

    def to_dict(self):
        return {'link': self.link, 'display': self.display}