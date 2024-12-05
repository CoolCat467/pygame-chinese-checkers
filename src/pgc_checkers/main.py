from pgc_checkers.game_logic.loops import *
from pgc_checkers.game_logic.game import *
from pgc_checkers.game_logic.player import *
from pgc_checkers.game_logic.literals import *
import pygame


def run():
    """Main entry point."""
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.SRCALPHA)
    pygame.display.set_caption('Chinese Checkers')

    lc = LoopController()

    while True:
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() """
        lc.mainLoop(window)


if __name__ == "__main__":
    run()
