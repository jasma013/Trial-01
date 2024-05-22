import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up screen dimensions
WIDTH, HEIGHT = 1000, 800

# Define ball and paddle properties
BALL_RADIUS = 15
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 25

# Ball class representing the game ball
class Ball:
    def __init__(self):
        # Initialize ball position at the center of the screen
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        # Initialize random speed in x-direction and constant speed in y-direction
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 2

    # Method to move the ball
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    # Method to check collision with walls
    def check_collision(self):
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y

# Paddle class representing the player's paddle
class Paddle:
    def __init__(self):
        # Initialize paddle dimensions and position at the bottom center of the screen
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10

    # Method to move the paddle
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10

# Game class managing game state and logic
class Game:
    def __init__(self):
        # Initialize ball, paddle, score, font, and game over flag
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    # Method to handle events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    # Method to update game state
    def update(self):
        self.ball.move()
        self.ball.check_collision()
        if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                self.ball.y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                self.ball.speed_y = -self.ball.speed_y
                self.score += 1
            else:
                self.game_over = True

    # Method to draw objects on the screen
    def draw(self, screen):
        # Clear the screen
        screen.fill(BLACK)
        # Draw the ball and paddle
        pygame.draw.circle(screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        pygame.draw.rect(screen, WHITE, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        # Draw the score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        # Display game over message if the game is over
        if self.game_over:
            game_over_text = self.font.render(f"Your score: {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(game_over_text, game_over_rect)

# Main function to initialize the game and run the game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    game = Game()
    
    # Game loop
    while not game.game_over:
        game.handle_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.paddle.move("left")
        if keys[pygame.K_RIGHT]:
            game.paddle.move("right")
        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()