import tkinter as tk
import customtkinter

class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

         # Create menu frame on left grid
        self.frame_menu = customtkinter.CTkFrame(master=self,width=200,corner_radius=0) # Need to set as 0, default has some radius
        self.frame_menu.grid(row=0, column=0, sticky="nswe") # (nswe makes it fill)

        # Create content frame on right grid
        self.frame_content = customtkinter.CTkFrame(master=self)
        self.frame_content.grid(row=0, column=1, sticky="nswe", padx=20, pady=20) # (nswe makes it fill)

         #+++++++++++++  Menu frame  +++++++++++++++++
        self.label_roster = customtkinter.CTkLabel(master=self.frame_menu, 
                                                    text="Roster",
                                                    text_font=("arial-bold", 23))  # font name and size in px
        self.label_roster.grid(row=1, column=0, pady=10, padx=10)
        
        self.menu_roster = customtkinter.CTkOptionMenu(master=self.frame_menu,
                                                        values=["Gunlancer", "Gigachad", "Scrapper"], # Need to make command to swap to spesific char + get values from string etc.. and be able to make character
                                                        text_font=("arial", 15)) 
        self.menu_roster.grid(row=2, column=0, pady=10, padx=20, sticky="n")

        self.button_gemcutter = customtkinter.CTkButton(master=self.frame_menu,text="Gem Cutter", text_font=("arial", 15))
        self.button_gemcutter.grid(row=3, column=0, pady=15, padx=20)  

        #  #  Made it disabled until we start / know we have enough time # #
        self.button_gemcutter.configure(state="disabled")

        #+++++++++++++  Content frame  +++++++++++++++++
        self.button_engragving = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Engraving",
                                                        width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15))
        self.button_engragving.grid(row=1, column=1, pady=10, padx=10) 
        self.button_tripod = customtkinter.CTkButton(master=self.frame_content,
                                                    text="Tripod",
                                                    width= 120, height= 32,
                                                    corner_radius = 8,
                                                    text_font=("arial", 15))
        self.button_tripod.grid(row=1, column=2, pady=10, padx=10)
        self.button_tier_set = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Tier Set",
                                                        width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15))
        self.button_tier_set.grid(row=1, column=3, pady=10, padx=10) 




"""
class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        label = customtkinter.CTkLabel(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = customtkinter.CTkButton(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = customtkinter.CTkButton(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

"""