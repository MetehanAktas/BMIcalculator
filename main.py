import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(bg="gray")
window.minsize(width=350, height=350)

# Functions
def calculate_bmi():
    user_kg = kg_entry.get()
    user_cm = cm_entry.get()


    if not user_kg or not user_cm:
        result_var.set("Please enter both weight and height.")
        return


    try:
        user_kg = float(user_kg)
        user_cm = float(user_cm)
    except ValueError:
        result_var.set("Please enter valid numbers.")
        return


    bmi = user_kg / ((user_cm / 100) ** 2)


    if bmi < 18.5:
        result_var.set(f"Your BMI is {bmi:.2f} and you are underweight.")
    elif 18.5 <= bmi < 24.9:
        result_var.set(f"Your BMI is {bmi:.2f} and you are normal.")
    elif 24.9 <= bmi < 29.9:
        result_var.set(f"Your BMI is {bmi:.2f} and you are overweight.")
    elif 29.9 <= bmi < 34.9:
        result_var.set(f"Your BMI is {bmi:.2f} and you are obese class 1.")
    elif 34.9 <= bmi < 39.9:
        result_var.set(f"Your BMI is {bmi:.2f} and you are obese class 2.")
    elif bmi >= 39.9:
        result_var.set(f"Your BMI is {bmi:.2f} and you are obese class 3.")

# Interface
header = tkinter.Label(text="BMI Calculator", bg="gray", fg="black", font=(50))
header.pack()

kg = tkinter.Label(text="KG", bg="gray", fg="black")
kg.place(x=50, y=100)

cm = tkinter.Label(text="CM", bg="gray", fg="black")
cm.place(x=50, y=160)

# Result Label
result_var = tkinter.StringVar()
result_var.set("")
result_message = tkinter.Label(textvariable=result_var, bg="gray", fg="black")
result_message.place(x=70, y=260)

# Entries
kg_entry = tkinter.Entry(width=20)
kg_entry.place(x=50, y=120)

cm_entry = tkinter.Entry(width=20)
cm_entry.place(x=50, y=180)

# Button
button_one = tkinter.Button(text="Calculate BMI", command=calculate_bmi)
button_one.place(x=120, y=220)

window.mainloop()