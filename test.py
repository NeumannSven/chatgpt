import tkinter as tk

root = tk.Tk()
root.title("Formen auf Canvas")
root.geometry("300x300")

canvas = tk.Canvas(root, width=250, height=250)
canvas.pack()

# Rotes Viereck mit abgerundeten Ecken zeichnen
x1, y1 = 50, 50
x2, y2 = 200, 200
r = 20 # Radius der abgerundeten Ecken
canvas.create_polygon(
    x1 + r, y1,
    x2 - r, y1,
    x2, y1 + r,
    x2, y2 - r,
    x2 - r, y2,
    x1 + r, y2,
    x1, y2 - r,
    x1, y1 + r,
    fill="red", outline=""
)

# Grünen Kreis zeichnen
canvas.create_oval(75, 75, 175, 175, fill="green", outline="")

root.mainloop()