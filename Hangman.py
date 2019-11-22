import random, os, platform
def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
os.system('title Hangman')
clear()
words = {
    "animals":{"fox","tiger","dog","cat","falcon"},
    "games":{"skyrim","super smash bros", "pokemon", "portal", "mortal combat"},
    "youtubers":{"mini ladd","vanoss","skydoesminecraft","jacksepticeye","pewdiepie","shroud"},
    "consoles":{"switch","xbox","nes","game cube","playstation","wii"},
    "companies":{"youtube","google","microsoft","apple","nintendo","gamefreak"},
    "candy":{"mnms","skittles","smarties","snickers","tootsierolls"},
    "superheros":{"superman","spiderman","captain america","black panther","flash","ben ten"},
    "card games":{"uno","poker","magic the gathering","yugioh","pokemon","superfight"}
}

letters = {
    "A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":False, "H":False, "I":False, "J":False, 
    "K":False, "L":False, "M":False, "N":False, "O":False, "P":False, "Q":False, "R":False, "S":False, "T":False, 
    "U":False, "V":False, "W":False, "X":False, "Y":False, "Z":False
}
guesses = 6

def esc(code):
    return "\033["+str(code)+"m"

def get_allwords():
    allwords = set(())
    for x in words:
        allwords.update(words[x])
    return allwords
words["any"]=get_allwords()

def get_word(category = "any"):
    return random.choice(list(words[category]))

def disp_letters():
    print("")
    letters_disp=[]
    for x in letters:
        if letters.get(x) == True:
            letters_disp.append(esc(33)+x+esc(0))
        else:
            letters_disp.append(x) 
    print(" ".join(letters_disp[:9]))
    print(" ".join(letters_disp[10:19]))
    print("  "+" ".join(letters_disp[19:]))
    print("")

def disp_lines():
    out = ""
    missing_letters = 0
    for x in word:
        out+=" "
        if x == " ":
            out+=x
        for y in letters:
            if x.lower() == y.lower():
                if letters.get(y) == True:
                    out+=esc(4)+x+esc(0)
                else:
                    missing_letters += 1
                    out+="_"
    print(out)
    if missing_letters == 0:
        raise StopIteration
def choose_letters():
    global guesses
    entered_letters = raw_input("Enter letters: ")
    for x in entered_letters:
        if x.upper() in letters and letters.get(x.upper()) == False:
            letters[x.upper()] = True
            if x not in word:
                guesses -= 1

while True:
    print("Available categories: "+", ".join(words.keys()))
    category = raw_input("Choose Category: ")
    if category == "":
        category = "any"
        break
    if category in words:
        break
    else:
        clear()
word = get_word(category)
clear()


while guesses != 0:
    clear()
    disp_letters()
    try:
        disp_lines()
    except StopIteration:
        break
    print(guesses)
    choose_letters()


clear()
print("Game Over")