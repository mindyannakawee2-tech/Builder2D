# Builder2D

![img_alt](https://github.com/mindyannakawee2-tech/Builder2D/blob/85d853caa1c77d9dd37fbaa8988ff33cb06d90cf/builder2Dicon.png)

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
## Requirements
* Python 3.14 or up
* PYSDL2
---
## Guide
# Builder2D User Guide

Builder2D is a small 2D Python game framework built around scenes, game objects, components, scripts, UI, animation, sound, and scene switching.

This guide explains how to use its syntax and main functions.

---

## 1. Basic idea

Builder2D works in a component style.

You usually:

1. Create a `Game`
2. Create a `Scene`
3. Create `GameObject`s
4. Add components like `SpriteRenderer`, `BoxCollider2D`, `Rigidbody2D`
5. Add scripts with `add_script(...)`
6. Add objects to the scene with `scene.add(...)`
7. Load the scene and run the game

Example:

```python
import builder2d
from builder2d import *

class PlayerController(Script):
    def start(self):
        self.rb = self.game_object.get_component(Rigidbody2D)

    def update(self):
        move = 0
        if Input.key_down("a"):
            move -= 1
        if Input.key_down("d"):
            move += 1

        self.rb.velocity.x = move * 300

        if Input.key_pressed("space") and self.rb.is_grounded:
            self.rb.velocity.y = -900


game = Game(title="Builder2D Demo")
scene = Scene("Main", background=Colors.SLATE, gravity=1600)

player = GameObject("Player", 120, 100)
player.add_component(SpriteRenderer(45, 45, Colors.CYAN))
player.add_component(BoxCollider2D(0, 0, 45, 45))
player.add_component(Rigidbody2D(gravity_scale=1.0))
player.add_script(PlayerController())

floor = GameObject("Floor", 0, 470)
floor.add_component(SpriteRenderer(960, 70, Colors.GROUND))
floor.add_component(BoxCollider2D(0, 0, 960, 70))

scene.add(player)
scene.add(floor)

game.load_scene(scene)
game.run()
```

---

## 2. Importing

You can import everything:

```python
from builder2d import *
```

Or use the module name too:

```python
import builder2d
from builder2d import *

game = builder2d.Game(title="My Game")
```

---

## 3. Main classes

## Game

Creates the window, runs the main loop, and manages scenes.

### Syntax

```python
Game(title="Builder2D", width=960, height=540, fps=60, borderless=False, fullscreen_desktop=False)
```

### Common usage

```python
game = Game(title="My Game", width=1280, height=720, fps=60)
```

### Fullscreen desktop

```python
game = Game(title="My Game", fullscreen_desktop=True)
```

### Borderless window

```python
game = Game(title="My Game", width=1280, height=720, borderless=True)
```

### Window Icon
```python
game = Game(
    title="My Game",
    width=960,
    height=540,
    icon_path="assets/icon.png",
)
```

### Main methods

```python
game.load_scene(scene)
game.add_scene(scene)
game.change_scene("Menu")
game.run()
```

---

## Scene

A scene contains game objects and optional UI.

### Syntax

```python
Scene(name="Scene", background=Colors.SLATE, gravity=1400.0)
```

### Example

```python
scene = Scene("Level1", background=Colors.BLACK, gravity=1600)
```

### Main methods

```python
scene.add(game_object)
scene.find("Player")
scene.set_canvas(canvas)
```

### Notes

* `background` is a `Color`
* `gravity` affects `Rigidbody2D`
* `find(name)` returns the first matching object or `None`

---

## GameObject

A game object is a container for components and scripts.

### Syntax

```python
GameObject(name="GameObject", x=0.0, y=0.0)
```

### Example

```python
player = GameObject("Player", 120, 100)
```

### Main methods

```python
player.add_component(component)
player.get_component(ComponentType)
player.add_script(script)
```

### Properties

* `name`
* `transform`
* `components`
* `scene`
* `active`

If `active` is `False`, the object is skipped by update and draw.

---

## Transform

Each `GameObject` has a transform.

### Properties

```python
obj.transform.position.x
obj.transform.position.y
obj.transform.scale.x
obj.transform.scale.y
obj.transform.rotation
```

### Example

```python
player.transform.position.x = 300
player.transform.position.y = 200
```

---

## 4. Components

## SpriteRenderer

Draws either a colored rectangle or an image.

### Colored rectangle syntax

```python
SpriteRenderer(width, height, color)
```

### Example

```python
player.add_component(SpriteRenderer(45, 45, Colors.CYAN))
```

### Image syntax

```python
SpriteRenderer.from_image("assets/player.png", width, height)
```

### Example

```python
logo = GameObject("Logo", 700, 20)
logo.add_component(SpriteRenderer.from_image("assets/logo.png", 120, 120))
```

### Notes

* PNG and BMP are supported in the newer builds
* width and height can be resized
* for spritesheets, `Animator` controls the source rectangle

---

## BoxCollider2D

Used for collision.

### Syntax

```python
BoxCollider2D(x, y, width, height, is_trigger=False)
```

### Example

```python
player.add_component(BoxCollider2D(0, 0, 45, 45))
```

### Meaning

* `x`, `y` = collider offset from object position
* `width`, `height` = collider size
* `is_trigger=True` means trigger-style overlap, not solid collision

### Method

```python
collider.intersects(other_collider)
```

### Example

```python
my_col = self.game_object.get_component(BoxCollider2D)
player_col = self.player.get_component(BoxCollider2D)
if my_col and player_col and my_col.intersects(player_col):
    self.game_object.active = False
```

---

## Rigidbody2D

Adds velocity and gravity.

### Syntax

```python
Rigidbody2D(gravity_scale=1.0, is_kinematic=False)
```

### Example

```python
player.add_component(Rigidbody2D(gravity_scale=1.0))
```

### Properties

```python
rb.velocity.x
rb.velocity.y
rb.is_grounded
rb.gravity_scale
rb.is_kinematic
```

### Example movement

```python
self.rb.velocity.x = 300
```

### Example jump

```python
if Input.key_pressed("space") and self.rb.is_grounded:
    self.rb.velocity.y = -900
```

---

## Animator

Controls animations from separate image frames or spritesheets.

### Syntax

```python
Animator(*clips, play_on_start="idle")
```

### Example with frame files

```python
player.add_component(
    Animator(
        AnimationClip.from_frames("idle", ["assets/player_idle.png"], fps=1),
        AnimationClip.from_frames(
            "walk",
            [
                "assets/player_walk_0.png",
                "assets/player_walk_1.png",
                "assets/player_walk_2.png",
                "assets/player_walk_3.png",
            ],
            fps=10,
            loop=True,
        ),
        play_on_start="idle",
    )
)
```

### Example with spritesheet

```python
orb.add_component(
    Animator(
        AnimationClip.from_spritesheet(
            "spin",
            "assets/orb_sheet.png",
            frame_width=32,
            frame_height=32,
            frame_count=4,
            fps=12,
            loop=True,
        ),
        play_on_start="spin",
    )
)
```

### Methods

```python
anim.play("walk")
anim.play("idle", restart=True)
```

---

## AnimationClip

Represents an animation.

### From frame list

```python
AnimationClip.from_frames(name, frame_paths, fps=8.0, loop=True)
```

### From spritesheet

```python
AnimationClip.from_spritesheet(
    name,
    image_path,
    frame_width,
    frame_height,
    frame_count,
    fps=8.0,
    loop=True,
    start_x=0,
    start_y=0,
    spacing=0,
    margin=0,
    row=0,
)
```

---

## 5. Scripts

Scripts are custom logic components.

To make one, inherit from `Script`.

### Common functions

```python
class MyScript(Script):
    def start(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass
```

### Useful references inside scripts

```python
self.game_object
self.transform
self.scene
```

### Example

```python
class PlayerController(Script):
    def start(self):
        self.rb = self.game_object.get_component(Rigidbody2D)

    def update(self):
        if Input.key_down("a"):
            self.rb.velocity.x = -300
```

---

## 6. Input

Builder2D supports keyboard input.

### Functions

```python
Input.key_down("a")
Input.key_pressed("space")
Input.key_released("escape")
```

### Meaning

* `key_down` = key is being held
* `key_pressed` = key was pressed this frame
* `key_released` = key was released this frame

### Example

```python
if Input.key_down("left"):
    self.rb.velocity.x = -300

if Input.key_pressed("space") and self.rb.is_grounded:
    self.rb.velocity.y = -900
```

---

## 7. Colors

Use built-in colors or make your own.

### Built-in colors

```python
Colors.BLACK
Colors.WHITE
Colors.RED
Colors.GREEN
Colors.BLUE
Colors.YELLOW
Colors.CYAN
Colors.SLATE
Colors.GROUND
Colors.PURPLE
Colors.ORANGE
```

### Custom color

```python
Color(59, 59, 59)
```

---

## 8. UI System

UI is separate from world objects.

Main UI classes:

* `Canvas`
* `Panel`
* `Label`
* `Button`

### Basic usage

```python
canvas = Canvas()

panel = Panel(20, 20, 260, 140, Colors.BLACK)
title = Label("Builder2D Menu", 40, 35, font_size=28, color=Colors.WHITE)
score_label = Label("Score: 0", 40, 75, font_size=22, color=Colors.YELLOW)
button = Button("Play", 40, 110, 120, 40, Colors.BLUE, on_click=lambda: print("Hello"))

canvas.add(panel)
canvas.add(title)
canvas.add(score_label)
canvas.add(button)

scene.set_canvas(canvas)
```

### Canvas

```python
canvas = Canvas()
canvas.add(element)
```

### Panel

```python
Panel(x, y, width, height, color)
```

### Label

```python
Label(text, x, y, font_size=24, color=Colors.WHITE)
```

### Button

```python
Button(text, x, y, width, height, color, on_click=function)
```

### Dynamic UI text

```python
score_label.text = f"Score: {score}"
```

---

## 9. Sound System

The engine includes a simple sound API.

### SoundEffect

Good for short sounds like clicks or jumps.

```python
click = SoundEffect("assets/click.wav")
click.play()
```

### Music

Good for background music.

```python
bgm = Music("assets/bgm.ogg", volume=96)
bgm.play()
```

### Example with button

```python
click = SoundEffect("assets/click.wav")

def add_score():
    global score
    score += 1
    click.play()
```

### Notes

* WAV is safest for sound effects
* OGG is commonly used for music

---

## 10. Scene Switching

Builder2D can manage multiple scenes.

### Add scenes

```python
game.add_scene(menu_scene)
game.add_scene(level_scene)
```

### Change scene

```python
game.change_scene("Level1")
```

### Example

```python
def start_game():
    game.change_scene("Level1")
```

### Script example

```python
class ReturnToMenu(Script):
    def update(self):
        if Input.key_pressed("escape"):
            self.scene.game.change_scene("Menu")
```

---

## 11. Common patterns

## Player movement

```python
class PlayerController(Script):
    def start(self):
        self.rb = self.game_object.get_component(Rigidbody2D)

    def update(self):
        move = 0
        if Input.key_down("a"):
            move -= 1
        if Input.key_down("d"):
            move += 1

        self.rb.velocity.x = move * 300
```

## Jump

```python
if Input.key_pressed("space") and self.rb.is_grounded:
    self.rb.velocity.y = -900
```

## Reset object position

```python
self.game_object.transform.position.x = 120
self.game_object.transform.position.y = 100
self.rb.velocity.x = 0
self.rb.velocity.y = 0
```

## Find another object

```python
self.player = self.scene.find("Player")
```

## Turn object off

```python
self.game_object.active = False
```

## Change sprite color

```python
spr = player.get_component(SpriteRenderer)
spr.color = Colors.GREEN
```

## Update UI label

```python
score_label.text = f"Score: {score}"
```

---

## 12. Full sample

```python
import builder2d
from builder2d import *

score = 0


def add_score():
    global score
    score += 1


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


class ScoreUI(Script):
    def update(self):
        global score
        score_label.text = f"Score: {score}"


game = Game(title="Builder2D Example")
scene = Scene("Main", background=Color(59, 59, 59), gravity=1600)

player = GameObject("Player", 120, 100)
player.add_component(SpriteRenderer(45, 45, Colors.CYAN))
player.add_component(BoxCollider2D(0, 0, 45, 45))
player.add_component(Rigidbody2D(gravity_scale=1.0))
player.add_script(PlayerController())

floor = GameObject("Floor", 0, 470)
floor.add_component(SpriteRenderer(960, 70, Colors.GROUND))
floor.add_component(BoxCollider2D(0, 0, 960, 70))

ui_updater = GameObject("UIUpdater", 0, 0)
ui_updater.add_script(ScoreUI())

scene.add(player)
scene.add(floor)
scene.add(ui_updater)

canvas = Canvas()
panel = Panel(20, 20, 260, 140, Colors.BLACK)
title = Label("Builder2D Menu", 40, 35, font_size=28, color=Colors.WHITE)
score_label = Label("Score: 0", 40, 75, font_size=22, color=Colors.YELLOW)
play_button = Button("Add Score", 40, 110, 120, 40, Colors.BLUE, on_click=add_score)

canvas.add(panel)
canvas.add(title)
canvas.add(score_label)
canvas.add(play_button)

scene.set_canvas(canvas)

game.load_scene(scene)
game.run()
```

---

## 13. Troubleshooting

## Problem: object position does not change

Use transform position:

```python
obj.transform.position.x = 100
obj.transform.position.y = 200
```

Not:

```python
obj.x = 100
obj.y = 200
```

## Problem: jump does not work

Make sure:

* object has `Rigidbody2D`
* object has `BoxCollider2D`
* floor has `BoxCollider2D`
* jump uses `rb.is_grounded`

## Problem: animation does not play

Make sure:

* object has `SpriteRenderer`
* object has `Animator`
* clip name is correct
* `anim.play("name")` matches the clip name exactly

## Problem: button callback crashes

Use:

```python
on_click=lambda: print("Hello")
```

Not:

```python
on_click=lambda print("Hello")
```

## Problem: score label shows wrong type

Use string text:

```python
score_label.text = f"Score: {score}"
```

Not:

```python
Label(["Score:", score], ...)
```

---

## 14. Summary

Main workflow:

* `Game` runs everything
* `Scene` holds world objects and UI
* `GameObject` holds components
* `Script` adds game logic
* `SpriteRenderer` draws
* `BoxCollider2D` collides
* `Rigidbody2D` moves with gravity
* `Animator` animates
* `Canvas` shows UI
* `SoundEffect` and `Music` play audio
* `change_scene()` switches scenes

Builder2D is easiest to use when you keep world objects in `scene.add(...)` and UI in `canvas.add(...)`.


---
## Author
c0b41t aka mindyannakawee2-tech
Made with Python and PYSDL2.
