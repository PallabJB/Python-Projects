from tkinter import *
import ctypes
import random
import tkinter

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup
window = Tk()
window.title('Typing Speed Test')
window.config(bg="#EBF3E8")

window.geometry('1080x720')

window.option_add("*Label.Font", "consolas 30")
window.option_add("*Button.Font", "consolas 30")


def handlinglabels():
    # Text List
    random_selection = [
        'A random statement can inspire authors and help them start writing. It challenges the author to use their imagination because the sentences subject is utterly ambiguous. The random sentence may be creatively used in a variety of ways by writers. The statement is most frequently used to start a tale. Another choice is to include it into the narrative. The issue of using it to conclude a tale is far more challenging. In all of these scenarios, the writer is compelled to use their imagination because they have no idea what words will come out of the tool.',
        'Python Code aims to teach beginning and intermediate programmers Python through tutorials, recipes, articles, and problem-solving techniques while also disseminating information globally. Everyone in the globe will be able to learn how to code for free thanks to Python Code. Python is a general-purpose, high-level, interpreted programming language. Code readability is prioritised in its design philosophy, which makes heavy use of indentation. Python uses garbage collection and has dynamic typing. It supports a variety of programming paradigms, including procedural, object-oriented, and functional programming as well as structured programming (especially this). Due to its extensive standard library, it is frequently referred to as a "batteries included" language.',
        'We begin with the imports as usual. We must import tkinter since we utilise it to create the user interface. In order to subsequently modify the typefaces on our components, we additionally import the font module from tkinter. The partial function is obtained from functools and is a brilliant function that accepts another function as a first argument, along with certain args and kwargs, and returns a reference to this function with those arguments. When we wish to add one of our functions to a command argument of a button or key binding, this is extremely helpful.',
        'A computer programmer is a person who writes computer programmes, frequently for bigger pieces of software. They are also known as software developers, software engineers, programmers, or coders. A programmer is a person who uses a particular programming language to construct or write computer software or applications. The majority of programmers have substantial computer and coding expertise across a wide range of platforms and programming languages, including SQL, Perl, XML, PHP, HTML, C, C++, and Java. The terms "programmer" and "software engineer" may be used to describe the same position at various businesses because there is no industry-wide vocabulary standard. Usually, a "programmer" or "software developer" will concentrate on translating a precise specification into computer code.'
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(random_selection).lower()

    split_point = 0

    global nameLabelLeft
    nameLabelLeft = Label(window, text=text[0:split_point], fg='green', bg="#EBF3E8")
    nameLabelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global nameLabelRight
    nameLabelRight = Label(window, text=text[split_point:], bg="#EBF3E8")
    nameLabelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentAlphabetLabel
    currentAlphabetLabel = Label(window, text=text[split_point], fg='grey', bg="#EBF3E8")
    currentAlphabetLabel.place(relx=0.5, rely=0.6, anchor=N)

    global secondsLeft
    headingLabel = Label(window, text=f'Typing Speed Test', fg='#7FBCD2', bg="#EBF3E8")
    headingLabel.place(relx=0.5, rely=0.2, anchor=S)
    secondsLeft = Label(window, text=f'0 Seconds', fg='#190482', bg="#EBF3E8")
    secondsLeft.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    window.bind('<Key>', handlekeypress)

    global secondsPassed
    secondsPassed = 0

    window.after(60000, stopgame)
    window.after(1000, timeaddition)


def stopgame():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amount_words = len(nameLabelLeft.cget('text').split(' '))

    secondsLeft.destroy()
    currentAlphabetLabel.destroy()
    nameLabelRight.destroy()
    nameLabelLeft.destroy()

    global labelOfResult
    labelOfResult = Label(window, text=f'Words per Minute (WPM): {amount_words}', fg='#190482', bg="#EBF3E8")
    labelOfResult.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restartgame the game
    global showcaseResults
    showcaseResults = Button(window, text=f'Retry', command=restartgame, bg="#00A9FF")
    showcaseResults.place(relx=0.5, rely=0.6, anchor=CENTER)


def restartgame():
    # Destroy result widgets
    labelOfResult.destroy()
    showcaseResults.destroy()
    handlinglabels()


def timeaddition():
    global secondsPassed
    secondsPassed += 1
    secondsLeft.configure(text=f'{secondsPassed} Seconds')

    if writeAble:
        window.after(1000, timeaddition)


def handlekeypress(event=None):
    try:
        if event.char.lower() == nameLabelRight.cget('text')[0].lower():
            nameLabelRight.configure(text=nameLabelRight.cget('text')[1:])
            nameLabelLeft.configure(text=nameLabelLeft.cget('text') + event.char.lower())
            currentAlphabetLabel.configure(text=nameLabelRight.cget('text')[0])
    except tkinter.TclError:
        pass


handlinglabels()

window.mainloop()