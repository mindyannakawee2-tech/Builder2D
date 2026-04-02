import builder2d
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

        if Input.key_pressed("escape"):
            self.scene.game.change_scene("Menu")

        if (Input.key_pressed("space") or Input.key_pressed("w") or Input.key_pressed("up")) and self.rb.is_grounded:
            self.rb.velocity.y = -900


game = builder2d.Game(title="Builder2D Scene Change Demo", width=960, height=540, fps=60)

menu_scene = Scene("Menu", background=Colors.SLATE, gravity=0)
level_scene = Scene("Level1", background=Color(59, 59, 59), gravity=1600)


def go_to_level():
    game.change_scene("Level1")


def back_to_menu():
    game.change_scene("Menu")


menu_canvas = Canvas()
menu_canvas.add(Panel(280, 120, 400, 240, Colors.BLACK))
menu_canvas.add(Label("Builder2D", 390, 155, font_size=34, color=Colors.WHITE))
menu_canvas.add(Label("Scene Change Demo", 350, 200, font_size=22, color=Colors.YELLOW))
menu_canvas.add(Button("Play", 390, 255, 160, 50, Colors.GREEN, on_click=go_to_level))
menu_scene.set_canvas(menu_canvas)

player = GameObject("Player", 120, 100)
player.add_component(SpriteRenderer(45, 45, Colors.CYAN))
player.add_component(BoxCollider2D(0, 0, 45, 45))
player.add_component(Rigidbody2D(gravity_scale=1.0))
player.add_script(PlayerController())

floor = GameObject("Floor", 0, 470)
floor.add_component(SpriteRenderer(960, 70, Colors.GROUND))
floor.add_component(BoxCollider2D(0, 0, 960, 70))

wall = GameObject("Wall", 700, 300)
wall.add_component(SpriteRenderer(50, 170, Colors.YELLOW))
wall.add_component(BoxCollider2D(0, 0, 50, 170))

level_scene.add(player)
level_scene.add(floor)
level_scene.add(wall)

level_canvas = Canvas()
level_canvas.add(Panel(16, 16, 300, 88, Colors.BLACK))
level_canvas.add(Label("A/D Move  Space Jump", 34, 34, font_size=22, color=Colors.WHITE))
level_canvas.add(Label("ESC = Back to Menu", 34, 66, font_size=20, color=Colors.YELLOW))
level_canvas.add(Button("Menu", 820, 20, 110, 40, Colors.BLUE, on_click=back_to_menu))
level_scene.set_canvas(level_canvas)

game.add_scene(menu_scene)
game.add_scene(level_scene)
game.change_scene("Menu")
game.run()
