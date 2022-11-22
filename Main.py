import tkinter as tk
import customtkinter
from StartPage import StartPage
from Engraving import EngravingCalc
from SetPlanner import SetPlanner




customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # Setting size and name of the app
        self.title("Lost Ark Planner")
        self.geometry('1300x800')

        # Container to stack frames ontop of each other
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        
        self.frames = {}
        for F in (StartPage, EngravingCalc, SetPlanner):          #Remember to add new page to this!
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location, stacking them
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SetPlanner") # Change to start page, can use other page while developing

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
