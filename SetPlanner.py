import tkinter as tk
from tkinter import ttk
import customtkinter

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

        
        self.sets = ["Selection", "Preordained Diligence", "Harsh Oath", "Demon Beast Strength", "Covetous Whisper",
                     "Poem of Salvation", "Dominion Fang", "Betrayal Instinct", "Swamp of Yearning", "Destructive Grasp",
                     "Charming Instinct", "Earth's Entropy", "Nightmare Flower", "Shrieking Hallucination"]

        self.set_bonuses = [
                            (
                              "2 piece" + '\n' + "Selection 2p bonus",
                              "5 piece" + '\n' + "Selection 5p bonus",
                              ""
                            ),
                            (
                              "2 piece" + '\n' + "diligence 2p",
                              "5 piece" + '\n' + "diligence 5p",
                              ""
                            ),
                            (
                              "2 piece" + '\n' + "harsh oath 2p",
                              "5 piece" + '\n' + "harsh oath 5p",
                              ""
                            ),
                            (
                              "2 piece" + '\n' + "demon beast 2p",
                              "4 piece" + '\n' + "demon beast 4p",
                              "6 piece" + '\n' + "demon beast 6p"
                            ),
                            (
                              "2 piece" + '\n' + "covetous 2p",
                              "4 piece" + '\n' + "covetous 4p",
                              "6 piece" + '\n' + "covetous 6p"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            ),
                            (
                              "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                              "4 piece" + '\n' + "Crit rate +17%",
                              "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%"
                            )]

        #Create a treeview for displaying all sets
        self.set_header = ttk.Treeview(self.frame_content, height=20, show = 'tree', selectmode='browse', style='SetPlanner.Treeview')
        self.set_header.heading('#0')
        self.set_header.column('#0', width=300, anchor='w')
        self.set_header.grid(row = 0, column= 1, pady=50, padx=10, sticky = 'nesw', rowspan=20)

        #Populate treeview with sets and set parts as children
        for index, set in enumerate(self.sets):
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
        self.set_info_name = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "Earth's Entropy",
                                               text_font = ('arial', 14),
                                               anchor = 'nw',
                                               justify = 'left')
        self.set_info_name.grid(row = 3, column = 2, sticky = "nsew", padx = 50)

        self.set_info_2p = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "2 piece" + '\n' + "Crit damage +17%" + '\n' + "Back and Head attacks modify this to 55%",
                                               text_font = ('arial', 14),
                                               anchor = 'w',
                                               justify = 'left')
        self.set_info_2p.grid(row = 4, column = 2, sticky = "nsew", padx = 50)

        self.set_info_4p = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "4 piece" + '\n' + "Crit rate +17%",
                                               text_font = ('arial', 14),
                                               anchor = 'w',
                                               justify = 'left')
        self.set_info_4p.grid(row = 5, column = 2, sticky = "nsew", padx = 50)

        self.set_info_6p = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "6 piece" + '\n' + "Damage to foes +7%" + '\n' + "Back and Head attacks modify this to 21%",
                                               text_font = ('arial', 14),
                                               anchor = 'w',
                                               justify = 'left')
        self.set_info_6p.grid(row = 6, column = 2, sticky = "nsew", padx = 50)

        #Placeholder icon
        self.test_icon = tk.PhotoImage(file='./Icons/scrapper.png')
        self.test_icon_smaller = self.test_icon.subsample(5,5)

        #+++++++++++++++ EQUIPPED ITEMS COLUMN ++++++++++++++++++
        self.equipped = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "Currently equipped:",
                                               text_font = ('arial', 15),
                                               anchor = 'w')
        self.equipped.grid(row = 2, column = 3, sticky = "nsew")

        self.equipped_weapon = customtkinter.CTkLabel(master = self.frame_content,
                                               text = " Earth's Entropy Weapon",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',
                                               anchor = 'w')
        self.equipped_weapon.grid(row = 3, column = 3, sticky = "nsew")

        self.equipped_headpiece = customtkinter.CTkLabel(master = self.frame_content,
                                               text = " Earth's Entropy Headpiece",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_headpiece.grid(row = 4, column = 3, sticky = "nsew")

        self.equipped_chestpiece = customtkinter.CTkLabel(master = self.frame_content,
                                               text = " Earth's Entropy Chestpiece",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_chestpiece.grid(row = 5, column = 3, sticky = "nsew")

        self.equipped_pants = customtkinter.CTkLabel(master = self.frame_content,
                                               text = " Earth's Entropy Pants",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_pants.grid(row = 6, column = 3, sticky = "nsew")

        self.equipped_gloves = customtkinter.CTkLabel(master = self.frame_content,
                                               text = " Earth's Entropy Gloves",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_gloves.grid(row = 7, column = 3, sticky = "nsew")

        self.equipped_pauldrons = customtkinter.CTkLabel(master = self.frame_content,
                                               text = " Earth's Entropy Pauldrons",
                                               text_font = ('arial', 13),
                                               image = self.test_icon_smaller,
                                               compound = 'left',                                               
                                               anchor = 'w')
        self.equipped_pauldrons.grid(row = 8, column = 3, sticky = "nsew")


        self.required_mats = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "Required materials:",
                                               text_font = ('arial', 15),                                               
                                               anchor = 'w')
        self.required_mats.grid(row = 11, column = 3, sticky = "nsew")

        self.required_bones = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "Valtan Bones: 35",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_bones.grid(row = 12, column = 3, sticky = "nsew")

        self.required_wings = customtkinter.CTkLabel(master = self.frame_content,
                                               text = "Vykas Wings: 40",
                                               text_font = ('arial', 13),                                               
                                               anchor = 'w')
        self.required_wings.grid(row = 13, column = 3, sticky = "nsew")

    
    #Changes displayed set info
    def switch_set_info(self, event):
        print(self.sets[int(self.set_header.focus())])
        print(self.set_header.focus())
        self.set_info_index = int(self.set_header.focus())
        self.set_info_name.configure(text = self.sets[self.set_info_index])
        self.set_info_2p.configure(text = self.set_bonuses[self.set_info_index][0])
        self.set_info_4p.configure(text = self.set_bonuses[self.set_info_index][1])
        self.set_info_6p.configure(text = self.set_bonuses[self.set_info_index][2])



    #Changes chosen equipped set piece when function is called(when a set piece is doubleclicked)
    def switch_equipped(self, event):
        self.len = len(self.set_header.focus())-1
        self.set_index = self.set_header.focus()[0:self.len]
        self.item_slot = self.set_header.focus()[self.len:]
        if self.item_slot == 'A':
          self.equipped_weapon.configure(text = self.sets[int(self.set_index)] + ' Weapon')
        elif self.item_slot == 'B':
          self.equipped_headpiece.configure(text = self.sets[int(self.set_index)] + ' Headpiece')
        elif self.item_slot == 'C':
          self.equipped_chestpiece.configure(text = self.sets[int(self.set_index)] + ' Chestpiece')
        elif self.item_slot == 'D':
          self.equipped_pants.configure(text = self.sets[int(self.set_index)] + ' Pants')
        elif self.item_slot == 'E':
          self.equipped_gloves.configure(text = self.sets[int(self.set_index)] + ' Gloves')
        elif self.item_slot == 'F':
          self.equipped_pauldrons.configure(text = self.sets[int(self.set_index)] + ' Pauldrons')

        
        

