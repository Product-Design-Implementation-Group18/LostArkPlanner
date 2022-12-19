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



        # Cleaning up padding x and y update needed  !!!!

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
            dropds[dropd_nr].grid(row=2, column = x, padx=5, pady=5)


        # Negative engraving dropdown boxes + label
        self.label_neg = customtkinter.CTkLabel(master=self.frame_content, text = "Negative Engravings")
        self.label_neg.grid(row=2, column = 8, pady = 5, padx = 5)

        dropdneg_nr = -1
        dropdneg = []
        for x in range(3, 9):
            dropdneg_nr += 1

            dropdneg.append(ttk.Combobox(master=self.frame_content, values = self.lst_negative))
            dropdneg[dropdneg_nr].grid(row=x, column = 9)


        # All items listed on the left 
        self.label_amulet = customtkinter.CTkLabel(master=self.frame_content, text = "Amulet")
        self.label_amulet.grid(row= 3, column = 0, pady=5, padx=5)

        self.label_earring1 = customtkinter.CTkLabel(master=self.frame_content, text = "Earring 1")
        self.label_earring1.grid(row= 4, column = 0, pady=5, padx=5)

        self.label_earring2 = customtkinter.CTkLabel(master=self.frame_content, text = "Earring 2")
        self.label_earring2.grid(row= 5, column = 0, pady=5, padx=5)

        self.label_ring1 = customtkinter.CTkLabel(master=self.frame_content, text = "Ring 1")
        self.label_ring1.grid(row= 6, column = 0, pady=5, padx=5)

        self.label_ring2 = customtkinter.CTkLabel(master=self.frame_content, text = "Ring 2")
        self.label_ring2.grid(row= 7, column = 0, pady=5, padx=5)

        self.label_stone = customtkinter.CTkLabel(master=self.frame_content, text = "Ability Stone")
        self.label_stone.grid(row= 8, column = 0, pady=5, padx=5)

        self.label_book1 = customtkinter.CTkLabel(master=self.frame_content, text = "Engraving Book 1")
        self.label_book1.grid(row= 9, column = 0, pady=5, padx=5)

        self.label_book2 = customtkinter.CTkLabel(master=self.frame_content, text = "Engraving Book 2")
        self.label_book2.grid(row= 10, column = 0, pady=5, padx=5)


        #Selection of engraving level
        eglvl_nr = -1
        eglvls = []
        for x in range (3,8):
            for y in range (1,7):
                eglvl_nr += 1
                
                eglvls.append(customtkinter.CTkComboBox(master=self.frame_content, values = ["0","1","2","3","4","5","6"]))
                eglvls[eglvl_nr].grid(row= x, column = y)
        #Selection of stone
        stonelvl_nr = -1
        stonelvls = []
        for y in range (1,7):
            eglvl_nr += 1
                
            stonelvls.append(customtkinter.CTkComboBox(master=self.frame_content, values = ["0","1","2","3","4","5","6","7","8","9","10"]))
            stonelvls[stonelvl_nr].grid(row= 8, column = y)

        #Selection of book
        booklvl_nr = -1
        booklvls = []
        for x in range (9,11):
            for y in range (1,7):
                booklvl_nr += 1
                
                booklvls.append(customtkinter.CTkComboBox(master=self.frame_content, values = ["0","3","6","9","12"]))
                booklvls[booklvl_nr].grid(row= x, column = y)

        #Negative selection box
        negativeg_nr = -1
        negative_eng = []
        for x in range(3, 9):
            negativeg_nr += 1

            negative_eng.append(ttk.Entry(master = self.frame_content))
            negative_eng[negativeg_nr].grid(row= x, column = 8)

        #label with the correct value
        total_nr = -1
        totals = []
        for x in range (1, 10):
            total_nr += 1
            totals.append(customtkinter.CTkLabel(master=self.frame_content, text = ''))
            totals[total_nr].grid(row= 11, column = x) 

        #Calculate sum of spesified boxes to spesific label
<<<<<<< Updated upstream
        def test():
            total = sum(int(e.get()) for e in (eglvls[0], eglvls[6],eglvls[12],eglvls[18],eglvls[24],eglvls[30],eglvls[36],eglvls[42]))
=======
        def Calculate_Eng():
            total = sum(int(e.get()) for e in (eglvls[0], eglvls[6],eglvls[12],eglvls[18],eglvls[24],booklvls[0],booklvls[6],stonelvls[0]))
>>>>>>> Stashed changes
            totals[0].configure(text= total)

            total1 = sum(int(e.get()) for e in (eglvls[1], eglvls[7],eglvls[13],eglvls[19],eglvls[25],booklvls[1],booklvls[7],stonelvls[1]))
            totals[1].configure(text = total1)

            total2 = sum(int(e.get()) for e in (eglvls[2], eglvls[8],eglvls[14],eglvls[20],eglvls[26],booklvls[2],booklvls[8],stonelvls[2]))
            totals[2].configure(text = total2)

            total3 = sum(int(e.get()) for e in (eglvls[3], eglvls[9],eglvls[15],eglvls[21],eglvls[27],booklvls[3],booklvls[9],stonelvls[3]))
            totals[3].configure(text = total3)

            total4 = sum(int(e.get()) for e in (eglvls[4], eglvls[10],eglvls[16],eglvls[22],eglvls[28],booklvls[4],booklvls[10],stonelvls[4]))
            totals[4].configure(text = total4)

            total5 = sum(int(e.get()) for e in (eglvls[5], eglvls[11],eglvls[17],eglvls[23],eglvls[29],booklvls[5],booklvls[11],stonelvls[5]))
            totals[5].configure(text = total5)

        #Calculate using the button
        self.testbut = customtkinter.CTkButton(master=self.frame_content, command = lambda: test(), text="Calculate" )
        self.testbut.grid(row= 12, column = 3)

        #Copy paste button command just swap showframe to page u want to enter
        self.testbut2 = customtkinter.CTkButton(master=self.frame_content, command=lambda: controller.show_frame("StartPage"))
        self.testbut2.grid(row= 12, column = 5)
