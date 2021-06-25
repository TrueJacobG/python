from pygame import *
import numpy as np
from random import randint


class matrix:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height//scale)
        self.rows = int(width//scale)
        self.size = (self.rows, self.columns)
        self.matrix_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.matrix_array[x][y] = randint(0, 1)

    def game_of_life(self, color_off, window):
        for x in range(self.rows):
            for y in range(self.columns):
                pos_x = x * self.scale
                pos_y = y * self.scale

                if self.matrix_array[x][y] == 1:
                    draw.rect(window, self.random_color(), (pos_x, pos_y,
                                                            self.scale - self.offset, self.scale - self.offset))
                else:
                    draw.rect(window, color_off, (pos_x, pos_y,
                                                  self.scale - self.offset, self.scale - self.offset))
        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.matrix_array[x][y]
                neighbours = self.get_neighbours(x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.matrix_array = next

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                edge_x = (x+n+self.rows) % self.rows
                edge_y = (y+m+self.columns) % self.columns
                total += self.matrix_array[edge_x][edge_y]
        total -= self.matrix_array[x][y]
        return total

    def random_color(self):
        return (randint(40, 210), randint(40, 210), randint(40, 210))
