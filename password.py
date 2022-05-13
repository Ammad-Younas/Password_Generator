from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip
import string
import random

root = Tk()

root.title("Password-Generator | Cyber-Spider")
root.iconbitmap('icon/logo.ico')
root.geometry("640x400+350+150")
root.resizable(height=FALSE, width=FALSE)


def upper():
    password_difficulty_combobox.config(state=DISABLED)
    u1 = string.ascii_uppercase
    list1 = []
    list1.extend(list(u1))
    random.shuffle(list1)
    output_text.config(state=NORMAL)
    result1 = "".join(list1[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result1)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def lower():
    password_difficulty_combobox.config(state=DISABLED)
    l1 = string.ascii_lowercase
    list2 = []
    list2.extend(list(l1))
    random.shuffle(list2)
    output_text.config(state=NORMAL)
    result2 = "".join(list2[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result2)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def digit():
    password_difficulty_combobox.config(state=DISABLED)
    d1 = string.digits
    list3 = []
    list3.extend(list(d1))
    random.shuffle(list3)
    output_text.config(state=NORMAL)
    result3 = "".join(list3[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result3)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def character():
    password_difficulty_combobox.config(state=DISABLED)
    p1 = string.punctuation
    list4 = []
    list4.extend(list(p1))
    random.shuffle(list4)
    output_text.config(state=NORMAL)
    result4 = "".join(list4[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result4)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def upper_and_lower():
    password_difficulty_combobox.config(state=DISABLED)
    u2 = string.ascii_uppercase
    l2 = string.ascii_lowercase
    list5 = []
    list5.extend(list(u2))
    list5.extend(list(l2))
    random.shuffle(list5)
    output_text.config(state=NORMAL)
    result5 = "".join(list5[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result5)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def upper_and_digit():
    password_difficulty_combobox.config(state=DISABLED)
    u3 = string.ascii_uppercase
    d2 = string.digits
    list6 = []
    list6.extend(list(u3))
    list6.extend(list(d2))
    random.shuffle(list6)
    output_text.config(state=NORMAL)
    result6 = "".join(list6[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result6)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def upper_and_character():
    password_difficulty_combobox.config(state=DISABLED)
    u4 = string.ascii_uppercase
    p2 = string.punctuation
    list7 = []
    list7.extend(list(u4))
    list7.extend(list(p2))
    random.shuffle(list7)
    output_text.config(state=NORMAL)
    result7 = "".join(list7[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result7)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def lower_and_digit():
    password_difficulty_combobox.config(state=DISABLED)
    l3 = string.ascii_lowercase
    d3 = string.digits
    list8 = []
    list8.extend(list(l3))
    list8.extend(list(d3))
    random.shuffle(list8)
    output_text.config(state=NORMAL)
    result8 = "".join(list8[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result8)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def lower_and_character():
    password_difficulty_combobox.config(state=DISABLED)
    l4 = string.ascii_lowercase
    p3 = string.punctuation
    list9 = []
    list9.extend(list(l4))
    list9.extend(list(p3))
    random.shuffle(list9)
    output_text.config(state=NORMAL)
    result9 = "".join(list9[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result9)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def digit_and_character():
    password_difficulty_combobox.config(state=DISABLED)
    d4 = string.digits
    p4 = string.punctuation
    list10 = []
    list10.extend(list(d4))
    list10.extend(list(p4))
    random.shuffle(list10)
    output_text.config(state=NORMAL)
    result10 = "".join(list10[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result10)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def upper_and_lower_and_digit():
    password_difficulty_combobox.config(state=DISABLED)
    u5 = string.ascii_uppercase
    l5 = string.ascii_lowercase
    d5 = string.digits
    list11 = []
    list11.extend(list(u5))
    list11.extend(list(l5))
    list11.extend(list(d5))
    random.shuffle(list11)
    output_text.config(state=NORMAL)
    result11 = "".join(list11[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result11)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def upper_and_lower_and_characters():
    password_difficulty_combobox.config(state=DISABLED)
    u6 = string.ascii_uppercase
    l6 = string.ascii_lowercase
    p5 = string.punctuation
    list12 = []
    list12.extend(list(u6))
    list12.extend(list(l6))
    list12.extend(list(p5))
    random.shuffle(list12)
    output_text.config(state=NORMAL)
    result12 = "".join(list12[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result12)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def upper_and_lower_and_digit_and_characters():
    password_difficulty_combobox.config(state=DISABLED)
    u7 = string.ascii_uppercase
    l7 = string.ascii_lowercase
    d6 = string.digits
    p6 = string.punctuation
    list13 = []
    list13.extend(list(u7))
    list13.extend(list(l7))
    list13.extend(list(p6))
    list13.extend(list(d6))
    random.shuffle(list13)
    output_text.config(state=NORMAL)
    result13 = "".join(list13[0:int(password_length_combobox.get())])
    password_length_combobox.config(state=DISABLED)
    output_text.insert('1.0', result13)
    output_text.config(state=DISABLED)
    generate_btn.config(state=DISABLED)
    copy_btn.config(state=NORMAL)
    clear_btn.config(state=NORMAL)


def for_difficulty_selection(e):
    if password_difficulty_combobox.get() == "Only Upper Case":
        password_length_combobox.config(values=for_only_upper_case)

    elif password_difficulty_combobox.get() == "Only Lower Case":
        password_length_combobox.config(values=for_only_lower_case)

    elif password_difficulty_combobox.get() == "Only Digits":
        password_length_combobox.config(values=for_only_digits)

    elif password_difficulty_combobox.get() == "Only Characters":
        password_length_combobox.config(values=for_only_characters)

    elif password_difficulty_combobox.get() == "Upper Case + Lower Case":
        password_length_combobox.config(values=for_upper_and_lower)

    elif password_difficulty_combobox.get() == "Upper Case + Digits":
        password_length_combobox.config(values=for_upper_and_digit)

    elif password_difficulty_combobox.get() == "Upper Case + Characters":
        password_length_combobox.config(values=for_upper_and_characters)

    elif password_difficulty_combobox.get() == "Lower Case + Digits":
        password_length_combobox.config(values=for_lower_and_digit)

    elif password_difficulty_combobox.get() == "Lower Case + Characters":
        password_length_combobox.config(values=for_lower_and_characters)

    elif password_difficulty_combobox.get() == "Digits + Characters":
        password_length_combobox.config(values=for_digit_and_characters)

    elif password_difficulty_combobox.get() == "Upper Case + Lower Case + Digits":
        password_length_combobox.config(values=for_upper_and_lower_and_digit)

    elif password_difficulty_combobox.get() == "Upper Case + Lower Case + Characters":
        password_length_combobox.config(values=for_upper_and_lower_and_characters)

    elif password_difficulty_combobox.get() == "Upper Case + Lower Case + Digits + Characters":
        password_length_combobox.config(values=for_upper_and_lower_and_digit_and_characters)

    else:
        password_length_combobox.set("")


def generate_programme():
    if password_difficulty_combobox.get() == "Options":
        messagebox.showwarning("Warning!", "Select Option")
    elif password_length_combobox.get() == "":
        messagebox.showwarning("Warning!", "Select Password Length")
    else:
        if password_difficulty_combobox.get() == "Only Upper Case":
            upper()
        elif password_difficulty_combobox.get() == "Only Lower Case":
            lower()
        elif password_difficulty_combobox.get() == "Only Digits":
            digit()
        elif password_difficulty_combobox.get() == "Only Characters":
            character()
        elif password_difficulty_combobox.get() == "Upper Case + Lower Case":
            upper_and_lower()
        elif password_difficulty_combobox.get() == "Upper Case + Digits":
            upper_and_digit()
        elif password_difficulty_combobox.get() == "Upper Case + Characters":
            upper_and_character()
        elif password_difficulty_combobox.get() == "Lower Case + Digits":
            lower_and_digit()
        elif password_difficulty_combobox.get() == "Lower Case + Characters":
            lower_and_character()
        elif password_difficulty_combobox.get() == "Digits + Characters":
            digit_and_character()
        elif password_difficulty_combobox.get() == "Upper Case + Lower Case + Digits":
            upper_and_lower_and_digit()
        elif password_difficulty_combobox.get() == "Upper Case + Lower Case + Characters":
            upper_and_lower_and_characters()
        elif password_difficulty_combobox.get() == "Upper Case + Lower Case + Digits + Characters":
            upper_and_lower_and_digit_and_characters()


def copy_programme():
    output_text.config(state=NORMAL)
    pyperclip.copy(output_text.get('1.0', END))
    messagebox.showinfo("Info!", "Copied!")
    output_text.config(state=DISABLED)
    copy_btn.config(state=DISABLED)


def clear_programme():
    password_difficulty_combobox.config(state=NORMAL)
    password_difficulty_combobox.set("Options")
    password_length_combobox.config(state=NORMAL)
    password_length_combobox.set("")
    output_text.config(state=NORMAL)
    output_text.delete('1.0', END)
    output_text.config(state=DISABLED)
    generate_btn.config(state=NORMAL)
    copy_btn.config(state=DISABLED)
    clear_btn.config(state=DISABLED)
    password_difficulty_combobox['state'] = 'readonly'
    password_length_combobox['state'] = 'readonly'


intro = Label(root, text="Password Generator", font=("times new roman", 30), bg='#053246', fg='White')
intro.place(x=0, y=0, relwidth=1)


option_label = Label(root, text="Select Option: ", fg="#262626", font=("Times new roman", 12, "bold"))
option_label.place(x=20, y=70)

# Password_Difficulty_Options
password_difficulty = ["Only Upper Case", "Only Lower Case", "Only Digits", "Only Characters", "Upper Case + Lower Case", "Upper Case + Digits", "Upper Case + Characters", "Lower Case + Digits", "Lower Case + Characters", "Digits + Characters", "Upper Case + Lower Case + Digits", "Upper Case + Lower Case + Characters", "Upper Case + Lower Case + Digits + Characters"]


# Upper
for_only_upper_case = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

# Lower
for_only_lower_case = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

# Digits
for_only_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Characters
for_only_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]

# Upper_and_lower
for_upper_and_lower = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52"]

# Upper and Digit
for_upper_and_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]

# Upper and Characters
for_upper_and_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58"]

# Lower and Digit
for_lower_and_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]

# Lower and Characters
for_lower_and_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58"]

# Digit and Characters
for_digit_and_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42"]

# Upper and Lower and Digits
for_upper_and_lower_and_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62"]

# Upper and Lower and Characters
for_upper_and_lower_and_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84"]

# Upper and Lower and Digit and Characters
for_upper_and_lower_and_digit_and_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94"]

# Password_Difficulty_Combobox
password_difficulty_combobox = ttk.Combobox(root, width=45, values=password_difficulty, state="readonly")
password_difficulty_combobox.set("Options")
password_difficulty_combobox.place(x=170, y=70)
password_difficulty_combobox.bind("<<ComboboxSelected>>", for_difficulty_selection)

# Label of Password Length
password_length_label = Label(root, text="Select Password Length: ", fg="#262626", font=("Times new roman", 10, "bold"))
password_length_label.place(x=20, y=130)

# Password Length Combobox
password_length_combobox = ttk.Combobox(root, width=10, values=[], state="readonly")
password_length_combobox.place(x=280, y=130)

output = LabelFrame(root, text="Generated Password", bd=7, relief=GROOVE, font=("Segoe Script", 12, "bold"), fg="purple")
output.place(x=110, y=200, height=75, width=420)

scroolbar_for_output = Scrollbar(output, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_output.pack(side=BOTTOM, fill=X)

output_text = Text(output, wrap=NONE, xscrollcommand=scroolbar_for_output.set)
output_text.pack(fill=BOTH, expand=1)

scroolbar_for_output.config(command=output_text.xview)

output_text.config(state=DISABLED)

generate_btn = Button(root, text="Generate", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", activebackground="white", command=generate_programme)
generate_btn.place(x=110, y=300)


copy_btn = Button(root, text="Copy", font=("times new roman", 15, "bold"), bg="grey", fg="white", cursor="hand2", activebackground="white", command=copy_programme)
copy_btn.place(x=290, y=300)
copy_btn.config(state=DISABLED)


clear_btn = Button(root, text="Clear *", font=("times new roman", 15, "bold"), bg="#A16DF0", fg="white", cursor="hand2", activebackground="white", command=clear_programme)
clear_btn.place(x=445, y=300)
clear_btn.config(state=DISABLED)


root.mainloop()
