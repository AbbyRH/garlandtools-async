# Enum with the following options: achievement, action, browse, fate, fishing, item, leve, map, mob, node, npc, quest, status, venture
from enum import Enum


class Type(Enum):
    ACHIEVEMENT = "achievement"
    ACTION = "action"
    BROWSE = "browse"
    FATE = "fate"
    FISHING = "fishing"
    ITEM = "item"
    LEVE = "leve"
    MAP = "map"
    MOB = "mob"
    NODE = "node"
    NPC = "npc"
    QUEST = "quest"
    STATUS = "status"
    VENTURE = "venture"