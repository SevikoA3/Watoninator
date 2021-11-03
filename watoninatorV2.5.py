import tkinter as tk
import os
from tkinter import ttk
import random

window = tk.Tk()
window.title("The Watoninator V2.5")
window.geometry("750x400")
window.minsize(750, 400)
window.iconbitmap(os.getcwd()+"\\watoninatora.ico")

tab = ttk.Notebook(window)
tab.pack(expand=1, fill="both")
tab.size()

frame1 = tk.Frame(tab)
frame2 = tk.Frame(tab)
frame1.pack(expand=1, fill="both")
frame2.pack(expand=1, fill="both")

tab.add(frame1, text="Normal")
tab.add(frame2, text="Advanced")

def delete() :
    label1.config(text="")

def ganti() :
    jawaban = ["A", "B", "C", "D", "E"]
    label1.config(text=random.choice(jawaban))

def ganti1() :
    jawaban1 = []
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0 and var5.get() == 0 :
        labelA1.config(text="")
    elif var1.get() == 1 or var2.get() == 1 or var3.get() == 1 or var4.get() == 1 or var5.get() == 1 :
        if var1.get() == 1 :
            jawaban1.append("A")
        if var2.get() == 1 :
            jawaban1.append("B")
        if var3.get() == 1 :
            jawaban1.append("C")
        if var4.get() == 1 :
            jawaban1.append("D")
        if var5.get() == 1 :
            jawaban1.append("E")
        labelA1.config(text=random.choice(jawaban1))

#tab Normal
label = tk.Label(frame1, text="Jawaban :", font="none 24 bold")
label.pack(pady=5)
label1 = tk.Label(frame1, text="", font="none 80 bold")
label1.place(anchor=tk.CENTER, relx=0.5, rely=0.45)
label2 = tk.Label(frame1, text="klik tombol dibawah ini untuk memulai atau mengganti jawaban", font="none 16")
label2.place(anchor=tk.CENTER, relx=0.5, rely=0.75)
button = tk.Button(frame1, text="Pilih Jawaban", font="none 12", padx=10, pady=5, command=ganti)
button.place(anchor=tk.CENTER, relx=0.36, rely=0.9, relwidth=0.224, relheight=0.125)
deleteButton = tk.Button(frame1, text="Hapus Jawaban", font="none 12", padx=10, pady=5, command=delete)
deleteButton.place(anchor=tk.CENTER, relx=0.61, rely=0.9, relwidth=0.224, relheight=0.125)

#tab Advanced
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()

labelA = tk.Label(frame2, text="Pilih jawaban yang diragukan :", font="none 24 bold")
labelA.pack(pady=5)

check1 = tk.Checkbutton(frame2, text="A", font="none 20 bold", variable=var1)
check1.place(anchor=tk.CENTER, relx = 0.3, rely=0.2)
check2 = tk.Checkbutton(frame2, text="B", font="none 20 bold", variable=var2)
check2.place(anchor=tk.CENTER, relx = 0.4, rely=0.2)
check3 = tk.Checkbutton(frame2, text="C", font="none 20 bold", variable=var3)
check3.place(anchor=tk.CENTER, relx = 0.5, rely=0.2)
check4 = tk.Checkbutton(frame2, text="D", font="none 20 bold", variable=var4)
check4.place(anchor=tk.CENTER, relx = 0.6, rely=0.2)
check5 = tk.Checkbutton(frame2, text="E", font="none 20 bold", variable=var5)
check5.place(anchor=tk.CENTER, relx = 0.7, rely=0.2)

buttonA = tk.Button(frame2, text="Pilih Jawaban", font="none 12", command=ganti1)
buttonA.place(anchor=tk.CENTER, relwidth=0.224, relheight=0.125, relx=0.5, rely=0.9)
labelA2 = tk.Label(frame2, text="klik tombol dibawah ini untuk memulai atau mengganti jawaban", font="none 16")
labelA2.place(anchor=tk.CENTER, relx=0.5, rely=0.75)
labelA1 = tk.Label(frame2, text=" ", font="none 80 bold")
labelA1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

window.mainloop()