import tkinter as tk
from tkinter import  ttk
import customtkinter
import json



class IncomeCalc(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Split to 2 columns 
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create content frame on right grid
        self.frame_content = customtkinter.CTkFrame(master=self)
        self.frame_content.grid(row=0, column=1, sticky="nswe", padx=20, pady=20) # (nswe makes it fill)

         # Create menu frame on left grid 
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
        self.button_tripod.grid(row=1, column=2, pady=10, padx=10)
        self.button_tier_set = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Tier Set", width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15), command=lambda: controller.show_frame("SetPlanner"))
        self.button_tier_set.grid(row=1, column=3, pady=10, padx=10)

    
        #Dungeon data and ilvl cutoffs
        self.dungs = ["Ancient Elveria - Demon Beast Canyon","Ancient Elveria - Necromancer's Origin","Phantom Palace - Hall of the twisted Warlord","Phantom Palace - Hildebrandt Palace","Ark of Arrogance - Road of Lament","Ark of Arrogance - Forge of Fallen Pride","Gate of Paradise - Sea of Indolence",
                    "Gate of Paradise - Tranquil Karkosa","Gate of Paradise - Alaric's Sanctuary",
                    "Oreha's Well - Aira's Oculus (Normal)","Oreha's Well - Oreha Preveza (Normal)","Oreha's Well - Aira's Oculus (Hard)","Oreha's Well - Oreha Preveza (Hard)","Argos P1","Argos P2","Argos P3","Valtan (All Stages) [Normal]","Valtan (All Stages) [Hard]","Vykas (All THREE Stages) [Normal]","Vykas (All THREE Stages) [Hard]", "Kakul-Saydon (ALL THREE Stages) [Normal]"]
        self.cutoff = ["840","840","960","960","1325","1325","1370","1370","1370","1415","1415","1415","1415","1475","1475","1475", "-", "-", "-", "-", "-"]
        self.weeklies = ["Large Gold Chest 1","Large Gold Chest 2 ","Large Gold Chest 3","Large Gold Chest 4"," Adventure Island 1"," Adventure Island 2"]

        #Titles for Main rows
        self.dungTitle = customtkinter.CTkLabel(master = self.frame_content, text = 'Dungeon/Raid')
        self.dungTitle.grid(row = 2, column=1)
        self.totalSpaceTitle = customtkinter.CTkLabel(master = self.frame_content, text = '')
        self.totalSpaceTitle.grid(row = 24, column=1)
        self.totalTitle = customtkinter.CTkLabel(master = self.frame_content, text = 'Character Total:')
        self.totalTitle.grid(row = 25, column=1)
        self.cutoffTitle = customtkinter.CTkLabel(master = self.frame_content, text = 'Maximum Ilvl')
        self.cutoffTitle.grid(row = 2, column=2)
        self.MainTitle = customtkinter.CTkLabel(master = self.frame_content, text = 'Character 1')
        self.MainTitle.grid(row = 2, column=3)
        self.Alt1Title = customtkinter.CTkLabel(master = self.frame_content, text = 'Character 2')
        self.Alt1Title.grid(row = 2, column=4)
        self.Alt2Title = customtkinter.CTkLabel(master = self.frame_content, text = 'Character 3')
        self.Alt2Title.grid(row = 2, column=5)
        self.Alt3Title = customtkinter.CTkLabel(master = self.frame_content, text = 'Character 4')
        self.Alt3Title.grid(row = 2, column=6)
        self.Alt4Title = customtkinter.CTkLabel(master = self.frame_content, text = 'Character 5')
        self.Alt4Title.grid(row = 2, column=7)
        self.Alt5Title = customtkinter.CTkLabel(master = self.frame_content, text = 'Character 6')
        self.Alt5Title.grid(row = 2, column=8)
        self.weekliesTitle = customtkinter.CTkLabel(master = self.frame_content, text = 'Weekly Reset')
        self.weekliesTitle.grid(row = 2, column=9, columnspan = 2, sticky='')
        self.weeklyTotal = customtkinter.CTkLabel(master = self.frame_content, text = 'Weekly Total:')
        self.weeklyTotal.grid(row = 9, column=9)


        # Loop over self.dungs
        for i, dung in enumerate(self.dungs):
            # create a label for each item 
            dunglabel = customtkinter.CTkLabel(self.frame_content, text=dung)
            dunglabel.grid(row=i+3, column=1)


        #Loop over self.cutoff
        for i, cut in enumerate(self.cutoff):
            # create a label for each element
            cutofflabel = customtkinter.CTkLabel(self.frame_content, text=cut)
            cutofflabel.grid(row=i+3, column=2)

        #Loop over self.weeklies
        for i, weekly in enumerate(self.weeklies):
            # create a label for each element
            weeklieslabel = customtkinter.CTkLabel(self.frame_content, text=weekly)
            weeklieslabel.grid(row=i+3, column=9)
        

        # Create a list of values for the checkboxes
        values = [80,80,80,80,100,100,100,100,100,600,900,900,1200,800,900,1000,3300,4500,3300,4500,4500]
        weeklyValues = [1000,1000,1000,1000,720,720]

        # Create a variable to store the sum
        mainSum = tk.IntVar()
        mainSum.set(0)

        def update_sum():
            # Set to 0
            mainSum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(21):
                if mainTotal[i].get():
                    mainSum.set(mainSum.get() + values[i])

        mainTotal = []
        for i in range(21):
            total = tk.IntVar()
            mainTotal.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum).grid(row=i+3, column=3)

        self.totalMain = customtkinter.CTkLabel(self.frame_content, textvariable=mainSum)
        self.totalMain.grid(row = 25, column = 3)


        # Create a variable to store the sum for Alt 1/Character 2
        alt1Sum = tk.IntVar()
        alt1Sum.set(0)

        def update_sum2():
            # Set to 0
            alt1Sum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(21):
                if alt1Total[i].get():
                    alt1Sum.set(alt1Sum.get() + values[i])

        alt1Total = []
        for i in range(21):
            total = tk.IntVar()
            alt1Total.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum2).grid(row=i+3, column=4)

        self.totalAlt1 = customtkinter.CTkLabel(self.frame_content, textvariable=alt1Sum)
        self.totalAlt1.grid(row = 25, column = 4)


        # Create a variable to store the sum for Alt 2/Character 3
        alt2Sum = tk.IntVar()
        alt2Sum.set(0)

        def update_sum3():
            # Set to 0
            alt2Sum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(21):
                if alt2Total[i].get():
                    alt2Sum.set(alt2Sum.get() + values[i])

        alt2Total = []
        for i in range(21):
            total = tk.IntVar()
            alt2Total.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum3).grid(row=i+3, column=5)

        self.totalAlt2 = customtkinter.CTkLabel(self.frame_content, textvariable=alt2Sum)
        self.totalAlt2.grid(row = 25, column = 5)

      # Create a variable to store the sum for Alt 3/Character 4
        alt3Sum = tk.IntVar()
        alt3Sum.set(0)

        def update_sum4():
            # Set to 0
            alt3Sum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(21):
                if alt3Total[i].get():
                    alt3Sum.set(alt3Sum.get() + values[i])

        alt3Total = []
        for i in range(21):
            total = tk.IntVar()
            alt3Total.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum4).grid(row=i+3, column=6)

        self.totalAlt3 = customtkinter.CTkLabel(self.frame_content, textvariable=alt3Sum)
        self.totalAlt3.grid(row = 25, column = 6)


        # Create a variable to store the sum for Alt 4/Character 5
        alt4Sum = tk.IntVar()
        alt4Sum.set(0)

        def update_sum5():
            # Set to 0
            alt4Sum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(21):
                if alt4Total[i].get():
                    alt4Sum.set(alt4Sum.get() + values[i])

        alt4Total = []
        for i in range(21):
            total = tk.IntVar()
            alt4Total.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum5).grid(row=i+3, column=7)

        self.totalAlt4 = customtkinter.CTkLabel(self.frame_content, textvariable=alt4Sum)
        self.totalAlt4.grid(row = 25, column = 7)

        # Create a variable to store the sum for Alt 4/Character 5
        alt5Sum = tk.IntVar()
        alt5Sum.set(0)

        def update_sum6():
            # Set to 0
            alt5Sum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(21):
                if alt5Total[i].get():
                    alt5Sum.set(alt5Sum.get() + values[i])

        alt5Total = []
        for i in range(21):
            total = tk.IntVar()
            alt5Total.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum6).grid(row=i+3, column=8)

        self.totalAlt5 = customtkinter.CTkLabel(self.frame_content, textvariable=alt5Sum)
        self.totalAlt5.grid(row = 25, column = 8)



        # Create a variable to store the sum for Weekly Activities
        weeklySum = tk.IntVar()
        weeklySum.set(0)

        def update_sum6():
            # Set to 0
            weeklySum.set(0)
            #Loop over all created checkboxes, adding value of checked ones
            for i in range(6):
                if weeklyTotal[i].get():
                    weeklySum.set(weeklySum.get() + weeklyValues[i])

        weeklyTotal = []
        for i in range(6):
            total = tk.IntVar()
            weeklyTotal.append(total)
            customtkinter.CTkCheckBox(self.frame_content, text='', variable=total, command=update_sum6).grid(row=i+3, column=10)

        self.weeklyTotal = customtkinter.CTkLabel(self.frame_content, textvariable= weeklySum)
        self.weeklyTotal.grid(row = 9, column = 10)

        totalGold = tk.IntVar()
        totalGold.set(0)

        def totalAll():
            totalGold.set(mainSum.get() + alt1Sum.get() + alt2Sum.get() + alt3Sum.get() + alt4Sum.get() + alt5Sum.get() + weeklySum.get()) 

        self.totalOverall = customtkinter.CTkLabel(self.frame_content, textvariable = totalGold)
        self.totalOverall.grid(row = 27, column = 5)

        self.Total = customtkinter.CTkButton(self.frame_content, text = 'Calculate Total', command=lambda: totalAll())
        self.Total.grid(row = 26, column = 5, padx = 10, pady = 10)
    

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
