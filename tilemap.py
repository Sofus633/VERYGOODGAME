from storage import *

class TileMap:
    def __init__(self, map, screen, tiles_path):
        self.map = map
        self.tiles = []
        self.screen = screen
        self.tilesimg = tiles_path
        self.cut_tiles()
    def display(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                screen.blit(self.tiles[self.map[x][y]], (x * TILE_SIZE, y * TILE_SIZE))
                
    def cut_tiles(self):
        
        tiles_img = pygame.image.load(self.tilesimg).convert_alpha()
        Number_tiles = math.ceil(tiles_img.get_size()[0] / TILE_SIZE)
        for x in range(0, Number_tiles):
            print(x * TILE_SIZE)
            left = x * TILE_SIZE
            top = 0
            print(left, top)
            rect = pygame.Rect(left, top, TILE_SIZE, TILE_SIZE)
            tile = tiles_img.subsurface(rect)
            self.tiles.append(tile)