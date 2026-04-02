# Builder2D

**Builder2D** is a Python-based 2D game framework inspired by **pygame**, built with **PYSDL2**.

Builder2D is designed to make 2D game creation simple and fast.  
It automatically draws entities using shapes or images, so you can focus on gameplay and scripting.

---

## Features

- Python-based 2D game framework
- Built with **PYSDL2**
- Automatic entity rendering
- Shape rendering support
- Image rendering support
- Simple component system
- Python class-based scripting
- Music and sound effect support
- Borderless window support
- Borderless fullscreen support

---

## Supported File Formats

Builder2D currently supports:

- `.png`
- `.bmp`
- `.mp3`
- `.wav`

---

## Installation

Inside the project folder, run:

```bat
install.bat
```

This will install the `builder2d` library.

> **Note:** `install.bat` is not ready yet.

---

## Import Builder2D

```python
from builder2d import *
```

---

## Basic Project Setup

### Borderless Fullscreen

```python
from builder2d import *

game = Game("ProjectWindowName", fullscreen_desktop=True)
scene = Scene("Main", background=Color(59, 59, 59), gravity=1600)

game.load_scene(scene)
game.run()
```

### Borderless Windowed Mode

```python
from builder2d import *

game = Game("ProjectWindowName", width=1280, height=720, borderless=True)
scene = Scene("Main", background=Color(59, 59, 59), gravity=1600)

game.load_scene(scene)
game.run()
```

---

## Core Objects

Builder2D uses these main objects:

- **Game** → creates the window and runs the game loop
- **Scene** → stores objects and world settings
- **GameObject** → represents an entity in the scene
- **Components** → add rendering, physics, collision, animation, etc.
- **Scripts** → add custom logic using Python classes

---

## GameObject

A `GameObject` is an entity in the scene.

### Create a GameObject

```python
entity = GameObject("Name", xPos, yPos)
```

### Add a Component

```python
entity.add_component(componentName)
```

Examples of components:

- `SpriteRenderer`
- `Rigidbody2D`
- `BoxCollider2D`
- `Animator`

### Add a Script

```python
entity.add_script(MyScript())
```

---

## Scripting

Builder2D scripting uses Python classes.

Scripts should inherit from `Script`.

### Script Structure

```python
class MyScript(Script):

    def start(self):
        pass

    def update(self):
        pass
```

### Common Script Functions

- `start()` → called when the object starts
- `update()` → called every frame

Use `start()` for setup.  
Use `update()` for movement, input, and real-time behavior.

---

## Script Example: Player Movement

```python
from builder2d import *

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


game = Game("Platformer Demo", width=1280, height=720, borderless=True)
scene = Scene("Main", background=Color(30, 30, 30), gravity=1600)

player = GameObject("Player", 120, 100)
player.add_component(SpriteRenderer(45, 45, Colors.CYAN))
player.add_component(BoxCollider2D(0, 0, 45, 45))
player.add_component(Rigidbody2D(gravity_scale=1.0))
player.add_script(PlayerController())

scene.add(player)

game.load_scene(scene)
game.run()
```

---

## Script Example: Console Tick

```python
from builder2d import *

updatedTime = 0
showConsole = False

class GameConsole(Script):
    def update(self):
        global updatedTime
        updatedTime += 1
        if showConsole:
            print("Tick:", updatedTime)

game = Game("Console Example", width=1280, height=720)
scene = Scene("Main", background=Color(59, 59, 59), gravity=1600)

consoled = GameObject("Console", 0, 0)
consoled.add_script(GameConsole())

scene.add(consoled)

game.load_scene(scene)
game.run()

print("Ended at Tick:", updatedTime)
```

---

## Images

To display an image, create a `GameObject` and add an image renderer.

```python
from builder2d import *

game = Game("ProjectWindowName", width=800, height=600, borderless=True)
scene = Scene("Main", background=Color(59, 59, 59), gravity=1600)

image = GameObject("Image", 0, 0)
image.add_component(SpriteRenderer.from_image("image.png", 100, 100))

scene.add(image)

game.load_scene(scene)
game.run()
```

---

## Music and Sound Effects

```python
music = Music("calmStream.mp3")
click = SoundEffect("click.mp3")

music.play()
click.play()
```

---

## Quick Start Example

```python
from builder2d import *

game = Game("My Builder2D Game", width=1280, height=720, borderless=True)
scene = Scene("Main", background=Color(59, 59, 59), gravity=1600)

game.load_scene(scene)
game.run()
```

---

## Current Status

Builder2D is currently in development.

Planned features include:

- Better scene workflow
- Animation system
- Physics improvements
- More collider types
- Better audio controls
- Scene changing system
- Easier project setup tools

---

## Requirements

- Python
- PYSDL2

---

## Goals

Builder2D aims to be:

- Easy to use
- Beginner-friendly
- Fast for prototyping
- Flexible for simple 2D games

---

## License

Add your license here.

Example:

```text
MIT License
```

---

## Author

Made with Python and PYSDL2.
