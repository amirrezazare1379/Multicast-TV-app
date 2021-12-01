from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('950x700')
root.title('Television | تلويزيون')
root.resizable(width=False, height=False)
color = 'green'
root.configure(bg=color)
#================================================================



num1 = StringVar()
num2 = StringVar()
res_value = StringVar()



top_first = Frame(root, width=800, height=50, bg='gray')
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg='gray')
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg='gray')
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg='gray')
top_forth.pack(side=TOP)







btn_plus = Button(top_third, text="+", width=10,
                  highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text="-", width=10,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text="*", width=10,
                 highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text="/", width=10,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ========================== Entries and Labels ==========================

label_first_num = Label(top_first, text='Input Number 1: ', bg=color)
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text='Input Number 2: ', bg=color)
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_forth, text='Result: ', bg=color)
res.pack(side=LEFT, pady=10, padx=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)







root.mainloop()