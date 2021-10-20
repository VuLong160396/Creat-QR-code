from tkinter import *
import qrcode
from tkinter import messagebox
import time


window = Tk()
window.title('QR-Code')
window.geometry('300x200')
window.config(background='teal')
window.resizable(False, False)
label1 = Label(window, text = 'Input Data', font='Arial 15').place(x=0, y=25)
data = Entry(window, border='35', justify=CENTER)
data.place(x=96, y=0)
button1 = Button(window, text='Create QR', border='10', font= 'Arial 15', bg='green', command=lambda: creat_QR())
button1.pack(side = BOTTOM)

if data.get()== '':
    button1.config(bg='red')
else:
    button1.config(bg='white')
def creat_QR():
    name = data.get()
    if len(name) > 0:
        data.config(state='disable')
        a = qrcode.make(name)
        a.save(f'{len(name)}.png')
        data.config(state='normal')
        button1.config(bg='yellow')
        time.sleep(1)
        button1.config(bg='green')
        notice = messagebox.showinfo(title='Notice', message='Completed')
        data.delete(0, END)
    else:
        warning = messagebox.showwarning(title='Warning', message='Empty Data!')
if data.get()== '':
    button1.config(bg='red')
else:
    button1.config(bg='white')

window.mainloop()