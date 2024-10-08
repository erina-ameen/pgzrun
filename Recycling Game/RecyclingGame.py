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

pgzrun.go()

