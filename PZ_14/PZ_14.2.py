import tkinter as tk

def calculate():
    A = int(entry_a.get())
    B = int(entry_b.get())

    result = A // B

    label_result.config(text=f"Ответ: {result}")

window = tk.Tk()
window.title("Отрезки")
window.geometry("250x150")

tk.Label(window, text="Введите A").pack()
entry_a = tk.Entry(window)
entry_a.pack()

tk.Label(window, text="Введите B").pack()
entry_b = tk.Entry(window)
entry_b.pack()

tk.Button(window, text="Найти", command=calculate).pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()