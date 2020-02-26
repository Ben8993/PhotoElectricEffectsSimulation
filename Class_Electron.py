import random
import math


class Electron():
    def __init__(self, canvas, light_energy, workfunction):
        self.kinetic_energy = 0
        self.velocity = 0
        self.electron_mass_constant = 9.11e-31
        self.y_coord = random.randint(1, 340)
        self.ball = canvas.create_oval(0, self.y_coord, 14, self.y_coord + 14, width=5, fill='#000000', tags='ball')
        self.canvas = canvas
        self.light_energy = light_energy
        self.workfunction = workfunction

    def calculate_velocity(self):
        self.kinetic_energy = self.light_energy - random.uniform(self.workfunction, self.light_energy)
        self.velocity = math.sqrt((2 * self.kinetic_energy) / self.electron_mass_constant) / 200000
        return self.velocity

    def destroy_ball(self):
        self.canvas.delete(self.ball)

    def move_ball(self):
        if self.canvas.coords(self.ball)[0] < 600:
            self.canvas.move(self.ball, self.velocity, 0)
            self.canvas.after(25, self.move_ball)
        else:
            self.y_coord = random.randint(1, 340)
            self.canvas.coords(self.ball, 0, self.y_coord, 14, self.y_coord + 14)
            self.canvas.move(self.ball, self.velocity, 0)
            self.canvas.after(25, self.move_ball)
