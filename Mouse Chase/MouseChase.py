import pgzrun, random
WIDTH=1000
HEIGHT=590
#Variables
score=0
game=False
seconds=10
#Actors
tom=Actor("tomcat.png")
jerry=Actor("jerrymouse.png")
tom.pos=100,240
jerry.pos=300,365

def move():
    jerry.x=random.randint(0,WIDTH)
    jerry.y=random.randint(0,HEIGHT)

def draw():
    screen.blit("staircase.jpg",(0,0))
    tom.draw()
    jerry.draw()
    screen.draw.text("Score:"+str(score),(10,10),fontsize=50)
    if game:
        screen.fill("Purple")
        screen.draw.text("Game Over! Your score is"+str(score),(10,10),fontsize=50)

def update():
    if keyboard.left:
        tom.x=tom.x-10
    if keyboard.right:
        tom.x=tom.x+10
    if keyboard.up:
        tom.y=tom.y-10
    if keyboard.down:
        tom.y=tom.y+10
    global score
    if tom.colliderect(jerry):
        score=score+1
        move()

def time():
    global game
    game=True

clock.schedule_interval(move,2.0)
clock.schedule_interval(time,seconds)
pgzrun.go()
