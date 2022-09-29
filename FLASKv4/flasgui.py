from tkinter import *
from tkinter import messagebox
import flaskStarter


#initialize Form
IPAddr = flaskStarter.findInternalIp()
form = Tk()
 
form.title("gnuRemote v1.0")
form.geometry("350x200")
form.resizable(False , False)
 
applictn = Frame(form)
applictn.grid()
 
 
def dialog():
    var = messagebox.showinfo(f'Remote Started' , f'Go to: https://{IPAddr} on your mobile phone browser.\n It will be started after you press okay.')
    form.destroy()
    flaskStarter.startFlaskServer()
    
#Start Button
btnOne = Button(applictn, text = " Start Remote " , width=20, command=dialog)
btnOne.grid(padx=100, pady=40)

#Shutdown Button
closeInfoLabel = Label(form,text = "How to close application?").place(x = 40, y = 95) 
closeInfo = Label(form,text = "Simply Close the terminal/CMD window \n\n --OR-- \n\n Press CTRL + C while on it.").place(x = 40, y = 115)


 
 #Draw the form
form.mainloop()
 