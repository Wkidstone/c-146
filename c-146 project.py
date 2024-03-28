from tkinter import *

root=Tk()
root.title("Fibonacci series")
root.geometry("400x400")

label=Label(root)
label1=Label(root)
inbox=Entry(root)

def fs():
    input=int(inbox.get())
    n1=0
    n2=1
    sum=0
    counter=1
    sum2=0
    i=1
    while (i<=input):
        label["text"]+= str(sum) + " "
        label1["text"] = "Fibonacci sum: " + str(sum2)
        i=i+1
        n1=n2
        n2=sum
        sum=n1+n2
        sum2= sum2 + sum

inbox.pack()
button=Button(root,text="Show", command= fs)
button.pack()
label.pack()
label1.pack()

root.mainloop()