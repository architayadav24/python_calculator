import tkinter as tk

#FUNCTION TO UPDATE EXPRESSION:-
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result=str(eval(expression))
            screen_var.set(result)
            expression = result
        except:
            screen_var.set("error")
            expressoin = ""
    elif(text == "C"):
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)
#MAIN WINDOW:-        
root = tk.Tk()
root.title("Calculator")
#root.geometry("400x500")

expression = ""
screen_var = tk.StringVar()
#DISPLAY SCREEN:-
screen = tk.Entry(root, textvar=screen_var,font="arial 20",bg="black",fg="red")
screen.pack(fill="both", ipadx=8, pady=10,padx=10)
#BUTTON LAYOUT:-
buttons=[
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','%','=','+'],
    ['C']
]
#CREAT BUTTONS:
for row in buttons:
    Frame = tk.Frame(root)
    Frame.pack(expand=True,fill="both")

    for btn in row:
        b=tk.Button(Frame, text=btn, font="arial 15",bg="red",fg="white")
        b.pack(side="left", expand=True,fill="both")
        b.bind("<Button-1>",click)
#RUM APP
root.mainloop()        













          
