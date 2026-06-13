import tkinter as tk

window = tk.Tk()
window.title("Belajar Form")
window.geometry("800x500")

# ===== User login info =====

frame1 = tk.LabelFrame(window, text="User login info")
frame1.pack(fill="x", padx=10, pady=10)

tk.Label(frame1, text="Username:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(frame1, width=30).grid(row=0, column=1)

tk.Label(frame1, text="Email:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(frame1, width=30).grid(row=1, column=1)

tk.Label(frame1, text="Password:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(frame1, width=30, show="*").grid(row=2, column=1)

# ===== Data diri =====

frame2 = tk.LabelFrame(window, text="Data diri")
frame2.pack(fill="x", padx=10, pady=10)

tk.Label(frame2, text="Alamat:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(frame2, width=30).grid(row=0, column=1)

tk.Label(frame2, text="Tanggal lahir:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(frame2, width=30).grid(row=1, column=1)

tk.Label(frame2, text="Usia:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(frame2, width=30).grid(row=2, column=1)

gender = tk.StringVar()

tk.Label(frame2, text="Jenis kelamin:").grid(row=3, column=0, padx=10, pady=10)

tk.Radiobutton(
    frame2,
    text="Pria",
    variable=gender,
    value="Pria"
).grid(row=3, column=1, sticky="w")

tk.Radiobutton(
    frame2,
    text="Wanita",
    variable=gender,
    value="Wanita"
).grid(row=3, column=2, sticky="w")

# ===== Нижний блок =====

frame3 = tk.Frame(window)
frame3.pack(fill="x", padx=10, pady=10)

agree = tk.IntVar()

tk.Checkbutton(
    frame3,
    text="Saya bersedia mengikuti aturan forum",
    variable=agree
).pack(anchor="w")

tk.Button(frame3, text="Reset").pack(side="left", padx=5)
tk.Button(frame3, text="Submit").pack(side="left", padx=5)

window.mainloop()