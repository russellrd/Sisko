import pyowm
import pygame
import threading
from newsapi import NewsApiClient

#https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds

class Sisko:
    def __init__(self):
        self.health = 100

    def feed(self):
        self.heath += 5

    def update(self):
        pass
    
    def display(self):
        weather_surface = COMIC_SANS.render(
            get_temp('Toronto, CA'), 0, (255, 255, 255))
        screen.blit(weather_surface, (WIDTH/2-50, HEIGHT/2-20))

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def get_temp(loc):
    location = owm.weather_at_place(loc)
    return str(location.get_weather().get_temperature(
        'celsius')['temp'])+"\u00b0"+"C"

def get_latest_news(loc):
    top_headlines = newsapi.get_top_headlines(country=loc)
    print(top_headlines)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Sisko')

    WIDTH = 800
    HEIGHT = 600
    COMIC_SANS = pygame.font.SysFont('Comic Sans MS', 40)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    owm = pyowm.OWM('a1ffcf0881e1c11c07889b475f8cde59')
    newsapi = NewsApiClient(api_key=open("newsapi.txt", "r").read())

    sisko = Sisko()
    print("Sisko is now awake...")

    get_latest_news('ca')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Sisko: Bye!")
                running = False
        screen.fill((100, 100, 0))
        sisko.update()
        sisko.display()
        pygame.display.update()
