from PIL import Image
from random import randint

arr = [
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
    [[randint(0, 256) for _ in range(3)] for _ in range(8)],
]

# IMAGE 8x8
# print(arr)

width, height = len(arr[0]), len(arr)

image = Image.new("RGB", (width, height))
image.putdata([tuple(x) for row in arr for x in row])
image.save("image.png")
