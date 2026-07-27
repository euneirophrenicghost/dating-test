# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Aradia")
define t = Character("Terezi")
define n = Character("Nepeta")
define f = Character("Feferi")
define k = Character("Kanaya")
define a = Character("Eridan")
define s = Character("Sollux")
define v = Character("Karkat")
define g = Character("Gamzee")
define t = Character("Tavros")
define r = Character("Vriska")
define j = Character("Jade")
define z = Character("Equius")
# Initialize affection points for love interests
default Terezi_points = 0
default Nepeta_points = 0
default Feferi_points = 0
# Define characters with custom name colors
define t = Character("Terezi", color="#1d97a2")
define n = Character("Nepeta, color="#5ba60b")
define e = Character("[Aradia, color="#A10000"]") # Dynamic name for the player
define f = Character("Feferi", color="#c50062"])


# The game starts here.

label start:
 # scene bg ("aradia_background_1.webp")
    # images directory to show it.

   # charac

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
