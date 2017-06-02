#!/usr/bin/kivy
import kivy
kivy.require('1.7.2')

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty, ObjectProperty


class CButton(Button):
    pass

class DURButton(Button):
    pass

class TYPEButton(Button):
    pass

class DesktopGUIApp(App):
    title = 'Bible Reading Plan'

    button_height = NumericProperty(30)
    button_width = NumericProperty(30)
    label_height = NumericProperty(30)
    dd_height = NumericProperty(30)

    def build(self):
        root = DesktopLayout()
        for i in range(1, 40):
            root.old_testament.add_widget(CButton(text=str(i)))
        for i in range(1, 28):
            root.new_testament.add_widget(CButton(text=str(i)))
        for i in range(1,8):
            root.plan_len_dropdown.add_widget(DURButton(text=str(i)))
        for i in range(1,5):
            root.plan_dur_dropdown.add_widget(TYPEButton(text=str(i)))
        return root


class PlanNameDropDown(DropDown):
    pass


class DesktopLayout(BoxLayout):
    pass


class DesktopLayout2(BoxLayout):
    pass

if __name__ == '__main__':
    DesktopGUIApp().run()