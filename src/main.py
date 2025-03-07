# Creation by T.E.C.H. Club Games Division, College of the Canyons 2025
# Developers: 1. Aram Aprahamian, 2. [name], 3. [name]
import pygame
import pygame_gui

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAME_RATE_CAP = 60

PLAYER_1_LEFT = pygame.K_a
PLAYER_1_RIGHT = pygame.K_d

PLAYER_2_LEFT = pygame.K_LEFT
PLAYER_2_RIGHT = pygame.K_RIGHT

def main():
    print("Initializing Space Tanks...")

    # Initialize Pygame
    pygame.init()
    # Set window size
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    # Create the window
    window = pygame.display.set_mode(window_size)
    # Set the window title
    pygame.display.set_caption("Space Tanks")
    # Create a clock
    clock = pygame.time.Clock()

    # Set the frame rate
    clock.tick(FRAME_RATE_CAP)

    # Create event loop
    is_running = True
    is_paused = False
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_paused = not is_paused
                    if is_paused:
                        pygame.time.set_timer(pygame.USEREVENT, 0)
                        print("Game is paused")
                    else:
                        pygame.time.set_timer(pygame.USEREVENT, 1000 // FRAME_RATE_CAP)
                        print("Game is unpaused")
                if event.key == PLAYER_1_RIGHT:
                    print("Player 1 right")
                if event.key == PLAYER_1_LEFT:
                    print("Player 1 left")
                if event.key == PLAYER_2_RIGHT:
                    print("Player 2 right")
                if event.key == PLAYER_2_LEFT:
                    print("Player 2 left")

        # Update the window
        pygame.display.update()
        pygame.display.flip()
    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()