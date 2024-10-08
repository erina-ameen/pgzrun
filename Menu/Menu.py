import pgzrun
WIDTH=800
HEIGHT=800

mathbutton = Actor("mathbutton.png")
mathbutton.pos = (400, 150)
factbutton = Actor("factbutton.png")
factbutton.pos = (400, 350)
wordbutton = Actor("wordbutton.png")
wordbutton.pos = (400, 550)
fact={"The world's largest land animal is the African elephant.","The average person laughs about 15 times a day.","A hummingbird's heart can beat up to 1,200 times per minute. That's a lot of energy for such a tiny bird!","The longest word in the English language that can be typed using only the left hand is stewardesses.","A giraffe's tongue is about 18 inches long. It's perfect for reaching those tasty leaves high up in trees!"}
math={"1. 2000","2. 46","3. 7687","4. hello"}
word={"1. Ephemeral: Lasting for a very short time. Example: The morning dew was ephemeral, disappearing as the sun rose.","2. Quixotic: Impractically idealistic. Example: His quixotic dream of flying to the moon was met with laughter.","3. Serendipity: Occurring by chance in a happy or beneficial way. Example: We found this amazing antique shop completely by serendipity.","4. Schadenfreude: Pleasure derived from the misfortunes of others. Example: There was a hint of schadenfreude in his voice when he heard about my mistake.","5. Ethereal: Light and delicate; seemingly not of this world. Example: The ethereal beauty of the sunset filled the sky with soft colors."}

def draw():
    screen.fill((255,255,255))
    mathbutton.draw()
    factbutton.draw()
    wordbutton.draw()

def on_mouse_down(pos):
    if mathbutton.collidepoint(pos):
        print(math)
        ans=int(input("Write the NUMBER of the correct answer to the sum --> 50 x 40:  "))
        
        if ans == 1:
            print("Correct!")
        else:
            math.remove("2. 46")
            math.remove("3. 7687")
            math.remove("4. hello")
            print("Incorrect. The correct number is ",(math))

    if factbutton.collidepoint(pos):
        ans2=int(input("Pick a number from 1-5 "))
        if ans2 == 1:
            fact.discard("The average person laughs about 15 times a day.")
            fact.discard("A hummingbird's heart can beat up to 1,200 times per minute. That's a lot of energy for such a tiny bird!")
            fact.discard("A giraffe's tongue is about 18 inches long. It's perfect for reaching those tasty leaves high up in trees!")
            fact.discard("The longest word in the English language that can be typed using only the left hand is stewardesses.")
            print(fact)
        if ans2 == 2:
            fact.discard("The world's largest land animal is the African elephant.")
            fact.discard("A hummingbird's heart can beat up to 1,200 times per minute. That's a lot of energy for such a tiny bird!")
            fact.discard("A giraffe's tongue is about 18 inches long. It's perfect for reaching those tasty leaves high up in trees!")
            fact.discard("The longest word in the English language that can be typed using only the left hand is stewardesses.")
            print(fact)
        if ans2 == 3:
            fact.discard("The world's largest land animal is the African elephant.")
            fact.discard("The average person laughs about 15 times a day.")
            fact.discard("A giraffe's tongue is about 18 inches long. It's perfect for reaching those tasty leaves high up in trees!")
            fact.discard("The longest word in the English language that can be typed using only the left hand is stewardesses.")
            print(fact)
        if ans2 == 4:
            fact.discard("The world's largest land animal is the African elephant.")
            fact.discard("The average person laughs about 15 times a day.")
            fact.discard("A hummingbird's heart can beat up to 1,200 times per minute. That's a lot of energy for such a tiny bird!")
            fact.discard("The longest word in the English language that can be typed using only the left hand is stewardesses.")
            print(fact)
        if ans2 == 5:
            fact.discard("The world's largest land animal is the African elephant.")
            fact.discard("The average person laughs about 15 times a day.")
            fact.discard("A hummingbird's heart can beat up to 1,200 times per minute. That's a lot of energy for such a tiny bird!")
            fact.discard("A giraffe's tongue is about 18 inches long. It's perfect for reaching those tasty leaves high up in trees!")
            print(fact)

    if wordbutton.collidepoint(pos):
        ans3=int(input("Pick a number from 1-5 "))
        if ans3 == 1:
            word.discard("2. Quixotic: Impractically idealistic. Example: His quixotic dream of flying to the moon was met with laughter.")
            word.discard("3. Serendipity: Occurring by chance in a happy or beneficial way. Example: We found this amazing antique shop completely by serendipity.")
            word.discard("4. Schadenfreude: Pleasure derived from the misfortunes of others. Example: There was a hint of schadenfreude in his voice when he heard about my mistake.")
            word.discard("5. Ethereal: Light and delicate; seemingly not of this world. Example: The ethereal beauty of the sunset filled the sky with soft colors.")
            print(word)
        if ans3 == 2:
            word.discard("1. Ephemeral: Lasting for a very short time. Example: The morning dew was ephemeral, disappearing as the sun rose.")
            word.discard("3. Serendipity: Occurring by chance in a happy or beneficial way. Example: We found this amazing antique shop completely by serendipity.")
            word.discard("4. Schadenfreude: Pleasure derived from the misfortunes of others. Example: There was a hint of schadenfreude in his voice when he heard about my mistake.")
            word.discard("5. Ethereal: Light and delicate; seemingly not of this world. Example: The ethereal beauty of the sunset filled the sky with soft colors.")
            print(word)
        if ans3 == 3:
            word.discard("1. Ephemeral: Lasting for a very short time. Example: The morning dew was ephemeral, disappearing as the sun rose.")
            word.discard("2. Quixotic: Impractically idealistic. Example: His quixotic dream of flying to the moon was met with laughter.")
            word.discard("4. Schadenfreude: Pleasure derived from the misfortunes of others. Example: There was a hint of schadenfreude in his voice when he heard about my mistake.")
            word.discard("5. Ethereal: Light and delicate; seemingly not of this world. Example: The ethereal beauty of the sunset filled the sky with soft colors.")
            print(word)
        if ans3 == 4:
           word.discard("1. Ephemeral: Lasting for a very short time. Example: The morning dew was ephemeral, disappearing as the sun rose.")
           word.discard("2. Quixotic: Impractically idealistic. Example: His quixotic dream of flying to the moon was met with laughter.")
           word.discard("3. Serendipity: Occurring by chance in a happy or beneficial way. Example: We found this amazing antique shop completely by serendipity.")
           word.discard("5. Ethereal: Light and delicate; seemingly not of this world. Example: The ethereal beauty of the sunset filled the sky with soft colors.")
           print(word)
        if ans3 == 5:
            word.discard("1. Ephemeral: Lasting for a very short time. Example: The morning dew was ephemeral, disappearing as the sun rose.")
            word.discard("2. Quixotic: Impractically idealistic. Example: His quixotic dream of flying to the moon was met with laughter.")
            word.discard("3. Serendipity: Occurring by chance in a happy or beneficial way. Example: We found this amazing antique shop completely by serendipity.")
            word.discard("4. Schadenfreude: Pleasure derived from the misfortunes of others. Example: There was a hint of schadenfreude in his voice when he heard about my mistake.")
            print(word)
            
pgzrun.go()