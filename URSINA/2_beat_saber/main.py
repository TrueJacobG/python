from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enable = False

bulletExist = True
shootNewBullet = False
points = 0


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            color=color.random_color()
            #color=color.rgb(.8, .91, .201),
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            if key == "right mouse down":
                destroy(self)


class Bullet(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            scale=0.5,
            model='cube',
            color=color.rgba(255, 255, 255, 128),
            position=position
        )

    def input(self, key):
        global bulletExist
        global shootNewBullet
        global points
        if self.hovered:
            if key == "left mouse down":
                bulletExist = False
                shootNewBullet = True
                points += 1
                destroy(self)

            if key == "right mouse down":
                bulletExist = False
                shootNewBullet = True
                points += 1
                destroy(self)


startX = 10


def buildObject():
    bullet = Bullet(position=(startX, 2, 0))
    return bullet


bullet = buildObject()


def update():
    global startX
    global bulletExist
    global shootNewBullet
    global bullet
    global points
    startX -= 2 * time.dt

    if bulletExist:
        bullet.set_x(startX)
        if bullet.x < -10:
            destroy(bullet)
            bulletExist = False
            shootNewBullet = True
            points -= 1

    if shootNewBullet:
        bullet = buildObject()
        shootNewBullet = False
        bulletExist = True
        startX = 10


    # platforms
for z in range(5):
    for x in range(5):
        voxel = Voxel(position=(x, 0, z))

for z in range(5):
    voxel = Voxel(position=(-1, 1, z))
    voxel = Voxel(position=(5, 1, z))

for x in range(5):
    voxel = Voxel(position=(x, 1, -1))
    voxel = Voxel(position=(x, 1, 5))


player = FirstPersonController()

app.run()
