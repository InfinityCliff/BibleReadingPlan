#!/usr/bin/kivy
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.lang import Builder

kivy.require('1.7.2')

Builder.load_string("""
                        
<StartScreen>:
    id: Start_Screen
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                id: LeftButton
                text: 'Menu'
                size_hint_y: 0.05
                pos_hint: {'top': 1} 
                on_release: root.manager.current = 'menu'
            Label:
                text: 'Bible Reading Plan'
                size_hint_y: 0.05
                pos_hint: {'top': 1}
            Button:
                text: 'new'
                size_hint_y: 0.05
                pos_hint: {'top': 1}
                on_release: root.manager.current = 'newplan'
                
<NewPlanScreen>:
    id: NewPlan_Screen
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                id: LeftButton
                text: '<'
                size_hint_y: 0.05
                pos_hint: {'top': 1} 
                on_release: root.manager.current = 'start'
            Label:
                text: 'New Plan'
                size_hint_y: 0.05
                pos_hint: {'top': 1}
            Button:
                text: 'quit'
                size_hint_y: 0.05
                pos_hint: {'top': 1}

[MButton@Button]
    size_hint_y: 0.05
    
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: 0.05               
            Button:
                id: LeftButton
                text: '<'
                size_hint_y: 0.05
                pos_hint: {'top': 1} 
                on_release: root.manager.current = 'start'
            Label:
                text: 'Menu'
                size_hint_y: 0.05
                pos_hint: {'top': 1} 
        Button:
            text: 'Settings'
            size_hint_y: 0.05
            pos_hint: {'top': 1}
            on_release: root.manager.current = 'settings'
        Button:
            text: 'About'
            size_hint_y: 0.05
        Button:
            text: 'Help'     
            size_hint_y: 0.05
        Button:
            text: 'Feedback'
            size_hint_y: 0.05
            
<SettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                id: LeftButton
                text: '<'
                size_hint_y: 0.05
                pos_hint: {'top': 1} 
                on_release: root.manager.current = 'menu'
            Label:
                text: 'Settings'
                size_hint_y: 0.05
                pos_hint: {'top': 1}

""")


class MenuMain(BoxLayout):
    pass


class NewPlanMenu(BoxLayout):
    pass


class StartScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class NewPlanScreen(Screen):
    pass


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

    def center_widget(self, widget):
        pass

class DesktopLayout(Desktop):

    def __init__(self, *args, **kwargs):
        super(DesktopLayout, self).__init__(*args, **kwargs)
        reading_plans = ['Alpha-Omega', 'Chronological', 'Gospels', 'Chrono-Gospel', 'Old Testament',
                         'New Testament', 'Big Five', 'Wisdom']
        self.ids.PlanName.values = reading_plans

        plan_durations = ['30 Days', '60 Days', '90 Days', '6 Months', '1 Year', '2 Years', '3 Years']
        self.ids.PlanDuration.values = plan_durations


class CButton(Button):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(NewPlanScreen(name='newplan'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(MenuScreen(name='menu'))

class DesktopGUIApp(App):
    title = 'Bible Reading Plan'

    button_height = NumericProperty(30)
    button_width = NumericProperty(30)
    # label_height = NumericProperty(30)
    __view = None
    __controller = None

    def build(self):
        #self.__view = DesktopLayout()
        #self.__view.set_controller(self.__controller)
        return sm

    def set_controller(self, controller):
        self.__controller = controller

if __name__ == '__main__':
    DesktopGUIApp().run()
