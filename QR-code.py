from tkinter import *
import qrcode
from tkinter import filedialog
from tkinter import messagebox


#Create window app
window = Tk()
window.geometry('475x120')
window.title('QR Code Generator')
window.resizable(False,False) #Tắt tính năng phóng to cửa sổ

#Tạo hàm mở đường dẫn lưu file
direct = ""
def open_path():
    global direct
    files = [('PNG','*.png')]
    direct = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
    entry_path.set(direct)
    if len(direct) == 0:
        msb_path = messagebox.showwarning(title='Cảnh báo',message='Bạn hãy nhập đường dẫn!')
    else:
        pass

#Tạo hàm tạo mã QR
def getqr():
    data = input_data.get() #Lấy dữ liệu người dùng nhập
    if len(data) == 0:
        msb_path = messagebox.showwarning(title='Cảnh báo', message='Hãy nhập dữ liệu')
    else:
        img=qrcode.make(data) #Tạo QR code
        img.save(direct) #lưu Qr dưới dạng ảnh vào đường dẫn đã chọn
        msb_result = messagebox.showinfo(title = 'Thông báo', message='Bạn đã hoàn thành')

link  = Label(window, text = 'Nhập dữ liệu', fg = 'black', font = 'arial 10')
link.place(x=20,y=20)

#Tạo hộp nhập dữ liệu
input = StringVar()
input_data = Entry(window, width=55, textvariable= input)
input_data.place(x= 115, y= 20)

path  = Label(window, text = 'Nơi lưu file', fg = 'black', font = 'arial 10')
path.place(x=20,y=50)

#Tạo hộp nhập đường dẫn lưu file
entry_path = StringVar()
link_path = Entry(window, width=40, textvariable= entry_path)
link_path.place(x= 115, y= 50)

#Tạo Button brower
btn_brower = Button(window, width=10, text='Duyệt', command = open_path)
btn_brower.place(x=368, y=46)

#Tạo Button Create
btn_create = Button(window, width=10, text='Tạo QR code', command = getqr)
btn_create.place(x=368, y=80)


window.mainloop()

