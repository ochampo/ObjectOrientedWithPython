from abc import abstractclassmethod, abstractmethod


Class JSONify(abc):
    @abstractmethod
    def toJson(self):
        pass


class GraphicsShape(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        return 3.14 * (self.radius **2)
    def toJson(self):
        return f"{{\" CIRCLE\" : {str(self.calcArea())} }}"



c = Circle(10)
print(c.CalcArea())
print(c.toJson())
