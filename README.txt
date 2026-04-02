# Builder2D
Builder2D is a python-based game framework inspired by pygame using ***PYSDL2***
And don't worry about displaying
Builder2D auto-draws all entity with shapes of picure

# Supportive
Builder2D supports some file formats
.png, .bmp, .mp3, .wav

# Installing
In the folder run install.bat(not ready yet) and it will install builder2d library

# Scripting
***SCRIPTING*** in Builder2D will need some knowledge in ***PYTHON***
scripting will be in classes like example

# EXAMPLES
# Platformer Player Movement
```
from mandaw import *

mandaw = Mandaw(title = "Window!", width = 800, height = 600, bg_color = (0, 0, 0, 255))

mandaw.loop()
python
class PlayerController(Script):

    def start(self):
        self.rb = self.game_object.get_component(Rigidbody2D)

    def update(self):
        move = 0

        if Input.key_down("a") or Input.key_down("left"):
            move -= 1
        if Input.key_down("d") or Input.key_down("right"):
            move += 1

        self.rb.velocity.x = move * 300
        
        if (Input.key_pressed("space") or Input.key_pressed("w") or Input.key_pressed("up")) and self.rb.is_grounded:
            self.rb.velocity.y = -900

player = GameObject("Player", 120, 100)
player.add_component(SpriteRenderer(45, 45, Colors.CYAN))
player.add_component(BoxCollider2D(0, 0, 45, 45))
player.add_component(Rigidbody2D(gravity_scale=1.0))
player.add_script(PlayerController())
```
# Music and SFX
```
music = Music("calmStream.mp3")
click = SoundEffect("click.mp3")
music.play()
click.play()
```
# Images
We need an entity for a picture
```
from builder2d import *

game = Game("ProjectWindowName", width=yourWidth, height=yourHeight, borderless=True)
scene = Scene("Main", background=Color(59,59,59), gravity=1600)

image = GameObject("Image", 0, 0)"
player.add_component(SpriteRenderer.from_image("image.png", 100, 100)

scene.add(image)

game.load_scene(scene)
game.run()
```

# GameObject
```
1. entity_name = GameObject("Name", xPos, yPos)
2. add_component(componentName) This will add component such as RigidBody, BoxCollider, Animator
3. add_script(className) This will dd functionality to the entity
```
# Project Set-Up
# Borderless Fullscreen
```
from builder2d import *

game = Game("ProjectWindowName", fullscreen_desktop=True)
scene = Scene("Main", background=Color(59,59,59), gravity=1600)
game.load_scene(scene)
game.run()
```
# Borderless Not Fullscreen
```
from builder2d import *

game = Game("ProjectWindowName", width=yourWidth, height=yourHeight, borderless=True)
scene = Scene("Main", background=Color(59,59,59), gravity=1600)
game.load_scene(scene)
game.run()
```
# Console Template
```
from builder2d import *

updatedTime = 0
showConsole = False

class GameConsole(Script):
    def update(self):
        global updatedTime
        updatedTime += 1
        if showConsole:
            print("Tick:", updatedTime)

consoled = GameObject("Console", 0, 0)
consoled.add_script(GameConsole())

scene.add(consoled)

game.load_scene(scene)
game.run()
print("Ended at Tick:", updatedTime)
```
