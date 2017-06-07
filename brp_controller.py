from BibleReadingPlan import ReadingPlan
from gui_desktop import DesktopGUIApp


class Controller(object):

    def __init__(self):
        self.__dataset = None
        self.__view = None

    def setDataSet(self, dataset):
        if self.__dataset is not None:
            # unregister the handler
            # on the previous dataset
            self.__dataset.modified -= self.onModified

        self.__dataset = dataset

    def set_view(self, view):
        if self.__view is not None:
            self.__view.onSwitchPsalm -= self.onSwitchPsalm
        self.__view = view
        self.__view.onSwitchPsalm += self.onSwitchPsalm

    def onSwitchPsalm(self):
        psalms, proverbs, wisdom = self.__view.switch_values()
        self.__dataset.update(psalms=psalms, proverbs=proverbs, wisdom=wisdom)

    def bulid_plan(self):
        self.__dataset.create_plan()


if __name__ == '__main__':
    reading_plan = ReadingPlan()
    controller = Controller()
    controller.setDataSet(reading_plan)
    view = DesktopGUIApp()
    controller.set_view(view)

    view.run()