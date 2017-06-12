#!/usr/bin/kivy
import kivy
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty, ObjectProperty
from BibleOutline import Bible_Outline
import operator
from Events import EventHook
import re

kivy.require('1.7.2')


def create_dropdown(title, items, height=30):

    dropdown = DropDown()

    for item in items:
        # when adding widgets, we need to specify the height manually (disabling
        # the size_hint_y) so the dropdown can calculate the area it needs.
        btn = DDButton(text=item, size_hint_y=None, height=height)
        # for each button, attach a callback that will call the select() method
        # on the dropdown. We'll pass the text of the button as the data of the
        # selection.
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        # then add the button inside the dropdown
        dropdown.add_widget(btn)
    # create a big main button
    mainbutton = Button(text=title, size_hint=(1, 1))
    # show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instance) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton.bind(on_release=dropdown.open)
    # one last thing, listen for the selection in the dropdown list and
    # assign the data to the button text.
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

    return mainbutton, dropdown

class PlanName(DropDown):
    pass

class CButton(Button):
    pass


class DDButton(Button):
    pass


class Desktop(Screen):
    # dd_btn = ObjectProperty(None)
    # psalms_switch = ObjectProperty(None)
    # proverbs_switch = ObjectProperty(None)
    # wisdom_switch = ObjectProperty(None)
    rpu = ObjectProperty(None)
    pd = ObjectProperty(None)
    dd = ObjectProperty(None)
    dd2 = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Desktop, self).__init__(*args, **kwargs)
        self._controller = None
        self.onChange = EventHook()
        self.onSwitchPsalm = EventHook()

    def on_rpu(self, *args):
        print('rpu: ', self.rpu.text)

    def on_dd(self, *args):
        print('dd', self.dd)

    def set_controller(self, controller):
        self._controller = controller

    def psalm_callback(self, value):
        self._controller.update_model(psalms=value)

    def proverb_callback(self, value):
        self._controller.update_model(proverbs=value)

    def wisdom_callback(self, value):
        self._controller.update_model(wisdom=value)

    def switch_values(self):
        return self.psalms_switch.active, \
               self.proverbs_switch.active, \
               self.wisdom_switch.active

    def reading_plan_update(self):
        print('reading_plan_update')

class TestLayout(Desktop):
    pass


class DesktopLayoutCondensed(Desktop):

    def __init__(self, *args, **kwargs):
        super(DesktopLayoutCondensed, self).__init__(*args, **kwargs)
        reading_plans = ['Alpha-Omega', 'Chronological', 'Gospels', 'Chrono-Gospel', 'Old Testament',
                         'New Testament', 'Big Five', 'Wisdom']
        self.rpu, self.dd = create_dropdown('Select Plan', reading_plans)
        self.ids.PlanOptions.add_widget(self.rpu)

        plan_durations = ['30 days', '60 days', '90 days', '6 months', '1 year', '2 years', '3 years']
        self.pd, self.dd2 = create_dropdown('Select Duration', plan_durations)
        self.ids.PlanOptions.add_widget(self.pd)


class DesktopLayout(Desktop):
    old_testament = ObjectProperty(None)
    new_testament = ObjectProperty(None)
    plan_options = ObjectProperty(None)


    def __init__(self, *args, **kwargs):
        super(DesktopLayout, self).__init__(*args, **kwargs)
        reading_plans = ['Alpha-Omega', 'Chronological', 'Gospels', 'Chrono-Gospel', 'Old Testament',
                         'New Testament', 'Big Five', 'Wisdom']
        self.plan_options.add_widget(create_dropdown('Select Plan', reading_plans))
        plan_durations = ['30 days', '60 days', '90 days', '6 months', '1 year', '2 years', '3 years']
        self.plan_options.add_widget(create_dropdown('Select Duration', plan_durations))
        bo = Bible_Outline()
        ot_books = bo.sorted_book_abbr('OT')
        for abbr, _ in ot_books:
            self.old_testament.add_widget(CButton(text=abbr))
        nt_books = bo.sorted_book_abbr('NT')
        for abbr, _ in nt_books:
            self.new_testament.add_widget(CButton(text=abbr))


class DesktopGUIApp(App):
    title = 'Bible Reading Plan'

    button_height = NumericProperty(30)
    button_width = NumericProperty(30)
    # label_height = NumericProperty(30)
    __view = None
    __controller = None

    def build(self):
        self.__view = DesktopLayoutCondensed()
        self.__view.set_controller(self.__controller)
        return self.__view

    def set_controller(self, controller):
        self.__controller = controller

if __name__ == '__main__':
    DesktopGUIApp().run()
