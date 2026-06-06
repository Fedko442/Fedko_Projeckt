import tkinter as tk

window = tk.Tk()
window.title("Регистрация")
window.geometry("300x300")

tk.Label(window, text="Логин").pack()
login = tk.Entry(window)
login.pack()

tk.Label(window, text="Email").pack()
email = tk.Entry(window)
email.pack()

tk.Label(window, text="Пароль").pack()
password = tk.Entry(window, show="*")
password.pack()

tk.Label(window, text="Возраст").pack()
age = tk.Entry(window)
age.pack()

tk.Button(window, text="Отправить").pack()

window.mainloop()