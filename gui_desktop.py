#!/usr/bin/kivy
import kivy
kivy.require('1.7.2')

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty, ObjectProperty


class cButton(Button):
    pass

class DesktopGUIApp(App):
    title = 'Bible Reading Plan'

    def build(self):
        root = DesktopLayout()
        for i in range(39):
            root.add_widget(cButton(text=str(i)))
        return root


class DesktopLayout(GridLayout):
    pass

if __name__ == '__main__':
    DesktopGUIApp().run()