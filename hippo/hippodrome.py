from tkinter import *
from PIL import Image, ImageTk

root = Tk()

width = 1024
height = 600

pos_x = root.winfo_screenwidth() // 2 - width // 2  # координаты для размещения окна х, у
pos_y = root.winfo_screenheight() // 2 - height // 2

# устанавливаем ширину, высоту, позицию
# root.geometry(f'{width} x {height} + {pos_x} + {pos_y}')  # відступи - не правильно!
root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')  # выбор позиции окна - строго по центру
root.title('Hippodrome')  # название окна
root.resizable(False, False)  # запрещаем изменение размеров окна

# button01 = Button()
# button01['text'] = 'Вот и вся программа)'
#
# x_btn = width // 2 - button01.winfo_reqwidth() // 2  # ширина и высота кнопки в зависимости от содержимого кнопки, размера шрифта
# y_btn = height // 2 - button01.winfo_reqheight() // 2
# button01.place(x = x_btn, y = y_btn)  # позиция кнопки
#
# button01['command'] = quit

# road_image = PhotoImage(file='road.png')
# road = Label(root, image=road_image)
# road.place(x=0, y=17)

road_image = Image.open("road.png")
road_image = ImageTk.PhotoImage(road_image)
road = Label(image=road_image)
road.image = road_image
road.place(x=0, y=17)


root.mainloop()  # вызов окна