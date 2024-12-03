import pgzrun, random
WIDTH=1200
HEIGHT=600

sylveon=Actor("sylveon.png")
pokeball=Actor("pokeball.png")
sylveon.pos=600,80
pokeball.pos=600,500
flashes=[]

def draw():
    global flashes
    screen.fill((229, 204, 255))
    pokeball.draw()
    sylveon.draw()
    for i in flashes:
        i.draw()

def on_key_down(key):
    global flashes
    if key==keys.SPACE:
        flashes.append(Actor("flash.png"))
        flashes[-1].x=pokeball.x
        flashes[-1].x=pokeball.y-50
        

def update():
    global flashes
    pass
    if keyboard.left:
        pokeball.x-=10
        if pokeball.x<=0:
            pokeball.x=10
    
    if keyboard.right:
        pokeball.x+=10
        if pokeball.x>=1200:
            pokeball.x=1190

    for i in flashes:
        i.y-=5

pgzrun.go()
