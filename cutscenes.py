import time
import sys

from pygame import QUIT


def cutscenes_apothis_bridge(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, cutscene_tic,
                             skip_button, player_overlay, player_overlay_2, SCREEN_WIDTH, SCREEN_HEIGHT,
                             game_window):

    in_cutscene = True
    first_viewed = False
    second_viewed = False
    third_viewed = False
    fourth_viewed = False
    fifth_viewed = False
    sixth_viewed = False

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(loops=-1)

    while in_cutscene:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                sys.exit()
            init_pos = list(pygame.mouse.get_pos())
            ratio_x = (SCREEN_WIDTH / 1280)
            ratio_y = (SCREEN_HEIGHT / 720)
            pos = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)
            if event.type == pygame.MOUSEBUTTONUP:
                if skip_button.rect.collidepoint(pos):
                    in_cutscene = False

        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

        if SCREEN_WIDTH != 1280 and SCREEN_HEIGHT != 720:
            # ----------------------------------------------------------------------------------------------------------
            if not first_viewed:
                for alpha in range(0, 255):
                    scene_1.set_alpha(alpha)
                    screen.blit(scene_1, (0, 0))
                    screen.blit(player_overlay.surf, player_overlay.rect)
                    screen.blit(skip_button.surf, skip_button.rect)
                    frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    game_window.blit(frame, frame.get_rect())
                    pygame.display.flip()
                first_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 8:
                if not second_viewed:
                    for alpha in range(0, 255):
                        scene_2.set_alpha(alpha)
                        screen.blit(scene_2, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 16:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        screen.blit(scene_3, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 24:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        screen.blit(scene_4, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 32:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        screen.blit(scene_5, (0, 0))
                        screen.blit(player_overlay_2.surf, player_overlay_2.rect)
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fifth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 40:
                if not sixth_viewed:
                    for alpha in range(0, 255):
                        scene_6.set_alpha(alpha)
                        screen.blit(scene_6, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    sixth_viewed = True

            if cutscene_duration > 48:
                if sixth_viewed:
                    in_cutscene = False

        else:
            # ----------------------------------------------------------------------------------------------------------
            if not first_viewed:
                for alpha in range(0, 255):
                    scene_1.set_alpha(alpha)
                    game_window.blit(scene_1, (0, 0))
                    game_window.blit(player_overlay.surf, player_overlay.rect)
                    game_window.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                first_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 8:
                if not second_viewed:
                    for alpha in range(0, 255):
                        scene_2.set_alpha(alpha)
                        game_window.blit(scene_2, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 16:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        game_window.blit(scene_3, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 24:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        game_window.blit(scene_4, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 32:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        game_window.blit(scene_5, (0, 0))
                        game_window.blit(player_overlay_2.surf, player_overlay_2.rect)
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fifth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 40:
                if not sixth_viewed:
                    for alpha in range(0, 255):
                        scene_6.set_alpha(alpha)
                        game_window.blit(scene_6, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    sixth_viewed = True

            if cutscene_duration > 48:
                if sixth_viewed:
                    in_cutscene = False


def cutscenes_apothis_dreth(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, scene_7,
                            scene_8, cutscene_tic, skip_button, SCREEN_WIDTH, SCREEN_HEIGHT, game_window):

    in_cutscene = True
    first_viewed = False
    second_viewed = False
    third_viewed = False
    fourth_viewed = False
    fifth_viewed = False
    sixth_viewed = False
    seventh_viewed = False
    eighth_viewed = False

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(loops=-1)

    while in_cutscene:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                sys.exit()
            init_pos = list(pygame.mouse.get_pos())
            ratio_x = (SCREEN_WIDTH / 1280)
            ratio_y = (SCREEN_HEIGHT / 720)
            pos = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)
            if event.type == pygame.MOUSEBUTTONUP:
                if skip_button.rect.collidepoint(pos):
                    in_cutscene = False

        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

        if SCREEN_WIDTH != 1280 and SCREEN_HEIGHT != 720:
            # ----------------------------------------------------------------------------------------------------------
            if not first_viewed:
                for alpha in range(0, 255):
                    scene_1.set_alpha(alpha)
                    screen.blit(scene_1, (0, 0))
                    screen.blit(skip_button.surf, skip_button.rect)
                    frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    game_window.blit(frame, frame.get_rect())
                    pygame.display.flip()
                first_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 8:
                if not second_viewed:
                    for alpha in range(0, 255):
                        scene_2.set_alpha(alpha)
                        screen.blit(scene_2, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 16:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        screen.blit(scene_3, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 24:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        screen.blit(scene_4, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 32:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        screen.blit(scene_5, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fifth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 40:
                if not sixth_viewed:
                    for alpha in range(0, 255):
                        scene_6.set_alpha(alpha)
                        screen.blit(scene_6, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    sixth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 48:
                if not seventh_viewed:
                    for alpha in range(0, 255):
                        scene_7.set_alpha(alpha)
                        screen.blit(scene_7, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    seventh_viewed = True
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 56:
                if not eighth_viewed:
                    for alpha in range(0, 255):
                        scene_8.set_alpha(alpha)
                        screen.blit(scene_8, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    eighth_viewed = True

            if cutscene_duration > 64:
                if eighth_viewed:
                    in_cutscene = False

        else:
            # ----------------------------------------------------------------------------------------------------------
            if not first_viewed:
                for alpha in range(0, 255):
                    scene_1.set_alpha(alpha)
                    game_window.blit(scene_1, (0, 0))
                    game_window.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                first_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 8:
                if not second_viewed:
                    for alpha in range(0, 255):
                        scene_2.set_alpha(alpha)
                        game_window.blit(scene_2, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 16:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        game_window.blit(scene_3, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 24:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        game_window.blit(scene_4, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 32:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        game_window.blit(scene_5, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fifth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 40:
                if not sixth_viewed:
                    for alpha in range(0, 255):
                        scene_6.set_alpha(alpha)
                        game_window.blit(scene_6, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    sixth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 48:
                if not seventh_viewed:
                    for alpha in range(0, 255):
                        scene_7.set_alpha(alpha)
                        game_window.blit(scene_7, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    seventh_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 56:
                if not eighth_viewed:
                    for alpha in range(0, 255):
                        scene_8.set_alpha(alpha)
                        game_window.blit(scene_8, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    eighth_viewed = True

            if cutscene_duration > 64:
                if eighth_viewed:
                    in_cutscene = False
