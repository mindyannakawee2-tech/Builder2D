# Builder2D

Builder2D is a python-based game framework inspired by pygame using ***PYSDL2***

# Installing
In the folder run install.cmd and it will install builder2d library

# Scripting
***SCRIPTING*** in Builder2D will need some knowledge in ***PYTHON***
scripting will be in classes like example

# EXAMPLES
```
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
```
-import and play music or sound
```
music = Music("calmStream.mp3")
click = SoundEffect("click.mp3")
music.play()
click.play()
```
# GameObject
```
GameObject will have three main functions:
1. entity_name = GameObject("Name", xPos, yPos)
2. add_component(componentName) This will add component such as RigidBody, BoxCollider, Animator
3. add_script(className) This will dd functionality to the entity
```
