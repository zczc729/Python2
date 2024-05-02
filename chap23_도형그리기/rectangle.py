from figure import Figure

class Rectangle(Figure):

    def draw(self):
        for i in range(self.height):
            print(self.ch * self.height)