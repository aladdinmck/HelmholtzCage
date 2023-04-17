from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from InputPipeline import fieldGenerator as fg
from InputPipeline import orbitPropagator as op

root = Tk()
root.title('Helmholtz Cage - User Interface')
root.geometry("1080x720")

day = 2
month = 2
year = 2023
test_length = 80 # test length in minutes
segments = 80    # how many segments to show on the graph


test = op.Orbit('ISS', test_length, segments)
test.generate()
test.display()
print(len(test.positions))

mag = fg.MagneticField(test.positions, day, month, year, test_length, segments)
mag.calculate()
mag.fix_datatype()
mag.display()
mag.plot_fields()


root.mainloop()

