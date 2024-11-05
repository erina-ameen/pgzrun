import pgzrun
TITLE="Pop Quiz"
WIDTH=900
HEIGHT=820

#Box Definition
scroll=Rect(0,0,900,200)
scroll.move_ip(0,0)
quest=Rect(0,0,600,180)
quest.move_ip(20,220)
timer=Rect(0,0,250,180)
timer.move_ip(630,220)
skip=Rect(0,0,250,360)
skip.move_ip(630,420)

opt1=Rect(0,0,270,180)
opt1.move_ip(20,420)
opt2=Rect(0,0,270,180)
opt2.move_ip(325,420)
opt3=Rect(0,0,270,180)
opt3.move_ip(20,615)
opt4=Rect(0,0,270,180)
opt4.move_ip(325,615)

#Game Variables
seconds=15
score=0
message=""
gameover=False
question="questions.txt"
opts=[opt1,opt2,opt3,opt4]
qlist=[]
qnumber=0
index=0

def draw():
    global message
    screen.fill((255,255,255))
    screen.draw.filled_rect(scroll,(229,204,255))
    screen.draw.filled_rect(quest,"light blue")
    screen.draw.filled_rect(timer,"light yellow")
    screen.draw.filled_rect(skip,"light green")
    screen.draw.filled_rect(opt1,"light pink")
    screen.draw.filled_rect(opt2,"light pink")
    screen.draw.filled_rect(opt3,"light pink")
    screen.draw.filled_rect(opt4,"light pink")
    message="Welcome to Pop Quiz"
    screen.draw.textbox(message,scroll,color="black")

def update():
    pass

pgzrun.go()
