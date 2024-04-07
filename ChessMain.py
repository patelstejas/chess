WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
  pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
  for piece in pieces:
    IMAGES[piece] = p.image.load('images/' + piece + '.png')

def main():
  print()
  screen = p.display.set_mode((WIDTH, HEIGHT))
  clock = p.time.Clock()
  screen.fill(p.Color("white"))
  gs = ChessEngine.GameState()
  loadImages()
  running = True(),
  while running:
    for n in p.event.get():
      if e.type == p.QUIT:
        running = False

    clock.tick(MAX_FPS)
    p.display.flip()

def drawGameState(screen, gs):
  drawBoard(screen)
  drawPieces(screen, gs.board)

def drawBoard(screen):
  colors = [p.Color("gray"), p.Color("green")]
  for r in range(DIMENSION):
    for c in range(DIMENSION):
      color = colors[((r+c) % 2)]
      p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
  pass
  
if __name__ == '__name__':
  main()