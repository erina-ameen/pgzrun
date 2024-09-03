import pgzrun, random, time
WIDTH=893
HEIGHT=500
start=0
time=0
end=0
fruits=[]
lines=[]
next=0

def create():
    global start
    blueberry=Actor("blueberry.png")
    cherry=Actor("cherry.png")
    kiwi=Actor("kiwi.png")
    pineapple=Actor("pineapple.png")
    strawberry=Actor("strawberry.png")
    fruits.extend([blueberry,cherry,kiwi,pineapple,strawberry])
    for i in fruits:
        i.pos=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    #start=time.time()

def draw():
    for i in fruits:
        i.draw()
create()

pgzrun.go()