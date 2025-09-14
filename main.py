from tkinter import*
from tkinter import filedialog
def openfile():
    filepath=filedialog.askopenfilename(initialdir='C:\\Users\\Dell\\PycharmProjects\\PythonProject1',
                                        title ='open file',filetypes = (('txt file','*.txt'),('all files','*.*')))

    file = open(filepath,'r')
    print(file.read())
    file.close()

window =Tk()
button = Button(window,text='Open file',command=openfile)
button.pack()
window.mainloop()