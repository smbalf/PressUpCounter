import pyxel


class App:
    def __init__(self):
        pyxel.init(50, 50, caption="Tally Counter")

        self.count = 0
        self.font = 0
        self.cls = 7

        self.cd_active = False
        self.timer_count = 0

        pyxel.sound(0).set("c2c2", "t", "6", "VFFN", 25)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.countdown()

    def draw(self):
        pyxel.cls(self.cls)
        pyxel.text(6, 1, "STAY HARD!", self.font)
        pyxel.text(22, 22, str(self.count), self.font)
        if self.cd_active:
            pyxel.text(22, 30, str(self.timer_count), self.font)
        pyxel.text(5, 44, "r to reset", self.font)
        pyxel.text(pyxel.mouse_x, pyxel.mouse_y, ".", 4)

        self.tally()
        self.colours()

    def tally(self):
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.count += 1
            self.cd_active = True

        elif pyxel.btnr(pyxel.KEY_R):
            self.count = 0

    def colours(self):
        if self.count < 10:
            self.font = 0
            self.cls = 7
        elif 10 <= self.count < 20:
            self.font = 7
            self.cls = 5
        elif 20 <= self.count < 30:
            self.font = 1
            self.cls = 10
        elif 30 <= self.count < 40:
            self.font = 0
            self.cls = 15
        elif self.count == 40:
            self.font = 10
            self.cls = 0

    def countdown(self):
        if self.cd_active:
            if pyxel.frame_count % 32 == 0:
                self.timer_count += 1
                print(self.timer_count)
                if self.timer_count == 30:
                    pyxel.play(0, 0, loop=False)
                    self.timer_count = 0
                    self.cd_active = False


App()
