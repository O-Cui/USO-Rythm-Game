import simplegui
import random
import time
import math

#Width and Height of the game canvas
WIDTH = 470
HEIGHT = 600

#Sound dictionary
SOUNDS = {"a":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/844797156263198730/a.mp3")
         ,"o":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/854053841775755274/o.mp3")
         ,"i":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/854055482174865418/i_-.mp3") 
         ,"u":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/854055829107638312/u.mp3")
         ,"e":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/854056086071541771/e.mp3") 
         ,"shotgun":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/844262964286193694/dsshotgn_online-audio-converter.com.mp3")
         ,"Vitality":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/849680354814328872/Mittsies_-_Vitality.mp3")
         ,"Slow_Vitality":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/855115982758740028/Slow_Mittsies_-_Vitality.mp3")
         ,"P_P":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/854954840462196766/PADORU_PADORU.mp3")
         ,"Slow_P_P":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/855114367002214400/Slow_PADORU_PADORU.mp3")
          
          
         ,"3":simplegui.load_sound("https://vgmsite.com/soundtracks/friday-night-funkin-gamerip/hkvkjrfooo/5.%20SFX%20-%20Intro%20-%203.mp3")
         ,"2":simplegui.load_sound("https://vgmsite.com/soundtracks/friday-night-funkin-gamerip/spfdctjwky/6.%20SFX%20-%20Intro%20-%202.mp3")
         ,"1":simplegui.load_sound("https://vgmsite.com/soundtracks/friday-night-funkin-gamerip/cwaulganir/7.%20SFX%20-%20Intro%20-%201.mp3")
         ,"Go!":simplegui.load_sound("https://vgmsite.com/soundtracks/friday-night-funkin-gamerip/fvpqwnwcvo/8.%20SFX%20-%20Intro%20-%20Go%21.mp3")
         }

#Image dictionary
IMG = {"BKG":simplegui.load_image("https://i.imgur.com/EQTl8Re.png")
    #Beat colors
      ,"RED":simplegui.load_image("https://i.imgur.com/kc6QwBs.png")
      ,"BLUE":simplegui.load_image("https://i.imgur.com/enb2E8J.png")
      ,"GREEN":simplegui.load_image("https://i.imgur.com/eGc1oDb.png")
      ,"YELLOW":simplegui.load_image("https://i.imgur.com/1LMkwQP.png")
      ,"PINK":simplegui.load_image("https://i.imgur.com/PWW1WuF.png")
      ,"PURPLE":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854753669727911956/Purple.png")
      ,"GAMEMODES":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854775350844325888/Title_Screen_Gamemodes.png")
      ,"GAMEMODES_BABY":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854775826976735282/Title_Screen_Gamemodes_Baby.png")
      ,"SMALL_WHITE":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/852605164346015754/White_Background_Small.png")
      ,"BIG_WHITE":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/852605148374499349/White_Background_Large.png")
      ,"V_WHITE":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854048133382144020/Vitality_White_Background.png")
      ,"P_P_White":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854048231809482752/Padoru_Padoru_White_Background.png")
      ,"H_A_D_White":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854048331315937320/H_A_D_White_Background.png")
      ,"GAMER_White":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854777432221155338/White_Background_GAMER.png")
      ,"baby_White":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854778697231761448/baby_White_Background.png")
      ,"C_ANIMATION":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/851503544975491172/ezgif.com-gif-maker.png")
      ,"CONTROLS":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854772699875377202/Controls.png")
      ,"SELECT":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854050386075975730/Song_Selection.png")
      ,"GAME_OVER":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/854765593270026250/Game_Over.png")
      }

letter = {90:"A",
          80:"B",
          70:"C",
          60:"D",
          50:"F"
         }

C_COL = 5
C_ROW = 13
#Sizes of images
IMG_SIZES = {IMG["BKG"]:[470,600]
            #Beats
            ,"BEAT":[100,100]
            ,IMG["GAMEMODES"]:[470, 600]
            ,IMG["GAMEMODES_BABY"]:[470, 600]
            ,IMG["SMALL_WHITE"]:[175, 75]
            ,IMG["BIG_WHITE"]:[235, 75]
            ,IMG["V_WHITE"]:[330, 75]
            ,IMG["H_A_D_White"]:[320, 75]
            ,IMG["P_P_White"]:[280, 75]
            ,IMG["GAMER_White"]:[380, 75]
            ,IMG["baby_White"]:[270, 75]
            ,IMG["C_ANIMATION"]:[[1615/C_COL/2, 3874/C_ROW/2],[1615/C_COL, 3874/C_ROW]]
            ,IMG["CONTROLS"]:[470, 600]
            ,IMG["SELECT"]:[470, 600]
            ,IMG["GAME_OVER"]:[470, 600]
            }
