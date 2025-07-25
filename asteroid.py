from circleshape import *
from main import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface = screen, color = "white", center = self.position, radius = self.radius, width = 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid_1_velocity = self.velocity.rotate(angle)
        asteroid_2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_1.velocity = asteroid_1_velocity * 1.2
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2.velocity = asteroid_2_velocity * 1.2
        