from ursina import *


class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='white_cube',
            color=color.white,
            rotation=Vec3(45, 45, 45)
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='quad',
            texture='brick',
            color=color.yellow,
            highlight_color=color.white,
            pressedd_color=color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print("BUTTON")


def update():
    if held_keys['a']:
        square.x -= 3 * time.dt
    if held_keys['d']:
        square.x += 3 * time.dt
    if held_keys['w']:
        square.y += 3*time.dt
    if held_keys['s']:
        square.y -= 3 * time.dt


app = Ursina()

square2 = Test_button()

square = Test_cube()

app.run()