offset = 0.26
#lengths
#44, 106, 168, 320, 292
#150 bpm, each beat is 0.4 seconds

vitality_soundtrack =  [(6.4-offset, 44, 67, "rest"), #Bars 1-8
          (0.4, 44, 74, 0),(0.4, 44, 70, 0),(0.4, 44, 75, 0),(0.4, 44, 71, 0), #Bar 9
          (0.4, 230, 79, 0),(0.4, 230, 87, 0),(0.4, 230, 80, 0),(0.4, 292, 81, 0), #Bar 10
          (0.4, 106, 74, 0),(0.4, 106, 75, 0),(0.4, 106, 79, 0),(0.4, 106, 80, 0), #Bar 15
          (0.4, 292, 79, 0),(0.4, 292, 75, 0),(0.4, 292, 74, 0),(0.4, 292, 72, 0), #Bar 16
          (0.2, 44, ord('F'), 0),(0.2, 230, ord('D'), 0),(0.4, 106, ord('S'), 0),(0.4, 292, ord('D'), 0),(0.4, 292, ord('A'), 0), #Bar 17 
          (0.4, 44, ord('G'), 0),(0.4, 230, ord('H'), 0),(0.4, 106, ord('G'), 0),(0.4, 292, ord('H'), 0), #Bar 18
          (0.4, 44, ord('N'), 0),(0.4, 230, ord('E'), 0),(0.4, 106, ord('W'), 0),(0.4, 292, ord('A'), 0), #Bar 19
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.4, 106, ord('I'), 0),(0.4, 292, ord('J'), 0), #Bar 20
          (0.2, 44, ord('N'), 0),(0.2, 230, ord('C'), 0),(0.4, 106, ord('N'), 0),(0.4, 292, ord('C'), 0),(0.4, 292, ord('W'), 0), #Bar 21             
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('K'), 0),(0.4, 106, ord('O'), 0),(0.2, 292, ord('F'), 0),(0.2, 292, ord('D'), 0),(0.4, 292, ord('W'), 0), #Bar 22
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('F'), 0),(0.4, 106, ord('K'), 0),(0.4, 292, ord('D'), 0), #Bar 23
          (0.2, 44, ord('F'), 0),(0.2, 230, ord('D'), 0),(0.2, 106, ord('S'), 0),(0.2, 292, ord('A'), 0),(0.2, 292, ord('S'), 0),(0.2, 292, ord('D'), 0),(0.2, 292, ord('F'), 0),(0.2, 292, ord('A'), 0), #Bar 24
          (0.2, 44, ord('N'), 0),(0.2, 230, ord('K'), 0),(0.4, 106, ord('N'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('J'), 0),(0.2, 292, ord('I'), 0),(0.2, 292, ord('J'), 0), #Bar 25
          (0.2, 44, ord('C'), 0),(0.2, 230, ord('N'), 0),(0.4, 106, ord('C'), 0),(0.2, 292, ord('X'), 0),(0.2, 292, ord('M'), 0),(0.2, 292, ord('X'), 0),(0.2, 292, ord('M'), 0), #Bar 26
          (0.2, 44, ord('A'), 0),(0.2, 230, ord('W'), 0),(0.4, 106, ord('E'), 0),(0.2, 292, ord('F'), 0),(0.2, 292, ord('C'), 0),(0.2, 292, ord('X'), 0),(0.2, 292, ord('Z'), 0), #Bar 27
          (0.2, 44, ord('N'), 0),(0.2, 230, ord('J'), 0),(0.4, 106, ord('K'), 0),(0.2, 292, ord('N'), 0),(0.2, 292, ord('N'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('I'), 0), #Bar 28
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 29
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 30
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 31
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 32                 
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 33
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 34
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 35
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 36              
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 37
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 38
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 39
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 40   
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 41
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 42
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 43
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0), #Bar 44              
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 45         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 46           
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 47         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 48         
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 49         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 50
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.2, 292, ord('P'), 0), #Bar 51         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 52
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 53        
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 54          
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 55         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 56       
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 56         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 57
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.2, 292, ord('P'), 0), #Bar 51         
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.2, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0),(0.2, 292, ord('P'), 0), #Bar 52             
          (1.6, 44, 74, "rest"), (0.4, 44, 74, "end")
                       ]                                 
                 
