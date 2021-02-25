from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture("textures/grass_block.png")
stone_texture = load_texture("textures/stone_block.png")
brick_texture = load_texture("textures/brick_block.png")
dirt_texture = load_texture("textures/dirt_block.png")
sky_texture = load_texture("textures/skybox.png")
arm_texture = load_texture("textures/arm_texture.png")

punch_sound = Audio("textures/punch_sound", loop=False, autoplay=False)

block_pick = 1


window.fps_counter.enable = False


def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='textures/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1:
                    alr_block = grass_texture
                if block_pick == 2:
                    alr_block = stone_texture
                if block_pick == 3:
                    alr_block = brick_texture
                if block_pick == 4:
                    alr_block = dirt_texture
                voxel = Voxel(position=self.position +
                              mouse.normal, texture=alr_block)

            if key == "right mouse down":
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="textures/arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
