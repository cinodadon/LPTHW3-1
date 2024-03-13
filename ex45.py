from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Death(Scene):
    quips = [
        "You died. WAAAAAAAAHHHHHHH, dead Mario!",
        "Looks like Bowser got the better of you.",
        "Your adventure ends here. Try again?",
        "Mamma Mia! You're not so good at this, are you?",
        "Game over, Mario. Game over.",
        "Go back to being a plumber."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Start(Scene):
    def enter(self):
        print(dedent("""
            Welcome to the Mushroom Kingdom! Princess Peach has
            been kidnapped by Bowser, and it's up to you, Mario,
            to rescue her. Your journey begins in the iconic
            Mushroom Kingdom.
            """))
        input("Press Enter to start your adventure...")
        return 'goombas_level'

class GoombasLevel(Scene):
    def enter(self):
        print(dedent("""
            You find yourself in a level filled with Goombas.
            They are marching towards you. How do you proceed?
            - Jump on them (jump)
            - Use a fire flower (fire flower)
            - Run away (run)
            """))
        action = input("> ")

        if action == "jump":
            print(dedent("""
                You start jumping on the Goombas, but you miss one
                and it catches you. Game over!
                """))
            return 'death'
        elif action == "fire flower":
            print(dedent("""
                You find a fire flower and use it to defeat the Goombas.
                Well done! You move on to the next level.
                """))
            return 'koopas_level'
        elif action == "run":
            print(dedent("""
                You try to run away, but the Goombas are faster.
                They catch you, and it's game over!
                """))
            return 'death'
        else:
            print("Invalid choice! Try again.")
            return 'goombas_level'

class KoopasLevel(Scene):
    def enter(self):
        print(dedent("""
            You enter a level filled with Koopa Troopas. They are
            marching back and forth. How do you proceed?
            Stomp on them (stomp)
            Use a star power (star)
            Sneak past them (sneak)
            """))
        action = input("> ")

        if action == "stomp":
            print(dedent("""
                You successfully stomp on the Koopa Troopas and
                make your way through the level.
                """))
            return 'castle_level'
        elif action == "star":
            print(dedent("""
                You grab a star power and become invincible. You
                plow through the Koopa Troopas and reach the next level.
                """))
            return 'castle_level'
        elif action == "sneak":
            print(dedent("""
                You try to sneak past the Koopa Troopas, but they
                spot you. It's game over!
                """))
            return 'death'
        else:
            print("Invalid choice! Try again.")
            return 'koopas_level'

class CastleLevel(Scene):
    def enter(self):
        print(dedent("""
            You reach Bowser's castle. It's heavily guarded.
            How do you proceed?
            Confront Bowser (confront)
            Look for a secret passage (passage)
            Retreat and come back later (retreat)
            """))
        action = input("> ")

        if action == "confront":
            print(dedent("""
                You confront Bowser, but he's too powerful. He
                captures you, and it's game over!
                """))
            return 'death'
        elif action == "passage":
            print(dedent("""
                You find a secret passage that leads you closer
                to Princess Peach. Well done! You move on to the final level.
                """))
            return 'rescue_princess'
        elif action == "retreat":
            print(dedent("""
                You decide to retreat for now. Bowser's castle is
                too dangerous at the moment. You may try again later.
                """))
            return 'death'  # 'death' is Mario loses
        else:
            print("Invalid choice! Try again.")
            return 'castle_level'

class RescuePrincess(Scene):
    def enter(self):
        print(dedent("""
            Congratulations, Mario! You've reached Princess Peach.
            Bowser is defeated, and you rescued the princess.
            You are the hero of the Mushroom Kingdom!
            """))
        exit(0)

class Map(object):
    scenes = {
        'start': Start(),
        'goombas_level': GoombasLevel(),
        'koopas_level': KoopasLevel(),
        'castle_level': CastleLevel(),
        'rescue_princess': RescuePrincess(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

# Start the game
a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
