import pgzrun, random

WIDTH=1200
HEIGHT=600

spider=Actor("spider.png")
spider.pos=600, 500
webs=[]
end=False
score=0
count=10
enemies=[]

def spawn_wave():
    global enemies
    enemies=[]
    for i in range(8):
        fly=Actor("fly.png")
        enemies.append(fly)
        enemies[-1].x=100+90*i
        enemies[-1].y=0

spawn_wave()

def draw():
    global webs, score
    screen.fill((34, 78, 255))
    spider.draw()
    for i in enemies:
        i.draw()
    screen.draw.text("Score:" + str(score), center=(70, 10), fontsize=35)
    for i in webs:
        i.draw()
    if end:
        screen.fill((43, 87, 255))
        screen.draw.text("Game Over!", center=(600, 300), fontsize=50)

def on_key_down(key):
    global webs
    if key == keys.SPACE:
        webs.append(Actor("web.png"))
        webs[-1].x=spider.x
        webs[-1].y=spider.y - 50

direction=1

def update():
    global webs, score, count, direction
    move=False

    if count==0:
        gameover()

    if keyboard.left:
        spider.x-=10
        if spider.x<=0:
            spider.x=10

    if keyboard.right:
        spider.x+=10
        if spider.x>=1200:
            spider.x=1190

    for i in webs:
        i.y-=10

    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        direction=direction*-1
        move=True

    for i in enemies:
        i.x+=5*direction
        if move:
            i.y+=80
        for bullet in webs:
            if i.colliderect(bullet):
                sounds.eep.play()
                enemies.remove(i)
                score+=20
                break

    if len(enemies)==0:
        spawn_wave()

def gameover():
    global end
    end=True

pgzrun.go()
