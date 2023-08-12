from gui import *
def main():
    """Method for creating the main window that holds all widgets"""
    window = Tk()
    window.title('Shopping Cart')
    window.geometry('750x800')
    window.resizable(False,False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()