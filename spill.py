class Figur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tegn():
        pass

class Spiller(Figur):
    def __init__(self, fartY):
        super().__init__(self.x, self.y)
        self.fartY = fartY
    
    def hopp():
        pass

    def fall():
        pass

    def er_over_hinder():
        pass


class Hinder(Figur):
    def __init__(self, x, y, fartX):
        super().__init__(x, y)
        self.fartX = fartX