

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

def socketMatch(socket, targetSocket):
    for index_letter,_ in enumerate(socket):
        if socket[index_letter] != targetSocket[-(index_letter+1)]:
            return False
    return True

class Tile:
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.x = self.column * RES
        self.y = self.row * RES
        self.img = pygame.image.load(PATH + f"{metadata[-1]['ID']}.png")
        self.rect = self.img.get_rect()
        self.rect.top_left = self.x, self.y
        # attr. related to WFC
        self.entropy = len(metadata)
        self.potential = list(metadata)
        self.collapsed = False
        self.sockets = ["" for _ in range(4)]
        self.RIGHT_neighbour = {"COLLAPSED": None, "SOCKET": None}
        self.DOWN_neighbour = {"COLLAPSED": None, "SOCKET": None}
        self.LEFT_neighbour = {"COLLAPSED": None, "SOCKET": None}
        self.UP_neighbour = {"COLLAPSED": None, "SOCKET": None}

    def draw(self):
        display.blit(self.img, self.rect)

    def updateEntropy(self,lowestEntropy):
        placeHolderTileSet = []
        for potentialTile in self.potential:
            validTile = True
            if self.RIGHT_neighbour["COLLAPSED"] and not socketMatch(potentialTile["SOCKETS"][0],self.RIGHT_neighbour["SOCKET"]):
                validTile = False
            if self.DOWN_neighbour["COLLAPSED"] and not socketMatch(potentialTile["SOCKETS"][1],self.DOWN_neighbour["SOCKET"]):
                validTile = False
            if self.LEFT_neighbour["COLLAPSED"] and not socketMatch(potentialTile["SOCKETS"][2],self.LEFT_neighbour["SOCKET"]):
                validTile = False
            if self.UP_neighbour["COLLAPSED"] and not socketMatch(potentialTile["SOCKETS"][3],self.UP_neighbour["SOCKET"]):
                validTile = False
            if validTile:
                placeHolderTileSet.append(potentialTile)
        self.potential = placeHolderTileSet

        seen = []
        for tile in self.potential:
            if tile["ID"] not in seen:
                seen.append(tile["ID"])
        self.entropy = len(seen)
        if self.entropy < lowestEntropy or lowestEntropy == None:
            return self.entropy
        return lowestEntropy

    def updateNeighbors(self):
        if not self.collapsed:
            column = self.column
            row = self.row
            if column < DIMS[0]-1:
                self.RIGHT_neighbour = {"COLLAPSED":grid[column+1][row].collapsed,"SOCKET":grid[column+1][row].sockets[2]}
            if row < DIMS[1]-1:
                self.DOWN_neighbour = {"COLLAPSED":grid[column][row+1].collapsed,"SOCKET":grid[column][row+1].sockets[3]}
            if column > 0:
                self.LEFT_neighbour = {"COLLAPSED":grid[column-1][row].collapsed,"SOCKET":grid[column-1][row].sockets[0]}
            if row > 0:
                self.UP_neighbour = {"COLLAPSED":grid[column][row-1].collapsed,"SOCKET":grid[column][row-1].sockets[1]}

    def collapse(self):
        self.collapsed = True
        if len(self.potential) > 0:
            potentialTile = random.choice(self.potential)
        else:
            potentialTile = metadata[-1]
        self.name = potentialTile["ID"]
        self.img = pygame.image.load(f"{PATH}/{self.name}.png")
        self.sockets = potentialTile["SOCKETS"]
        self.entropy = 0
        self.img = pygame.transform.rotate(self.img, -90 * potentialTile["ROTATION"])
