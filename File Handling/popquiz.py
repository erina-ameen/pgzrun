import pgzrun

TITLE="Pop Quiz"
WIDTH=900
HEIGHT=820

scroll=Rect(0, 0, 900, 200)
scroll.move_ip(0, 0)
quest=Rect(0, 0, 600, 180)
quest.move_ip(20, 220)
timer=Rect(0, 0, 250, 180)
timer.move_ip(630, 220)
skip=Rect(0, 0, 250, 360)
skip.move_ip(630, 420)

opt1=Rect(0, 0, 270, 180)
opt1.move_ip(20, 420)
opt2=Rect(0, 0, 270, 180)
opt2.move_ip(325, 420)
opt3=Rect(0, 0, 270, 180)
opt3.move_ip(20, 615)
opt4=Rect(0, 0, 270, 180)
opt4.move_ip(325, 615)

# Game Variables
seconds=15
score=0
message=""
gameover=False
question1="questions.txt"
opts=[opt1, opt2, opt3, opt4]
qlist=[]
qnumber=0
index=0

def draw():
    global message, seconds
    screen.fill((229, 204, 255))
    screen.draw.filled_rect(scroll, (229, 204, 255))
    screen.draw.filled_rect(quest, "light blue")
    screen.draw.filled_rect(timer, "light yellow")
    screen.draw.filled_rect(skip, "light green")
    screen.draw.filled_rect(opt1, "light pink")
    screen.draw.filled_rect(opt2, "light pink")
    screen.draw.filled_rect(opt3, "light pink")
    screen.draw.filled_rect(opt4, "light pink")
    message="Welcome to Pop Quiz"
    screen.draw.textbox(message, scroll, color="black")
    screen.draw.textbox("Skip", skip, color="black",angle=-90)
    screen.draw.textbox(str(seconds), timer, color="black")
    screen.draw .textbox(question[0].strip(),quest, color="black")
    c=1
    for i in opts:
        screen.draw.textbox(question[c].strip(),i, color="black")
        c+=1
        
def read_file():
    global qnumber,qlist
    reading=open("questions.txt","r",encoding="utf-8")
    for i in reading:
        qlist.append(i)
        qnumber+=1
    reading.close()

def next_question():
    global index
    index+=1
    return qlist.pop(0).split(",")

def skipping():
    global question, qlist, seconds
    if qlist and gameover==False:
        question=next_question()
        seconds=15
    else:
        finish()

def move():
    scroll.x-=4
    if scroll.right<0:
        scroll.left=900

def update():
    move()

def update_timer():
    global seconds, gameover
    if seconds >0:
        seconds-=1
    if seconds==0:
        finish()

def on_mouse_down(pos):
    global skip, gameover
    index=1
    for i in opts:
        if i.collidepoint(pos):
            if index == int(question[5]):
                correct()
            else:
                finish()
        index+=1

    if skip.collidepoint(pos):
        skipping()
        

def finish():
    global question, seconds, gameover
    message=f"Game Over!\nYou got {score} questions correct!"
    question = [message, "-", "-", "-", "-",5]
    seconds=0

def correct():
    global score, question, seconds, qlist
    score+=1
    if qlist:
        question=next_question()
        seconds=15

clock.schedule_interval(update_timer,1)
read_file()
question=next_question()
pgzrun.go()
