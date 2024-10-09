import pygame

pygame.init()

screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("France")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

british_flag = pygame.image.load('flag.png')
british_flag = pygame.transform.scale(british_flag, (200, 120))

bag_image = pygame.image.load('backup bag.jpg')

tower_image = pygame.image.load('tower.png')
tower_image = pygame.transform.scale(tower_image, (200, 200))

shakespeare_image = pygame.image.load('napoleon.jpg')
shakespeare_image = pygame.transform.scale(shakespeare_image, (200, 200))

font_title = pygame.font.Font(None, 80)
font_subtitle = pygame.font.Font(None, 40)
font_text = pygame.font.Font(None, 30)

title_text = font_title.render("Welcome to France", True, RED)
subtitle_text = font_subtitle.render("Famous for its rich history and culture", True, BLUE)
fact1 = font_text.render("France is known for its interesting language", True, WHITE)
fact2 = font_text.render("and cultural contributions. It has been home to iconic", True, WHITE)
fact3 = font_text.render("The creator(Gabe) likes listening to french music", True, WHITE)
fact31 = font_text.render("and is interested in the culture", True, WHITE)
fact4 = font_text.render("french people have alot of iconic foods", True, WHITE)
fact5 = font_text.render("history and modernity, with sights such as the Eiffel tower", True, WHITE)

pygame.mixer.music.load("french song i like.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))

    pygame.draw.rect(screen, RED, [50, 100, 900, 5])
    pygame.draw.rect(screen, RED, [50, 500, 900, 5])

    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 20))
    screen.blit(subtitle_text, (300, 150))
    screen.blit(fact1, (300, 200))
    screen.blit(fact2, (300, 230))
    screen.blit(fact3, (300, 260))
    screen.blit(fact31, (300,290))
    screen.blit(fact4, (300, 320))
    screen.blit(fact5, (300, 350))

    screen.blit(british_flag, (25, 150))
    screen.blit(bag_image, (0, 375))
    screen.blit(tower_image, (420, 400))
    screen.blit(shakespeare_image, (800, 400))

    pygame.display.flip()

pygame.quit()
