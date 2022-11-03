from tkinter import *

# Настройка окна
root = Tk()
root.title("Calculator")
root.geometry("460x600")
root["bg"] = "white"

# Переменная для хранения первого числа
NUM_1 = 0
NUM_2 = 0
SIGN = ""

# ФУНКЦИИ

#Функции для кнопок с арифметическими операциями

def click_plus():
  global NUM_1
  global NUM_2
  global SIGN
  NUM_2 = NUM_1
  NUM_1 = 0
  SIGN = "+"

def click_minus():
  global NUM_1
  global NUM_2
  global SIGN
  NUM_2 = NUM_1
  NUM_1 = 0
  SIGN = "-"

def click_del():
  global NUM_1
  global NUM_2
  global SIGN
  NUM_2 = NUM_1
  NUM_1 = 0
  SIGN = "/"

def click_um():
  global NUM_1
  global NUM_2
  global SIGN
  NUM_2 = NUM_1
  NUM_1 = 0
  SIGN = "*"

def click_ravno():
  global NUM_1
  global NUM_2
  global SIGN

  result = 0

  if SIGN == "+":
    result = NUM_2 + NUM_1
  elif SIGN == "-":
    result = NUM_2 - NUM_1
  elif SIGN == "/":
    result = NUM_2 / NUM_1
  elif SIGN == "*":
    result = NUM_2 * NUM_1

  res.configure(text=result)

# Функции для кнопок с цифрами

def clean():
  global NUM_1
  global NUM_2
  global SIGN
  NUM_1 = 0
  NUM_2 = 0
  SIGN = ""
  res.configure(text=NUM_1)

def click_1():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 1
  res.configure(text=NUM_1)

def click_2():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 2
  res.configure(text=NUM_1)

def click_3():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 3
  res.configure(text=NUM_1)

def click_4():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 4
  res.configure(text=NUM_1)

def click_5():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 5
  res.configure(text=NUM_1)


def click_6():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 6
  res.configure(text=NUM_1)

def click_7():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 7
  res.configure(text=NUM_1)

def click_8():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 8
  res.configure(text=NUM_1)

def click_9():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 9
  res.configure(text=NUM_1)

def click_0():
  global NUM_1
  NUM_1 = NUM_1 * 10 + 0
  res.configure(text=NUM_1)


# СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРЕЙСА

res = Label(root, text="0", bg = "white", font=("Arial Bold", 30))

# Кнопки +, -, /, *
b_plus = Button(root, text="+", bg="grey", width = 8, height = 5, fg="black", command = click_plus)
b_minus = Button(root, text="-", bg="grey", width = 8, height = 5, fg="black", command = click_minus)
b_um = Button(root, text="/", bg="grey", width = 8, height = 5, fg="black", command = click_um)
b_del = Button(root, text="x", bg="grey", width = 8, height = 5, fg="black", command = click_del)

# Кнопки 7, 8, 9, CE
b7 = Button(root, text="7", bg="white", width = 8, height = 5, fg="black", command=click_7)
b8 = Button(root, text="8", bg="white", width = 8, height = 5, fg="black", command=click_8)
b9 = Button(root, text="9", bg="white", width = 8, height = 5, fg="black", command=click_9)
b_ce = Button(root, text="CE", bg="orange", width = 8, height = 5, fg="black", command = clean)

# Кнопки 4, 5, 6, =
b4 = Button(root, text="4", bg="white", width = 8, height = 5, fg="black", command=click_4)
b5 = Button(root, text="5", bg="white", width = 8, height = 5, fg="black", command=click_5)
b6 = Button(root, text="6", bg="white", width = 8, height = 5, fg="black", command=click_6)
b_r = Button(root, text="=", bg="orange", width = 8, height = 5, fg="black", command = click_ravno)

# Кнопки 1, 2, 3, 0
b1 = Button(root, text="1", bg="white", width = 8, height = 5, fg="black", command=click_1)
b2 = Button(root, text="2", bg="white", width = 8, height = 5, fg="black", command=click_2)
b3 = Button(root, text="3", bg="white", width = 8, height = 5, fg="black", command=click_3)
b0 = Button(root, text="0", bg="white", width = 8, height = 5, fg="black", command=click_0)

# ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ НА ЭКРАН
res.grid(column=0, row=0, columnspan=4, sticky = "e")

# Кнопки с действиями
b_plus.grid(row=1, column=0)
b_minus.grid(row=1, column=1)
b_um.grid(row=1, column=2)
b_del.grid(row=1, column=3)

# Кнопки 7, 8, 9, CE
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b_ce.grid(row=2, column=3)

# Кнопки 4, 5, 6, =
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b_r.grid(row=3, column=3)

# Кнопки 1, 2, 3, 0
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b0.grid(row=4, column=3)

root.mainloop()
