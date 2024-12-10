import pgzrun, random
WIDTH=1200
HEIGHT=600

fly=Actor("fly.png")
spider=Actor("spider.png")
fly.pos=600,80
spider.pos=600,500
webs=[]
end=False
score=0
count=10

def draw():
    global webs,score
    screen.fill((229, 204, 255))
    spider.draw()
    fly.draw()
    screen.draw.text("Score:"+str(score),center=(70,10),fontsize=35)
    for i in webs:
        i.draw()
    if end==True:
        screen.fill((43,87,255))
        screen.draw.text("Game Over!",center=(600,300),fontsize=50)

def on_key_down(key):
    global webs
    if key==keys.SPACE:
        webs.append(Actor("flash.png"))
        webs[-1].x=spider.x
        webs[-1].y=spider.y-50      

def update():
    global webs, score, count
    pass
    fly.y+=5.5
    if fly.y>=600:
        fly.y=0
        fly.x=random.randint(0,1200)
        score-=10
        count-=1
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

    for bullet in webs :
        if fly.colliderect(bullet):
            fly.y=0
            fly.x=random.randint(0,1200)
            score+=20

def gameover():
    global end
    end=True


pgzrun.go()