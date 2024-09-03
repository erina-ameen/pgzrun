import pgzrun, random
WIDTH=1000
HEIGHT=667
#Variables
score=0
game=False
seconds=60
halftime=30
half=False
#Actors
star=Actor("star.png")
fallingstar=Actor("fallingstar.png")
spaceship=Actor("spaceship.png")
asteroid=Actor("asteroid.png")
asteroid2=Actor("asteroid2.png")
star.pos=100,240
fallingstar.pos=300,365
spaceship.pos=456,345

def move():
    star.x=random.randint(0,WIDTH)
    star.y=random.randint(0,HEIGHT)
def shift():
    fallingstar.x=random.randint(0,WIDTH)
    fallingstar.y=random.randint(0,HEIGHT)
def gone():
    asteroid.x=random.randint(0,WIDTH)
    asteroid.y=random.randint(0,HEIGHT)    
def gone2():
    asteroid2.x=random.randint(0,WIDTH)
    asteroid2.y=random.randint(0,HEIGHT)    

def draw():
    screen.blit("galaxy.jpg",(0,0))
    star.draw()
    fallingstar.draw()
    spaceship.draw()
    asteroid.draw()
    screen.draw.text("Score:"+str(score),(10,10),fontsize=50)
    
    if half:
        asteroid2.draw()

    if game:
        screen.fill("Purple")
        screen.draw.text("Game Over! Your score is"+str(score),(10,10),fontsize=50)

def update():
    if keyboard.left:
        spaceship.x=spaceship.x-10
    if keyboard.right:
        spaceship.x=spaceship.x+10
    if keyboard.up:
        spaceship.y=spaceship.y-10
    if keyboard.down:
        spaceship.y=spaceship.y+10
    global score
    if spaceship.colliderect(star):
        score=score+1
        move()
    if spaceship.colliderect(fallingstar):
        score=score+2
        shift()
    if spaceship.colliderect(asteroid):
        score=score-1
        gone()
    if spaceship.colliderect(asteroid2):
        score=score-2
        gone2()
        move()
        shift()

def lvl2():
    global half
    half=True

def time():
    global game
    game=True

clock.schedule_interval(move,2.0)
clock.schedule_interval(shift,1.0)
clock.schedule_interval(gone,1.0)
clock.schedule_interval(lvl2,halftime)
clock.schedule_interval(time,seconds)
pgzrun.go()
