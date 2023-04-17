import digitalio
import board

class Pins():
    def __init__(self):
        
        #H-bridge Flags need to be input pins
        self.FF1_X = digitalio.DigitalInOut(board.D20) #GPIO 20
        self.FF1_X.direction = digitalio.Direction.INPUT
        
        self.FF2_X = digitalio.DigitalInOut(board.D21)    #GPI0 21
        self.FF2_X.direction = digitalio.Direction.INPUT
        
        self.FF1_Y = digitalio.DigitalInOut(board.D22)    #GPIO 22
        self.FF1_Y.direction = digitalio.Direction.INPUT
        
        self.FF2_Y = digitalio.DigitalInOut(board.D27)    #GPIO 27
        self.FF2_Y.direction = digitalio.Direction.INPUT
        
        self.FF1_Z = digitalio.DigitalInOut(board.D19)    #GPIO19
        self.FF1_Z.direction = digitalio.Direction.INPUT
        
        self.FF2_Z = digitalio.DigitalInOut(board.D18)    #GPIO18
        self.FF2_Z.direction = digitalio.Direction.INPUT
        
        #Ouputs to set the direction of the field
        self.DIR_X = digitalio.DigitalInOut(board.D25)    #GPIO 25
        self.DIR_X.direction = digitalio.Direction.OUTPUT
        
        self.DIR_Y = digitalio.DigitalInOut(board.D24)    #GPIO 24
        self.DIR_Y.direction = digitalio.Direction.OUTPUT
        
        self.DIR_Z = digitalio.DigitalInOut(board.D16)    #GPIO 16
        self.DIR_Z.direction = digitalio.Direction.OUTPUT
        
        
        #Analog signals from the current monitors, won't need bc adc
        #self.Current_Out_X = 29
        #self.Current_Out_Y = 26
        #self.Current_Out_Z = 24
        
        #reset the H-bridge to clear if error flags are thrown, outputs
        self.resetX = digitalio.DigitalInOut(board.D5)    #GPIO 5
        self.resetX.direction = digitalio.Direction.OUTPUT
        self.resetX.value = True
        
        self.resetY = digitalio.DigitalInOut(board.D23)   #GPIO 23
        self.resetY.direction = digitalio.Direction.OUTPUT
        self.resetY.value = True
        
        self.resetZ = digitalio.DigitalInOut(board.D17)   #GPIO 17
        self.resetZ.direction = digitalio.Direction.OUTPUT
        self.resetZ.value = True

    def set_directions(self, x, y, z):
        if x == 1:
            self.DIR_X.value = True
        else:
            self.DIR_X.value = False

        if y == 1:
             self.DIR_Y.value = True
        else:
            self.DIR_Y.value = False

        if z == 1:
            self.DIR_Z.value = True
        else:
            self.DIR_Z.value = False
            


            


        
        