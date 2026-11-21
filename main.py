import pygame
from pathfinding import bfs, astar
import time

visited = set()
path = []
exploration_order = []
displayed_path = []
animation_index = 0
last_update_time = 0
ANIMATION_DELAY = 30
path_index = 0

algorithm_name = None

walls = set()


WIDTH = 900
HEIGHT = 600
CELL_SIZE = 20
PANEL_WIDTH = 300
GRID_WIDTH = WIDTH - PANEL_WIDTH
ROWS = HEIGHT // CELL_SIZE
COLS = GRID_WIDTH // CELL_SIZE

start = None
goal = None

def draw_grid(screen):
    for row in range(ROWS):
        for col in range(COLS):
            x =  CELL_SIZE * col
            y = CELL_SIZE * row

            if (row, col) == start:
                color = (0,255,0)

            elif (row, col) == goal:
                color = (255,0,0)

            elif (row, col) in displayed_path:
                color = (255, 255, 0)


            elif (row, col) in visited:
                color = (102, 255, 255)

            elif (row, col) in walls:
                color = (0,0,0)

            else:
                color = (255,255,255) 

            pygame.draw.rect(screen, color, (x,y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (100,100,100), (x,y, CELL_SIZE, CELL_SIZE), 1)


def draw_panel(screen):
    pygame.draw.rect(screen, (0, 0, 0), (GRID_WIDTH, 0, PANEL_WIDTH, HEIGHT))

    text = font.render("Pathfinding Stats", True, (255,255,255))
    screen.blit(text, (620,30))

    text_2 = font.render(f"Algorithm: {algorithm_name}", True, (255,255,255))
    screen.blit(text_2, (620,60))

    if path:
        path_length = len(path) - 1
    else:
        path_length = "N/A"

    text_3 =  font.render(f"Path length: {path_length}", True, (255,255,255))
    screen.blit(text_3, (620,90))

    explored_count = len(exploration_order)

    text_4 = font.render(f"Explored cells: {explored_count}", True, (255,255,255))
    screen.blit(text_4, (620,120))
    execution_time = "N/A"

    if algorithm_name == "BFS":
        execution_time = bfs_time

    elif algorithm_name == "A*":
        execution_time = astar_time
    
    text_5 = font.render(f"Execution time: {execution_time} ms", True, (255,255,255))
    screen.blit(text_5, (620,150))
    
    


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding Visualiser")
font = pygame.font.SysFont("Arial", 24)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    
            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE
            position = (row, col)

            visited.clear()
            path.clear()
            exploration_order.clear()
            displayed_path.clear()
            animation_index = 0
            path_index = 0
            algorithm_name = None


            if 0 <= row < ROWS and 0 <= col < COLS:

                if event.button == 1:
                    
                    if position != start and position != goal:
                        
                        if position in walls:
                            walls.remove(position)
                        
                        else:
                            walls.add(position)

                elif event.button == 2:

                    if position not in walls and position != start:
                        goal = position

                elif event.button == 3:
                    
                    if position not in walls:
                       
                        if position == goal:
                            goal = None

                        start = position

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_r:
                walls.clear()
                start = None
                goal = None
                visited.clear()
                displayed_path.clear()
                path.clear()
                exploration_order.clear()
                last_update_time = pygame.time.get_ticks()
                animation_index = 0
                path_index = 0
                algorithm_name = None

            if event.key == pygame.K_b and start is not None and goal is not None:
                start_time = time.perf_counter()
                path, visited, exploration_order = bfs(start, goal, ROWS, COLS, walls)
                end_time = time.perf_counter()
                bfs_time = round((end_time - start_time) * 1000, 2)
                visited.clear()
                displayed_path.clear()
                animation_index = 0
                path_index = 0
                algorithm_name = "BFS"
                last_update_time = pygame.time.get_ticks()

            elif event.key == pygame.K_a and start is not None and goal is not None:
                start_time = time.perf_counter()
                path, visited, exploration_order = astar(start, goal, ROWS, COLS, walls)
                end_time = time.perf_counter()
                astar_time = round((end_time - start_time) * 1000, 2)
                visited.clear()
                displayed_path.clear()
                animation_index = 0
                path_index = 0
                algorithm_name = "A*"
                last_update_time = pygame.time.get_ticks()

    current_time = pygame.time.get_ticks()
    
    if current_time - last_update_time >= ANIMATION_DELAY:

        if animation_index < len(exploration_order):
            visited.add(exploration_order[animation_index])
            animation_index += 1
            last_update_time = current_time

        else:
            if path_index < len(path):
                displayed_path.append(path[path_index])
                path_index += 1
                last_update_time = current_time


    draw_grid(screen)
    draw_panel(screen)


    pygame.display.flip()

pygame.quit()