#44, 106, 168, 230, 292
#95 bpm
p_p_soundtrack = [(180/190-0.5, 44, 67, "rest"),
                 (60/190, 44, ord('J'), 0), (60/190, 44, ord('J'), 0), (60/190, 230, ord('O'), 0), (60/190, 292, ord('I'), 0), (60/190, 168, ord('J'), 0), (180/190, 106, ord('J'), 0),
                 (60/190, 44, ord('F'), 0), (60/190, 44, ord('F'), 0), (60/190, 230, ord('W'), 0), (60/190, 292, ord('E'), 0), (60/190, 168, ord('F'), 0), (180/190, 106, ord('F'), 0),
                 (60/190, 44, ord('J'), 0), (60/190, 44, ord('J'), 0), (60/190, 230, ord('L'), 0), (60/190, 292, ord('K'), 0), (60/190, 168, ord('J'), 0), (180/190, 106, ord('L'), 0),
                 (60/190, 44, ord('F'), 0), (60/190, 44, ord('F'), 0), (60/190, 230, ord('S'), 0), (60/190, 292, ord('D'), 0), (60/190, 168, ord('F'), 0), (180/190, 106, ord('S'), 0),
                 (60/190, 44, ord('N'), 0), (60/190, 44, ord('N'), 0), (60/190, 230, ord('O'), 0), (60/190, 292, ord('I'), 0), (60/190, 168, ord('N'), 0), (180/190, 106, ord('N'), 0),
                 (60/190, 44, ord('C'), 0), (60/190, 44, ord('C'), 0), (60/190, 230, ord('W'), 0), (60/190, 292, ord('E'), 0), (60/190, 168, ord('C'), 0), (180/190, 106, ord('C'), 0),
                 (60/190, 44, ord('J'), 0), (60/190, 44, ord('J'), 0), (60/190, 230, ord('L'), 0), (60/190, 292, ord('K'), 0), (60/190, 168, ord('J'), 0), (180/190, 106, ord('L'), 0),
                 (60/190, 44, ord('F'), 0), (60/190, 44, ord('F'), 0), (60/190, 230, ord('S'), 0), (60/190, 292, ord('D'), 0), (60/190, 168, ord('F'), 0), (180/190, 106, ord('S'), 0),
                 (60/190, 44, ord('J'), 0), (60/190, 44, ord('J'), 0), (60/190, 230, ord('O'), 0), (60/190, 292, ord('I'), 0), (60/190, 168, ord('J'), 0), (180/190, 106, ord('J'), 0),
                 (60/190, 44, ord('F'), 0), (60/190, 44, ord('F'), 0), (60/190, 230, ord('W'), 0), (60/190, 292, ord('E'), 0), (60/190, 168, ord('F'), 0), (180/190, 106, ord('F'), 0),
                 (60/190, 44, ord('J'), 0), (60/190, 44, ord('J'), 0), (60/190, 230, ord('L'), 0), (60/190, 292, ord('K'), 0), (60/190, 168, ord('J'), 0), (180/190, 106, ord('L'), 0),
                 (60/190, 44, ord('F'), 0), (60/190, 44, ord('F'), 0), (60/190, 230, ord('S'), 0), (60/190, 292, ord('D'), 0), (60/190, 168, ord('F'), 0), (180/190, 106, ord('S'), 0),
                 (180/190, 44, 67, "rest"), (180/190, 44, 67, "end")
                 ]

h_a_d_soundtrack = []
    
    #"Vitality"       "P_P"           "H_A_D"
songs = {0:[vitality_soundtrack, 150]
        ,1:[p_p_soundtrack, 190]
        ,2:[h_a_d_soundtrack]}

