import pyfirmata

comport = 'COM3'

board = pyfirmata.Arduino(comport)

Led1 = board.get_pin('d:8:o')
Led2 = board.get_pin('d:9:o')
Led3 = board.get_pin('d:10:o')
Led4 = board.get_pin('d:11:o')
Led5 = board.get_pin('d:12:o')

def led (fingerUp):
    if fingerUp == [0, 0, 0, 0, 0]:
        Led1.write(0)
        Led2.write(0)
        Led3.write(0)
        Led4.write(0)
        Led5.write(0)

    elif fingerUp == [0, 1, 0, 0, 0]:
        Led1.write(1)
        Led2.write(0)
        Led3.write(0)
        Led4.write(0)
        Led5.write(0)

    elif fingerUp == [0, 1, 1, 0, 0]:
        Led1.write(1)
        Led2.write(1)
        Led3.write(0)
        Led4.write(0)
        Led5.write(0)

    elif fingerUp == [0, 1, 1, 1, 0]:
        Led1.write(1)
        Led2.write(1)
        Led3.write(1)
        Led4.write(0)
        Led5.write(0)

    elif fingerUp == [0, 1, 1, 1, 1]:
        Led1.write(1)
        Led2.write(1)
        Led3.write(1)
        Led4.write(1)
        Led5.write(0)

    elif fingerUp == [1, 1, 1, 1, 1]:
        Led1.write(1)
        Led2.write(1)
        Led3.write(1)
        Led4.write(1)
        Led5.write(1)
