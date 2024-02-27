

# MODULES
import pygame
import random
import create_image

# DD
RES = 16
DIMS = (40, 40)
SCREEN = (DIMS[0] * RES, DIMS[1] * RES)
display = pygame.display.set_mode(SCREEN)
TILES = "tiles"
PATH = f"./{TILES}/res_{RES}/"
PATH_METADATA = f"./metadata.txt"


def rotate_sockets(sockets, angle):
    return [sockets[i - angle] for i in range(4)]


# Metadata parser
# metadata = [Dict, ...]
metadata = []
with open(PATH_METADATA, "r") as file:
    file = file.readlines()
    for line in file:
        line = line.strip().split("\t")
        if line[5] == "1":
            metaEntry = {
                "ID": line[0],
                "SOCKETS": [line[1], line[2], line[3], line[4]],
                "FIXED": True,
                "ROTATION": 0
            }
            metadata.append(metaEntry)
        else:
            for a in range(4):
                metaEntry = {
                    "ID": line[0],
                    "SOCKETS": rotate_sockets([line[1], line[2], line[3], line[4]], a),
                    "FIXED": False,
                    "ROTATION": a
                }
                metadata.append(metaEntry)


class Tile:
    def __init__(self, c, r):
        self.c = c
        self.r = r
        self.x = self.c * RES
        self.y = self.r * RES
        self.img = pygame.image.load(PATH + f"{metadata[-1]['ID']}.png")
        self.rect = self.img.get_rect()
        self.rect.top_left = self.x, self.y
        # attr. related to WFC
        self.entropy = len(metadata)
        self.potential = list(metadata)
        self.collapsed = False
        self.sockets = ["" for _ in range(4)]
        self.RIGHT_neighbour = {"COLLAPSED": None, "SOCKETS": None}
        self.DOWN_neighbour = {"COLLAPSED": None, "SOCKETS": None}
        self.LEFT_neighbour = {"COLLAPSED": None, "SOCKETS": None}
        self.UP_neighbour = {"COLLAPSED": None, "SOCKETS": None}

    def draw(self):
        display.blit(self.img, self.rect)

    def updateEntropy(self,lowestEntropy):
        placeHolderTileSet = []
        for potentialTile in self.potentialTiles:
            validTile = True
            if self.RIGHT_neighbour["COLLAPSED"] and not socketMatch(potentialTile["SOCKETS"][0],self.RIGHT_neighbour["SOCKETS"]):
                validTile = False
