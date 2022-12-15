import time


def cutscenes_apothis_bridge(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6):
    pygame.mixer.music.fadeout(200)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=-1)

    # ------------------------------------------------------------------------------------------------------------------
    cutscene_tic = time.perf_counter()
    for alpha in range(0, 255):
        scene_1.set_alpha(alpha)
        screen.blit(scene_1, (0, 0))
        pygame.display.flip()

    cutscene_toc = time.perf_counter()
    cutscene_duration = cutscene_toc - cutscene_tic

    while cutscene_duration < 7:
        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

    # ------------------------------------------------------------------------------------------------------------------
    cutscene_tic = time.perf_counter()
    for alpha in range(0, 255):
        scene_2.set_alpha(alpha)
        screen.blit(scene_2, (0, 0))
        pygame.display.flip()

    cutscene_toc = time.perf_counter()
    cutscene_duration = cutscene_toc - cutscene_tic

    while cutscene_duration < 8:
        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

    # ------------------------------------------------------------------------------------------------------------------
    cutscene_tic = time.perf_counter()
    for alpha in range(0, 255):
        scene_3.set_alpha(alpha)
        screen.blit(scene_3, (0, 0))
        pygame.display.flip()

    cutscene_toc = time.perf_counter()
    cutscene_duration = cutscene_toc - cutscene_tic

    while cutscene_duration < 8:
        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

    # ------------------------------------------------------------------------------------------------------------------
    cutscene_tic = time.perf_counter()
    for alpha in range(0, 255):
        scene_4.set_alpha(alpha)
        screen.blit(scene_4, (0, 0))
        pygame.display.flip()

    cutscene_toc = time.perf_counter()
    cutscene_duration = cutscene_toc - cutscene_tic

    while cutscene_duration < 8:
        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

    # ------------------------------------------------------------------------------------------------------------------
    cutscene_tic = time.perf_counter()
    for alpha in range(0, 255):
        scene_5.set_alpha(alpha)
        screen.blit(scene_5, (0, 0))
        pygame.display.flip()

    cutscene_toc = time.perf_counter()
    cutscene_duration = cutscene_toc - cutscene_tic

    while cutscene_duration < 5:
        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

    # ------------------------------------------------------------------------------------------------------------------
    cutscene_tic = time.perf_counter()
    for alpha in range(0, 255):
        scene_6.set_alpha(alpha)
        screen.blit(scene_6, (0, 0))
        pygame.display.flip()

    cutscene_toc = time.perf_counter()
    cutscene_duration = cutscene_toc - cutscene_tic

    while cutscene_duration < 8:
        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic
