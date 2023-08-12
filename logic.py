





def submit(self):
    # Calculations for total cost of items
    self.label_invalid2.config(text="")
    try:
        cookie = int(self.input_cookie.get())
        sandwhich = int(self.input_Sandwhich.get())
        water = int(self.input_Water.get())

        if not isinstance(cookie, (int)):
            raise TypeError()
        if not isinstance(sandwhich, (int)):
            raise TypeError()
        if not isinstance(water, (int)):
            raise TypeError()

        if isinstance(cookie, int) and cookie < 0:
            raise ValueError()
        if isinstance(sandwhich, int) and sandwhich < 0:
            raise ValueError()
        if isinstance(water, int) and water < 0:
            raise ValueError()

        total_cookies = cookie * 1.50
        total_sandwhich = sandwhich * 4.00
        total_water = water * 1.00
        final_total = total_cookies + total_sandwhich + total_water

        self.cookie_cost.set("${:.2f}".format(total_cookies))
        self.sandwhich_cost.set("${:.2f}".format(total_sandwhich))
        self.water_cost.set("${:.2f}".format(total_water))
        self.final_cost.set("Total:${:.2f}".format(final_total))
        # Switches Windows from Cart Menu to My Cart
        self.cart_menu_to_my_cart()
        # Calculates the cost of items
        self.calc_total()
        # Displays the Item Numbers
        self.item_amounts()
    except ValueError as ve:  # negatives
        self.label_invalid2.config(text="Please enter positive values")
    except TypeError as te:  # non-integers
        self.label_invalid2.config(text="Please enter whole numbers")
