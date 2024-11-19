import pgzrun

TITLE = "Math Quiz"
WIDTH = 900
HEIGHT = 820

scroll = Rect(0, 0, 900, 200)
scroll.move_ip(0, 0)
quest = Rect(0, 0, 600, 180)
quest.move_ip(20, 220)
timer = Rect(0, 0, 250, 180)
timer.move_ip(630, 220)
skip = Rect(0, 0, 250, 360)
skip.move_ip(630, 420)

opt1 = Rect(0, 0, 270, 180)
opt1.move_ip(20, 420)
opt2 = Rect(0, 0, 270, 180)
opt2.move_ip(325, 420)
opt3 = Rect(0, 0, 270, 180)
opt3.move_ip(190, 615)

# Game Variables
seconds = 15
score = 0
message = ""
gameover = False
question_file = "mathquestion.txt"
options = [opt1, opt2, opt3]
questions = []
current_question = 0
current_option = 0

def draw():
    global message, seconds
    screen.fill("white")
    screen.draw.filled_rect(scroll, "pink")
    screen.draw.filled_rect(quest, "blue")
    screen.draw.filled_rect(timer, "green")
    screen.draw.filled_rect(skip, "green")
    screen.draw.filled_rect(opt1, "purple")
    screen.draw.filled_rect(opt2, "purple")
    screen.draw.filled_rect(opt3, "purple")
    screen.draw.textbox(message, scroll, color="black")
    screen.draw.textbox("Skip", skip, color="black", angle=-90)
    screen.draw.textbox(str(seconds), timer, color="black")
    screen.draw.textbox(questions[0].strip(), quest, color="black")
    index=1
    for i in options:
        screen.draw.textbox(questions[index].strip(), i, color="black")
        index+=1

def read_file():
    global questions
    with open(question_file, "r") as f:
        for line in f:
            questions.append(line)

def update_timer():
    global seconds, gameover
    if seconds > 0:
        seconds -= 1
    if seconds == 0:
        gameover = True

clock.schedule_interval(update_timer, 1)
read_file()
pgzrun.go()