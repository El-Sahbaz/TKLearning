from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

BMI = 0
result_var = StringVar()
result_var.set("")

def BMI_Calculation():
    global BMI
    BMI = 0
    try:
        weight = float(my_entry.get())
        height = float(my_entry_2.get())

        if height == 0 or weight == 0:
            result_var.set("Height and Weight cannot be zero!")
            return

        BMI = weight / (height * height)

        if BMI < 18.5:
            result_var.set(f"Your BMI is {BMI:.2f}. You are UNDERWEIGHT!")
        elif 18.5 <= BMI < 24.9:
            result_var.set(f"Your BMI is {BMI:.2f}. You are NORMAL.")
        elif 25 <= BMI < 29.9:
            result_var.set(f"Your BMI is {BMI:.2f}. You are OVERWEIGHT!")
        elif BMI >= 30:
            result_var.set(f"Your BMI is {BMI:.2f}. You are OBESE. Consider a healthier lifestyle.")
    except ValueError:
        result_var.set("Please fill in the blanks with valid numbers.")

# Label - Weight
my_label = Label(text="Enter Your Weight (kg) (e.g. 70)")
my_label.config(pady=3)
my_label.pack()

# Entry - Weight
my_entry = Entry(width=20)
my_entry.pack()

# Label - Height
my_label_2 = Label(text="Enter Your Height (m) (e.g. 1.75)")
my_label_2.config(pady=3)
my_label_2.pack()

# Entry - Height
my_entry_2 = Entry(width=20)
my_entry_2.pack()

# Button - Calculate
my_button = Button(text="Calculate", command=BMI_Calculation)
my_button.pack()

# Label - Result (Dynamic)
my_label_4 = Label(textvariable=result_var, fg="black", padx=5, pady=5)
my_label_4.pack()

window.mainloop()
