#!/usr/bin/kivy
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty


kivy.require('1.7.2')


class Desktop(Screen):

    def __init__(self, *args, **kwargs):
        super(Desktop, self).__init__(*args, **kwargs)
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    def psalm_callback(self, value):
        self._controller.update_model(psalms=value)

    def proverb_callback(self, value):
        self._controller.update_model(proverbs=value)

    def wisdom_callback(self, value):
        if value:
            self.ids.PsalmsSwitch.active = False
            self.ids.PsalmsSwitch.disabled = True
            self.ProverbsSwitch.active = False
            self.ProverbsSwitch.disabled = True
        else:
            self.ids.PsalmsSwitch.disabled = False
            self.ProverbsSwitch.disabled = False
        self._controller.update_model(wisdom=value)

    def select_plan_name(self, name):
        self.ids.PlanName.selected = True
        self._controller.update_model(plan_id=name)
        self.enable_create()

    def select_plan_duration(self, duration):
        self.ids.PlanDuration.selected = True
        self._controller.update_model(day_count=duration)
        self.enable_create()

    def select_week_day(self, day):
        self.ids.WeekDay.selected = True
        self._controller.update_model(weekday=day)
        self.enable_create()

    def enable_create(self):
        self.ids.CreateButton.disabled = not (self.ids.PlanDuration.selected and
                                              self.ids.PlanName.selected and
                                              self.ids.WeekDay.selected)

    def create_plan(self):
        self._controller.create_plan()


class DesktopLayout(Desktop):

    def __init__(self, *args, **kwargs):
        super(DesktopLayout, self).__init__(*args, **kwargs)
        reading_plans = ['Alpha-Omega', 'Chronological', 'Gospels', 'Chrono-Gospel', 'Old Testament',
                         'New Testament', 'Big Five', 'Wisdom']
        self.ids.PlanName.values = reading_plans

        plan_durations = ['30 Days', '60 Days', '90 Days', '6 Months', '1 Year', '2 Years', '3 Years']
        self.ids.PlanDuration.values = plan_durations


class DesktopGUIApp(App):
    title = 'Bible Reading Plan'

    button_height = NumericProperty(30)
    button_width = NumericProperty(30)
    # label_height = NumericProperty(30)
    __view = None
    __controller = None

    def build(self):
        self.__view = DesktopLayout()
        self.__view.set_controller(self.__controller)
        return self.__view

    def set_controller(self, controller):
        self.__controller = controller

if __name__ == '__main__':
    DesktopGUIApp().run()
