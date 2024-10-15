import pgzrun, random, time
WIDTH=960
HEIGHT=768
start=0
timer=0
end=0
fruits=[]
lines=[]
next=0
no=5
game=False
begin=False
score=0

def create():
    global start
    blueberry=Actor("blueberry.png")
    cherry=Actor("cherry.png")
    kiwi=Actor("kiwi.png")
    pineapple=Actor("pineapple.png")
    strawberry=Actor("strawberry.png")
    fruits.extend([blueberry,cherry,kiwi,pineapple,strawberry])
    for j in fruits:
        j.pos=random.randint(20,WIDTH-20),random.randint(20,HEIGHT-20)
    start=time.time()

def draw():
    global start, timer, game, begin
    screen.clear()
    if not begin:
        screen.draw.text("CONNECT THE FRUITS",(70,200),fontsize=30)
        screen.draw.text("Connect each fruit according to it's number.",(70,240),fontsize=30)
        screen.draw.text("As you connect the fruits, a line will appear between each fruit.",(70,280),fontsize=30)
        screen.draw.text("If you press the wrong number, the lines will disappear and you must restart.",(70,320),fontsize=30)
        screen.draw.text("There is a 20 second time-limit.",(70,360),fontsize=30)
        screen.draw.text("PRESS THE SPACEBAR TO CONTINUE",(70,400),fontsize=30)
        return

    screen.blit("forest.jpeg",(0,0))
    var=1
    for j in fruits:
        j.draw()
        screen.draw.text(str(var),(j.pos[0],j.pos[1]+5),fontsize=50)
        var=var+1
    for y in lines:
        screen.draw.line(y[0],y[1],(56,123,189))

    if not game:
        timer = time.time() - start
        screen.draw.text(str(round(timer,1)),(700,465),fontsize=60)
    else:
        screen.draw.text("Game Over!",(700,465),fontsize=60)
    
    screen.draw.text(f"Score:{score}",(700,465),fontsize=60)
    if timer <= 0 and not game:
        game = True
        #screen.fill((0, 0, 0))
        #screen.draw.text("Game Over!",(380,370),fontsize=70)

def update():
    global begin, game
    if not begin:
        if keyboard.space:
            begin=True
            create()
    if timer <= 0:
        game = True

def on_mouse_down(pos):
    global lines, next, score, no, game, fruits
    if game or not begin:
        return
    if next<no:
        if fruits[next].collidepoint(pos):
            score+=1
            if next:
                lines.append((fruits[next-1].pos,fruits[next].pos))
            next=next+1
        else:
            score-=1
            lines=[]
            next=0
            no-=1
            fruits.pop()
        if next >= no:
            game=True
create()

pgzrun.go()
