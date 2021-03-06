import pygame
from PlanSprite import *
class PlanGame(object):
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprite()
    def startGame(self):
        print("游戏开始...")
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
            pass
    def __create_sprite(self):
        pass
    def __event_handler(self):
        pass
    def __check_collide(self):
        pass
    def __update_sprites(self):
        pass
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__':
    plangame = PlanGame()
    plangame.startGame()
