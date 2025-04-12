import random
import pygame

class Button():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False

class RpsGame():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        # Load images
        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()
        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()

        # Display buttons
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))

        # Initialize buttons
        self.rock_btn = Button(30, 520, (30, 520), 300, 140)
        self.paper_btn = Button(340, 520, (340, 520), 300, 140)
        self.scissors_btn = Button(640, 520, (640, 520), 300, 140)
 
        # Fonts and scores
        self.font = pygame.font.Font(('Splatch.ttf'), 90)
        self.text = self.font.render(f"", True, (255, 255, 255))
        self.pl_score = 0
        self.pc_score = 0

    def player(self):
        if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked(340):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        else:
            self.scissors_btn.clicked(640)
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (120, 200))
        return self.p_option

    def computer(self):
        self.pc_random_choice = ""
        option = ["rock", "paper", "scissors"]
        pc_choice_str = random.choice(option)
        self.pc_random_choice = pc_choice_str

        if pc_choice_str == "rock":
            pc_choice = self.choose_rock
        elif pc_choice_str == "paper":
            pc_choice = self.choose_paper
        else:
            pc_choice = self.choose_scissors

        self.screen.blit(pc_choice, (600, 200))
        return pc_choice

    def pl_score_cache(self):
        pl = self.p_option
        pc = self.pc_random_choice
        if (pl == "rock" and pc == "paper") or \
           (pl == "paper" and pc == "scissors") or \
           (pl == "scissors" and pc == "rock"):
            self.pc_score += 1
        elif pl == pc:
            pass
        else:
            self.pl_score += 1
        return self.pl_score

    def pc_score_cache(self):
        return self.pc_score

    def image_reset(self):
        self.text = self.font.render("", True, (0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            pygame.display.update()

            # Render and center score
            score_text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))
            text_rect = score_text.get_rect(center=(self.screen.get_width() // 2, 50))
            self.screen.blit(score_text, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked(30) or \
                       self.paper_btn.clicked(340) or \
                       self.scissors_btn.clicked(640):
                        self.image_reset()
                        self.player()
                        self.computer()
                        self.pl_score_cache()
                        self.pc_score_cache()

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = RpsGame()
    game.game_loop()
