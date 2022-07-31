from tkinter import *
import random,string
import py_compile

root =Tk()
root.geometry("400.400")
root.resizable(0,0)
root.title("DataFlair - PASSWORD GENERATOR")

# TK initialized tkinter which means window was created
# geometry set the width and height of the window
# resizable set a fixed size of the window
# title sets the title of the window

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='DataFlair', font ='arial 15 bold').pack(side = BOTTOM)
# label displays one or more lines of text that users cannot be able to modify
# root is the name we refer to our window
# text that we display on the label
# Font in which the text is displayed in
# pack organized widget in block

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()
# pass_len stores the length of the password
# spinbox is used to specify the length of the password, in this case its from 8 to 32
pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
Entry(root , textvariable = pass_str).pack()    

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)