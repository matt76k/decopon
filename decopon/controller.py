from abc import ABC, abstractmethod
from typing import Tuple

import pygame


class Controller(ABC):
    @abstractmethod
    def update(self, info) -> Tuple[bool, bool, bool]:
        return True, True, True


class Human(Controller):
    def __init__(self) -> None:
        super().__init__()

    def update(self, info) -> Tuple[bool, bool, bool]:
        pressedKeys = pygame.key.get_pressed()
        return pressedKeys[pygame.K_LEFT], pressedKeys[pygame.K_RIGHT], pressedKeys[pygame.K_SPACE]
