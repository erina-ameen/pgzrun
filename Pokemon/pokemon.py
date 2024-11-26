import pgzrun, random
WIDTH=1200
HEIGHT=600

sylveon=Actor("sylveon.png")
pokeball=Actor("pokeball.png")
sylveon.pos=600,80
pokeball.pos=600,500
def draw():
    screen.fill((229, 204, 255))
    pokeball.draw()
    sylveon.draw()

def update():
    pass

pgzrun.go()