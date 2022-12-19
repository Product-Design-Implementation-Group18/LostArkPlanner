import tkinter as tk
from tkinter import ttk
import customtkinter
import json


class SkillTree(customtkinter.CTkFrame):

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

        # All the classes of Lost Ark
        self.classes = ["Berserker","Destroyer","Gunlancer","Paladin","Arcanist","Bard","Sorceress","Wardancer","Scrapper",
                    "Soulfist","Glavier","Striker","Reaper","Deathblade","Shadowhunter","Sharpshooter","Deadeye","Artillerist","Machinist","Gunslinger"]


        #Create a treeview for displaying all skills
        self.skill_tree = ttk.Treeview(self.frame_content, height=20, show = 'tree', selectmode='browse', style='Skill.Treeview')
        self.skill_tree.heading('#0')
        self.skill_tree.column('#0', width=350, anchor='w')
        self.skill_tree.grid(row = 2, column= 2, pady=10, padx=10, sticky = 'nesw', rowspan=20)

        #Create a treeview for displaying all classes
        self.class_tree = ttk.Treeview(self.frame_content, height=20, show = 'tree', selectmode='browse', style='Skill.Treeview')
        self.class_tree.heading('#0')
        self.class_tree.column('#0', width=200, anchor='w')
        self.class_tree.grid(row = 2, column= 1, pady=10, padx=10, sticky = 'nesw', rowspan=20)
        
        
        #Create a treeview for displaying all tripods
        self.tripod_tree = ttk.Treeview(self.frame_content, height=10, show = 'tree', selectmode='browse', style='Skill.Treeview')
        self.tripod_tree.heading('#0')
        self.tripod_tree.column('#0', width=200, anchor='w')
        self.tripod_tree.grid(row = 3, column= 6, pady=10, padx=20, sticky = 'nesw', rowspan=7)


        #Populate class tree with data
        for index, skill in enumerate(self.classes):
          self.class_tree.insert('', 'end', text = skill , iid = index, open=False, tags=('class_main'))

        #Styling to make treeview look good
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure('Skill.Treeview', rowheight=25, borderwidth=0, fieldbackground = '#292929')
        self.skill_tree.tag_configure('skill_main', font=('arial', 15), background='#292929', foreground='white')
        self.class_tree.tag_configure('class_main', font=('arial', 15), background='#292929', foreground='white')
        self.tripod_tree.tag_configure('tripod_main', font=('arial', 15), background='#292929', foreground='white')



        #Label for skill desc & name
        self.skillName = customtkinter.CTkLabel(master = self.frame_content,
                                                text = '',
                                                width = 20, 
                                                height = 20, 
                                                justify = 'center', 
                                                text_font = ('arial', 15))
        self.skillName.grid(row = 2, column = 4, padx=10, columnspan = 2)
        self.skillDesc = customtkinter.CTkLabel(master = self.frame_content, 
                                                text = '',
                                                width=10,
                                                text_font = ('arial', 11),
                                                wraplength=300,
                                                justify = 'left')
        self.skillDesc.grid(row=3, column = 4, padx=10, columnspan = 2)
        
        #test
        tripod_nr = -1
        tripods = []
        for x in range(4,7):
            for y in range (4,6):
                tripod_nr += 1
                tripods.append(customtkinter.CTkLabel(master = self.frame_content,
                                                     text = '',
                                                     width = 20, height = 20,
                                                     justify = 'left'))
                tripods[tripod_nr].grid(row= x, column = y)
                

        #Tripod info, desc and name
        self.tripodsLabel = customtkinter.CTkLabel(master = self.frame_content,
                                                   text = '', 
                                                   justify = 'center', 
                                                   text_font = ('arial', 15))
        self.tripodsLabel.grid(row = 2, column = 6, padx=10)
        self.tripodName = customtkinter.CTkLabel(master = self.frame_content,
                                                text = '',
                                                width = 20,  
                                                justify = 'center', 
                                                text_font = ('arial', 15))
        self.tripodName.grid(row = 10, column = 6, padx=10)
        self.tripodTier = customtkinter.CTkLabel(master = self.frame_content,
                                                text = '',
                                                width = 20,  
                                                justify = 'center', 
                                                text_font = ('arial', 15))
        self.tripodTier.grid(row = 11, column = 6, padx=10)
        self.tripodDesc = customtkinter.CTkLabel(master = self.frame_content, 
                                                text = '',
                                                width=10,
                                                text_font = ('arial', 11),
                                                wraplength=300,
                                                justify = 'left')
        self.tripodDesc.grid(row=12, column = 6, padx=10)



        #Open skilldata and call 'data' where needed to use
        with open('skilldata.json', 'r') as f:
                data = json.load(f)

        def selectClass(a):
            #Focus on class tree and get details on what was clicked
            curItem = self.class_tree.focus()
            details = self.class_tree.item(curItem)
            class_name = details.get("text")

            # Clear previous data (Not best practice)
            self.skill_tree.delete(*self.skill_tree.get_children())
            self.tripod_tree.delete(*self.tripod_tree.get_children())
            self.tripodName.configure(text='')
            self.tripodDesc.configure(text='')
            self.tripodsLabel.configure(text='')
            self.skillName.configure(text='')
            self.skillDesc.configure(text='')
            self.tripodTier.configure(text= '')
            tripods[0].configure(text='')
            tripods[1].configure(text='')
            tripods[2].configure(text='')
            tripods[3].configure(text='')
            tripods[4].configure(text='')
            tripods[5].configure(text='')


            # Simplified data fetching.
            for value in data:
                if class_name == value:
                    for skills in data[value]:
                        self.skill_tree.insert('', 'end', text = skills['skill'], open=False, tags=('skill_main'))



        def selectSkill(a):
            #Focus on skill tree and get details on what was clicked
            curItem = self.skill_tree.focus()
            details = self.skill_tree.item(curItem)
            skill_name = details.get("text")

            #Focus on class tree and get details on what was clicked
            curClass = self.class_tree.focus()
            classDetails = self.class_tree.item(curClass)
            class_name = classDetails.get("text")

            #Clean previously written data 
            self.tripod_tree.delete(*self.tripod_tree.get_children())
            self.tripodName.configure(text='')
            self.tripodDesc.configure(text='')
            self.tripodTier.configure(text='')
            tripods[1].configure(text= '' )
            tripods[3].configure(text= '' )
            tripods[5].configure(text= '' )
            self.tripodTier.configure(text= '')
                  
            self.buttontest = customtkinter.CTkButton(master=self.frame_content, text = "Add tripod", command = lambda: addTripod())
            self.buttontest.grid(row=10, column = 10)
            
            for row in data[class_name]:
                #Find correct skill and write its name and description.
                if skill_name == row['skill']:
                    self.skillName.configure(text = row['skill'])
                    self.skillDesc.configure(text = row['desc'])
                    tripods[0].configure(text= 'Tier 1' )
                    tripods[2].configure(text= 'Tier 2' )
                    tripods[4].configure(text= 'Tier 3' )
                    self.tripodsLabel.configure(text = "Tripods")
                    for tripod in row['tripods']:
                        self.tripod_tree.insert('', 'end', text = tripod['name'], open=False, tags=('tripod_main'))


        def selectTripod(a):
            #Focus on skill tree and get details on what was clicked
            curItem = self.skill_tree.focus()
            details = self.skill_tree.item(curItem)
            skill_name = details.get("text")

            #Focus on class tree and get details on what was clicked
            curClass = self.class_tree.focus()
            classDetails = self.class_tree.item(curClass)
            class_name = classDetails.get("text")

            #Focus on tripod tree and get details on what was clicked
            curTripd = self.tripod_tree.focus()
            tripodDetails = self.tripod_tree.item(curTripd)
            tripod_name = tripodDetails.get("text")
            
            
            for row in data[class_name]:
                #Find correct skill and write its name and description.
                if skill_name == row['skill']:
                    for tripod in row['tripods']:
                        if tripod_name == tripod['name']:
                            self.tripodName.configure(text=tripod['name'])
                            self.tripodDesc.configure(text=tripod['desc'])
                            self.tripodTier.configure(text= 'Tier ' + tripod['tripodlevel'])


        def addTripod():
            #Focus on skill tree and get details on what was clicked
            curItem = self.skill_tree.focus()
            details = self.skill_tree.item(curItem)
            skill_name = details.get("text")

            #Focus on class tree and get details on what was clicked
            curClass = self.class_tree.focus()
            classDetails = self.class_tree.item(curClass)
            class_name = classDetails.get("text")

            #Focus on tripod tree and get details on what was clicked
            curTripd = self.tripod_tree.focus()
            tripodDetails = self.tripod_tree.item(curTripd)
            tripod_name = tripodDetails.get("text")
            
            
            for row in data[class_name]:
                #Find correct skill and write its name and description.
                if skill_name == row['skill']:
                    for tripod in row['tripods']:
                        if tripod_name == tripod['name']:
                            if tripod['tripodlevel'] == "1":
                                tripods[1].configure(text= tripod['name'] )
                            if tripod['tripodlevel'] == "2":
                                tripods[3].configure(text= tripod['name'] )
                            if tripod['tripodlevel'] == "3":
                                tripods[5].configure(text= tripod['name'] )


        #Releasing left click calls select class function to get data what was clicked
        self.class_tree.bind('<ButtonRelease-1>', selectClass)
        self.skill_tree.bind('<ButtonRelease-1>', selectSkill)
        self.tripod_tree.bind('<ButtonRelease-1>', selectTripod)
