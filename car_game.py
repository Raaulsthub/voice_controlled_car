import pygame
from speech_recog import SpeechRecognition

# speech recognition
recog = SpeechRecognition('./audio/audio.wav')

# Initialize Pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("My Game")

# Load the image for the square
square_image = pygame.image.load("images/car.png")

# Scale the image to 50% of its original size
square_image = pygame.transform.scale(square_image, (square_image.get_width() // 5, square_image.get_height() // 5))

# Get the size of the image
square_rect = square_image.get_rect()

# Set the initial position of the square
x_pos = 350
y_pos = 250

# Speed of the square
speed = 2

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set the initial state of the keys
key_up = key_down = key_left = key_right = False

# Initial angle of the image
angle = 0

# Loop until the user clicks the close button
done = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                text = recog.record_recognize()
                print(text)
                if (text == 'move forward'):
                    key_up = True
                    key_down = False
                    key_left = False
                    key_right = False
                elif (text == 'move backwards'):
                    key_up = False
                    key_down = True
                    key_left = False
                    key_right = False
                elif (text == 'move right'):
                    key_up = False
                    key_down = False
                    key_left = False
                    key_right = True
                elif (text == 'move left'):
                    key_up = False
                    key_down = False
                    key_left = True
                    key_right = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         key_up = True
        #         angle = 0
        #     elif event.key == pygame.K_s:
        #         key_down = True
        #         angle = 180 
        #     elif event.key == pygame.K_a:
        #         key_left = True
        #         angle = 90
        #     elif event.key == pygame.K_d:
        #         key_right = True
        #         angle = 270
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_w:
        #         key_up = False
        #     elif event.key == pygame.K_s:
        #         key_down = False
        #     elif event.key == pygame.K_a:
        #         key_left = False
        #     elif event.key == pygame.K_d:
        #         key_right = False

    # --- Game logic should go here
    if key_up:
        y_pos -= speed
    if key_down:
        y_pos += speed
    if key_left:
        x_pos -= speed
    if key_right:
        x_pos += speed

    # --- Drawing code should go here
    screen.fill((0, 0, 0))
    rotated_image = pygame.transform.rotate(square_image, angle)
    screen.blit(rotated_image, (x_pos, y_pos))
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
