import pygame
import random
import sys

WIDTH, HEIGHT = 800, 480
FPS = 30

COLOR_BG = (24, 26, 32)
COLOR_TILE = (58, 120, 190)
COLOR_TILE_LIT = (140, 205, 255)
COLOR_TILE_WRONG = (210, 70, 70)
COLOR_TEXT = (235, 235, 240)
COLOR_MUTED = (150, 155, 165)
COLOR_BUTTON = (70, 110, 200)
COLOR_BUTTON_HOVER = (95, 135, 225)
COLOR_WAIT = (190, 60, 60)
COLOR_GO = (60, 170, 95)
FONT_NAME = None

class Button:
    def __init__(self, rect, label, font_size=36):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.font = pygame.font.Font(FONT_NAME, font_size)

    def draw(self, surface, mouse_pos):
        color = COLOR_BUTTON_HOVER if self.rect.collidepoint(mouse_pos) else COLOR_BUTTON
        pygame.draw.rect(surface, color, self.rect, border_radius=14)
        text = self.font.render(self.label, True, COLOR_TEXT)
        surface.blit(text, text.get_rect(center=self.rect.center))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_text(surface, text, font, color, center):
    surf = font.render(text, True, color)
    surface.blit(surf, surf.get_rect(center=center))

def header(surface, app, title, subtitle):
    draw_text(surface, title, app.font_med, COLOR_TEXT, (WIDTH // 2, 40))
    draw_text(surface, subtitle, app.font_small, COLOR_MUTED, (WIDTH // 2, 75))

def decay(flashes, dt):
    for key in list(flashes):
        flashes[key] -= dt
        if flashes[key] <= 0:
            del flashes[key]

class TileGame:
    GRID_COLS = GRID_ROWS = CELL_SIZE = CELL_GAP = 0
    START_Y = 110

    def __init__(self, app):
        self.app = app
        self.cells = self._build_grid()
        self.flash = {}

    def _build_grid(self):
        size, gap = self.CELL_SIZE, self.CELL_GAP
        start_x = (WIDTH - (self.GRID_COLS * size + (self.GRID_COLS - 1) * gap)) // 2
        return [
            pygame.Rect(start_x + col * (size + gap), self.START_Y + row * (size + gap), size, size)
            for row in range(self.GRID_ROWS) for col in range(self.GRID_COLS)
        ]

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Memory Testing Device")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.Font(FONT_NAME, 54)
        self.font_med = pygame.font.Font(FONT_NAME, 32)
        self.font_small = pygame.font.Font(FONT_NAME, 22)

        self.state = "menu"
        self.last_game = None
        self.last_score = 0
        self.games = {}

        self.menu_buttons = {
            "memory": Button((90, 140, 290, 85), "Memory Test", font_size=28),
            "chimp": Button((420, 140, 290, 85), "Chimp Test", font_size=28),
            "whack": Button((90, 245, 290, 85), "Whack-a-Mole", font_size=28),
            "rps": Button((420, 245, 290, 85), "Rock-Paper-Scissors", font_size=24),
            "reaction": Button((255, 350, 290, 85), "Reaction Time", font_size=28),
        }
        self.result_buttons = {
            "again": Button((140, 330, 230, 80), "Play Again"),
            "menu": Button((430, 330, 230, 80), "Back to Menu"),
        }
        self.back_button = Button((10, 10, 160, 50), "Back to Menu", font_size=22)

        self.game_titles = {name: btn.label for name, btn in self.menu_buttons.items()}
        self.result_labels = {"reaction": "Avg reaction time (ms)"}

    def go_to_menu(self):
        self.state = "menu"

    def start_game(self, which):
        self.last_game = which
        self.games[which] = GAME_CLASSES[which](self)
        self.state = which

    def finish_game(self, score):
        self.last_score = score
        self.state = "result"

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.screen.fill(COLOR_BG)
            if self.state == "menu":
                self.draw_menu(mouse_pos)
            elif self.state == "result":
                self.draw_result(mouse_pos)
            elif self.state in self.games:
                game = self.games[self.state]
                game.update(dt)
                game.draw(self.screen)
                self.back_button.draw(self.screen, mouse_pos)
            pygame.display.flip()

    def handle_click(self, pos):
        if self.state == "menu":
            for name, btn in self.menu_buttons.items():
                if btn.is_clicked(pos):
                    self.start_game(name)
                    break
        elif self.state == "result":
            if self.result_buttons["again"].is_clicked(pos):
                self.start_game(self.last_game)
            elif self.result_buttons["menu"].is_clicked(pos):
                self.go_to_menu()
        elif self.state in self.games:
            if self.back_button.is_clicked(pos):
                self.go_to_menu()
            else:
                self.games[self.state].handle_click(pos)

    def draw_menu(self, mouse_pos):
        draw_text(self.screen, "Memory Testing Device", self.font_big, COLOR_TEXT, (WIDTH // 2, 65))
        draw_text(self.screen, "Choose a game", self.font_small, COLOR_MUTED, (WIDTH // 2, 103))
        for btn in self.menu_buttons.values():
            btn.draw(self.screen, mouse_pos)

    def draw_result(self, mouse_pos):
        title = self.game_titles.get(self.last_game, "Game")
        label = self.result_labels.get(self.last_game, "Score")
        draw_text(self.screen, f"{title} - Result", self.font_big, COLOR_TEXT, (WIDTH // 2, 110))
        draw_text(self.screen, f"{label}: {self.last_score}", self.font_med, COLOR_MUTED, (WIDTH // 2, 190))
        for btn in self.result_buttons.values():
            btn.draw(self.screen, mouse_pos)

# Memory Test
class MemoryGame(TileGame):
    GRID_COLS, GRID_ROWS, CELL_SIZE, CELL_GAP = 4, 4, 80, 14
    CLICK_FLASH_TIME = 0.3
    ADVANCE_PAUSE = 0.45

    def __init__(self, app):
        super().__init__(app)
        self.level = 1
        self._new_round()

    def _new_round(self):
        self.sequence = [random.randrange(len(self.cells)) for _ in range(self.level + 2)]
        self.player_index = self.show_index = 0
        self.phase = "showing"
        self.timer = 0.6
        self.lit_tile = None
        self.flash = {}

    def update(self, dt):
        decay(self.flash, dt)
        if self.phase == "showing":
            self.timer -= dt
            if self.timer <= 0:
                if self.lit_tile is not None:
                    self.lit_tile, self.timer = None, 0.25
                    if self.show_index >= len(self.sequence):
                        self.phase = "waiting"
                    return
                self.lit_tile = self.sequence[self.show_index]
                self.show_index += 1
                self.timer = 0.6
        elif self.phase == "advancing":
            self.timer -= dt
            if self.timer <= 0:
                self.level += 1
                self._new_round()

    def handle_click(self, pos):
        if self.phase != "waiting":
            return
        for idx, rect in enumerate(self.cells):
            if rect.collidepoint(pos):
                if idx == self.sequence[self.player_index]:
                    self.flash[idx] = self.CLICK_FLASH_TIME
                    self.player_index += 1
                    if self.player_index == len(self.sequence):
                        self.phase, self.timer = "advancing", self.ADVANCE_PAUSE
                else:
                    self.app.finish_game(self.level)
                break

    def draw(self, surface):
        header(surface, self.app, "Memory Test", f"Level {self.level}")
        for idx, rect in enumerate(self.cells):
            lit = idx == self.lit_tile or idx in self.flash
            pygame.draw.rect(surface, COLOR_TILE_LIT if lit else COLOR_TILE, rect, border_radius=10)

# Chimp Test
class ChimpGame(TileGame):
    GRID_COLS, GRID_ROWS, CELL_SIZE, CELL_GAP = 5, 4, 78, 10

    def __init__(self, app):
        super().__init__(app)
        self.level = 1
        self._new_round()

    def _new_round(self):
        count = min(self.level + 2, len(self.cells))
        chosen = random.sample(range(len(self.cells)), count)
        self.numbers = {cell: i + 1 for i, cell in enumerate(chosen)}
        self.next_expected = 1
        self.hidden = False
        self.reveal_timer = 1.2
        self.flash = {}

    def update(self, dt):
        decay(self.flash, dt)
        if not self.hidden:
            self.reveal_timer -= dt
            self.hidden = self.reveal_timer <= 0

    def handle_click(self, pos):
        if not self.hidden:
            return
        for cell, rect in enumerate(self.cells):
            if rect.collidepoint(pos) and cell in self.numbers:
                if self.numbers[cell] == self.next_expected:
                    self.flash[cell] = 0.3
                    self.next_expected += 1
                    if self.next_expected > len(self.numbers):
                        self.level += 1
                        self._new_round()
                else:
                    self.app.finish_game(self.level)
                break

    def draw(self, surface):
        header(surface, self.app, "Chimp Test", f"Level {self.level}")
        for cell, rect in enumerate(self.cells):
            if cell not in self.numbers:
                continue
            color = COLOR_TILE_LIT if cell in self.flash else COLOR_TILE
            pygame.draw.rect(surface, color, rect, border_radius=10)
            if not self.hidden:
                draw_text(surface, str(self.numbers[cell]), self.app.font_med, COLOR_TEXT, rect.center)

# Whack-a-Mole
class WhackGame(TileGame):
    GRID_COLS, GRID_ROWS, CELL_SIZE, CELL_GAP = 3, 3, 96, 24
    START_MOLE_TIME, MIN_MOLE_TIME, SPEEDUP_PER_HIT = 1.6, 0.5, 0.1

    def __init__(self, app):
        super().__init__(app)
        self.hits = 0
        self._spawn_mole()

    def _spawn_mole(self):
        self.mole_cell = random.randrange(len(self.cells))
        self.mole_timer = max(self.START_MOLE_TIME - self.hits * self.SPEEDUP_PER_HIT, self.MIN_MOLE_TIME)

    def update(self, dt):
        decay(self.flash, dt)
        if self.mole_cell is None:
            return
        self.mole_timer -= dt
        if self.mole_timer <= 0:
            self.mole_cell = None
            self.app.finish_game(self.hits)

    def handle_click(self, pos):
        if self.mole_cell is None:
            return
        for idx, rect in enumerate(self.cells):
            if rect.collidepoint(pos):
                if idx == self.mole_cell:
                    self.hits += 1
                    self.flash[idx] = 0.2
                    self.mole_cell = None
                    self._spawn_mole()
                else:
                    self.mole_cell = None
                    self.app.finish_game(self.hits)
                break

    def draw(self, surface):
        header(surface, self.app, "Whack-a-Mole", f"Hits: {self.hits}")
        for idx, rect in enumerate(self.cells):
            lit = idx == self.mole_cell or idx in self.flash
            pygame.draw.ellipse(surface, COLOR_TILE_LIT if lit else COLOR_TILE, rect)

# Rock-Paper-Scissors
class RPSGame:
    CHOICES = ["Rock", "Paper", "Scissors"]
    BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    def __init__(self, app):
        self.app = app
        self.wins = self.losses = self.ties = 0
        self.computer_choice = None
        self.result_text = ""
        self.result_color = COLOR_MUTED
        self.buttons = {c: Button((x, 320, 200, 90), c, font_size=30)
                         for c, x in zip(self.CHOICES, (60, 300, 540))}

    def update(self, dt):
        pass

    def handle_click(self, pos):
        for choice, btn in self.buttons.items():
            if btn.is_clicked(pos):
                self._play_round(choice)
                break

    def _play_round(self, player):
        computer = self.computer_choice = random.choice(self.CHOICES)
        if player == computer:
            self.ties += 1
            self.result_text, self.result_color = f"Tie! Both chose {player}", COLOR_MUTED
        elif self.BEATS[player] == computer:
            self.wins += 1
            self.result_text = f"You win! {player} beats {computer}"
            self.result_color = COLOR_TILE_LIT
        else:
            self.losses += 1
            self.result_text = f"You lose! {computer} beats {player}"
            self.result_color = COLOR_TILE_WRONG

    def draw(self, surface):
        draw_text(surface, "Rock - Paper - Scissors", self.app.font_med, COLOR_TEXT, (WIDTH // 2, 40))
        tally = f"Wins: {self.wins}   Losses: {self.losses}   Ties: {self.ties}"
        draw_text(surface, tally, self.app.font_small, COLOR_MUTED, (WIDTH // 2, 80))
        if self.computer_choice:
            draw_text(surface, f"Computer chose: {self.computer_choice}", self.app.font_med,
                       COLOR_TEXT, (WIDTH // 2, 170))
            draw_text(surface, self.result_text, self.app.font_med, self.result_color, (WIDTH // 2, 230))
        else:
            draw_text(surface, "Pick Rock, Paper or Scissors", self.app.font_med, COLOR_MUTED, (WIDTH // 2, 200))
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons.values():
            btn.draw(surface, mouse_pos)

# Reaction Time
class ReactionGame:
    ROUNDS = 5
    MIN_WAIT, MAX_WAIT = 1.0, 3.0

    def __init__(self, app):
        self.app = app
        self.round_num = 1
        self.times = []
        self.last_reaction = 0
        self._start_wait()

    def _start_wait(self):
        self.phase = "waiting"
        self.wait_timer = random.uniform(self.MIN_WAIT, self.MAX_WAIT)

    def update(self, dt):
        if self.phase == "waiting":
            self.wait_timer -= dt
            if self.wait_timer <= 0:
                self.phase, self.ready_tick = "ready", pygame.time.get_ticks()

    def handle_click(self, pos):
        if self.phase == "waiting":
            self.phase = "too_soon"
        elif self.phase == "too_soon":
            self._start_wait()
        elif self.phase == "ready":
            self.last_reaction = pygame.time.get_ticks() - self.ready_tick
            self.times.append(self.last_reaction)
            self.phase = "round_done"
        elif self.round_num < self.ROUNDS:
            self.round_num += 1
            self._start_wait()
        else:
            self.app.finish_game(round(sum(self.times) / len(self.times)))

    def draw(self, surface):
        mid = (WIDTH // 2, HEIGHT // 2)
        if self.phase in ("waiting", "too_soon"):
            surface.fill(COLOR_WAIT)
            too_soon = self.phase == "too_soon"
            title = "Too soon!" if too_soon else "Wait for green..."
            sub = "Tap to try again" if too_soon else f"Round {self.round_num} / {self.ROUNDS}"
            draw_text(surface, title, self.app.font_big, COLOR_TEXT, (mid[0], mid[1] - 20))
            draw_text(surface, sub, self.app.font_small, COLOR_TEXT, (mid[0], mid[1] + 40))
        elif self.phase == "ready":
            surface.fill(COLOR_GO)
            draw_text(surface, "Tap now!", self.app.font_big, COLOR_TEXT, mid)
        else:
            draw_text(surface, f"{self.last_reaction} ms", self.app.font_big, COLOR_TEXT, (mid[0], mid[1] - 20))
            draw_text(surface, "Tap to continue", self.app.font_small, COLOR_MUTED, (mid[0], mid[1] + 40))

GAME_CLASSES = {
    "memory": MemoryGame, "chimp": ChimpGame, "whack": WhackGame, "rps": RPSGame, "reaction": ReactionGame,
}

if __name__ == "__main__":
    App().run()