import pygame, sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateble, drawable)
    Shot.containers = (shots, updateble, drawable)
    Asteroid.containers = (asteroids, updateble, drawable)
    AsteroidField.containers = updateble
    asteroids_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updateble:
            obj.update(dt)
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collishion(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collishion(shot):
                    asteroid.kill()
                    shot.kill()
                
        pygame.display.flip()
                
        # limit the framerate to 60FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()