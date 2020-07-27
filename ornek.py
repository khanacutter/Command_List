from tkinter import *

path= "ornek.txt"
k=0

def komut():
    global k
    k=k+1

    A= giris.get()
    yazi=Label(window)
    yazi.config(text="Write command here",bg="black",fg="white")
    yazi.pack()

    yazi.config(text=str(k)+'. '+giris.get())
    yazi.pack()

    with open(path,"a") as f:
        f.write(str(k)+'. '+str(A)+'\n')


def komut2():
    with open(path,"r") as f:
        readed=f.read()

    window2= Tk()

    yazi2= Label(window2)
    yazi2.config(text=readed)
    yazi2.pack()
    
    buton3=Button(window2,text="Go Back",fg="green",command=window2.destroy)
    buton3.pack()

    

window= Tk()
window.title("Command_LisT")

window.configure(bg="black")

giris=Entry(window)
giris.pack(pady=50)

buton=Button(window,text=">>>Click here write a command",command=komut,fg="red")
buton.pack(padx=50,pady=0)

buton2=Button(window,text=">>>Click here to see command",command=komut2,fg="green")
buton2.pack(padx=50,pady=100)



mainloop()