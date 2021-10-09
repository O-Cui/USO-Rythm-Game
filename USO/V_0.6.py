import simplegui
import random
import time
import math

#Width and Height of the game canvas
WIDTH = 470
HEIGHT = 600


#Sound dictionary
SOUNDS = {"a":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/844797156263198730/a.mp3")
         , "shotgun":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/844262964286193694/dsshotgn_online-audio-converter.com.mp3")
         , "Vitality":simplegui.load_sound("https://cdn.discordapp.com/attachments/507330999852466238/849680354814328872/Mittsies_-_Vitality.mp3")
         }

#Image dictionary
IMG = {"BKG":simplegui.load_image("https://i.imgur.com/EQTl8Re.png")
    #Beat colors
      ,"RED":simplegui.load_image("https://i.imgur.com/kc6QwBs.png")
      ,"BLUE":simplegui.load_image("https://i.imgur.com/enb2E8J.png")
      ,"GREEN":simplegui.load_image("https://i.imgur.com/eGc1oDb.png")
      ,"YELLOW":simplegui.load_image("https://i.imgur.com/1LMkwQP.png")
      ,"PINK":simplegui.load_image("https://i.imgur.com/PWW1WuF.png")
      ,"GAMEMODES":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/850049971830128701/Title_Screen_Gamemodes.png")
      ,"CHALK_SCRIBBLE":simplegui.load_image("https://cdn.discordapp.com/attachments/507330999852466238/850053644695109632/chalk.png")
      
      }

#lengths
#44, 106, 168, 320, 292
#150 bpm, each beat is 0.4 seconds
vitality_soundtrack =  [(6.4-0.3173298835754395, 44, 67, "rest"), #Bars 1-8
          (0.4, 44, 74, 0),(0.4, 44, 70, 0),(0.4, 44, 75, 0),(0.4, 44, 71, 0), #Bar 9
          (0.4, 230, 79, 0),(0.4, 230, 87, 0),(0.4, 230, 80, 0),(0.4, 292, 81, 0), #Bar 10
        #  (0.4, 44, 74, 0),(0.4, 230, 70, 0),(0.2, 106, 74, 0),(0.2, 230, 74, 0),#(0.4, 230, 74, 0), #Bar 11
        #  (0.4, 44, 70, 0),(0.4, 230, 74, 0),(0.2, 106, 70, 0),(0.2, 230, 70, 0),#(0.4, 230, 70, 0), #Bar 12
        #  (0.4, 44, 67, 0),(0.4, 230, 67, 0),(0.2, 106, 67, 0),(0.2, 230, 67, 0),(0.4, 230, 67, 0), #Bar 13
        #  (0.4, 44, 74, 0),(0.4, 230, 70, 0),(0.4, 106, 75, 0),(0.4, 292, 71, 0), #Bar 14
          (0.4, 106, 74, 0),(0.4, 106, 75, 0),(0.4, 106, 79, 0),(0.4, 106, 80, 0), #Bar 15
          (0.4, 292, 79, 0),(0.4, 292, 75, 0),(0.4, 292, 74, 0),(0.4, 292, 72, 0), #Bar 16
          (0.2, 44, ord('F'), 0),(0.2, 230, ord('D'), 0),(0.4, 106, ord('S'), 0),(0.4, 292, ord('D'), 0),(0.4, 292, ord('A'), 0), #Bar 17 
          (0.4, 44, ord('G'), 0),(0.4, 230, ord('H'), 0),(0.4, 106, ord('G'), 0),(0.4, 292, ord('H'), 0), #Bar 18
          (0.4, 44, ord('N'), 0),(0.4, 230, ord('E'), 0),(0.4, 106, ord('W'), 0),(0.4, 292, ord('A'), 0), #Bar 19
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.4, 106, ord('I'), 0),(0.4, 292, ord('J'), 0), #Bar 20
          (0.2, 44, ord('N'), 0),(0.2, 230, ord('C'), 0),(0.4, 106, ord('N'), 0),(0.4, 292, ord('O'), 0),(0.4, 292, ord('W'), 0), #Bar 21
          (0.2, 44, ord('J'), 0),(0.2, 230, ord('K'), 0),(0.4, 106, ord('O'), 0),(0.2, 292, ord('F'), 0),(0.2, 292, ord('D'), 0),(0.4, 292, ord('W'), 0), #Bar 22
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('K'), 0),(0.4, 106, ord('L'), 0),(0.4, 292, ord('F'), 0), #Bar 23
          (0.2, 44, ord('M'), 0),(0.2, 230, ord('E'), 0),(0.2, 106, ord('G'), 0),(0.2, 292, ord('A'), 0),(0.2, 292, ord('L'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('V'), 0),(0.2, 292, ord('A'), 0), #Bar 24
          (0.2, 44, ord('N'), 0),(0.2, 230, ord('I'), 0),(0.4, 106, ord('A'), 0),(0.2, 292, ord('L'), 0),(0.2, 292, ord('S'), 0),(0.2, 292, ord('L'), 0),(0.2, 292, ord('S'), 0), #Bar 25
          (0.2, 44, ord('C'), 0),(0.2, 230, ord('N'), 0),(0.4, 106, ord('C'), 0),(0.2, 292, ord('X'), 0),(0.2, 292, ord('M'), 0),(0.2, 292, ord('X'), 0),(0.2, 292, ord('M'), 0), #Bar 26
          (0.2, 44, ord('A'), 0),(0.2, 230, ord('W'), 0),(0.4, 106, ord('E'), 0),(0.2, 292, ord('F'), 0),(0.2, 292, ord('C'), 0),(0.2, 292, ord('X'), 0),(0.2, 292, ord('Z'), 0), #Bar 27
          (0.2, 44, ord('N'), 0),(0.2, 230, ord('J'), 0),(0.4, 106, ord('K'), 0),(0.2, 292, ord('N'), 0),(0.2, 292, ord('N'), 0),(0.2, 292, ord('O'), 0),(0.4, 292, ord('I'), 0), #Bar 28
          (0.4, 44, ord('J'), 0),(0.2, 230, ord('O'), 0),(0.4, 106, ord('J'), 0),(0.4, 292, ord('N'), 0),(0.4, 292, ord('P'), 0), #Bar 29
          (0.4, 44, ord('J'), 0),(0.4, 230, ord('O'), 0),(0.2, 106, ord('J'), 0),(0.2, 292, ord('O'), 0),(0.2, 292, ord('P'), 0) #Bar 30
        
                      
                      ]

