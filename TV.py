# Class TV

class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Некий список каналов по умолчанию
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = 5

    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex > self.nChannels:
            self.channelIndex -= 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print(' TV is: On')
            print(' Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print(' Volume is:', self.volume, '(sound is muted)')
            else:
                print(' Volume is:', self.volume)

        else:
            print(' TV is: Off')

oTV = TV()

oTV.power()
oTV.showInfo()

oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

oTV.volumeDown()
oTV.mute()
oTV.showInfo()

oTV.setChannel(11)
oTV.mute()
oTV.showInfo()