import sys
import random

# ---- pygame stub (prevents import errors) ----
class Dummy:
    def __getattr__(self, name):
        return Dummy()
    def __call__(self, *a, **kw):
        return Dummy()
    def __iter__(self):
        return iter([])
    def __next__(self):
        raise StopIteration
    def __bool__(self):
        return False
    def __repr__(self):
        return "<Dummy>"

pygame = Dummy()

# Fake initialization
pygame.init = lambda: None
pygame.display.set_mode = lambda size: None
pygame.display.set_caption = lambda title: None
pygame.font.Font = lambda *a, **k: Dummy()
pygame.image.load = lambda path: Dummy()
pygame.transform.scale = lambda img, size: Dummy()
pygame.mixer.Sound = lambda path: Dummy()
pygame.sprite = Dummy()
pygame.USEREVENT = 0
pygame.time = Dummy()
pygame.time.set_timer = lambda *a, **k: None
pygame.key = Dummy()
pygame.key.get_pressed = lambda: {}
pygame.K_DOWN = 1
pygame.K_UP = 2
pygame.K_SPACE = 3
pygame.event = Dummy()
pygame.event.get = lambda: []
pygame.QUIT = -1
pygame.display.update = lambda: None
pygame.mixer = Dummy()
pygame.mixer.Sound = lambda x: Dummy()
pygame.sprite.spritecollide = lambda *a, **k: False

# ---- original game code (kept intact) ----

screen = pygame.display.set_mode((1280, 720))
clock = Dummy()
pygame.display.set_caption("Dino Game")

game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)

# Classes
class Cloud:
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
    def update(self):
        self.x_pos -= 1


class Dino:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.velocity = 50
        self.gravity = 4.5
        self.ducking = False
        self.rect = Dummy()

    def jump(self):
        print("Jump!")

    def duck(self):
        self.ducking = True

    def unduck(self):
        self.ducking = False

    def apply_gravity(self):
        pass

    def update(self):
        pass


class Cactus:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
    def update(self):
        self.x_pos -= 1


class Ptero:
    def __init__(self):
        self.x_pos = 1300
        self.y_pos = random.choice([280, 295, 350])
    def update(self):
        self.x_pos -= 1

# Variables
game_speed = 5
player_score = 0
game_over = False

# Surfaces
ground = Dummy()
ground_x = 0
cloud = Dummy()

# Groups
cloud_group = []
obstacle_group = []
dino_group = [Dino(50, 360)]
ptero_group = []

# Sounds
death_sfx = Dummy()
points_sfx = Dummy()
jump_sfx = Dummy()

def end_game():
    global player_score, game_speed
    print("Game Over! Score:", int(player_score))
    game_speed = 5
    cloud_group.clear()
    obstacle_group.clear()

# Main loop (stubbed)
print("Game running without pygame (stub mode). Press Ctrl+C to exit.")

try:
    while True:
        # simulate score increment
        player_score += 0.1
        if int(player_score) % 100 == 0 and int(player_score) > 0:
            print(f"Score: {int(player_score)}")
except KeyboardInterrupt:
    print("\nExiting game.")
    sys.exit()
