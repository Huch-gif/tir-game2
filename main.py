
import pygame
import random
import sys
import time


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tir-game2: Яблочная мишень")


BACKGROUND_COLORS = [(173, 216, 230), (144, 238, 144), (255, 223, 0)]  # светло-голубой, светло-зелёный, золотой


font = pygame.font.SysFont("Arial", 24)


try:
    apple_image = pygame.image.load("img.png")
except FileNotFoundError:
    print(" Используется замена — красный круг.")
    apple_image = pygame.Surface((60, 60), pygame.SRCALPHA)
    pygame.draw.circle(apple_image, (255, 0, 0), (30, 30), 30)

apple_size = (60, 60)
apple_image = pygame.transform.scale(apple_image, apple_size)


def random_position():
    x = random.randint(0, WIDTH - apple_size[0])
    y = random.randint(0, HEIGHT - apple_size[1])
    return x, y

apple_rect = pygame.Rect(random_position(), apple_size)


bg_index = 0


hits = 0
start_time = time.time()
total_time = 30  # Игра длится 30 секунд



clock = pygame.time.Clock()


running = True
while running:
    elapsed_time = time.time() - start_time
    remaining_time = max(0, int(total_time - elapsed_time))

    if remaining_time == 0:
        print("Время вышло!")
        running = False
        break

    screen.fill(BACKGROUND_COLORS[bg_index])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
            break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if apple_rect.collidepoint(mouse_pos):
                hits += 1
                apple_rect.x, apple_rect.y = random_position()
                bg_index = (bg_index + 1) % len(BACKGROUND_COLORS)


    screen.blit(apple_image, apple_rect)


    mx, my = pygame.mouse.get_pos()
    pygame.draw.line(screen, (255, 0, 0), (mx - 10, my), (mx + 10, my), 2)
    pygame.draw.line(screen, (255, 0, 0), (mx, my - 10), (mx, my + 10), 2)


    score_text = font.render(f"Попаданий: {hits}", True, (0, 0, 0))
    time_text = font.render(f"Осталось: {remaining_time} с", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (WIDTH - 200, 10))


    pygame.display.flip()
    clock.tick(60)

end_screen = True
while end_screen:
    screen.fill((0, 0, 0))
    result_text = font.render(f"Игра окончена! Попаданий: {hits}", True, (255, 255, 255))
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            end_screen = False

pygame.mixer.music.stop()
pygame.quit()
sys.exit()