songs = {"Vitality":vitality_soundtrack}

#Sizes of images
IMG_SIZES = {IMG["BKG"]:[470,600]
            #Beats
            ,"BEAT":[100,100]
            ,IMG["GAMEMODES"]:[470, 600]
            ,IMG["CHALK_SCRIBBLE"]:[1600, 400]
            }

gamemode = "home"

#List holding all the beats
beat_list = []
#Beats per minute
tempo = 150
#How many points you have
points = 500
#Points multiplier
combo = 1
#Where the bullets can spawn on the screen (x coord)
spawn_choices = [44,106,168,230,292]
#Whether it was "Miss", "Ok", or "Great"
score_type = ""
#List of vowels (a, e, i, o, u)
VOWELS = [65, 69, 73, 79, 85]
#List of consonants
CONSONANTS = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89]
#If the last letter was a vowel or consonant
prev_letter = "vowel"

beat_value = {"q":1, 'h':2, 'e':0.5}
possible_notes = ["q", "h", "e"]
note = "q"

# different x position = different color
pos_color = {44:IMG["RED"], 106:IMG["BLUE"], 
             168:IMG["YELLOW"] ,230:IMG["PINK"], 292:IMG["GREEN"]}
# different qualities = different color
quality_color = {"Miss":"red", "Ok":"green", "Great":"yellow"}
    
#Endless mode variables
note_count = 0    
  
beat_spawned = False
  
    
#Title screen variables
selected_gm = 0

#First list is position on canvas, second position is dimensions of chalk
#0 = story mode, 1 = endless, 2 = settings
gm = {0:[[335, 230], [225, 75]]
      ,1:[[370, 320], [175, 75]]
      ,2:[[370, 405], [175, 75]]}


#Falling Beats class
class Beats():
    def __init__(self, length, position, key):
        
        #Position of the beat
        self.pos = position
        #Picking the color of the beat
        #Lane 1 = Red
        self.img = pos_color[self.pos[0]]

        #Length of the beat (y axis)
        self.length = length
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
        
        #Remove points
        points -= 150 + combo*100
        #Set the beat quality to "Miss"
        score_type = "Miss"
        #Delete the beat

        #reset combo to 1
        combo = 1
        
        if gamemode == "endless":
            #Play the bad sound effect
            SOUNDS["shotgun"].play()
            #Make all beats move slightly slower
            tempo *= 0.90
        beat_list.pop(0)
        
        
    def hit(self, type, base_points):
        global points
        global score_type
        global combo
        global tempo
        
        points += base_points*combo

        score_type = type
        combo += 1
        if gamemode == "endless":
            SOUNDS["a"].play()
            tempo *= 1 + 0.05/math.ceil(combo/5)
        beat_list.pop(0)
        
    #Beats fall and change score
    def update(self):
        global points
        global HEIGHT
        global tempo
        tempo_divided = tempo/12
        
        #Move down
        self.pos[1] += tempo_divided
  
        #Remove from list if off the screen or if you press early
        if self.pos[1]+(self.length/2) > HEIGHT + self.length - 105  and gamemode == "vitality" or self.pos[1]+(self.length/2) > HEIGHT + self.length - 95 and gamemode == "endless" or self.pressed == True and self.pos[1] + (self.length/2) < HEIGHT - 105:
            self.miss()

        #If pressed at right time, start counting how long the key has been held
        elif self.pressed == True and gamemode == "endless":
            self.held_time += tempo_divided

        elif self.pressed == True and gamemode == "vitality":
            self.hit("Great", 25)
            
        #After you let go, how long have you held the note?
        if self.pressed == False or self.pos[1]-(self.length/2) > HEIGHT - 105 and gamemode == "endless":
            #If you hold for less than 50% of the note, Miss

            if self.held_time > 0 and self.held_time < (self.length/tempo_divided)/2:
                self.miss()
            #If you held for more than 80% of the beat, Great
            elif self.held_time/tempo_divided > ((self.length/tempo_divided)/5*4):
                self.hit("Great", 25)
            #If you held for more than 50% of the beat, oOk
            elif self.held_time/tempo_divided > ((self.length/tempo_divided)/2):
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
        canvas.draw_text(str(combo), (WIDTH-125, 100), 25, "red")
            
        #Draw upcoming beats
        #First beat
        if len(beat_list) > 0:
            canvas.draw_text(chr(beat_list[0].key),
                   (WIDTH-100, HEIGHT/4*3), 70, 'RED')
        #Second beat
        if len(beat_list) > 1:
            canvas.draw_text(chr(beat_list[1].key),
                   (WIDTH-100, HEIGHT/4*3 - 122), 70, 'RED')
        #Third beat
        if len(beat_list) > 2:
            canvas.draw_text(chr(beat_list[2].key),
                   (WIDTH-100, HEIGHT/4*3 - 245), 70, 'RED')
            
 
