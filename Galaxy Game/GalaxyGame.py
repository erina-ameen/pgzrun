import pgzrun, random
WIDTH=1000
HEIGHT=700
#Variables
score=0
game=False
seconds=60
halftime=30
half=False
timer=20
#Actors
star=Actor("star.png")
star2=Actor("star2.png")
star3=Actor("star3.png")
fallingstar=Actor("fallingstar.png")
spaceship=Actor("spaceship.png")
asteroid=Actor("asteroid.png")
asteroid2=Actor("asteroid2.png")
star.pos=100,240
fallingstar.pos=300,365
spaceship.pos=456,345

def update():
    global begin, game
    if timer <= 0:
        game = True

def move():
    star.x=random.randint(0,WIDTH)
    star.y=random.randint(0,HEIGHT)
def move2():
    star2.x=random.randint(0,WIDTH)
    star2.y=random.randint(0,HEIGHT)
def move3():
    star3.x=random.randint(0,WIDTH)
    star3.y=random.randint(0,HEIGHT)
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
    star2.draw()
    star3.draw()
    fallingstar.draw()
    spaceship.draw()
    asteroid.draw()
    asteroid2.draw()
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
        score=score+10
        move()
    if spaceship.colliderect(star2):
        score=score+10
        move2()
    if spaceship.colliderect(star3):
        score=score+10
        move3()
    if spaceship.colliderect(fallingstar):
        score=score+20
        shift()
    if spaceship.colliderect(asteroid):
        score=score-10
        gone()
    if spaceship.colliderect(asteroid2):
        score=score-10
        gone2()

def lvl2():
    global half
    half=True

def time():
    global game
    game=True
    if timer <= 0 and not game:
        game = True
        screen.fill((0,0,0))
        screen.draw.text("Game Over!",(150,350),fontsize=70)


clock.schedule_interval(move,4.0)
clock.schedule_interval(shift,4.0)
clock.schedule_interval(gone,4.0)
clock.schedule_interval(lvl2,halftime)
clock.schedule(time,seconds)
pgzrun.go()
