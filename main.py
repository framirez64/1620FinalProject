from gui import *
def main():
    window = Tk()
    window.title('Shopping Cart')
    window.geometry('750x800')
    window.resizable(False,False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()