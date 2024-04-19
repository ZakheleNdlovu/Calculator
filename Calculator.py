import tkinter

win = tkinter.Tk()
win.title('Calculator')
win.geometry('265x368')
win.resizable(False,False)

x= tkinter.StringVar()

def show_num(value):
    val = display.get() + str(value)
    x.set(val)

def solve():
    results =eval(display.get())
    x.set(results)

def clear():
    c= ''
    x.set(c)

display = tkinter.Entry(win, textvariable=x, font=('Ink Free', 17),bg='sky blue')
display.grid(row=0,column=0,columnspan=4)

button = tkinter.Button(win, text='(', width=8, height=2, command=lambda:show_num('('), bg='orange')
button.grid(row=1,column=0)
button = tkinter.Button(win, text=')', width=8, height=2, command=lambda:show_num(')'), bg='orange')
button.grid(row=1,column=1)
button = tkinter.Button(win, text='%', width=8, height=2, command=lambda:show_num('%'), bg='orange')
button.grid(row=1,column=2)
button = tkinter.Button(win, text='C', width=8, height=2, command=lambda:clear(), bg='orange')
button.grid(row=1,column=3)
button = tkinter.Button(win, text='7', width=8, height=4, command=lambda:show_num(7))
button.grid(row=2,column=0)
button = tkinter.Button(win, text='8', width=8, height=4, command=lambda:show_num(8))
button.grid(row=2,column=1)
button = tkinter.Button(win, text='9', width=8, height=4, command=lambda:show_num(9))
button.grid(row=2,column=2)
button = tkinter.Button(win, text='*', width=8, height=4, command=lambda:show_num('*'))
button.grid(row=2,column=3)
button = tkinter.Button(win, text='4', width=8, height=4, command=lambda:show_num(4))
button.grid(row=3,column=0)
button = tkinter.Button(win, text='5', width=8, height=4, command=lambda:show_num(5))
button.grid(row=3,column=1)
button = tkinter.Button(win, text='6', width=8, height=4, command=lambda:show_num(6))
button.grid(row=3,column=2)
button = tkinter.Button(win, text='/', width=8, height=4, command=lambda:show_num('/'))
button.grid(row=3,column=3)
button = tkinter.Button(win, text='1', width=8, height=4, command=lambda:show_num(1))
button.grid(row=4,column=0)
button = tkinter.Button(win, text='2', width=8, height=4, command=lambda:show_num(2))
button.grid(row=4,column=1)
button = tkinter.Button(win, text='3', width=8, height=4, command=lambda:show_num(3))
button.grid(row=4,column=2)
button = tkinter.Button(win, text='-', width=8, height=4, command=lambda:show_num('-'))
button.grid(row=4,column=3)
button = tkinter.Button(win, text='+', width=8, height=4, command=lambda:show_num('+'))
button.grid(row=5,column=0)
button = tkinter.Button(win, text='0', width=8, height=4, command=lambda:show_num(0))
button.grid(row=5,column=1)
button = tkinter.Button(win, text='.', width=8, height=4, command=lambda:show_num('.'))
button.grid(row=5,column=2)
button = tkinter.Button(win, text='=', width=8, height=4, command=lambda:solve())
button.grid(row=5,column=3)


win.mainloop()