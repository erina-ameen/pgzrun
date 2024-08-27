import pgzrun, random
TITLE="Shoot The Flower"
WIDTH=1606
HEIGHT=900
txt=""
heart=Actor("heart.png")
def draw():
    screen.clear()
    screen.blit("pinkclouds.png",(0,0))
    heart.draw()
    screen.draw.text(txt,center=(400,560),fontsize=50)

def move():
    heart.x=random.randint(0,WIDTH)
    heart.y=random.randint(0,HEIGHT)

def on_mouse_down(pos):
    global txt
    if heart.collidepoint(pos):
        txt="good job"
        move()
    else:
        txt="you missed!"
    

clock.schedule_interval(move,1.0)    
pgzrun.go()