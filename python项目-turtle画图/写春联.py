import time
from tkinter import *

window = Tk()
window.title('新年快乐')
canvas = Canvas(window, width=500, height=460, bg='lightsalmon')
canvas.pack()

for i in range(0, 451):
    canvas.create_rectangle(10, 3, 76, i, outline='#FFA07A', fill='red')
    window.update()

str_1 = '早上不起晚上不睡'
str_3 = '一年到末啥也不会'
str_4 = '啊对对对'

str_5 = []
for i in range(len(str_4)):
    str_5.append(175 + 50 * i)

str_2 = []
for i in range(len(str_1)):
    str_2.append(70 + 50 * i)

for i in range(len(str_1)):
    canvas.create_text(40, str_2[i], text=str_1[i], fill='#FFD700', font=('楷体', 30, 'bold'))
    window.update()
    time.sleep(0.5)

for i in range(150, 350):
    canvas.create_rectangle(150, 3, i, 62, outline='#FFA07A', fill='red')
    window.update()

for i in range(len(str_4)):
    canvas.create_text(str_5[i], 33, text=str_4[i], fill='#FFD700', font=('楷体', 30, 'bold'))
    window.update()
    time.sleep(0.5)

for i in range(0, 451):
    canvas.create_rectangle(424, 3, 490, i, outline='#FFA07A', fill='red')
    window.update()

for i in range(len(str_3)):
    canvas.create_text(454, str_2[i], text=str_3[i], fill='#FFD700', font=('楷体', 30, 'bold'))
    window.update()
    time.sleep(0.5)

for i in range(167, 251):
    canvas.create_rectangle(167, 130, i, 441, outline='#FFA07A', fill='red')
    window.update()

for i in range(250, 334):
    canvas.create_rectangle(250, 130, i, 441, outline='#FFA07A', fill='red')
    window.update()

canvas.create_text(210, 280, fill='#FFD700', text='开', font=('楷体', 45, 'bold'))
canvas.create_text(290, 280, fill='#FFD700', text='摆', font=('楷体', 45, 'bold'))

mainloop()