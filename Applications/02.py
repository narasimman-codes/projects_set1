import tkinter as tk

app = tk.Tk()
app.title("Test App")
app.geometry("200x100")
label = tk.Label(app, text="Tkinter is working!")
label.pack()
app.mainloop()
