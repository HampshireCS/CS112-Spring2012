class TiledImage(object):
    def __init__(self, image, rect=None):

        self.image = image

        if rect is None:
            self.rect = image.get_rect()
        else:
            self.rect = rect

    
    def draw(self, surf, rect=None):
        # if no rect is given, use surfaces rect
        if rect is None:
            rect = surf.get_rect()

        w, h = self.rect.size
        x, y = self.rect.topleft

        # calculate the start and end points
        x0 = rect.x - (-x % w)
        x1 = rect.x + rect.width

        y0 = rect.y - (-y % h)
        y1 = rect.y + rect.height

        # loop through and draw images
        for y in xrange(y0, y1, h):
            for x in xrange(x0, x1, w):
                surf.blit(self.image, (x, y))

