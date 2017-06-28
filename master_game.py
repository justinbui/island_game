from sys import exit
from random import randint

#Define scene actions
class Initial(): 
    def begin(self):
        print "You open your eyes. It's hot, it's sunny, it's sandy."
        print "You hear the waves crashing on the beach."
        print "You smell the salt from the ocean and the fresh air"
        print 'It seems that you\'re alone. You only have the clothes you\'re wearing'
        print "Your mouth is dry."
        print "You see a freshwater (?) river that flows into the ocean."
        action = raw_input("Follow the river deeper into the island or further investigate the beach?\n> ")
        
        while(True):
            if 'river' in action:
                return 'koi_pond'
            elif 'beach' in action:
                return 'beach'
            else:
                action = raw_input("Which path do you take? Follow the river or investigate the beach?\n> ")
                
class Beach():
    def begin(self):
        print "You walk along the coastline and observe the coconut trees"
        print "They're just a bit too high and you're a little too lazy to climb it"
        print "You look further down the coast and you see a girl sun-bathing"
        print "Excited to see another human-being, you run up to her."
        print "As you get closer, you find out she is the most beautiful girl you've ever seen"
        print "You were running a little too fast and sprayed her with sand as you came to a stop"
        print "Mysterious Girl: You got sand all over me! What the hell?"
        print "You ignore her and extend your hand and introduce yourself."
        name = raw_input("Mysterious Girl: What's your name?\n> ")
        
        if len(name) == 0:
            print "Mysterious Girl: That's not very funny, ' '"
            return 'death'

        while(True):
            if len(name) == 0:
                print "Mysterious Girl: That's not very funny, ' '"
                return 'death'
            elif 65 <= ord(name[0]) <= 77:
                print "Mysterious Girl: I'm Michelle. I like you, '%s'. You're kind of cute." % name
                return 'village'
            elif 77 < ord(name[0]) <= 90:
                print "Mysterious Girl: Uh, no. I don't like that name. I think your name is Mr. Covered Me In Sand."
                return 'death'
            else:
                name = raw_input("Mysterious Girl: Sorry, I couldn't hear you. One more time?\n> ")

class KoiPond():
    def begin(self):
        print "You follow the stream away from the ocean and into the island."
        print "You run into a small Koi Pond, the fish are very pretty."
        print "You see an extremely shiny rock at the bottom of the pool."
        choice = raw_input("You want the rock, do you jump in clothes on or naked?\n> ")

        while(True):
            if "naked" in choice:
                print "You take off your clothes and jump in."
                print "You get the rock, but come back and your clothes are gone."
                print "You look at your naked body and the feeling of embarassment becomes overwhelming."
                return 'death'
            elif "clothes" in choice:
                print "Your clothes are dirty anyway, you jump in fully clothed."
                print "You get the rock AND you got clean. Great job!"
                print "The rock begins to glow brightly in your hands."
                print "It begins to pull in an unknown direction."
                choice = raw_input("Do you go to where the rock is pulling?\n> ")
                if "yes" in choice:
                    print "The rock leads us to an unknown cave"
                    return 'cave'
                else:
                    print "The rock flies out of your hands into the air. It stops for a second and comes crashing down on your head."
                    return 'death'
            else:
                choice = raw_input("Clothes on or naked?\n> ")

class Village():
    def begin(self):
        print "The mysterious girl grabs you by the hand and you walk deeper into the island."
        print "You begin to hear loud music and cheering."
        print "The mysterious girl presents you to the chief, you find out she is the daugher to the chief."
        response = raw_input("The chief asks you, 'Do you babapacha or bokonachos?'\n> ")
        
        if "babapacha" in response:
            print "He is one of us, take him to the shrine."
            return 'secret_shrine'
        else:
            print "He is not native to this island."
            print "He will be subject to watching Lady Gaga music videos until the end of time."
            return 'death'

class SecretShrine():
    def begin(self):
        print "You've entered the secret shrine."
        print "You see a statue of Steve Berra."
        response = raw_input("The statues speaks to you, 'How many tries does it take for you to land a kickflip?\n> ")
        
        if response == "1":
            print "I see you are a first try type of guy."
            print "Very well, take this custom-signed Berrics skateboard."
            return 'victory'
        else:
            print "One try too many, you are banished to the shadow realm."
            return 'death'

class Cave():
    def begin(self):
       print "You enter the cave, but quickly it becomes a dead end."
       print "The engravings on the wall read: 'Total combinations there are 16, 1 - 4 is your choice'"
       
       count = 0
       challenge = str(randint(1,4)) + str(randint(1,4))
       
       while(count <= 9):
           guess = raw_input("What is your guess?\n> ")
           if guess == challenge:
               print "YOU ARE CORRECT."
               print "The cave begins to shake violently."
               print "A secret door opens."
               print "You walk into the hidden room and find a skateboard."
               return 'victory'
           count += 1
           print "You have %d attempt(s) left." % ( 10 - count )
       return 'death'

class Death():
    def begin(self):
        print "The light is really bright, almost blinding. You can't see."
        print "You're dead."
        exit(1)

class Victory():
    def begin(self):
        print "You feel immense joy holding this object."
        print "It emmits a bright light, you are temporarily blinded."
        print "You smell pepperoni pizza."
        print "You hear your favorite pop song on the radio."
        print "You're dead."
        exit(1)

class Scene_Master(object):
    #Map shortcuts to scene classes in a dict
    scenes = {
        'init' : Initial(),
        'beach' : Beach(),
        'koi_pond' : KoiPond(),
        'village' : Village(),
        'secret_shrine' : SecretShrine(),
        'cave' : Cave(),
        'death' : Death(),
        'victory' : Victory()
    }
    
    def __init__(self, start_scene):
        if start_scene in Scene_Master.scenes:
            self.start_scene = start_scene
        else:
            print "Error, initial scene not found."
            exit(1)
    
    #Takes in a scene shortcut and returns corresponding location in memory
    def next_scene(self, scene_name):
        memory_location = Scene_Master.scenes.get(scene_name)
        return memory_location
    
    #Takes start_scene from program and returns location in memory 
    def intro_scene(self):
        return self.next_scene(self.start_scene)

class Game_Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    #Loop the game until the player reaches the final scene
    def play(self):
       
       #Set first and last scene using Scene_master()
        current_scene = self.scene_map.intro_scene()
        last_scene = self.scene_map.next_scene('victory') 

        while current_scene != last_scene:
            next_scene_name = current_scene.begin() #Scene starts
            print ""
            current_scene = self.scene_map.next_scene(next_scene_name) #Update scene

        current_scene.begin() #Start the victory scene when all scenes are complete
        
def main():
    scene_init = Scene_Master('init')
    game = Game_Engine(scene_init)
    game.play()

if __name__ == "__main__":
    main()

