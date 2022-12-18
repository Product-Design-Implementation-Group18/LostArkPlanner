import tkinter as tk
from tkinter import ttk
import customtkinter
import json

class SetPlanner(customtkinter.CTkFrame):

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

        # Top bar, figure out better way to put it in pages prob
        self.button_engragving = customtkinter.CTkButton(master=self.frame_content, 
                                                        text="Engraving",
                                                        width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15),
                                                        command=lambda: controller.show_frame("EngravingCalc"))
        self.button_engragving.grid(row=1, column=1, pady=5, padx=10) 
        self.button_tripod = customtkinter.CTkButton(master=self.frame_content,
                                                    text="Tripod",
                                                    width= 120, height= 32, corner_radius = 8,
                                                    text_font=("arial", 15))
        self.button_tripod.grid(row=1, column=2, pady=5, padx=10)
        self.button_tier_set = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Tier Set", 
                                                        width= 120, height= 32, corner_radius = 8,
                                                        text_font=("arial", 15), 
                                                        command=lambda: controller.show_frame("SetPlanner"))
        self.button_tier_set.grid(row=1, column=3, pady=5, padx=10) 


        # Load set data from JSON file
        self.open_sets = open('Sets.json')
        self.set_data = json.load(self.open_sets)
        # Make an indexable list from set names for functions
        self.set_data_list = list(self.set_data['sets'])

        # Dictionary for storing current equipped gear
        self.items_equipped = {
          "Weapon" : "Earth's Entropy",
          "Headpiece" : "Earth's Entropy",
          "Chestpiece" : "Earth's Entropy",
          "Pants" : "Earth's Entropy",
          "Gloves" : "Earth's Entropy",
          "Pauldrons" : "Earth's Entropy"
        }

        #Create a treeview for displaying all sets
        self.set_header = ttk.Treeview(self.frame_content, height=20, show = 'tree', selectmode='browse', style='SetPlanner.Treeview')
        self.set_header.heading('#0')
        self.set_header.column('#0', width=300, anchor='w')
        self.set_header.grid(row = 0, column= 1, pady=50, padx=10, sticky = 'nesw', rowspan=20)

        #Populate treeview with sets and set parts as children
        for index, set in enumerate(self.set_data['sets']):
          self.set_header.insert('', 'end', text = set + ' Gear', iid = index, open=False, tags=('set_main'))
          self.set_header.insert(parent = index, index='end', text= set + ' Weapon', iid = str(index) +'A', tags=('set_item'))
          self.set_header.insert(parent = index, index='end', text= set + ' Headpiece', iid = str(index) +'B', tags=('set_item'))
          self.set_header.insert(parent = index, index='end', text= set + ' Chestpiece', iid = str(index) +'C', tags=('set_item'))
          self.set_header.insert(parent = index, index='end', text= set + ' Pants', iid = str(index) +'D', tags=('set_item'))
          self.set_header.insert(parent = index, index='end', text= set + ' Gloves', iid = str(index) +'E', tags=('set_item'))
          self.set_header.insert(parent = index, index='end', text= set + ' Pauldrons', iid = str(index) +'F', tags=('set_item'))

        #Styling to make treeview look good
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure('SetPlanner.Treeview', rowheight=30, borderwidth=0, fieldbackground = '#292929')
        self.set_header.tag_configure('set_main', font=('arial', 15), background='#292929', foreground='white')
        self.set_header.tag_configure('set_item', background='#292929', foreground='white')

        #Add bindings for functions to tree items
        self.set_header.tag_bind('set_main', '<ButtonRelease>', self.switch_set_info)
        self.set_header.tag_bind('set_item', '<Double-Button>', self.switch_equipped)

        #+++++++++++++++ SET INFO COLUMN ++++++++++++++++++
        self.set_info_frame = customtkinter.CTkFrame(master = self.frame_content, width = 300, fg_color = '#292929', padx = 25)
        self.set_info_frame.grid(row = 1, column = 2, sticky = "nsew", rowspan = 20)

        self.set_info_name = customtkinter.CTkLabel(master = self.set_info_frame,
                                               text = "Click on a set to display its bonuses here",
                                               text_font = ('arial', 12),
                                               anchor = 'nw',
                                               justify = 'left',
                                               wraplength = 300)
        self.set_info_name.grid(row = 3, column = 1, sticky = "nsew", padx = 10, pady = 10)

        self.set_info_first_bonus = customtkinter.CTkLabel(master = self.set_info_frame,
                                               text = "",
                                               text_font = ('arial', 12),
                                               anchor = 'w',
                                               justify = 'left',
                                               wraplength = 300)
        self.set_info_first_bonus.grid(row = 4, column = 1, sticky = "nsew", padx = 10, pady = 10)

        self.set_info_second_bonus = customtkinter.CTkLabel(master = self.set_info_frame,
                                               text = "",
                                               text_font = ('arial', 12),
                                               anchor = 'w',
                                               justify = 'left',
                                               wraplength = 300)
        self.set_info_second_bonus.grid(row = 5, column = 1, sticky = "nsew", padx = 10, pady = 10)

        self.set_info_third_bonus = customtkinter.CTkLabel(master = self.set_info_frame,
                                               text = "",
                                               text_font = ('arial', 12),
                                               anchor = 'w',
                                               justify = 'left',
                                               wraplength = 300)
        self.set_info_third_bonus.grid(row = 6, column = 1, sticky = "nsew", padx = 10, pady = 10)

        #Placeholder icon
        self.test_icon = tk.PhotoImage(file='./Icons/scrapper.png')
        self.test_icon_smaller = self.test_icon.subsample(5,5)

        #+++++++++++++++ EQUIPPED ITEMS COLUMN ++++++++++++++++++
        self.set_equip_frame = customtkinter.CTkFrame(master = self.frame_content, width = 300, fg_color = '#292929', padx = 25)
        self.set_equip_frame.grid(row = 1, column = 3, sticky = "nsew", rowspan = 20)

        self.equipped = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "Currently equipped:",
                                               text_font = ('arial', 15),
                                               anchor = 'w')
        self.equipped.grid(row = 2, column = 1, sticky = "nsew")

        self.equipped_weapon = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = " Earth's Entropy Weapon",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',
                                               anchor = 'w')
        self.equipped_weapon.grid(row = 3, column = 1, sticky = "nsew")

        self.equipped_headpiece = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = " Earth's Entropy Headpiece",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_headpiece.grid(row = 4, column = 1, sticky = "nsew")

        self.equipped_chestpiece = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = " Earth's Entropy Chestpiece",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_chestpiece.grid(row = 5, column = 1, sticky = "nsew")

        self.equipped_pants = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = " Earth's Entropy Pants",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_pants.grid(row = 6, column = 1, sticky = "nsew")

        self.equipped_gloves = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = " Earth's Entropy Gloves",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_gloves.grid(row = 7, column = 1, sticky = "nsew")

        self.equipped_pauldrons = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = " Earth's Entropy Pauldrons",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_pauldrons.grid(row = 8, column = 1, sticky = "nsew")


        self.required_mats = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "Required materials:",
                                               text_font = ('arial', 15),                                               
                                               anchor = 'w')
        self.required_mats.grid(row = 11, column = 1, sticky = "nsew")

        self.required_bones = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_bones.grid(row = 13, column = 1, sticky = "nsew")

        self.required_wings = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_wings.grid(row = 12, column = 1, sticky = "nsew")

        self.required_fangs = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_fangs.grid(row = 14, column = 1, sticky = "nsew")

        self.required_veins = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_veins.grid(row = 15, column = 1, sticky = "nsew")

        self.required_argos = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_argos.grid(row = 16, column = 1, sticky = "nsew")

        self.required_oreha = customtkinter.CTkLabel(master = self.set_equip_frame,
                                               text = "",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_oreha.grid(row = 17, column = 1, sticky = "nsew")

        #Count gear mats on load
        self.count_gear_mats()


    
    #Changes displayed set info
    def switch_set_info(self, event):
       # print(self.set_data['sets'][int(self.set_header.focus())])
       # print(self.set_header.focus())
       # print(self.set_data_list[int(self.set_header.focus())])
        self.set_info_index = int(self.set_header.focus())
        self.set_info_chosen_name = self.set_data_list[self.set_info_index]
        self.set_info_name.configure(text = self.set_info_chosen_name)
        self.set_info_first_bonus.configure(text = self.set_data['sets'][self.set_info_chosen_name]['first_bonus'])
        self.set_info_second_bonus.configure(text = self.set_data['sets'][self.set_info_chosen_name]['second_bonus'])
        self.set_info_third_bonus.configure(text = self.set_data['sets'][self.set_info_chosen_name]['third_bonus'])


    #Changes chosen equipped set piece when function is called(when a set piece is double-clicked)
    def switch_equipped(self, event):
        self.len = len(self.set_header.focus())-1
        self.set_index = self.set_header.focus()[0:self.len]
        self.item_slot = self.set_header.focus()[self.len:]
        self.set_name = self.set_data_list[int(self.set_index)]
        if self.item_slot == 'A':
          self.equipped_weapon.configure(text = self.set_name + ' Weapon')
          self.items_equipped["Weapon"] = self.set_name
        elif self.item_slot == 'B':
          self.equipped_headpiece.configure(text = self.set_name + ' Headpiece')
          self.items_equipped["Headpiece"] = self.set_name
        elif self.item_slot == 'C':
          self.equipped_chestpiece.configure(text = self.set_name + ' Chestpiece')
          self.items_equipped["Chestpiece"] = self.set_name
        elif self.item_slot == 'D':
          self.equipped_pants.configure(text = self.set_name + ' Pants')
          self.items_equipped["Pants"] = self.set_name
        elif self.item_slot == 'E':
          self.equipped_gloves.configure(text = self.set_name + ' Gloves')
          self.items_equipped["Gloves"] = self.set_name
        elif self.item_slot == 'F':
          self.equipped_pauldrons.configure(text = self.set_name + ' Pauldrons')
          self.items_equipped["Pauldrons"] = self.set_name
        self.count_gear_mats()

    
    # Counts how many of what materials needed for equipped items
    def count_gear_mats(self):
       self.vykas_wings = 0
       self.valtan_bones = 0
       self.vykas_fang = 0
       self.valtan_vein = 0
       self.argos_blood = 0
       self.oreha_empyrean = 0
       for item in self.items_equipped:
        self.item_set = self.items_equipped[item]
        self.item_type = item
        self.item_info = self.set_data['sets'][self.item_set][self.item_type]
        if self.item_info["type"] == "Covetous Wing" :
          self.vykas_wings += self.item_info["amount"]
        if self.item_info["type"] == "Demonic Beast's Bone" :
          self.valtan_bones += self.item_info["amount"]
        if self.item_info["type"] == "Covetous Fang" :
          self.vykas_fang += self.item_info["amount"]
        if self.item_info["type"] == "Demonic Beast Vein" :
          self.valtan_vein += self.item_info["amount"]
        if self.item_info["type"] == "Argos's Blood" :
          self.argos_blood += self.item_info["amount"]
        if self.item_info["type"] == "Empyrean Dawn" :
          self.oreha_empyrean += self.item_info["amount"]
       self.show_gear_mats(self.vykas_wings, self.valtan_bones, self.vykas_fang, self.valtan_vein, self.argos_blood, self.oreha_empyrean)

    
    # Takes counted material requirements and displays them
    def show_gear_mats(self, wings, bones, fangs, veins, bloods, empyreans):
        if wings == 0:
          self.required_wings.grid_forget()
        else :
          self.required_wings.configure(text = "Covetous Wing: " + str(wings))
          self.required_wings.grid(row = 12, column = 1, sticky = "nsew")
        if bones == 0:
          self.required_bones.grid_forget()
        else :
          self.required_bones.configure(text = "Demon Beast's Bones: " + str(bones))
          self.required_bones.grid(row = 13, column = 1, sticky = "nsew")
        if fangs == 0:
          self.required_fangs.grid_forget()
        else :
          self.required_fangs.configure(text = "Covetous Fangs: " + str(fangs))
          self.required_fangs.grid(row = 14, column = 1, sticky = "nsew")
        if veins == 0:
          self.required_veins.grid_forget()
        else :
          self.required_veins.configure(text = "Demonic Beast Veins: " + str(veins))
          self.required_veins.grid(row = 15, column = 1, sticky = "nsew")
        if bloods == 0:
          self.required_argos.grid_forget()
        else :
          self.required_argos.configure(text = "Argos's Bloods: " + str(bloods))
          self.required_argos.grid(row = 16, column = 1, sticky = "nsew")
        if empyreans == 0:
          self.required_oreha.grid_forget()
        else :
          self.required_oreha.configure(text = "Empyrean Dawns: " + str(empyreans))
          self.required_oreha.grid(row = 17, column = 1, sticky = "nsew")


        


        
        

