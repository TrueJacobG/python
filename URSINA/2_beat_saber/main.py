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
    def __init__(self, position=(0, 0, 0), direction="N"):
        self.direction = direction
        super().__init__(
            parent=scene,
            scale=0.5,
            model='cube',
            #color=color.rgba(255, 255, 255, 122),
            color=color.random_color(),
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
                # print(points)
                destroy(self)

            if key == "right mouse down":
                bulletExist = False
                shootNewBullet = True
                points += 1
                # print(points)
                destroy(self)


def randomX():
    x = random.randint(10, 15)
    return x


def randomZ():
    z = random.randint(0, 4)
    return z


def destroyBullet():
    global shootNewBullet
    global bullet
    global points
    destroy(bullet)
    bulletExist = False
    shootNewBullet = True
    points -= 1


# startings
startingX = 10
bullet = Bullet(position=(startingX, 2, randomZ()), direction="N")


def update():
    global startingX
    global bulletExist
    global shootNewBullet
    global bullet
    global points

    if bulletExist:
        if bullet.direction == 'N':
            startingX -= 2 * time.dt
            bullet.set_x(startingX)
            if bullet.x < -10:
                destroyBullet()

        if bullet.direction == 'S':
            startingX += 2 * time.dt
            bullet.set_x(startingX)
            if bullet.x > 10:
                destroyBullet()

    if shootNewBullet:
        directions = ["N", "N", "S", "S"]
        startings = [10, 10, -10, -10]
        r = random.randint(0, 3)

        startingX = startings[r]

        bullet = Bullet(position=(startings[r], 2, randomZ()),
                        direction=directions[r])
        shootNewBullet = False
        bulletExist = True

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