song_names = {0:['', "Vitality", "Slow_Vitality", 0.26]
             ,1:['', "P_P", "Slow_P_P",0.5]
             ,2:"h_a_d"}
songtrack = 0

gamemode = "controls"

#Beats per minute
tempo = 150

#Where the bullets can spawn on the screen (x coord)
spawn_choices = [44,106,168,230,292]
#Whether it was "Miss", "Ok", or "Great"

#List of vowels (a, e, i, o, u)
VOWELS = [65, 69, 73, 79, 85]
#List of consonants
CONSONANTS = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89]

beat_value = {"q":1, 'h':2,}
possible_notes = ["q", "h", "q"]
note = "q"

# different qualities = different color
quality_color = {"Miss":"red", "Ok":"green", "Great":"yellow"}
    
#Endless mode variables

  
beat_spawned = False
deafen_time = 0  
deafen = False   
#Title screen variables
selected_gm = 0

home_select = False
#First list is position on canvas, second position is dimensions of chalk
#0 = story mode, 1 = endless, 2 = controls
gm = {0:[[340, 210], IMG["BIG_WHITE"]]
      ,1:[[370, 308], IMG["SMALL_WHITE"]]
      ,2:[[370, 410], IMG["SMALL_WHITE"]]
      ,3:[[280, 500], IMG["GAMER_White"]]}

gm_select = {0:[[235, 240], IMG["V_WHITE"]]
      ,1:[[200, 360], IMG["P_P_White"]] 
      ,2:[[230, 470], IMG["H_A_D_White"]]}
      
# different x position = different color and sound
pos_value = {44:[IMG["RED"],"a"], 
             106:[IMG["BLUE"],"o"], 
             168:[IMG["YELLOW"],"i"],
             230:[IMG["PINK"], "u"], 
             292:[IMG["GREEN"], "e"]}

#How many mistakes you can make -1 (so mistake limit = -9 means 10 mistakes)
mistake_limit = -100000

prev_endless = True

difficulty_multiplier = 1

#Variables to reset when replaying a game
def new_game():
    global beat_list
    global start_time
    global points
    global combo
    global score_type
    global prev_letter
    global countdown
    global note_count
    global highest_combo
    #List holding all the beats
    beat_list = []
    start_time = 0
    #How many points you have
    points = 500
    #Points multiplier
    combo = 0
    score_type = ""
    #If the last letter was a vowel or consonant
    prev_letter = "vowel"
    #3-2-1-Go! counter
    countdown = True
    note_count = 0    
    highest_combo = 0
new_game()

