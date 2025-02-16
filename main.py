import pygame

# Initialize Pygame
pygame.init()

HEIGHT = 512
WIDTH = 512
DIMENSION = 8
square_size = HEIGHT // DIMENSION
MAX_FPS = 20

# Piece images
IMAGES = {
    "wkg": "wkg.png", "wq": "wq.png", "wr": "wr.png", "wb": "wb.png", "wk": "wk.png", "wp": "wp.png",
    "bkg": "bkg.png", "bq": "bq.png", "br": "br.png", "bb": "bb.png", "bk": "bk.png", "bp": "bp.png"
}
COLORS = [pygame.Color("white"), pygame.Color("grey")]

class Board:
    def __init__(self):
        pygame.display.set_caption("Chess Game")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # Initialize board state
        self.board = [
            ["br", "bk", "bb", "bq", "bkg", "bb", "bk", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo"],
            ["oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo"],
            ["oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo"],
            ["oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wk", "wb", "wq", "wkg", "wb", "wk", "wr"]
        ]

        # Preload images
        self.piece_images = {}
        for key, path in IMAGES.items():
            img = pygame.image.load(path)
            self.piece_images[key] = pygame.transform.scale(img, (square_size, square_size))

    def draw_board(self):
        """Draws the chessboard."""
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                color = COLORS[(row + col) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

    def draw_pieces(self):
        """Draws chess pieces on the board."""
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                piece = self.board[row][col]
                if piece in self.piece_images:
                    self.screen.blit(self.piece_images[piece], (col * square_size, row * square_size))

    def display_board(self):
        """Main game loop."""
        running = True
        square_selected = None  # Tracks the selected piece
        clicks = []  # Stores [(row, col), (target_row, target_col)]

        while running:
            self.draw_board()
            self.draw_pieces()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    col = mouse_pos[0] // square_size
                    row = mouse_pos[1] // square_size

                    if square_selected == (row, col):
                        square_selected = None  # Deselect
                        clicks = []
                    else:
                        square_selected = (row, col)
                        clicks.append(square_selected)

                    # Handle second click (attempt move)
                    if len(clicks) == 2:
                        row1, col1 = clicks[0]
                        row2, col2 = clicks[1]

                        # Move piece if destination is empty or valid
                        # Move only to empty spaces
                        self.board[row2][col2] = self.board[row1][col1]
                        self.board[row1][col1] = "oo"

                        square_selected = None  # Reset selection
                        clicks = []

            self.clock.tick(MAX_FPS)

        pygame.quit()
        exit()

# Run the game
game = Board()
game.display_board()


