import pygame
import math


def draw_arm(screen, startPos, image, direction):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if direction == 1:  
        offset_x, offset_y = -10, -18  # Offset from the startPos parameter
    if direction == 0:
        offset_x, offset_y = -12, -18  # Offset from the startPos parameter
    start_x, start_y = startPos[0] + offset_x, startPos[1] + offset_y

    dx = mouse_x - start_x
    dy = mouse_y - start_y
    angle = math.atan2(dy, dx)

    # Calculate the angle in degrees for rotation
    rotation_angle_deg = math.degrees(angle) + 270

    # Calculate the position to draw the rotated image
    image_rect = image.get_rect(center=(start_x,start_y))
    rotated_image = pygame.transform.rotozoom(image, -rotation_angle_deg, 1.0)

    rotated_rect = rotated_image.get_rect(center=image_rect.midtop)

    # Draw the rotated image
    screen.blit(rotated_image, rotated_rect.topleft)