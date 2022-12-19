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

        self.main_menu = customtkinter.CTkButton(master=self.frame_menu,text="Home", text_font=("arial", 15), command=lambda: controller.show_frame("StartPage"))
        self.main_menu.grid(row=2, column=0, pady=10, padx=20, sticky="n")

        

        #+++++++++++++  Content frame  +++++++++++++++++

        self.welcome = customtkinter.CTkLabel(master=self.frame_content,text="Welcome", text_font=("arial", 20))
        self.welcome.grid(row=2, column = 2, pady=10, padx=10, columnspan = 4, sticky='')

        self.spacerL = customtkinter.CTkLabel(master=self.frame_content,text = '')
        self.spacerL.grid(row = 1, column = 1, pady=10, padx=100, rowspan = 5)
        
        self.spacerTop = customtkinter.CTkLabel(master=self.frame_content, text ='')
        self.spacerTop.grid(row=3, column = 2, pady = 40, padx = 10)

        self.button_engragving = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Engraving",
                                                        width= 160, height= 54, corner_radius = 8,
                                                        text_font=("arial", 15), command=lambda: controller.show_frame("EngravingCalc"))
        self.button_engragving.grid(row=5, column=2, pady=20, padx=20) 
        self.button_tripod = customtkinter.CTkButton(master=self.frame_content,
                                                    text="Spellbook",
                                                    width= 160, height= 54,
                                                    corner_radius = 8,
                                                    text_font=("arial", 15), command=lambda: controller.show_frame("SkillTree"))
        self.button_tripod.grid(row=5, column=3, pady=20, padx=20)
        self.button_tier_set = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Tier Set",
                                                        width= 160, height= 54, corner_radius = 8,
                                                        text_font=("arial", 15), command=lambda: controller.show_frame("SetPlanner"))
        self.button_tier_set.grid(row=5, column=4, pady=20, padx=20) 
        self.button_IncomeCalc = customtkinter.CTkButton(master=self.frame_content,
                                                        text="Weekly Income",
                                                        width= 160, height= 54, corner_radius = 8,
                                                        text_font=("arial", 15), command=lambda: controller.show_frame("IncomeCalc"))
        self.button_IncomeCalc.grid(row=5, column=5, pady=20, padx=20) 

        self.engravingInfo = customtkinter.CTkLabel(master=self.frame_content,
                                                    text = 'In this page you can calculate your Engravings. By setting value you get from the gear and your books. You can also track the negative Engravings from each piece on the right to help on not getting negative Engravings',
                                                    wraplength=200)
        self.engravingInfo.grid(row= 6, column = 2, sticky = 'n', padx=20, pady=20)
        self.tripodInfo = customtkinter.CTkLabel(master=self.frame_content,
                                                text = 'This page you can read what your skills and the tripods for your skills do. You can also simulate adding Tripods to your skills and make different variations of it.', wraplength=200)
        self.tripodInfo.grid(row= 6, column = 3, sticky = 'n', padx=20, pady=20)
        self.tier_setInfo = customtkinter.CTkLabel(master=self.frame_content,
                                                text = 'Blaa blaa Blaa blaa Blaa blaa Blaa blaa Blaa blaa Blaa blaa Blaa blaa Blaa blaa Blaa blaa Blaa blaa', wraplength=200)
        self.tier_setInfo.grid(row= 6, column = 4, sticky = 'n', padx=20, pady=20)
        self.goldInc = customtkinter.CTkLabel(master=self.frame_content,
                                                text = 'Calculate how much gold income you have weekly. You can calculate how much each character can earn weekly from dungeons/raids. You also have option to add Weekly gold income to the total.', wraplength=200)
        self.goldInc.grid(row= 6, column = 5, sticky = 'n', padx=20, pady=20)


