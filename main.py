import powder as pd, colors
import pygame

FRAMERATE = 60
CELL_SIZE = 5
HEIGHT = 480
WIDTH = 960

if __name__ == "__main__":
    print("Welcome to the Powder Sim")
    
    #grid = pd.Grid(WIDTH, HEIGHT)
    grid = pd.Grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)
    for i in range(0, grid.width, 2):
        grid[i][0] = pd.Sand()
        grid[i + 1][0] = pd.Water()
    
    # Screen initialization
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    while (running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYUP and pygame.K_ESCAPE)): running = False
            
        screen.fill("black")
        
        # Game here
        for y in range(grid.height):
            for x in range(grid.width):
                pygame.draw.rect(screen, grid[x][y].color.to_pygame_color(), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Display and framerate
        pygame.display.flip()
        clock.tick(FRAMERATE)
    
    pygame.quit()