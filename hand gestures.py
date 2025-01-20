import cv2
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the video window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hand Gesture Video Player")

# Set up the video player
video_path = "E:\Roshan\video.mp4"
cap = cv2.VideoCapture(video_path)

# Get video information
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_size = (width, height)

# Set up the Pygame clock
clock = pygame.time.Clock()

# Initialize variables for hand gesture control
prev_volume = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert OpenCV image to Pygame surface
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = np.rot90(img)
    img = pygame.surfarray.make_surface(img)
    img = pygame.transform.scale(img, (640, 480))

    # Display the video frame
    screen.blit(img, (0, 0))
    pygame.display.flip()

    # Check for hand gesture to control volume
    # Implement your hand gesture recognition logic here

    # Adjust volume based on hand gesture
    # The following line is a placeholder; you need to replace it with your volume control logic
    volume = 0.5  # Set a default volume level
    pygame.mixer.music.set_volume(volume)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Control frame rate
    clock.tick(int(fps))

# Release resources
pygame.quit()
cap.release()
cv2.destroyAllWindows()