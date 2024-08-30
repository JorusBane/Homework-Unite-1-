class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = "i train, sleep and repeat"
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy
class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
    def move(self, dx, dy):
        super().fly(dy)
        super().run(dx)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)

class Hippo(Eagle, Horse):
    def __init__(self):
        super().__init__()
    def move(self, dx, dy):
        super().fly(dy)
        super().run(dx)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)






print(Pegasus.mro())
print(Eagle.mro())
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

h1 = Hippo()
print(Hippo.mro())
print(h1.get_pos())
h1.move(8, 90)
print(h1.get_pos())
h1.move(-7, 70)
print(h1.get_pos())

h1.voice()
