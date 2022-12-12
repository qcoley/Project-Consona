def cutscenes_apothis_bridge(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=-1)

    for alpha in range(0, 300):
        scene_1.set_alpha(alpha)
        screen.blit(scene_1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    pygame.time.delay(1000)

    for alpha in range(0, 300):
        scene_2.set_alpha(alpha)
        screen.blit(scene_2, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)
    pygame.time.delay(2000)

    for alpha in range(0, 300):
        scene_3.set_alpha(alpha)
        screen.blit(scene_3, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    pygame.time.delay(2000)

    for alpha in range(0, 300):
        scene_4.set_alpha(alpha)
        screen.blit(scene_4, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    pygame.time.delay(2000)

    for alpha in range(0, 300):
        scene_5.set_alpha(alpha)
        screen.blit(scene_5, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    pygame.time.delay(2000)

    for alpha in range(0, 300):
        scene_6.set_alpha(alpha)
        screen.blit(scene_6, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    pygame.time.delay(2000)

