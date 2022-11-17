import tkinter as tk
from tkinter import ttk
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

        # All engravings in a list   
        self.lst = ["--Combat Engraving--","Adrenaline","All-Out Attack","Ambush Master","Awakening","Barricade","Broken Bone","Contender","Crisis Evasion","Crushing Fist","Cursed Doll","Disrespect","Divine Protection",
                    "Drops of Ether","Emergency Rescue","Enhanced Shield","Ether Predator","Expert","Explosive Expert","Fortitude","Grudge","Heavy Armor","Hit Master","Keen Blunt Weapon","Lightning Fury",
                    "Magick Stream","Mass Increase","Master Brawler","Master of Escape","Master's Tenacity","Max MP Increase","Necromacy","Precise Dagger","Preemptive Strike","Propulsion","Raid Captain",
                    "Shield Piercing","Sight Focus","Spirit Absorption","Stabilized Status","Strong Will","Super Charge","Vital Point Hit", "--Class Engravings--", "Mayhem","Berserker's Technique","Enhanced Weapon",
                    "Pistoleer","Esoteric Skill Enhancement","First Intetion","Ultimate Skill: Taijutsu","Shock Training","Barrage","Firepower Enhancement","True Courage","Desperate Salvation","Reflux", "Igniter",
                    "Esoteric Flurry","Deathblow","Time To Hunt","Peacemaker","Blessed Aura","Judgement","Demonic Impulse","Perfect Suppression","Surge","Remaining Energy","Death Strike", "Loyal Companion",
                    "Energy Overflow","Robust Spirit","Lone Knight","Combat Readiness"]

        self.lst_negative = ["Attack Power Reduction", "Attack Speed Reduction", "Defence reduction", "Movementspeed reduction"]

        # Fill top with engraving comboboxes
        dropd_nr = -1
        dropds = []
        for x in range(1, 7):
            dropd_nr += 1

            dropds.append(ttk.Combobox(master=self.frame_content, values = self.lst))
            dropds[dropd_nr].grid(row=1, column = x, padx=5, pady=5)


        dropdneg_nr = -1
        dropdneg = []
        for x in range(2, 8):
            dropdneg_nr += 1

            dropdneg.append(ttk.Combobox(master=self.frame_content, values = self.lst_negative))
            dropdneg[dropdneg_nr].grid(row=x, column = 9)


        self.label_neg = customtkinter.CTkLabel(master=self.frame_content, text = "Negative Engravings")
        self.label_neg.grid(row=1, column = 8, pady = 5, padx = 5)


        # All items listed on the left 
        self.label_amulet = customtkinter.CTkLabel(master=self.frame_content, text = "Amulet")
        self.label_amulet.grid(row= 2, column = 0, pady=5, padx=5)

        self.label_earring1 = customtkinter.CTkLabel(master=self.frame_content, text = "Earring 1")
        self.label_earring1.grid(row= 3, column = 0, pady=5, padx=5)

        self.label_earring2 = customtkinter.CTkLabel(master=self.frame_content, text = "Earring 2")
        self.label_earring2.grid(row= 4, column = 0, pady=5, padx=5)

        self.label_ring1 = customtkinter.CTkLabel(master=self.frame_content, text = "Ring 1")
        self.label_ring1.grid(row= 5, column = 0, pady=5, padx=5)

        self.label_ring2 = customtkinter.CTkLabel(master=self.frame_content, text = "Ring 2")
        self.label_ring2.grid(row= 6, column = 0, pady=5, padx=5)

        self.label_stone = customtkinter.CTkLabel(master=self.frame_content, text = "Ability Stone")
        self.label_stone.grid(row= 7, column = 0, pady=5, padx=5)

        self.label_book1 = customtkinter.CTkLabel(master=self.frame_content, text = "Engraving Book 1")
        self.label_book1.grid(row= 8, column = 0, pady=5, padx=5)

        self.label_book2 = customtkinter.CTkLabel(master=self.frame_content, text = "Engraving Book 2")
        self.label_book2.grid(row= 9, column = 0, pady=5, padx=5)


        #Test trash
        self.label_trash = customtkinter.CTkLabel(master=self.frame_content, text = "3")
        self.label_trash.grid(row=2, column = 8, pady=5, padx=5)
        self.label_trash2 = customtkinter.CTkLabel(master=self.frame_content, text = "1")
        self.label_trash2.grid(row=3, column = 8, pady=5, padx=5)
