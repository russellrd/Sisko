import pyowm
import pygame


class Sisko:
    def __init__(self):
        pass

    def update(self):
        weather_surface = COMIC_SANS.render(
            get_temp('Toronto, CA'), 0, (255, 255, 255))
        screen.blit(weather_surface, (WIDTH/2-50, HEIGHT/2-20))


def get_temp(loc):
    location = owm.weather_at_place(loc)
    return str(location.get_weather().get_temperature(
        'celsius')['temp'])+"\u00b0"+"C"


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sisko')

    WIDTH = 800
    HEIGHT = 600
    COMIC_SANS = pygame.font.SysFont('Comic Sans MS', 40)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    owm = pyowm.OWM('a1ffcf0881e1c11c07889b475f8cde59')
    sisko = Sisko()
    print("Sisko is now awake...")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Sisko: Bye!")
                running = False
        screen.fill((100, 100, 0))
        sisko.update()
        pygame.display.update()
