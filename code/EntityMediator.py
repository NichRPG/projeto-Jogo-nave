from code.Enimy import Enimy
from code.EnimyShot import EnimyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent: Entity):
        if isinstance(ent, Enimy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnimyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_colision_window(entity1)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
