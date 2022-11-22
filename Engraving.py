import tkinter as tk
import customtkinter

class EngravingCalc(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Split to 2 columns 
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create content frame on right grid
        self.frame_content = customtkinter.CTkFrame(master=self)
        self.frame_content.grid(row=0, column=1, sticky="nswe", padx=20, pady=20) # (nswe makes it fill)

         # Create menu frame on left grid               /             Need to figure out smarter way for this!!!!!
        self.frame_menu = customtkinter.CTkFrame(master=self,width=200,corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nswe") # (nswe makes it fill)

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


        self.label_empty = customtkinter.CTkLabel(master=self.frame_content, text = "")
        self.label_empty.grid(row= 1, column = 0, pady=5, padx=10)
        #   
        self.lst = ["Adrenaline","All-Out Attack","Ambush Master","Awakening","Barricade","Broken Bone","Contender","Crisis Evasion","Crushing Fist","Cursed Doll","Disrespect","Divine Protection",
                    "Drops of Ether","Emergency Rescue","Enhanced Shield","Ether Predator","Expert","Explosive Expert","Fortitude","Grudge","Heavy Armor","Hit Master","Keen Blunt Weapon","Lightning Fury",
                    "Magick Stream","Mass Increase","Master Brawler","Master of Escape","Master's Tenacity","Max MP Increase","Necromacy","Precise Dagger","Preemptive Strike","Propulsion","Raid Captain",
                    "Shield Piercing","Sight Focus","Spirit Absorption","Stabilized Status","Strong Will","Super Charge","Vital Point Hit"]

        # Fill top with engraving comboboxes
        dd_nr = -1
        dds = []
        for x in range(1, 7):
            dd_nr += 1

            dds.append(customtkinter.CTkComboBox(master=self.frame_content, values = self.lst))
            dds[dd_nr].grid(row=1, column = x, padx=5, pady=5)