#Falling Beats class
class Beats():
    def __init__(self, length, position, key):
        
        #Position of the beat
        self.pos = position
        
        #Length of the beat (y axis)
        self.length = length
        
        #Picking the color of the beat
        if self.length == 300 or gamemode == "soundtrack":
            self.img = pos_value[self.pos[0]][0]
        else:
            self.img = IMG["PURPLE"]
        #Width of the beat (x axis)
        self.width = 62
        
        #Whether the beat's key is pressed or not
        self.pressed = False
        #The key you must press for the beat
        self.key = key
        
        #How long the beat has been held
        self.held_time = 0

        
        #Draw beats falling
    def draw(self, canvas):
        width, height = IMG_SIZES["BEAT"]
        canvas.draw_image(self.img, [width/2, height/2],
                          [width, height], self.pos, 
                          [self.width, self.length])
        if self.pressed == True:
            canvas.draw_polygon([(self.pos[0]+self.width/2, self.pos[1]+self.length/2)
                                 ,(self.pos[0]+self.width/2, self.pos[1]-self.length/2)
                                 ,(self.pos[0]-self.width/2, self.pos[1]-self.length/2)
                                 ,(self.pos[0]-self.width/2, self.pos[1]+self.length/2)], 
                                10, "white")
        #What to do when a beat is missed
    def miss(self):
        global points
        global tempo
        global combo
        global score_type
        global deafen_time
        global deafen
        global gamemode
        global difficulty_multiplier
        
        #Remove points
        if combo >= 0:
            if points*0.1 > abs(combo)*50+50:
                points = (points * 9)//10
            else:
                points -= abs(combo)*50+50
        else:
            points -= 50
        #Set the beat quality to "Miss"
        score_type = "Miss"
        
        #reset combo to 1
        if combo > 0:
            combo = 0
        elif combo == mistake_limit:
            SOUNDS[song_names[songtrack][difficulty_multiplier]].rewind()
            gamemode = "game_over"
            frame.set_draw_handler(draw_game_over)
        else:
            combo -= 1
        
        if gamemode == "endless":
            #Play the bad sound effect
            SOUNDS["shotgun"].play()
            #Make all beats move slightly slower
            tempo *= 0.95
            
        deafen = True
        deafen_time = time.time()
        beat_list.pop(0)
        

    def hit(self, type, base_points):
        global points
        global score_type
        global combo
        global tempo
        global highest_combo
        global difficulty_multiplier
        
        if combo >= highest_combo:
            highest_combo += 1
        print(highest_combo)
        if combo >= 0:
            points += base_points*combo
        else:
            points += base_points
            
        score_type = type
        
        if combo >= 0:
            combo += 1
        else: 
            combo = 1
            
        if gamemode == "endless":
            SOUNDS[pos_value[self.pos[0]][1]].play()
            tempo *= 1 + 0.05/math.ceil(combo/5)
        elif gamemode == "soundtrack":
            SOUNDS[song_names[songtrack][difficulty_multiplier]].set_volume(1)
            
        beat_list.pop(0)
        
    #Beats fall and change score
    def update(self):
        global points
        global HEIGHT
        global tempo
        global difficulty_multiplier
        tempo_divided = tempo/(10*difficulty_multiplier)
        
        #Move down
        self.pos[1] += tempo_divided
        
        #if self.pos[1] +(self.length/2) >= HEIGHT -105:
       #     print(time.time()-start_time)
       #     beat_list.pop(0)
        #Remove from list if off the screen or if you press early
        if self.pos[1]+(self.length/2) > HEIGHT + self.length - 105  and gamemode == "soundtrack" or self.pos[1]+(self.length/2) > HEIGHT + self.length - 95 and gamemode == "endless" or self.pressed == True and self.pos[1] + (self.length/2) < HEIGHT - 105:
            #print("missed")
            self.miss()

        elif self.pressed == True and gamemode == "soundtrack" or (self.length == 300 and self.pressed == True):
            self.hit("Great", 25)
            
        #If pressed at right time, start counting how long the key has been held
        elif self.pressed == True and gamemode == "endless":
            self.held_time += tempo_divided
            
            
        #After you let go, how long have you held the note?
        if self.pressed == False or self.pos[1]-(self.length/2) > HEIGHT - 105 and gamemode == "endless":
            #If you hold for less than 40% of the note, Miss

            if self.held_time > 0 and self.held_time < (self.length/tempo_divided)*2/5:
                self.miss()
            #If you held for more than 70% of the beat, Great
            elif self.held_time/tempo_divided > ((self.length/tempo_divided)*7/10):
                self.hit("Great", 25)
            #If you held for more than 40% of the beat, oOk
            elif self.held_time/tempo_divided > ((self.length/tempo_divided)*2/5):
                self.hit("Ok", 10)

            
    def on_screen(self):
        return self.pos[1]-self.length/2 > 0
                    
#Class for drawing anything but beats
class Interface():
    def __init__(self, key, width):
        #What letter is supposed to be pressed 
        self.key = key
        self.width = width
        
    #Draw side menu
    def draw(self, canvas):

        global score_type
        color = "blue"
        
        canvas.draw_text(str(points), (WIDTH - 120, 50),
                                    50, 'white')
        #The size of the background
        #Draw the background
        canvas.draw_image(IMG["BKG"], 
                          [235, 300],
                          IMG_SIZES[IMG["BKG"]],
                          [235, 300], 
                          [470, 600])

        #Draw the quality at the bottom right
        if score_type != "":
            canvas.draw_text(score_type, (WIDTH-125, HEIGHT-50), 50, quality_color[score_type])
           
        #Draw the combo under points
        if combo < 25:
            canvas.draw_text(str(combo)+"x", (WIDTH-125, 100), 25, "white")
        else:
            canvas.draw_text(str(combo)+"x", (WIDTH-125, 100), 25, "yellow")
        #Draw upcoming beats
        #First beat
        if len(beat_list) > 0:
            canvas.draw_text(chr(beat_list[0].key),
                   (WIDTH-100, HEIGHT/4*3), 70, 'white')

        #Second beat
        if len(beat_list) > 1:
            canvas.draw_text(chr(beat_list[1].key),
                   (WIDTH-100, HEIGHT/4*3 - 122), 70, 'white')
        #Third beat
        if len(beat_list) > 2:
            canvas.draw_text(chr(beat_list[2].key),
                   (WIDTH-100, HEIGHT/4*3 - 245), 70, 'white')        
            
