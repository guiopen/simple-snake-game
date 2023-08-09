import pygame, sys, random

pygame.init()
cell_size = 40
cell_amount = 17
cell_limit = cell_size * (cell_amount - 1)


class Snake:

    def __init__(self):
        self.size = 3
        self.x = int(cell_amount / 2) * cell_size
        self.y = (cell_amount - self.size) * cell_size
        self.body = [[self.x, self.y], [self.x, self.y - 2 * cell_size], [self.x, self.y - 3 * cell_size]]
        self.direction = 'up'
        self.direction_x = 0 * cell_size
        self.direction_y = -1 * cell_size

    def draw(self):
        for x,y in self.body:
            self.body_rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (30,120,30), self.body_rect)
 
    def move(self, direction_x, direction_y):
        self.new_block = [self.body[0][0] + direction_x, self.body[0][1] + direction_y]
        self.body.insert(0, self.new_block)
        self.body_copy = self.body[-1]
        self.body.pop()


class Fruit:
    def __init__(self):
        self.x = random.randint(1, cell_amount - 2) * cell_size
        self.y = random.randint(1, cell_amount - 2) * cell_size
        self.pos = [self.x, self.y]
    
    def respawn(self):
        self.x = random.randint(1, cell_amount - 2) * cell_size
        self.y = random.randint(1, cell_amount - 2) * cell_size
        self.pos = [self.x, self.y]

    def draw(self):
        fruit_hitbox = pygame.Rect(self.x, self.y, cell_size, cell_size)
        pygame.draw.rect(screen,(220,40,40),fruit_hitbox)


screen_size = cell_size * cell_amount
screen = pygame.display.set_mode((screen_size, screen_size))
fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if snake.direction == 'up' or snake.direction == 'down':
                if event.key == pygame.K_RIGHT:
                    snake.direction = 'right'
                    snake.direction_x = 1 * cell_size
                    snake.direction_y = 0 * cell_size

                elif event.key == pygame.K_LEFT:
                    snake.direction = 'left'
                    snake.direction_x = -1 * cell_size
                    snake.direction_y = 0 * cell_size
  
            elif snake.direction == 'right' or snake.direction == 'left':
                if event.key == pygame.K_UP:
                    snake.direction = 'up'
                    snake.direction_x = 0 * cell_size
                    snake.direction_y = -1 * cell_size

                elif event.key == pygame.K_DOWN:
                    snake.direction = 'down'
                    snake.direction_x = 0 * cell_size
                    snake.direction_y = 1 * cell_size

    screen.fill((140,210,70))
    snake.move(snake.direction_x, snake.direction_y)
    if fruit.pos == snake.body[0]:
        fruit.respawn()
        snake.body.append(snake.body_copy)
    if snake.body[0][0] < 0 or snake.body[0][0] > cell_limit:
        print('game over')
        pygame.time.wait(1000)
        sys.exit()
    elif snake.body[0][1] < 0 or snake.body[0][1] > cell_limit:
        print('game over')
        pygame.time.wait(1000)
        sys.exit()
    for block in snake.body[1:]:
        if snake.body[0] == block:
            print('game over')
            pygame.time.wait(1000)
            sys.exit()
    fruit.draw()
    snake.draw()
    pygame.display.update()
    pygame.time.wait(200)
