from ursina import Ursina
from character import Character


app = Ursina()
player = Character()
app.run()

def input(key):
    if key == 'escape':
        quit()