class S_Spectrum():
    def __init__(self, image, pos):
        self.img = image
        self.pos = pos
        self.time = 0
        
    def draw(self, canvas):
        center1 = IMG_SIZES[self.img][0]
        width, height = IMG_SIZES[self.img][1]
        col = self.time%C_COL
        row = self.time//C_COL
        title_center = [center1[0] + col*width,
                        center1[1] + row*height]
        
        canvas.draw_image(self.img, 
                          title_center,
                          IMG_SIZES[self.img][1],
                          self.pos,
                          [200,200])
    
    def update(self):
        self.time += 1
        self.time = self.time%56
                                                     
def make_beat(len, choice, chr):
    global beat_list
    new_beat = Beats(len,  [choice, 0-len/2], chr)
    beat_list.append(new_beat)
            
def break_countdown(canvas):
    global start_time
    global countdown
    global songtrack
    global sound_names
    global difficulty_multiplier
    
    if countdown == True:
        if time.time() - start_time <= 0.5:
            SOUNDS["3"].play()
            canvas.draw_text('3', (WIDTH/3, HEIGHT/2),
                                    75, 'Blue') 
            
        elif time.time() - start_time <= 1:
            SOUNDS["2"].play()
            canvas.draw_text('2', (WIDTH/3, HEIGHT/2),
                                        75, 'Red')  
            
        elif time.time() - start_time <= 1.5:
            SOUNDS["1"].play()
            canvas.draw_text('1', (WIDTH/3, HEIGHT/2),
                                        75, 'Green')   
            
        elif time.time() - start_time <= 2:
            SOUNDS["Go!"].play()
            canvas.draw_text("Go!", (WIDTH/3 - 25, HEIGHT/2),
                                        75, 'Yellow')  
        else:
            countdown = False
            start_time = time.time()
            if gamemode == "soundtrack":
                SOUNDS[song_names[songtrack][difficulty_multiplier]].play()
                
#Draws and updates
def draw_game(canvas):
    global note
    global prev_letter
    global sound_counter
    #Draw points

    #Draw canvas
    interface.draw(canvas)
    break_countdown(canvas)
    if countdown == False:
        #Draw each beat and run update()
        for beat in beat_list:
            was_on_screen = beat.on_screen()

            beat.draw(canvas)
            beat.update()

            if beat.on_screen() and not was_on_screen:
                #Spawn beats
                #Possible lengths for the beats

                spawn_length = int(beat_value[note]*300)

                
                if gamemode == "endless":
                    if prev_letter == "vowel":
                        prev_letter = random.choice([VOWELS, CONSONANTS])
                    else:
                        prev_letter = random.choice([VOWELS, VOWELS, CONSONANTS])

                    #Make a new beat
                    make_beat(spawn_length, random.choice(spawn_choices), random.choice(prev_letter))
                    note = random.choice(possible_notes)


        if len(beat_list) == 0 and gamemode == "endless":

            spawn_length = int(beat_value[note]*300)

            if prev_letter == "vowel":
                prev_letter = random.choice([VOWELS, CONSONANTS])
            else:
                prev_letter = random.choice([VOWELS, VOWELS, CONSONANTS])


            make_beat(spawn_length, random.choice(spawn_choices), random.choice(prev_letter))
            note = random.choice(possible_notes)
        

        #Need to put this after beats are created so it covers them up
        #Cover the top part of the background
        canvas.draw_polygon([[0, 0], [WIDTH, 0], [WIDTH, 13], 
                             [0, 13]], 1, "Black", "Black" )
        #Cover the bottom part of the background
        canvas.draw_polygon([[0, HEIGHT], [WIDTH, HEIGHT],
                             [WIDTH, HEIGHT-13], 
                             [0, HEIGHT-13]], 1, "Black", "Black" )
    
