from tkinter import *
root = Tk()
root.title('Calculator')

operator = ''
text_input = StringVar()
textdisplay = Entry(root, font=('arial',20,'bold'),textvariable=text_input, bd=30, bg='powder blue').grid(columnspan = 4)


# operator = 12 + 4
def btn_click(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def btn_clear_display():
    global operator
    operator = ''
    text_input.set(operator)

def btn_answer():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ''

# number button
btn_1 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='1', command = lambda:btn_click(1))
btn_2 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='2', command = lambda:btn_click(2))
btn_3 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='3', command = lambda:btn_click(3))
btn_4 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='4', command = lambda:btn_click(4))
btn_5 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='5', command = lambda:btn_click(5))
btn_6 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='6', command = lambda:btn_click(6))
btn_7 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='7', command = lambda:btn_click(7))
btn_8 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='8', command = lambda:btn_click(8))
btn_9 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='9', command = lambda:btn_click(9))
btn_0 = Button(root, padx=16, pady=16,bd = 8, fg='black',font=('arial',20,'bold'),text='0', command = lambda:btn_click(0))

# operator button

btn_add = Button(root, padx=16, pady=16, bd=8, fg='black',font=('arial',20,'bold'),text='+',command = lambda:btn_click('+'))
btn_mins = Button(root, padx=16, pady=16, bd=8, fg='black',font=('arial',20,'bold'),text='-',command = lambda:btn_click('-'))
btn_multi = Button(root, padx=16, pady=16, bd=8, fg='black',font=('arial',20,'bold'),text='x',command = lambda:btn_click('*'))
btn_divis = Button(root, padx=16, pady=16, bd=8, fg='black',font=('arial',20,'bold'),text='/',command = lambda:btn_click('/'))
btn_equal = Button(root, padx=16, pady=16, bd=8, fg='black',font=('arial',20,'bold'),text='=', command = btn_answer)
btn_clear = Button(root, padx=16, pady=16, bd=8, fg='black',font=('arial',20,'bold'),text='c', command = btn_clear_display)

btn_7.grid(row = 1, column=0)
btn_8.grid(row = 1, column=1)
btn_9.grid(row = 1, column=2)
btn_add.grid(row = 1, column=3)

btn_4.grid(row = 2, column=0)
btn_5.grid(row = 2, column=1)
btn_6.grid(row = 2, column=2)
btn_mins.grid(row = 2, column=3)

btn_1.grid(row = 3, column=0)
btn_2.grid(row = 3, column=1)
btn_3.grid(row = 3, column=2)
btn_multi.grid(row = 3, column=3)

btn_0.grid(row = 4, column=0)
btn_divis.grid(row = 4, column=1)
btn_equal.grid(row = 4, column=2)
btn_clear.grid(row = 4, column=3)

root.mainloop()
