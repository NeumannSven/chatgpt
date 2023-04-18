import os
import openai
import 

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = """
Schreibe ein Python Programm mit TKinter Fenster auf dem ein Rotes Viereck mit abgerundeten Ecken und ein grüner Kreis auf einen Canvas dargestellt wird.
Zunächst müssen wir das notwendige Modul `tkinter` importieren. Danach können wir ein Fenster erstellen und den Titel sowie die Größe des Fensters festlegen:

```
import tkinter as tk

root = tk.Tk()
root.title("Formen auf Canvas")
root.geometry("300x300")
```

Als nächstes erstellen wir ein `Canvas` Widget und geben seine Größe an:

```
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack()
```

Nun definieren wir die Formen, die wir auf dem `Canvas` darstellen möchten. Wir beginnen mit dem roten Viereck:

```
rectangle = canvas.create_rounded_rectangle(50, 50, 200, 200, fill="red", outline="")
```

Hier speichern wir das Ergebnis der Funktion `create_rounded_rectangle()` in der Variable `rectangle`. Diese Funktion erstellt ein abgerundetes Rechteck mit den Koordinaten (50, 50) für den linken oberen Punkt und (200, 200) für den rechten unteren Punkt. Die Farbe des Füllens wird mit `fill="red"` festgelegt und der Rahmen wird auf unsichtbar gesetzt.

Als Nächstes erstellen wir den grünen Kreis:

```
circle = canvas.create_oval(75, 75, 175, 175, fill="green", outline="")
```

Auch hier speichern wir das Ergebnis wiederum in einer Variable: `circle`. `create_oval()` erstellt einen Kreis mit den Koordinaten (75, 75) für den linken oberen Punkt und (175, 175) für den rechten unteren Punkt. Die Farbe wird mit `fill="green"` festgelegt und der Rahmen wird auf unsichtbar gesetzt.

Zum Abschluss starten wir das `tkinter` Fenster:

```
root.mainloop()
```

Das gesamte Programm sieht nun wie folgt aus:

```
import tkinter as tk

root = tk.Tk()
root.title("Formen auf Canvas")
root.geometry("300x300")

canvas = tk.Canvas(root, width=250, height=250)
canvas.pack()

rectangle = canvas.create_rounded_rectangle(50, 50, 200, 200, fill="red", outline="")
circle = canvas.create_oval(75, 75, 175, 175, fill="green", outline="")

root.mainloop()
```
>>> %Run test.py
Traceback (most recent call last):
  File "/Users/sven/Desktop/projects/pyspacehb/chatgpt/test.py", line 11, in <module>
    rectangle = canvas.create_rounded_rectangle(50, 50, 200, 200, fill="red", outline="")
AttributeError: 'Canvas' object has no attribute 'create_rounded_rectangle'

"""

prompt += input("?")


response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
    {'role': 'user',
     'content': f'{prompt}'}
    ])

print(response['choices'][0]['message']['content'])

