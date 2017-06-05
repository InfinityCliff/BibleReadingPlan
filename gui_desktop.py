#!/usr/bin/kivy
import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ReferenceListProperty, ObjectProperty


class CButton(Button):
    pass


class DDButton(Button):
    pass


class DesktopLayout(Screen):
    dd_btn = ObjectProperty(None)
    plan_options = ObjectProperty(None)
    old_testament = ObjectProperty(None)
    new_testament = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(DesktopLayout, self).__init__(*args, **kwargs)

        reading_plans = ['Alpha-Omega', 'Chronological', 'Gospels', 'Chrono-Gospel', 'Old Testament',
                         'New Testament', 'Big Five', 'Wisdom']
        self.plan_options.add_widget(self.create_dropdown('Select Plan', reading_plans))
        plan_durations = ['30 days', '60 days', '90 days', '6 months', '1 year', '2 years', '3 years']
        self.plan_options.add_widget(self.create_dropdown('Select Duration', plan_durations))

        for i in range(1, 39):
            self.old_testament.add_widget(CButton(text=str(i)))
        for i in range(1, 29):
            self.new_testament.add_widget(CButton(text=str(i)))

    def create_dropdown(self, title, items, height=30):
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

        return mainbutton


class DesktopGUIApp(App):
    title = 'Bible Reading Plan'

    button_height = NumericProperty(30)
    button_width = NumericProperty(30)
    label_height = NumericProperty(30)

    def build(self):

        return DesktopLayout()

if __name__ == '__main__':
    DesktopGUIApp().run()