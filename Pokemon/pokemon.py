import pgzrun, random
WIDTH=1200
HEIGHT=600

sylveon=Actor("sylveon.png")
pokeball=Actor("pokeball.png")
sylveon.pos=600,80
pokeball.pos=600,500
flashes=[]
end=False
score=0
count=10

def draw():
    global flashes,score
    screen.fill((229, 204, 255))
    pokeball.draw()
    sylveon.draw()
    screen.draw.text("Score:"+str(score),center=(70,10),fontsize=35)
    for i in flashes:
        i.draw()
    if end==True:
        screen.fill((43,87,255))
        screen.draw.text("Game Over!",center=(600,300),fontsize=50)

def on_key_down(key):
    global flashes
    if key==keys.SPACE:
        flashes.append(Actor("flash.png"))
        flashes[-1].x=pokeball.x
        flashes[-1].y=pokeball.y-50      

def update():
    global flashes, score, count
    pass
    sylveon.y+=5.5
    if sylveon.y>=600:
        sylveon.y=0
        sylveon.x=random.randint(0,1200)
        score-=10
        count-=1
        if count==0:
            gameover()

    if keyboard.left:
        pokeball.x-=10
        if pokeball.x<=0:
            pokeball.x=10
    
    if keyboard.right:
        pokeball.x+=10
        if pokeball.x>=1200:
            pokeball.x=1190

    for i in flashes:
        i.y-=10

    for bullet in flashes:
        if sylveon.colliderect(bullet):
            sylveon.y=0
            sylveon.x=random.randint(0,1200)
            score+=20

def gameover():
    global end
    end=True


pgzrun.go()
