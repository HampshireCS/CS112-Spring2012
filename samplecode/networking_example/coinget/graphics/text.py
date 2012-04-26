from pygame import Rect, Surface, SRCALPHA

LEFT=0
RIGHT=1
CENTER=2

class TextBlock(object):
    
    LEFT = LEFT
    RIGHT = RIGHT
    CENTER = CENTER

    def __init__(self, font, padding=10, justify=LEFT, margin=5):
        self.font = font
        self.padding = padding
        self.margin = margin
        self.justify = justify


    def render(self, lines, antialias, fg, bg=None):
        block = []
        bounds = Rect(0,0,self.margin,self.margin)
        for line in lines:

            if bg is not None:
                text = self.font.render(line, antialias, fg, bg)
            else:
                text = self.font.render(line, antialias, fg)

            rect = text.get_rect()
            if bounds.bottom > self.margin:
                rect.top = bounds.bottom + self.padding

            bounds.union_ip(rect)
            block.append((text,rect))
        
        bounds.height += self.margin


        surf = Surface(bounds.size, SRCALPHA)

        if bg is not None:
            surf.fill(bg)
        else:
            surf.fill((0,0,0,0))

        for line,rect in block:

            if self.justify == LEFT:
                rect.left = bounds.left + self.margin
            elif self.justify == RIGHT:
                rect.right = bounds.right - self.margin
            elif self.justify == CENTER:
                rect.centerx = bounds.centerx

            surf.blit(line, rect)

        return surf


