class Drawer():

    def __init__(self):
        pass

    def draw(self):
        pass

    @property
    def system(self):
        print("accessing through prop")
        return self.__system

    @system.setter
    def system(self, system):
        print("setting trough prop")
        self.__system = system