def draw_soundtrack(canvas):
    global start_time
    global note_count
    global beat_list
    global beat_spawned
    global difficulty_multiplier

    
    deafen_sound(song_names[songtrack][difficulty_multiplier])
    interface.draw(canvas)
    break_countdown(canvas)
    for beat in beat_list:
        beat.draw(canvas)
        beat.update()
        
    if countdown == False and note_count < len(songs[songtrack][0]):
        
        if songs[songtrack][0][note_count][3] == "end":
            song_win()
            
        if beat_spawned == False and songs[songtrack][0][note_count][3] != "rest":

            spawn_length = songs[songtrack][0][note_count][0]*650

                  
            make_beat(spawn_length, songs[songtrack][0][note_count][1], songs[songtrack][0][note_count][2])
            beat_spawned = True

        if (time.time() - start_time) >= songs[songtrack][0][note_count][0]*difficulty_multiplier:
            start_time = time.time() - (time.time() - start_time - songs[songtrack][0][note_count][0]*difficulty_multiplier)
            note_count += 1
            beat_spawned = False
            
    #Need to put this after beats are created so it covers them up
        #Cover the top part of the background
    canvas.draw_polygon([[0, 0], [WIDTH, 0], [WIDTH, 13], 
                         [0, 13]], 1, "Black", "Black" )
    #Cover the bottom part of the background
    canvas.draw_polygon([[0, HEIGHT], [WIDTH, HEIGHT],
                         [WIDTH, HEIGHT-13], 
                         [0, HEIGHT-13]], 1, "Black", "Black" )

    
def draw_win(canvas):
    global difficulty_multiplier
    #Draw the background
    canvas.draw_image(IMG["GAME_OVER"], 
                          [235, 300],
                          IMG_SIZES[IMG["GAME_OVER"]],
                          [235, 300], 
                          [470, 600])

    canvas.draw_text(str(song_names[songtrack][difficulty_multiplier]), (270-(frame.get_canvas_textwidth(str(song_names[songtrack][difficulty_multiplier]), 50, 'serif')/2), 210), 50, "red")
    
    canvas.draw_text(str(points), (233-(frame.get_canvas_textwidth(str(points), 50, "serif")/2), 350), 50, "red")
    canvas.draw_text(str(highest_combo), (233-(frame.get_canvas_textwidth(str(highest_combo), 50, "serif")/2), 485), 50, "red")
     
    
    
#When you press a key
def key_down(key):
    global pause_screen
    global gamemode
    global tempo
    global sound_counter
    global start_time
    global selected_gm
    global songtrack
    global home_select
    global prev_endless
    global difficulty_multiplier
    
    if len(beat_list) > 0:
        #If you press the right key
        if key == beat_list[0].key:
            beat_list[0].pressed = True

    if gamemode == "home":
     
        if not home_select: #Gamemode home page
            if key == 13 and selected_gm == 0:

                home_select = True

            elif key == 13 and selected_gm == 3:
                if difficulty_multiplier == 1:
                    difficulty_multiplier = 2
                    gm[3] = [[330, 500], IMG["baby_White"]]
                else:
                    difficulty_multiplier = 1
                    gm[3] = [[280, 500], IMG["GAMER_White"]]
                
                
            elif key == 13:
                gamemode = game_dict[selected_gm][0]
                tempo = game_dict[selected_gm][1]
                start_time = time.time()
                prev_endless = True
                frame.set_draw_handler(game_dict[selected_gm][2])

            elif key == 38:
                selected_gm = (int(selected_gm)-1)%4

            elif key == 40:
                selected_gm = (int(selected_gm)+1)%4
                
        else: #selecting song page
            if key == 27 and home_select:
                selected_gm = 0
                home_select = False
                
            elif key == 38:
                songtrack = (int(songtrack)-1)%3

            elif key == 40:
                songtrack = (int(songtrack)+1)%3
                
            elif key == 13 and home_select:
                gamemode = "soundtrack"
                prev_endless = False

                if difficulty_multiplier == 2:
                    offset = song_names[songtrack][3]/difficulty_multiplier
                else:
                    offset = song_names[songtrack][3]
                tempo = songs[songtrack][1]
                print(tempo)  
                start_time = time.time()
                frame.set_draw_handler(draw_soundtrack)
              
    elif gamemode == "controls" or gamemode == "game_over" and key == 27:
        gamemode = "home"
        home_select = False
        new_game()
        frame.set_draw_handler(draw_home)

