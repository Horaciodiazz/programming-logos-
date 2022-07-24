import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
default_size = 35
default_Font = 'sansserif'

class text:

    def __init__(self):
        pass

    def write(self, font=default_Font, size=default_size, text='Simple text',
     color=(255, 255, 255), background_color=None, surface=None, x=0, y=0):

        type_text = pygame.font.SysFont(font, size)
        text1 = type_text.render(str(text), True, color, background_color)

        width_Text = text1.get_width()
        height_Text = text1.get_height()

        written_text = surface.blit(text1, (x - width_Text / 2, y - height_Text / 2))

        return written_text
