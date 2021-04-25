from tkinter import Tk, Radiobutton, Label, Entry, Button, IntVar, StringVar


class RemiseCal:

    def __init__(self):
        window = Tk()
        window.title("Calcul de remise")
        window.configure(background="light gray")
        window.geometry("450x220")
        window.resizable(height=False, width=False)

        self.bill_cost = StringVar()
        self.discount_percent = IntVar()
        self.discount = StringVar()
        self.final_cost = StringVar()

        discount_percent = Label(window, text="Pourcentage", fg="green")
        discount_percent.grid(column=0, row=0, padx=15, pady=15)

        bill_amount = Label(window, text="Facture", fg="black")
        bill_amount.grid(column=1, row=0, padx=40)

        bill_amount_entry = Entry(window, textvariable=self.bill_cost, width=14)
        bill_amount_entry.grid(column=2, row=0)

        five_percent_discount = Radiobutton(window, text="5%  ", variable=self.discount_percent, value=5)
        five_percent_discount.grid(column=0, row=1)
        ten_percent_discount = Radiobutton(window, text="10%", variable=self.discount_percent, value=10)
        ten_percent_discount.grid(column=0, row=2)
        fifteen_percent_discount = Radiobutton(window, text="15%", variable=self.discount_percent, value=15)
        fifteen_percent_discount.grid(column=0, row=3)
        twenty_percent_discount = Radiobutton(window, text="20%", variable=self.discount_percent, value=20)
        twenty_percent_discount.grid(column=0, row=4)
        twentyfive_percent_discount = Radiobutton(window, text="25%", variable=self.discount_percent, value=25)
        twentyfive_percent_discount.grid(column=0, row=5)
        thirty_percent_discount = Radiobutton(window, text="30%", variable=self.discount_percent, value=30)
        thirty_percent_discount.grid(column=0, row=6)

        discount_amount_lbl = Label(window, text="Valeur Remise", fg="black")
        discount_amount_lbl.grid(column=1, row=2, padx=40)
        discount_amount_entry = Entry(window, textvariable=self.final_cost, width=14)
        discount_amount_entry.grid(column=2, row=2)

        final_cost_lbl = Label(window, text="Montant final", fg="black")
        final_cost_lbl.grid(column=1, row=3, padx=40)
        final_cost_entry = Entry(window, textvariable=self.discount, fg="green", width=14)
        final_cost_entry.grid(column=2, row=3)

        calculate_btn = Button(window, text="Calculer", bg="light green", fg="black", width=14, command="")
        calculate_btn.grid(column=1, row=6)

        clear_btn = Button(window, text="Effacer", bg="light gray", fg="black", width=14, command="")
        clear_btn.grid(column=2, row=6)


        window.mainloop()

RemiseCal()
