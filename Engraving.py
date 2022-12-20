import tkinter as tk
from tkinter import ttk
import customtkinter
import json

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

        self.main_menu = customtkinter.CTkButton(master=self.frame_menu,text="Home", text_font=("arial", 15), command=lambda: controller.show_frame("StartPage"))
        self.main_menu.grid(row=2, column=0, pady=10, padx=20, sticky="n")


        # Open roster data from a JSON file
        with open('Characters.json', encoding = 'utf-8') as chars:
          self.char_data = json.load(chars)
        self.char_amount = len(self.char_data['Roster'])
        self.char_names = list(self.char_data['Roster'])

        # Load current character from JSON file
        with open('Characters.json', encoding = 'utf-8') as chars:
          self.character_info = json.load(chars)
        self.active_character = self.character_info['active_character']

        # A dictionary of class icons that can be called later
        self.class_icons = {}

        self.arcana = tk.PhotoImage(file='./Icons/arcana.png').subsample(5,5)
        self.class_icons['arcana'] = self.arcana
        self.artillerist = tk.PhotoImage(file='./Icons/artillerist.png').subsample(5,5)
        self.class_icons['artillerist'] = self.artillerist
        self.artist = tk.PhotoImage(file='./Icons/artist.png').subsample(5,5)
        self.class_icons['artist'] = self.artist
        self.bard = tk.PhotoImage(file='./Icons/bard.png').subsample(5,5)
        self.class_icons['bard'] = self.bard
        self.berserker = tk.PhotoImage(file='./Icons/berserker.png').subsample(5,5)
        self.class_icons['berserker'] = self.berserker
        self.deadeye = tk.PhotoImage(file='./Icons/deadeye.png').subsample(5,5)
        self.class_icons['deadeye'] = self.deadeye
        self.deathblade = tk.PhotoImage(file='./Icons/deathblade.png').subsample(5,5)
        self.class_icons['deathblade'] = self.deathblade
        self.destroyer = tk.PhotoImage(file='./Icons/destroyer.png').subsample(5,5)
        self.class_icons['destroyer'] = self.destroyer
        self.glaivier = tk.PhotoImage(file='./Icons/glaivier.png').subsample(5,5)
        self.class_icons['glaivier'] = self.glaivier
        self.gunlancer = tk.PhotoImage(file='./Icons/gunlancer.png').subsample(5,5)
        self.class_icons['gunlancer'] = self.gunlancer
        self.gunslinger = tk.PhotoImage(file='./Icons/gunslinger.png').subsample(5,5)
        self.class_icons['gunslinger'] = self.gunslinger
        self.paladin = tk.PhotoImage(file='./Icons/paladin.png').subsample(5,5)
        self.class_icons['paladin'] = self.paladin
        self.reaper = tk.PhotoImage(file='./Icons/reaper.png').subsample(5,5)
        self.class_icons['reaper'] = self.reaper
        self.scouter = tk.PhotoImage(file='./Icons/scouter.png').subsample(5,5)
        self.class_icons['scouter'] = self.scouter
        self.scrapper = tk.PhotoImage(file='./Icons/scrapper.png').subsample(5,5)
        self.class_icons['scrapper'] = self.scrapper
        self.shadowhunter = tk.PhotoImage(file='./Icons/shadowhunter.png').subsample(5,5)
        self.class_icons['shadowhunter'] = self.shadowhunter
        self.sharpshooter = tk.PhotoImage(file='./Icons/sharpshooter.png').subsample(5,5)
        self.class_icons['sharpshooter'] = self.sharpshooter
        self.sorceress = tk.PhotoImage(file='./Icons/sorceress.png').subsample(5,5)
        self.class_icons['sorceress'] = self.sorceress
        self.soulfist = tk.PhotoImage(file='./Icons/soulfist.png').subsample(5,5)
        self.class_icons['soulfist'] = self.soulfist
        self.striker = tk.PhotoImage(file='./Icons/striker.png').subsample(5,5)
        self.class_icons['striker'] = self.striker
        self.summoner = tk.PhotoImage(file='./Icons/summoner.png').subsample(5,5)
        self.class_icons['summoner'] = self.summoner
        self.wardancer = tk.PhotoImage(file='./Icons/wardancer.png').subsample(5,5)
        self.class_icons['wardancer'] = self.wardancer

        # Loop through all roster characters and make labels for each
        for i in range(self.char_amount):
          self.char_row = i + 3
          self.image_name = self.char_data['Roster'][self.char_names[i-1]]['Class'].lower()
          self.char_label = ttk.Label(
                                      master = self.frame_menu,
                                      text = self.char_names[i-1],
                                      font=('arial', 15),
                                      image = self.class_icons[self.image_name],
                                      compound = 'left',    
                                      anchor = 'w',
                                      background='#292929',
                                      foreground='white'
                                      )
          self.char_label.grid(row = self.char_row, column = 0, pady = 20)
          self.char_label.bind('<Button-1>', self.change_character)

        self.active_character_label = customtkinter.CTkLabel(
                                                            master = self.frame_menu,
                                                            text = "Current character:",
                                                            text_font=("arial", 15)
                                                            )
        self.active_character_label.grid(row = 50, column = 0, sticky = 's', pady = (200, 0))
        self.active_character_label_name = customtkinter.CTkLabel(
                                                            master = self.frame_menu,
                                                            text = self.active_character,
                                                            text_font=("arial", 15),
                                                            image = self.class_icons[self.char_data['Roster'][self.active_character]['Class'].lower()],
                                                            compound = 'left',
                                                            anchor = 'w'
                                                            )
        self.active_character_label_name.grid(row = 51, column = 0, sticky = 's', pady = 10)


        
        
        # Top bar, figure out better way to put it in pages prob
        self.button_engragving = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Engraving", 
                                                        width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15), 
                                                        command=lambda: controller.show_frame("EngravingCalc"))
        self.button_engragving.grid(row=1, column=1, pady=10, padx=10) 
        self.button_tripod = customtkinter.CTkButton(master=self.frame_content,
                                                    text="Spellbook", width= 120, height= 32, corner_radius = 8,
                                                    text_font=("arial", 15), 
                                                    command=lambda: controller.show_frame("SkillTree"))
        self.button_tripod.grid(row=1, column=3, pady=10, padx=10)
        self.button_tier_set = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Tier Set", width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15), command=lambda: controller.show_frame("SetPlanner"))
        self.button_tier_set.grid(row=1, column=5, pady=10, padx=10) 

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
        def Calculate_Eng():
            total = sum(int(e.get()) for e in (eglvls[0], eglvls[6],eglvls[12],eglvls[18],eglvls[24],booklvls[0],booklvls[6],stonelvls[0]))
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
        self.testbut = customtkinter.CTkButton(master=self.frame_content, command = lambda: Calculate_Eng(), text="Calculate" )
        self.testbut.grid(row= 12, column = 3)


    # Function for changing character from sidebar
    def change_character(self, event):
        self.character = event.widget
        with open('Characters.json', encoding = 'utf-8') as chars:
          self.char_data = json.load(chars)
        self.char_data['active_character'] = self.character.cget("text")
        self.active_character_label_name.configure(
                                                  text = self.character.cget("text"),
                                                  image = self.class_icons[self.char_data['Roster'][self.character.cget("text")]['Class'].lower()]
                                                  )
        with open("Characters.json", 'w', encoding = 'utf-8') as chars:
          json.dump(self.char_data, chars, indent=2, ensure_ascii = False)
