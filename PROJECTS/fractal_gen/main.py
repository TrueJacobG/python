import turtle as t

# t.speed(0)
# t.shape("classic")

screen = t.Screen()
t.color("lightgreen", "gray")
screen.bgcolor("black")
# disable animation
t.tracer(0, 0)


def tree(size, levels, angle):
    if levels == 0:
        t.color("green")
        t.dot(size//1.2)
        t.color("lightgreen")
        return

    t.forward(size)
    t.right(angle)

    tree(size * 0.8, levels-1, angle)

    # move from right to left position
    t.left(2*angle)

    tree(size * 0.8, levels-1, angle)

    # go back to the middle
    t.right(angle)
    t.backward(size)


def forest(how_many_trees):
    # start,
    for _ in range(how_many_trees):
        t.left(360//how_many_trees)
        # size, levels, angle
        tree(80, 7, 30)


def snowflake_part(length, levels):
    if levels == 0:
        t.forward(length)
        return

    length /= 3.0
    snowflake_part(length, levels-1)
    t.left(60)
    snowflake_part(length, levels-1)
    t.right(120)
    snowflake_part(length, levels-1)
    t.left(60)
    snowflake_part(length, levels-1)


def snowflake(length, sides):
    for _ in range(sides):
        snowflake_part(length, sides)
        t.right(360//sides)


def main():
    # how many trees
    # forest(4)

    snowflake(200, 3)

    # run
    t.update()
    t.mainloop()


if __name__ == '__main__':
    main()
