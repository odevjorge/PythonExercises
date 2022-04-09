import math
import numpy as np
from graphics import *

janela = GraphWin(width=600, height=600)
janela.setBackground("black")
janela.setCoords(-3, -3, 3, 3)

for cx in np.arange(-2.0, 2.0, 0.001):
    for cy in np.arange(-2.0, 2.0, 0.001):
        print(cx, cy)
        zx = 0.0
        zy = 0.0

        for i in range(0, 256):
            zzx = zx*zx - zy*zy + cx
            zzy = 2.0*zx*zy + cy

            zx = zzx
            zy = zzy

            if(math.sqrt(zx*zx + zy*zy) >= 2):
                break
            elif(i == 255):
                janela.plot(cx, cy, "cyan")

janela.getMouse()