#When you lift a key    
def key_up(key):
    if len(beat_list) > 0:
         #If you let go of the right key
        if key == beat_list[0].key:
            beat_list[0].pressed = False

def draw_home(canvas):
    
    global selected_gm

    if not home_select:
        circle_spec.draw(canvas)
        circle_spec.update()
        
        
        
        #Draw the outline
        canvas.draw_image(gm[selected_gm][1], 
                          [IMG_SIZES[gm[selected_gm][1]][0]/2, IMG_SIZES[gm[selected_gm][1]][1]/2],
                          IMG_SIZES[gm[selected_gm][1]],
                          gm[selected_gm][0], 
                          IMG_SIZES[gm[selected_gm][1]])
        
        if difficulty_multiplier == 1:
            #Draw the background
            canvas.draw_image(IMG["GAMEMODES"], 
                              [235, 300],
                              IMG_SIZES[IMG["GAMEMODES"]],
                              [235, 300], 
                              [470, 600])
        else:
            canvas.draw_image(IMG["GAMEMODES_BABY"], 
                              [235, 300],
                              IMG_SIZES[IMG["GAMEMODES_BABY"]],
                              [235, 300], 
                              [470, 600])
    else:
        
        #Draw the white outline
        canvas.draw_image(gm_select[songtrack][1], 
                          [IMG_SIZES[gm_select[songtrack][1]][0]/2, IMG_SIZES[gm_select[songtrack][1]][1]/2],
                          IMG_SIZES[gm_select[songtrack][1]],
                          gm_select[songtrack][0], 
                          IMG_SIZES[gm_select[songtrack][1]])
        
        #draw the words
        canvas.draw_image(IMG["SELECT"], 
                          [235, 300],
                          IMG_SIZES[IMG["SELECT"]],
                          [235, 300], 
                          [470, 600])
        
def draw_controls(canvas):

        canvas.draw_image(IMG["CONTROLS"], 
                          [470/2, 600/2],
                          IMG_SIZES[IMG["CONTROLS"]],
                          [WIDTH/2, HEIGHT/2], 
                          [470, 600])

def deafen_sound(song):
    global deafen_time
    global deafen
    global song_names
    global songtrack
    global difficulty_multiplier
    if deafen == True:

        SOUNDS[song_names[songtrack][difficulty_multiplier]].set_volume(0.2)
        if time.time()-deafen_time > 0.2:
            SOUNDS[song].set_volume(1)
            deafen = False      
   
def draw_game_over(canvas):
    global difficulty_multiplier
    #Draw the background
    canvas.draw_image(IMG["GAME_OVER"], 
                          [235, 300],
                          IMG_SIZES[IMG["GAME_OVER"]],
                          [235, 300], 
                          [470, 600])
    
    if prev_endless:
        canvas.draw_text("Endless", (270-(frame.get_canvas_textwidth(("endless"), 50, "serif")/2), 210), 50, "red")
    else:
        canvas.draw_text(str(song_names[songtrack][difficulty_multiplier]), (270-(frame.get_canvas_textwidth(str(song_names[songtrack][difficulty_multiplier]), 50, 'serif')/2), 210), 50, "red")
    
    canvas.draw_text(str(points), (233-(frame.get_canvas_textwidth(str(points), 50, "serif")/2), 350), 50, "red")
    canvas.draw_text(str(highest_combo), (233-(frame.get_canvas_textwidth(str(highest_combo), 50, "serif")/2), 485), 50, "red")
    
game_dict = {0:["soundtrack", 150, draw_soundtrack]
            ,1:["endless", 50, draw_game]
            ,2:["controls", 0, draw_controls]
            }

def mouse_handler(position):
    print(position)
    
circle_spec = S_Spectrum(IMG["C_ANIMATION"], [125, 365]) 
#Canvas
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT, 100)
#Draw interface
interface = Interface("a", HEIGHT)
#Draw Handler
frame.set_draw_handler(draw_controls)
#Key press handlers
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(mouse_handler)

#Run
frame.start()