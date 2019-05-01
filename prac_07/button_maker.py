"""
CP1404 prac
Kivy program which creates more buttons using a list of strings
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class Button_Maker(App):
    def __init__(self):
        self.word_list = ("Herbert", "William", "Susan")

    def build(self):
        self.title = "Button Maker"
        self.root = Builder.load_file("button_maker.kv")
        self.button_creater()
        return self.root

    def button_creator(self):
        for word in self.word_list:
            new_button = Button(text=word, id=word)
            new_button.bind()

Button_Maker().run()