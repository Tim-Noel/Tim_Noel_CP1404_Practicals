"""
CP1404 prac
Kivy program which creates more buttons using a list of strings
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class Button_Maker:
    def __init__(self):
        self.word_list = ("Herbert", "William", "Susan")
