from time import sleep
from random import choice


class TrafficLights:
    __colours = ('green', 'yellow', 'red', 'fecal')

    def running(self):
        # while True: # без остановки
        i = 0
        while i < 3:
            i += 1
            colour = choice(self.__colours)
            if colour != 'fecal':
                if colour == 'green':
                    print('GO!')
                    sleep(10)
                    print('WAIT!')
                    sleep(2)
                    print('STOP!')
                    sleep(7)
                    print('WAIT!')
                    sleep(2)
                elif colour == 'yellow':
                    print('WAIT!')
                    sleep(2)
                    print('STOP!')
                    sleep(7)
                    print('WAIT!')
                    sleep(2)
                    print('GO!')
                    sleep(10)
                    print('WAIT!')
                    sleep(2)
                else:
                    print('STOP!')
                    sleep(7)
                    print('WAIT!')
                    sleep(2)
                    print('GO!')
                    sleep(10)
                    print('WAIT!')
                    sleep(2)
            else:
                print('@#$%!!!The electricity has run out!')
                break


tl = TrafficLights()
tl.running()
