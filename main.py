import tkinter as tk

class HesapMakinesiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")

        self.entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 1, 4), ('(', 2, 4), (')', 3, 4), ('Del',4, 4)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, padx=40, pady=20, font=('Arial', 15),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, value):
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Hata!")
        elif value == 'Del':
            current_value = self.entry.get()
            self.entry.delete(len(current_value)-1)
            
        else:
            current_text = self.entry.get()
            if current_text == "Hata!":
                self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = HesapMakinesiApp(root)
    root.mainloop()
