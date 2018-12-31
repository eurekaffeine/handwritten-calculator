import tkinter as Tk
import tkinter.font
from functools import partial
import PIL
from PIL import Image, ImageDraw
from mnist_recognition import mnist_recognition
from operand_recognition import OperandRecogniton
from tkinter import messagebox

# Initialize the parameters of the canvas used for drawing
width = 200
height = 200
black = (0, 0, 0)

img = PIL.Image.new("RGB", (width, height), black)
# Define the background used to cover and clear the canvas
bg = PIL.Image.new("RGB", (width, height), black)
res = 0

def main():


    def get_input(entry, argu):
        entry.insert(Tk.END, argu)

    def backspace(entry):
        input_len = len(entry.get())
        entry.delete(input_len - 1)

    def clear(entry):
        entry.delete(0, Tk.END)

    # Function of calculation
    # def calc(entry):
    #     output = str(eval(entry.get().strip()))
    #     clear(entry)
    #     entry.insert(Tk.END, output)
    def calc(entry):
        input = entry.get()
        try:
            output = str(eval(input.strip()))
            clear(entry)
            entry.insert(Tk.END, output)
        except SyntaxError:
            messagebox.showinfo('Error','invalid equation!')
    # The paint() & the draw_clear() are the main function of drawing
    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        cv.create_oval(x1, y1, x2, y2, fill="black", width=8)
        draw.line([x1, y1, x2, y2], fill="red", width=7)

    def draw_clear(event):
        event.widget.delete('all')
        img.paste(bg, [0, 0])

    # Check the status of the model used. Default to be the digit recognition model
    def checkflag():
        check=flag.get()
        flag.set(not check)

    # Function of recognition
    def new_recognize(entry, img):
        value=flag.get()
        if value==True:
            res = OperandRecogniton().recognition(img)

        else:
            res = mnist_recognition().read_img(img)
        entry.insert(Tk.END, res)

    # Tkinter Layout
    top = Tk.Tk()
    top.title("Calculator")
    top.resizable(0, 0)
    flag = Tk.BooleanVar()
    flag.set(True)
    entry_font = tkinter.font.Font(size=12)
    entry = Tk.Entry(top, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=6, sticky=Tk.N+Tk.E+Tk.W+Tk.S, padx=5, pady=5)

    button_bg = '#D5E0EE'
    button_active_bg = '#E4E35A'

    Button = partial(Tk.Button, top, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)

    button_7 = Button(text='7', command=lambda: get_input(entry, '7'))
    button_7.grid(row=1, column=5, pady=5,sticky=Tk.E)

    button_8 = Button(text='8', command=lambda: get_input(entry, '8'))
    button_8.grid(row=1, column=6, pady=5)

    button_9 = Button(text='9', command=lambda: get_input(entry, '9'))
    button_9.grid(row=1, column=7, pady=5)

    button_plus = Button(text='+', command=lambda: get_input(entry, '+'))
    button_plus.grid(row=1, column=8, pady=5)

    button_4 = Button(text='4', command=lambda: get_input(entry, '4'))
    button_4.grid(row=2, column=5, pady=5,sticky=Tk.E)

    button_5 = Button(text='5', command=lambda: get_input(entry, '5'))
    button_5.grid(row=2, column=6, pady=5)

    button_6 = Button(text='6', command=lambda: get_input(entry, '6'))
    button_6.grid(row=2, column=7, pady=5)

    button_minus = Button(text='-', command=lambda: get_input(entry, '-'))
    button_minus.grid(row=2, column=8, pady=5)

    button_1 = Button(text='1', command=lambda: get_input(entry, '1'))
    button_1.grid(row=3, column=5, pady=5,sticky=Tk.E)

    button_2 = Button(text='2', command=lambda: get_input(entry, '2'))
    button_2.grid(row=3, column=6, pady=5)

    button_3 = Button(text='3', command=lambda: get_input(entry, '3'))
    button_3.grid(row=3, column=7, pady=5)

    button_multi = Button(text='*', command=lambda: get_input(entry, '*'))
    button_multi.grid(row=3, column=8, pady=5)

    button_0 = Button(text='0', command=lambda: get_input(entry, '0'))
    button_0.grid(row=4, column=6,columnspan=2, padx=3, pady=5,sticky=Tk.S+Tk.W+Tk.E+Tk.N)

    button_dot = Button(text='.', command=lambda: get_input(entry, '.'))
    button_dot.grid(row=4, column=5, pady=5,padx=3,sticky=Tk.E)

    button_div = Tk.Button(top, text='/', bg=button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button_div.grid(row=4, column=8, pady=5)

    button_del = Tk.Button(top, text='del', bg=button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button_del.grid(row=5, column=5, pady=5,padx=2,sticky=Tk.E)

    button_equal = Tk.Button(top, text='=', bg=button_bg, padx=10, pady=3,
                         command=lambda: calc(entry), activebackground=button_active_bg)
    button_equal.grid(row=5, column=7, columnspan=2, padx=3, pady=5, sticky=Tk.N + Tk.S + Tk.E + Tk.W)

    button_clear = Tk.Button(top, text='C', bg=button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button_clear.grid(row=5, column=6, pady=5)


    cv = Tk.Canvas(top, width=width, height=height, bg="#FAEBD7")
    cv.grid(row=1,column=0,columnspan=5, rowspan=5)

    # Track the motion of the digital mouse
    cv.bind("<B1-Motion>", paint)

    # Interactively doube click the canvas to clear it.
    cv.bind("<Double-1>", draw_clear)

    draw = ImageDraw.Draw(img)
    button = Tk.Button(text="recognize", command=lambda:new_recognize(entry, img))
    button.grid(row=6,column=0)
    C1 = Tk.Checkbutton(top, variable=flag, onvalue=1, offvalue=0, text='operand', command=checkflag())
    C1.grid(row=6,column=5,sticky=Tk.E)
    top.mainloop()

if __name__ == '__main__':
    main()