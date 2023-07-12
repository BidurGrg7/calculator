


#x=float(input("Insert first number"))
#y=float(input("Insert your second number"))


#print("1= addition")
#print("2=subtraction")
#print("3=multiplication")
#print("4=Division")

#choice=int(input("Select what operation you want to do"))


#if   choice==1 :
        #result=x+y
        #print(result)

#elif  choice==2 :
       # result=x-y
        #print(result)

#elif choice==3:
       # result=x*y
       # print(result)

#elif choice==4 and y !=0 :
 #       result=x/y
  #      print(result)

#else:
 #   print("Invalid operation selected")


import tkinter as tk
window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")
window.config(bg='grey')

num1 = 0
num2 = 0
operation = ""
result = ""

def button_input(choices):
    global num1, num2
    if choices == '1':
        num1 = float(choices)
        print(num1)
    else:
        num2 = float(choices)
        print(num2)



def button_clicked(operation):
     global result
     if operation == "division":
             if num2 == 0:
                 print('Operation not possible')
                 return
             else:
                 result = num1 / num2

     elif operation == "addition":
             result = num1 + num2
     elif operation == "subtration":
             result = num1 - num2
     elif operation == "multiplication":
             result = num1 * num2

     print(result)
     result_display.config(text="Result=" + str(result))



def create_Button4operation(text, x, y, bg, width, height) :
    Button = tk.Button(window, text=text, bg=bg, width=int(width), height=int(height))
    Button.place(x=x,y=y)
    Button.bind('<Button-1>', lambda event, operation = operation: button_clicked(operation))
    #Button.bind('<Button-1>', lambda event, entries = choices :button_input(choices))


def create_Button4input(text,x,y,bg,width,height,choices) :
    Button=tk.Button(window,text=text,bg=bg,width=int(width),height=int(height))
    Button.place(x=x,y=y)
    Button.bind('<Button-1>', lambda event, choices=choices: button_input(choices))



create_Button4input('2',100,100,'red',2,1.5,'2')
create_Button4input('1',50,100,'red',2,1.5,'1')
create_Button4operation('Addition',0,50,'green',6,1.5)
create_Button4operation('Subtraction',70, 50,'black',8,1.5)
create_Button4operation('Multiplication', 165, 50,'white',9,1.5)
create_Button4operation('Division',270,50,'white',8,1.5 )

result_display = tk.Label(window, text="Result= ")
result_display.place(x=50, y=150)

window.mainloop()



