import tkinter as tk

root = tk.Tk()
root.geometry("250x300")
root.resizable(False, False)
root.title("Calculator")

previous_operand = None
current_operand = None
operator = None


# functions
def update_screen():
    global previous_operand, current_operand

    show_previous_operand = "" if previous_operand is None else previous_operand
    show_current_operand = "" if current_operand is None else current_operand

    calculatorScreen2.config(state="normal")
    calculatorScreen1.config(state="normal")
    calculatorScreen2.delete(1.0, "end")
    calculatorScreen1.delete(1.0, "end")
    calculatorScreen2.insert("end", str(show_current_operand))
    calculatorScreen1.insert("end", str(show_previous_operand))
    calculatorScreen2.config(state="disabled")
    calculatorScreen1.config(state="disabled")


def append_number(n):
    global current_operand

    if n == "." and current_operand is None:
        current_operand = "0."
        update_screen()
        return

    if n == "." and n in current_operand:
        return

    if (current_operand is None and n == 0) or (current_operand == "0" and n == 0):
        current_operand = "0"
        update_screen()
        return

    current_operand = str(n) if current_operand is None else current_operand+str(n)

    update_screen()


def evaluate():
    global current_operand, previous_operand, operator

    if current_operand is None:
        return

    try:
        return eval(previous_operand+current_operand)
    except:
        return "Error"


def final_evaluation():
    global current_operand, previous_operand, operator

    if previous_operand is None or current_operand is None:
        return

    current_operand = str(evaluate())
    previous_operand = None

    update_screen()
    current_operand = None


def change_plus_minus_sign():
    global current_operand
    if current_operand is None:
        return

    current_operand = current_operand[1:len(current_operand)] if current_operand[:1] == "-" else "-"+current_operand

    update_screen()


def operation(operator_type):
    global operator, previous_operand, current_operand

    match operator_type:
        case "add":
            operator = "+"
        case "subtract":
            operator = "-"
        case "multiply":
            operator = "*"
        case "divide":
            operator = "/"

    if current_operand is None and previous_operand is None:
        return

    if current_operand is None and previous_operand is not None:
        previous_operand = previous_operand[0:len(previous_operand)-1]+operator
        update_screen()
        return

    if current_operand is not None and previous_operand is not None:
        previous_operand = str(evaluate())+operator
        current_operand = None
        update_screen()
        return

    previous_operand = current_operand+operator
    current_operand = None

    update_screen()


def clear_all():
    global current_operand, previous_operand, operator

    current_operand = None
    previous_operand = None
    operator = None

    update_screen()


def delete_last_char():
    global current_operand

    if current_operand is None:
        return

    current_operand = current_operand[:-1]
    update_screen()


calculatorFrame = tk.Frame(root, width=350, height=500, bd=3, relief='ridge')
calculatorFrame.grid(column=0, row=0)

calculatorScreen1 = tk.Text(calculatorFrame, width=16, height=1, bg="white", font=("Arial", 14), state="disabled")
calculatorScreen1.grid(column=0, row=0, columnspan=4, rowspan=1)
calculatorScreen2 = tk.Text(calculatorFrame, width=15, height=1, bg="white", font=("Arial", 16), state="disabled")
calculatorScreen2.grid(column=0, row=1, columnspan=4, rowspan=1)

clearButton = tk.Button(calculatorFrame, text="C", font=("Arial", 16), width=3, height=1, command=lambda: clear_all())
clearButton.grid(column=0, row=2)
deleteButton = tk.Button(calculatorFrame, text="CE", font=("Arial", 16), width=3, height=1, command=lambda: delete_last_char())
deleteButton.grid(column=1, row=2)
percentButton = tk.Button(calculatorFrame, text="%", font=("Arial", 16), width=3, height=1)
percentButton.grid(column=2, row=2)
plusMinusButton = tk.Button(calculatorFrame, text="±", font=("Arial", 16), width=3, height=1, command=lambda: change_plus_minus_sign())
plusMinusButton.grid(column=3, row=2)
numberSeven = tk.Button(calculatorFrame, text="7", font=("Arial", 16), width=3, height=1, command=lambda: append_number(7))
numberSeven.grid(column=0, row=3)
numberEight = tk.Button(calculatorFrame, text="8", font=("Arial", 16), width=3, height=1, command=lambda: append_number(8))
numberEight.grid(column=1, row=3)
numberNine = tk.Button(calculatorFrame, text="9", font=("Arial", 16), width=3, height=1, command=lambda: append_number(9))
numberNine.grid(column=2, row=3)
multiplyButton = tk.Button(calculatorFrame, text="*", font=("Arial", 16), width=3, height=1, command=lambda: operation("multiply"))
multiplyButton.grid(column=3, row=3)
numberFour = tk.Button(calculatorFrame, text="4", font=("Arial", 16), width=3, height=1, command=lambda: append_number(4))
numberFour.grid(column=0, row=4)
numberFive = tk.Button(calculatorFrame, text="5", font=("Arial", 16), width=3, height=1, command=lambda: append_number(5))
numberFive.grid(column=1, row=4)
numberSix = tk.Button(calculatorFrame, text="6", font=("Arial", 16), width=3, height=1, command=lambda: append_number(6))
numberSix.grid(column=2, row=4)
divideButton = tk.Button(calculatorFrame, text="/", font=("Arial", 16), width=3, height=1, command=lambda: operation("divide"))
divideButton.grid(column=3, row=4)
numberOne = tk.Button(calculatorFrame, text="1", font=("Arial", 16), width=3, height=1, command=lambda: append_number(1))
numberOne.grid(column=0, row=5)
numberTwo = tk.Button(calculatorFrame, text="2", font=("Arial", 16), width=3, height=1, command=lambda: append_number(2))
numberTwo.grid(column=1, row=5)
numberThree = tk.Button(calculatorFrame, text="3", font=("Arial", 16), width=3, height=1, command=lambda: append_number(3))
numberThree.grid(column=2, row=5)
subtractButton = tk.Button(calculatorFrame, text="-", font=("Arial", 16), width=3, height=1, command=lambda: operation("subtract"))
subtractButton.grid(column=3, row=5)
numberZero = tk.Button(calculatorFrame, text="0", font=("Arial", 16), width=3, height=1, command=lambda: append_number(0))
numberZero.grid(column=0, row=6)
decimalButton = tk.Button(calculatorFrame, text=".", font=("Arial", 16), width=3, height=1, command=lambda: append_number("."))
decimalButton.grid(column=1, row=6)
equalsButton = tk.Button(calculatorFrame, text="=", font=("Arial", 16), width=3, height=1, command=lambda: final_evaluation())
equalsButton.grid(column=2, row=6)
addButton = tk.Button(calculatorFrame, text="+", font=("Arial", 16), width=3, height=1, command=lambda: operation("add"))
addButton.grid(column=3, row=6)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()