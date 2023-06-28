import tkinter as tk


class Kalkulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator")

        self.wyświetlacz = tk.Entry(self.master, width=40, borderwidth=5)
        self.wyświetlacz.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.utwórz_przyciski()

    def utwórz_przyciski(self):
        lista_przycisków = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "/", "=",
            "Cofnij"
        ]

        wiersz = 1
        kolumna = 0
        for przycisk in lista_przycisków:
            if kolumna > 3:
                wiersz += 1
                kolumna = 0
            if przycisk == "=":
                tk.Button(self.master, text="=", width=10, height=5, command=self.oblicz).grid(row=wiersz,
                                                                                               column=kolumna, padx=10,
                                                                                               pady=10)
            elif przycisk == "Cofnij":
                tk.Button(self.master, text="Cofnij", width=10, height=5, command=self.cofnij).grid(row=wiersz,
                                                                                                    column=kolumna,
                                                                                                    padx=10, pady=10)
            else:
                cmd = lambda x=przycisk: self.dodaj(x)
                tk.Button(self.master, text=przycisk, width=10, height=5, command=cmd).grid(row=wiersz, column=kolumna,
                                                                                            padx=10, pady=10)
            kolumna += 1

    def dodaj(self, wartość):
        self.wyświetlacz.insert(tk.END, wartość)

    def oblicz(self):
        try:
            wynik = eval(self.wyświetlacz.get())
            self.wyświetlacz.delete(0, tk.END)
            self.wyświetlacz.insert(0, wynik)
        except:
            self.wyświetlacz.delete(0, tk.END)
            self.wyświetlacz.insert(0, "Błąd")

    def cofnij(self):
        self.wyświetlacz.delete(len(self.wyświetlacz.get()) - 1, tk.END)
root = tk.Tk()
app = Kalkulator(root)
root.mainloop()