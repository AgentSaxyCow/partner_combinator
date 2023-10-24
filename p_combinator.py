from tkinter import *
import ttkbootstrap as tb
from app import App

def main():
    root = tb.Window(themename="superhero")
    App(root)
    root.mainloop()

if __name__=="__main__":
    main()