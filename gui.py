from tkinter import *
from logic import *

class Gui():
    def __init__(self, window):
        """
        Method for initialziing the GUI and creating the main window and widgets
        Method also contains dynamic variables which will be used later
        :param window: Main Window containing all widgets
        """
        # MainWindow
        self.window = window
        # Title
        self.frame_Menu = Frame(self.window)
        self.label_Menu = Label(self.frame_Menu, text='Main Menu', font=('Algerian', 20))
        self.label_Menu.pack(pady=10)
        self.frame_Menu.pack()
        # ShopButton
        self.frame_Shop = Frame(self.window)
        self.label_Shop = Button(self.frame_Shop, text='Shop', width=50, height=9, bd=2, relief='solid',
                                 command=self.main_menu_to_cart_menu)
        button_font = ('Helvetica', 14)
        self.label_Shop.configure(font=button_font)
        self.label_Shop.pack(side='top', pady=50)
        self.frame_Shop.pack()
        # QuitButton
        self.frame_Quit = Frame(self.window)
        self.label_Quit = Button(self.frame_Quit, text='Quit', width=50, height=9, bd=2, relief='solid',
                                 command=self.quit)
        button_font = ('Helvetica', 14)
        self.label_Quit.configure(font=button_font)
        self.label_Quit.pack(side='top', pady=50)
        self.frame_Quit.pack()

        #Variables for number of items and amount
        self.cookie_sum = IntVar()
        self.cookie_cost = DoubleVar()
        self.sandwhich_sum = IntVar()
        self.sandwhich_cost = DoubleVar()
        self.water_sum = IntVar()
        self.water_cost = DoubleVar()
        self.final_cost = DoubleVar()
        #Error Message
        self.frame_invalid2 = Frame(self.window)
        self.label_invalid2 = Label(self.frame_invalid2, text='', font=('Algerian', 20))
        self.frame_invalid2.pack()
        self.label_invalid2.pack()

    def hide_main_menu(self):
        """ Method for hiding Old Widgets"""
        self.label_Menu.pack_forget()
        self.frame_Menu.pack_forget()
        self.label_Shop.pack_forget()
        self.frame_Shop.pack_forget()
        self.label_Quit.pack_forget()
        self.frame_Quit.pack_forget()

    def hide_cart_menu(self):
        """Method for hiding the Cart Menu"""
        self.label_CartMenu.forget()
        self.frame_CartMenu.forget()
        self.label_Total.forget()
        self.frame_Total.forget()
        self.input_cookie.forget()
        self.label_Cookie.forget()
        self.frame_Cookie.forget()
        self.input_Sandwhich.forget()
        self.label_Sandwhich.forget()
        self.frame_Sandwhich.forget()
        self.input_Water.forget()
        self.label_Water.forget()
        self.frame_Water.forget()
        self.label_sub.forget()
        self.frame_sub.forget()


    def main_menu_to_cart_menu(self):
        """Method that switches Windows"""
        self.hide_main_menu()
        self.show_cart_menu()

    def cart_menu_to_my_cart(self):
        """Method that swithces windows by triggering two functions"""
        self.hide_cart_menu()
        self.show_my_cart()

    def show_cart_menu(self):
        """Method for displaying New Widgets starting with cart Menu"""
        self.frame_CartMenu = Frame(self.window)
        self.label_CartMenu = Label(self.frame_CartMenu, text='Cart Menu', font=('Algerian', 20))
        self.label_CartMenu.pack(pady=10)
        self.frame_CartMenu.pack()
        # TotalHeading
        self.frame_Total = Frame(self.window)
        self.label_Total = Label(self.frame_CartMenu, text='Total:', font=('Elephant', 20))
        self.label_Total.pack(padx=340, anchor="ne")
        self.frame_Total.pack(padx=340, anchor="ne")
        # CookieOption
        self.frame_Cookie = Frame(self.window)
        self.label_Cookie = Label(self.frame_Cookie, text='Cookie-$1.50', font=('Arial', 20), bd=2, relief='solid',
                                  fg='black', bg='#FFD4B8', highlightbackground='red', width=15, height=3)
        self.input_cookie = Entry(self.frame_Cookie, width=5, bd=2, relief='solid', fg='black')
        self.input_cookie.pack(side='right', padx=100)
        self.label_Cookie.pack(side="top", anchor="nw", padx=10, pady=10)
        self.frame_Cookie.pack(side="top", anchor="nw", padx=10, pady=10)
        # SandwhichOption
        self.frame_Sandwhich = Frame(self.window)
        self.label_Sandwhich = Label(self.frame_Sandwhich, text='Sandwhich-$4.00', font=('Arial', 20), bd=2,
                                     relief='solid', fg='black', bg='#D2EBD8', highlightbackground='red', width=15,
                                     height=3)
        self.input_Sandwhich = Entry(self.frame_Sandwhich, width=5, bd=2, relief='solid', fg='black')
        self.input_Sandwhich.pack(side='right', padx=100)
        self.label_Sandwhich.pack(anchor="w", padx=10, pady=10)
        self.frame_Sandwhich.pack(anchor="w", padx=10, pady=10)
        # WaterOption
        self.frame_Water = Frame(self.window)
        self.label_Water = Label(self.frame_Water, text='Water-$1.00', font=('Arial', 20), bd=2, relief='solid',
                                 fg='black', bg='#C8E8E9', highlightbackground='red', width=15, height=3)
        self.input_Water = Entry(self.frame_Water, width=5, bd=2, relief='solid', fg='black')
        self.input_Water.pack(side='right', padx=100)
        self.label_Water.pack(anchor="w", padx=10, pady=10)
        self.frame_Water.pack(anchor="w", padx=10, pady=10)
        # SubmitButton
        self.frame_sub = Frame(self.window)
        self.label_sub = Button(self.frame_sub, text="Submit", command=lambda: submit(self))
        self.label_sub.pack()
        self.frame_sub.pack()
    def show_my_cart(self):
        """Method that displays the My Cart window"""
        self.frame_mycart = Frame(self.window)
        self.label_mycart = Label(self.frame_mycart, text='My Cart', font=('Algerian', 20))
        self.label_mycart.pack(pady=10)
        self.frame_mycart.pack()
        # Total Labels
        self.frame_labels = Frame(self.window)
        self.label_amount = Label(self.frame_labels, text='#', font=('Elephant', 20))
        self.label_item = Label(self.frame_labels, text='Item', font=('Elephant', 20))
        self.label_sum = Label(self.frame_labels, text='Total', font=('Elephant', 20))
        self.frame_labels.pack()
        self.label_amount.pack(side='left', padx=95)
        self.label_item.pack(side='left', padx=95)
        self.label_sum.pack(side='left', padx=95)
        # Cookie Items
        self.frame_cookierow = Frame(self.window)
        self.cookie_item = Label(self.frame_cookierow, text='Cookie(s)', font=('Arial', 20), bd=2, relief='solid',
                                 fg='black', bg='#C8E8E9', width=15)
        self.cookie_total = Label(self.frame_cookierow, textvariable=self.cookie_cost, font=('Arial', 20), bd=2,
                                  relief='solid', fg='black', bg='#C8E8E9', width=8)
        self.cookie_amount = Label(self.frame_cookierow, textvariable=self.cookie_sum, font=('Arial', 20), bd=2,
                                   relief='solid', fg='black', bg='#C8E8E9', width=8)
        self.frame_cookierow.pack()
        self.cookie_amount.pack(padx=45, pady=50, side='left')
        self.cookie_total.pack(padx=45, pady=50, side='right')
        self.cookie_item.pack(pady=50)
        # Sandwhich Items
        self.frame_sandwhichtotal = Frame(self.window)
        self.sandwhich_item = Label(self.frame_sandwhichtotal, text='Sandwhich(es)', font=('Arial', 20), bd=2,
                                    relief='solid', fg='black', bg='#C8E8E9', width=15)
        self.sandwhich_total = Label(self.frame_sandwhichtotal, textvariable=self.sandwhich_cost, font=('Arial', 20),
                                     bd=2, relief='solid', fg='black', bg='#C8E8E9', width=8)
        self.sandwhich_amount = Label(self.frame_sandwhichtotal, textvariable=self.sandwhich_sum, font=('Arial', 20),
                                      bd=2, relief='solid', fg='black', bg='#C8E8E9', width=8)
        self.frame_sandwhichtotal.pack()
        self.sandwhich_amount.pack(padx=45, pady=50, side='left')
        self.sandwhich_total.pack(padx=45, pady=50, side='right')
        self.sandwhich_item.pack(pady=50)
        # Water Items
        self.frame_watertotal = Frame(self.window)
        self.water_item = Label(self.frame_watertotal, text='Water(s)', font=('Arial', 20), bd=2, relief='solid',
                                fg='black', bg='#C8E8E9', width=15)
        self.water_total = Label(self.frame_watertotal, textvariable=self.water_cost, font=('Arial', 20), bd=2,
                                 relief='solid', fg='black', bg='#C8E8E9', width=8)
        self.water_amount = Label(self.frame_watertotal, textvariable=self.water_sum, font=('Arial', 20), bd=2,
                                  relief='solid', fg='black', bg='#C8E8E9', width=8)
        self.frame_watertotal.pack()
        self.water_amount.pack(padx=45, pady=50, side='left')
        self.water_total.pack(padx=45, pady=50, side='right')
        self.water_item.pack(pady=50)

    def quit(self):
        """Method for triggering window to close"""
        self.window.quit()

    def item_amounts(self):
        """Method for changing the value of cookie,water, and sandwhich labels to the inputted amount"""
        cookie_value = int(self.input_cookie.get())
        self.cookie_sum.set(cookie_value)
        sandwhich_value = int(self.input_Sandwhich.get())
        self.sandwhich_sum.set(sandwhich_value)
        water_value = int(self.input_Water.get())
        self.water_sum.set(water_value)

    def calc_total(self):
        """Method that creates the label for the total cost"""
        self.frame_final = Frame(self.window)
        self.label_final = Label(self.frame_final,textvariable=self.final_cost,font=('Algerian',20))
        self.frame_final.pack()
        self.label_final.pack()

