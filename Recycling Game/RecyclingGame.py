import pgzrun, random
WIDTH=800
HEIGHT=448

#Variables
levels=5
speed=14
nonbio=["battery.png","carrierbag.png","crisps.png","plasticbottle.png"]
done=False
finish=False
current=1
options=[]

def draw():
    screen.clear()
    screen.blit("recycling.jpg",(0,0))
    if done:
        screen.fill((0,56,78))
        screen.draw.text('Game Over',center=(400,200),fontsize=70,color='white')
    else:
        for i in options:
            i.draw()

def picture(extra):
    collect=[]
    choices=["biobag.png"]+random.choices(nonbio,k=extra)
    random.shuffle(choices)
    #Creating Actors
    for i in choices:
        items=Actor(i)
        collect.append(items)
    gap=WIDTH/(len(collect)+1)
    for i,item in enumerate(collect):
        item.x=(i+1)*gap
        item.y=0
        animate(item,duration=speed-current,on_finished=gameover,y=HEIGHT)
    return collect

def update():
    global options,current
    if len(options)==0:
        options=picture(current)

def gameover():
    global done
    done=True

def on_mouse_down(pos):
    global options, current, finish
    for i in options:
        if i.collidepoint(pos):
            if "biobag" in i.image:
                if current==levels:
                    finish=True
                else:
                    current=current+1
                    options.clear()
            else:
                gameover()

pgzrun.go()

