from BibleReadingPlan import ReadingPlan
from gui_desktop import DesktopGUIApp


class Controller(object):

    def __init__(self):
        self.__dataset = None
        self.__view = None

    def setDataSet(self, dataset):
        self.__dataset = dataset

    def set_view(self, view):
        self.__view = view

    def update_model(self, **kwargs):
        self.__dataset.update(**kwargs)


    def bulid_plan(self):
        self.__dataset.create_plan()


if __name__ == '__main__':
    reading_plan = ReadingPlan()
    controller = Controller()
    controller.setDataSet(reading_plan)

    view = DesktopGUIApp()
    view.set_controller(controller)

    controller.set_view(view)

    view.run()
