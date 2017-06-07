# https://stackoverflow.com/questions/1092531/event-system-in-python
# http://www.voidspace.org.uk/python/weblog/arch_d7_2007_02_03.shtml#e616
from kivy.uix.screenmanager import Screen


class EventHook(object):
    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)


class MainForm(Screen):

    def __init__(self):
        self._controller = Controller()
        self.observers = [self._controller]

    def loadDataset(self):
        dataset = self.magicallyGetNewDataset()

        for observer in self.observers:
            observer.dataset = dataset


class Controller(object):

    def __init__(self):
        self.__dataset = None

    def setDataSet(self, dataset):
        if self.__dataset is not None:
            # unregister the handler
            # on the previous dataset
            self.__dataset.modified -= self.onModified

        self.__dataset = dataset

        # register the handler
        # on the new dataset
        self.__dataset.modified += self.onModified

    dataset = property(lambda self: self.__dataset, setDataSet)

    def onModified(self):
        # do something in response
        # to changes in the dataset
        pass


class DataSet(object):
    def __init__(self):
        self.modified = EventHook()

    def doSomething(self):
        # code which does something
        if somethingHasChanged:
            self.modified.fire()
