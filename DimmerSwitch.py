# Class DimmerSwitch

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLever(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

oDimmer = DimmerSwitch()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

oDimmer.lowerLever()
oDimmer.lowerLever()
oDimmer.turnOff()
oDimmer.show()

oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

