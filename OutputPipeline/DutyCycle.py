class DutyCycle:

    def __init__(self, Bx, By, Bz):
        self.xDutyCycle = []
        self.yDutyCycle = []
        self.zDutyCycle = []
        self.dir_x = []
        self.dir_y = []
        self.dir_z = []
        self.Bx = Bx
        self.By = By
        self.Bz = Bz

    def calculate(self):
        # sets direction of current flow according to current value
        for i in range(len(self.Bx)):
            if self.Bx[i] < 0:
                self.dir_x.append(0)
            else:
                self.dir_x.append(1)
        # converts current into a dutyCycle
        self.xDutyCycle = [int(abs(ele)-2.48e-7/2.8e-9) for ele in self.Bx]
        print('xDutyCyle: ' + str(self.xDutyCycle))
        #self.xDutyCycle = int(Ix_abs)  # 7.5A/65535 = .000144 mA

        for j in range(len(self.By)):
            if self.By[j] < 0:
                self.dir_y.append(0)
            else:
                self.dir_y.append(1)

        self.yDutyCycle = [int(abs(ele)-1.38e-7/2.55e-9) for ele in self.By]
        #self.yDutyCycle = int(Iy_abs)  # 7.5A/65535 = .000144 mA
        print('yDutyCycle: ' + str(self.yDutyCycle))

        for k in range(len(self.Bz)):
            if self.Bz[k] < 0:
                self.dir_z.append(0)
            else:
                self.dir_z.append(1)

        self.zDutyCycle = [int(abs(ele)-5.79e-7/2.71e-9) for ele in self.Bz]
        print('zDutyCycle: ' + str(self.zDutyCycle))



    def single_calc(self):

        if self.Bx < 0:
            self.dir_x.append(0)
        else:
            self.dir_x.append(1)

        self.xDutyCycle = int((abs(self.Bx)-2.48e-7)/2.8e-9)
        #self.zDutyCycle = int(Iz_abs)  # 7.5A/65535 = .000144 mA
        if self.By < 0:
            self.dir_y.append(0)
        else:
            self.dir_y.append(1)
        self.yDutyCycle = int((abs(self.By)-1.38e-7)/2.55e-9)
        #self.yDutyCycle = 0.000144

        if self.Bz < 0:
            self.dir_z.append(0)
        else:
            self.dir_z.append(1)

        self.zDutyCycle = int((abs(self.Bz)-5.79e-7)/2.71e-9)

