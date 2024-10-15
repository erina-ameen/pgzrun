import pgzrun, random
WIDTH=800
HEIGHT=448

#Variables
levels=5
speed=14
nonbio=["battery.png","carrierbag.png","crisps.png","plasticbottle.png"]
gameover=False
finish=False
current=1
options=[]

def draw():
    screen.clear()
    screen.blit("recycling.jpg",(0,0))

def picture(extra):
    collect=[]
    choices=["biobag.png"]+random.choices(nonbio,k=extra)
    random.shuffle(choices)
    #Creating Actors
    for i in choices:
        items=Actor(i)
        collect.append(items)

pgzrun.go()
