import random
from tkinter import *
from PIL import Image, ImageTk
from manipulator import SpeedCalc
import threading
import time

BIG_FONT = ("Arial", 30, "bold")


# Setting up the user interface
class TypingSpeedUI:
    def __init__(self, speed_calc: SpeedCalc):
        self.window = Tk()
        self.window.title = "Typing Speed Tester"
        self.window.geometry("1550x1000")
        self.window.config(padx=80, pady=10, bg="#F5F5F5")
        self.speed_calc = speed_calc

        rectangle_img = Image.open("images/blue_rectangle.png")
        rectangle_img_width, rectangle_img_height = rectangle_img.size
        rectangle_img_width = int(rectangle_img_width / 3.7)
        rectangle_img_height = int(rectangle_img_height / 5)
        rectangle_img = rectangle_img.resize((rectangle_img_width, rectangle_img_height), Image.LANCZOS)
        rectangle_img = ImageTk.PhotoImage(rectangle_img)
        self.rectangle_block_label = Label(image=rectangle_img, bg="#F5F5F5", highlightthickness=0)
        self.rectangle_block_label.grid(row=0, column=1, columnspan=4, padx=(40, 0))

        text_label_ = Label(text="Typing Speed Tester", font=BIG_FONT, fg="white", bg="#5EB8CC")
        text_label_.grid(row=0, column=1, columnspan=6, padx=(20, 0))

        square_card1 = Image.open("images/square_white_card.png")
        square_card1_width, square_card1_height = square_card1.size
        square_card1_width = int(square_card1_width / 6)
        square_card1_height = int(square_card1_height / 6)
        square_card1 = square_card1.resize((square_card1_width, square_card1_height), Image.LANCZOS)
        square_card1 = ImageTk.PhotoImage(square_card1)
        self.square_cared1_label = Label(image=square_card1, bg="#F5F5F5", highlightthickness=0)
        self.square_cared1_label.grid(row=1, column=1, pady=(30, 0), padx=(0, 0))
        self.text1_label = Label(text="WPM\n0:00", bg="white", highlightthickness=0,
                                 font=("Helvetica", 15, "bold"), fg="#72939A")
        self.text1_label.grid(row=1, column=1, pady=(30, 0), padx=(0, 0))

        self.square_cared1_label = Label(image=square_card1, bg="#F5F5F5", highlightthickness=0)
        self.square_cared1_label.grid(row=1, column=1, pady=(30, 0), padx=(250, 0))
        self.text2_label = Label(text="CPM\n0:00", bg="white", highlightthickness=0,
                                 font=("Helvetica", 15, "bold"), fg="#72939A")
        self.text2_label.grid(row=1, column=1, pady=(30, 0), padx=(250, 0))

        self.square_cared1_label = Label(image=square_card1, bg="#F5F5F5", highlightthickness=0)
        self.square_cared1_label.grid(row=1, column=1, pady=(30, 0), padx=(500, 0))
        self.text3_label = Label(text="CPS\n0:00", bg="white", highlightthickness=0,
                                 font=("Helvetica", 15, "bold"), fg="#72939A")
        self.text3_label.grid(row=1, column=1, pady=(30, 0), padx=(500, 0))

        rect_white_card1 = Image.open("images/rect_white_card1.png")
        rect_white_card1_width, rect_white_card1_height = rect_white_card1.size
        rect_white_card1_width = int(rect_white_card1_width / 6)
        rect_white_card1_height = int(rect_white_card1_height / 7)
        rect_white_card1 = rect_white_card1.resize((rect_white_card1_width, rect_white_card1_height), Image.LANCZOS)
        rect_white_card1 = ImageTk.PhotoImage(rect_white_card1)
        self.rect_white_card1_label = Label(image=rect_white_card1, bg="#F5F5F5", highlightthickness=0)
        self.rect_white_card1_label.grid(row=1, column=2, columnspan=2, pady=(30, 0), padx=(0, 30))
        self.text4_label = Label(text="Highest Score\nWPM: 0:00  CPM: 0:00", bg="white", highlightthickness=0,
                                 font=("Helvetica", 13, "bold"), fg="#71D86F")
        self.text4_label.grid(row=1, column=2, columnspan=2, pady=(30, 0), padx=(0, 30))

        rect_white_card2 = Image.open("images/rect_white_card2.png")
        rect_white_card2_width, rect_white_card2_height = rect_white_card2.size
        rect_white_card2_width = int(rect_white_card2_width / 3)
        rect_white_card2_height = int(rect_white_card2_height / 4)
        rect_white_card2 = rect_white_card2.resize((rect_white_card2_width, rect_white_card2_height), Image.LANCZOS)
        rect_white_card2 = ImageTk.PhotoImage(rect_white_card2)
        self.rect_white_card2_label = Label(image=rect_white_card2, bg="#F5F5F5", highlightthickness=0)
        self.rect_white_card2_label.grid(row=2, column=1, columnspan=6, pady=(20, 0), padx=(15, 0))

        self.text_label = Label(text="hi bro", bg="white", highlightthickness=0,
                                font=("Helvetica", 20, "normal"), fg="#494949")
        self.text_label.grid(row=2, column=1, columnspan=6, padx=(25, 0))

        rect_white_card3 = Image.open("images/rect_white_card3.png")
        rect_white_card3_width, rect_white_card3_height = rect_white_card3.size
        rect_white_card3_width = int(rect_white_card3_width / 4)
        rect_white_card3_height = int(rect_white_card3_height / 7)
        rect_white_card3 = rect_white_card3.resize((rect_white_card3_width, rect_white_card3_height), Image.LANCZOS)
        rect_white_card3 = ImageTk.PhotoImage(rect_white_card3)
        self.rect_white_card3_label = Label(text="Hello Bro", image=rect_white_card3, bg="#F5F5F5",
                                            highlightthickness=0)
        self.rect_white_card3_label.grid(row=3, column=1, columnspan=4, pady=(30, 0), padx=(40, 0))
        self.typed_text = Entry(self.window, font=("Arial", 20, "normal"), bg="white",
                                fg="#3E3E3E", width=50, highlightthickness=0, borderwidth=0,
                                border=0, justify=CENTER, relief=GROOVE)
        self.typed_text.grid(row=3, column=1, columnspan=4, padx=(40, 0), pady=(30, 0))
        self.typed_text.bind("<KeyPress>", self.start)

        # Start button
        start_button_image = Image.open("images/reset_button.png")
        start_button_image_width, start_button_image_height = start_button_image.size
        start_button_image_width = int(start_button_image_width)
        start_button_image_height = int(start_button_image_height)
        start_button_image = start_button_image.resize((start_button_image_width,
                                                        start_button_image_height), Image.LANCZOS)
        start_button_img = ImageTk.PhotoImage(start_button_image)
        start_button_img_label = Label(image=start_button_img)
        self.select_button = Button(image=start_button_img, highlightthickness=0, padx=20,
                                    borderwidth=0, command=self.reset)
        self.select_button.grid(column=1, row=4, pady=(30, 5), padx=(520, 0))

        self.sample_paragraph_text = self.speed_calc.display_sample_paragraph()

        self.running = False
        self.counter = 0
        self.cpm = 0
        with open("cpm_highscore.txt") as data:
            self.cpm_high_score = float(data.read())

        with open("wpm_highscore.txt") as data:
            self.wpm_high_score = float(data.read())

        self.wpm = 0
        self.cps = 0
        self.wps = 0
        self.highest_score = False

        self.display_sample_text()
        self.display_typed_word_text()
        # self.update_score_board()

        self.window.mainloop()

    def display_typed_word_text(self):
        self.speed_calc.display_type_words()
        # self.typed_text = Entry()

    def display_sample_text(self):
        typed_words = self.speed_calc.display_type_words()
        sample_paragraph_text = self.speed_calc.display_sample_paragraph()
        self.text_label.config(text=random.choice(sample_paragraph_text), wraplength=1100)

    def start(self, event):
        if not self.running:
            self.update_score_board()
            # For shift, alt and ctrl keys
            if not event.keycode in [16, 17, 18]:
                self.running = True
                thread = threading.Thread(target=self.time_thread)
                thread.start()
        if not self.text_label.cget("text").startswith(self.typed_text.get()):
            self.typed_text.config(fg="red")
        else:
            self.typed_text.config(fg="black")
        if self.typed_text.get() == self.text_label.cget("text")[:-1]:
            self.running = False
            # self.text4_label.config(text=f"WPM: {self.wpm_high_score:.2f} CPM: {self.cpm_high_score:.2f}")
            self.typed_text.config(fg="#71D86F")
            # self.text4_label.config(text="CPM \n{:.2f}".format(self.cpm))

    def time_thread(self):
        while self.running:
            highest_score = True
            time.sleep(0.1)
            self.counter += 0.1
            self.cps = len(self.typed_text.get())/self.counter
            self.cpm = self.cps * 60
            self.wps = len(self.typed_text.get().split(" "))/self.counter
            self.wpm = self.wps * 60

            self.text1_label.config(text="WPM \n{:.2f}".format(self.wpm))
            self.text2_label.config(text="CPM \n{:.2f}".format(self.cpm))
            self.text3_label.config(text="CPS \n{:.2f}".format(self.cps))

    def reset(self):
        self.running = False
        self.counter = 0
        self.text1_label.config(text="WPM \n0.00")
        self.text2_label.config(text="CPM \n0.00")
        self.text3_label.config(text="CPS \n0.00")

        sample_paragraph_text = self.speed_calc.display_sample_paragraph()
        self.text_label.config(text=random.choice(sample_paragraph_text))
        self.typed_text.delete(0, END)
        if self.cpm > self.cpm_high_score:
            self.cpm_high_score = self.cpm
        if self.wpm > self.wpm_high_score:
            self.wpm_high_score = self.wpm
            with open("wpm_highscore.txt", mode="w") as data:
                data.write(f"{self.wpm_high_score}")
            with open("cpm_highscore.txt", mode="w") as data:
                data.write(f"{self.cpm_high_score}")
        self.update_score_board()

    def update_score_board(self):
        self.text4_label.config(text=f"Highest Score\nWPM: {self.wpm_high_score:.2f} "
                                     f"CPM: {self.cpm_high_score:.2f}")







typing_sample.py

typing_sample_data = [
    {"text": "Nature is an important and integral part of mankind. "
             "It is one of the greatest blessings for human life; "
             "however, nowadays humans fail to recognize it as one. "
             "Nature has been an inspiration for numerous poets, writers, "
             "artists and more of yesteryears."},
    {"text": "They truly valued nature which reflects in their works even today. "
             "Essentially, nature is everything we are surrounded by like "
             "the water we drink, the air we breathe, the sun we soak in, "
             "the birds we hear chirping, the moon we gaze at and more."},
    {"text": "Nature has been in existence long before humans and ever since "
             "it has taken care of mankind and nourished it forever. In other "
             "words, it offers us a protective layer which guards us against "
             "all kinds of damages and harms."},
    {"text": "If nature has the ability to protect us, it is also powerful enough "
             "to destroy the entire mankind. Every form of nature, for instance, "
             "the plants, animals, rivers, mountains, moon, and more holds equal "
             "significance for us."}
]



other files include:

cpm_highscore.txt
wpm_highsocre.txt
requirements.txt