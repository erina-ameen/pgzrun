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
    global start, timer
    screen.clear()
    screen.blit("forest.jpeg",(0,0))
    var=1
    for j in fruits:
        j.draw()
        screen.draw.text(str(var),(j.pos[0],j.pos[1]+5),fontsize=50)
        var=var+1
    for y in lines:
        screen.draw.line(y[0],y[1],(56,123,189))
    if next < no:
        timer = time.time() - start 
        screen.draw.text(str(round(timer,1)),(700,465),fontsize=60)
    else:
        screen.draw.text(str(round(timer,1)),(700,465),fontsize=60)

def on_mouse_down(pos):
    global lines, next
    if next<no:
        if fruits[next].collidepoint(pos):
            if next:
                lines.append((fruits[next-1].pos,fruits[next].pos))
            next=next+1

create()

pgzrun.go()