def make_beat(len, choice, chr):
    global beat_list
    
    new_beat = Beats(len,  [choice, 0-len/2], chr)

    beat_list.append(new_beat)

#Draws and updates
def draw_game(canvas):
    global note
    global prev_letter
    global sound_counter
    #Draw points
    canvas.draw_text(str(points), (WIDTH - 120, 50),
                                    50, 'Red')
    #Draw canvas
    interface.draw(canvas)
    
    #Draw each beat and run update()
    for beat in beat_list:
        was_on_screen = beat.on_screen()
        
        beat.draw(canvas)
        beat.update()

        if beat.on_screen() and not was_on_screen:
                #Spawn beats
            #Possible lengths for the beats

            spawn_length = beat_value[note]*60*5
            
            
            if gamemode == "endless":
                if prev_letter == "vowel":
                    prev_letter = random.choice([VOWELS, CONSONANTS])
                else:
                    prev_letter = random.choice([VOWELS, VOWELS, CONSONANTS])

                #Make a new beat
                make_beat(spawn_length, random.choice(spawn_choices), random.choice(prev_letter))
                note = random.choice(possible_notes)

    
    if len(beat_list) == 0 and gamemode == "endless":
        spawn_length = beat_value[note]*60*5
        
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
    
    interface.draw(canvas)
    
    for beat in beat_list:
        beat.draw(canvas)
        beat.update()

    if beat_spawned == False and vitality_soundtrack[note_count][3] != "rest":
        
        spawn_length = vitality_soundtrack[note_count][0]*600
        make_beat(spawn_length, vitality_soundtrack[note_count][1], vitality_soundtrack[note_count][2])
        beat_spawned = True
        
    
    if (time.time() - start_time) >= vitality_soundtrack[note_count][0]:
        start_time = time.time()
        note_count += 1
        beat_spawned = False

        
#When you press a key
def key_down(key):
    global pause_screen
    global gamemode
    global tempo
    global sound_counter
    global start_time
    global selected_gm
   

    if len(beat_list) > 0:
        #If you press the right key
        if key == beat_list[0].key:
            beat_list[0].pressed = True

    if gamemode == "home":
        
        if key == 13:
            gamemode = game_dict[selected_gm][0]
            tempo = game_dict[selected_gm][1]
            
            if gamemode == "vitality":
                start_time = time.time() 
                SOUNDS["Vitality"].play()
            frame.set_draw_handler(game_dict[selected_gm][2])
            
        elif key == 38:
            selected_gm = (int(selected_gm)-1)%3
            
        elif key == 40:
            selected_gm = (int(selected_gm)+1)%3
            

#When you lift a key    
def key_up(key):

    if len(beat_list) > 0:
         #If you let go of the right key
        if key == beat_list[0].key:
            beat_list[0].pressed = False

    
def draw_home(canvas):
    
    global selected_gm

    #Draw the chalk
    canvas.draw_image(IMG["CHALK_SCRIBBLE"], 
                      [800, 200],
                      IMG_SIZES[IMG["CHALK_SCRIBBLE"]],
                      gm[selected_gm][0], 
                      gm[selected_gm][1])
    
    #Draw the background
    canvas.draw_image(IMG["GAMEMODES"], 
                      [235, 300],
                      IMG_SIZES[IMG["GAMEMODES"]],
                      [235, 300], 
                      [470, 600])
    
def mouse_handler(position):
   print(position)


game_dict = {0:["vitality", 150, draw_soundtrack]
            ,1:["endless", 50, draw_game]
            ,2:["settings", 0, draw_game]
            }
    
#Canvas
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT, 100)
#Draw interface
interface = Interface("a", HEIGHT)
#Draw Handler
frame.set_draw_handler(draw_home)
#Key press handlers
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)



frame.set_mouseclick_handler(mouse_handler)

#Run

frame.start()