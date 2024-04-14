import time
import sys

from pygame import QUIT


def cutscenes_apothis_bridge(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, cutscene_tic,
                             skip_button, player_overlay, player_overlay_2, SCREEN_WIDTH, SCREEN_HEIGHT,
                             game_window, time_of_day, scene_1_night, scene_2_night, scene_3_night, scene_4_night,
                             scene_5_night, scene_6_night):

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
                    if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                        scene_1_night.set_alpha(alpha)
                        screen.blit(scene_1_night, (0, 0))
                    else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_2_night.set_alpha(alpha)
                            screen.blit(scene_2_night, (0, 0))
                        else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_3_night.set_alpha(alpha)
                            screen.blit(scene_3_night, (0, 0))
                        else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_4_night.set_alpha(alpha)
                            screen.blit(scene_4_night, (0, 0))
                        else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_5_night.set_alpha(alpha)
                            screen.blit(scene_5_night, (0, 0))
                        else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_6_night.set_alpha(alpha)
                            screen.blit(scene_6_night, (0, 0))
                        else:
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
                    if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                        scene_1_night.set_alpha(alpha)
                        game_window.blit(scene_1_night, (0, 0))
                    else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_2_night.set_alpha(alpha)
                            game_window.blit(scene_2_night, (0, 0))
                        else:
                            scene_2.set_alpha(alpha)
                            game_window.blit(scene_2, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 16:
                if not third_viewed:
                    for alpha in range(0, 255):
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_3_night.set_alpha(alpha)
                            game_window.blit(scene_3_night, (0, 0))
                        else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_4_night.set_alpha(alpha)
                            game_window.blit(scene_4_night, (0, 0))
                        else:
                            scene_4.set_alpha(alpha)
                            game_window.blit(scene_4, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 32:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_5_night.set_alpha(alpha)
                            game_window.blit(scene_5_night, (0, 0))
                        else:
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
                        if time_of_day == 0 or time_of_day == 6 or time_of_day == 7:
                            scene_6_night.set_alpha(alpha)
                            game_window.blit(scene_6_night, (0, 0))
                        else:
                            scene_6.set_alpha(alpha)
                            game_window.blit(scene_6, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    sixth_viewed = True

            if cutscene_duration > 48:
                if sixth_viewed:
                    in_cutscene = False

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


def cutscenes_apothis_dreth(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, scene_7,
                            scene_8, cutscene_tic, skip_button, SCREEN_WIDTH, SCREEN_HEIGHT, game_window):

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


def cutscenes_final_dreth(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, scene_7,
                          scene_8, scene_9, scene_10, scene_11, scene_12, scene_13, scene_14, cutscene_tic, skip_button,
                          SCREEN_WIDTH, SCREEN_HEIGHT, game_window, big_hp_bar, big_hp_2, big_hp_3, big_hp_4, big_hp_5,
                          big_hp_6, big_hp_7, big_hp_8, big_hp_9, big_hp_10, big_hp_11, big_hp_12, big_hp_13, big_hp_14,
                          big_hp_15, big_hp_16, big_hp_17, big_hp_18, big_hp_19, big_hp_20, big_hp_21, big_hp_22,
                          big_hp_23, big_hp_24, big_hp_25):

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    in_cutscene = True
    first_viewed = False
    second_viewed = False
    third_viewed = False
    fourth_viewed = False
    fifth_viewed = False
    sixth_viewed = False
    seventh_viewed = False
    eighth_viewed = False
    ninth_viewed = False
    tenth_viewed = False
    eleventh_viewed = False
    twelfth_viewed = False
    thirteenth_viewed = False
    fourteenth_viewed = False

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
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 64:
                if not ninth_viewed:
                    for alpha in range(0, 255):
                        scene_9.set_alpha(alpha)
                        screen.blit(scene_9, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    ninth_viewed = True
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 72:
                if not tenth_viewed:
                    for alpha in range(0, 255):
                        scene_10.set_alpha(alpha)
                        screen.blit(scene_10, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    tenth_viewed = True
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 80:
                if not eleventh_viewed:
                    for alpha in range(0, 255):
                        scene_11.set_alpha(alpha)
                        screen.blit(scene_11, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    eleventh_viewed = True
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 88:
                if not twelfth_viewed:
                    for alpha in range(0, 255):
                        scene_12.set_alpha(alpha)
                        screen.blit(scene_12, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    twelfth_viewed = True
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 96:
                if not thirteenth_viewed:
                    for alpha in range(0, 255):
                        scene_13.set_alpha(alpha)
                        screen.blit(scene_13, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    thirteenth_viewed = True
            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 104:
                if not fourteenth_viewed:
                    for alpha in range(0, 255):
                        scene_14.set_alpha(alpha)
                        screen.blit(scene_14, (0, 0))
                        screen.blit(skip_button.surf, skip_button.rect)
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fourteenth_viewed = True

            if 105 > cutscene_duration > 104.5:
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 105.5 > cutscene_duration > 105:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_2)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 106 > cutscene_duration > 105.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_3)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 106.5 > cutscene_duration > 106:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_4)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 107 > cutscene_duration > 106.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_5)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 107.5 > cutscene_duration > 107:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_6)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 108 > cutscene_duration > 107.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_7)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 108.5 > cutscene_duration > 108:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_8)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 109 > cutscene_duration > 108.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_9)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 109.5 > cutscene_duration > 109:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_10)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 110 > cutscene_duration > 109.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_11)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 110.5 > cutscene_duration > 110:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_12)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 111 > cutscene_duration > 110.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_13)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 111.5 > cutscene_duration > 111:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_14)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 112 > cutscene_duration > 111.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_15)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 112.5 > cutscene_duration > 112:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_16)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 113 > cutscene_duration > 112.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_17)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 113.5 > cutscene_duration > 113:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_18)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 114 > cutscene_duration > 113.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_19)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 114.5 > cutscene_duration > 114:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_20)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 115 > cutscene_duration > 114.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_21)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 115.5 > cutscene_duration > 115:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_22)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 116 > cutscene_duration > 115.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_23)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 116.5 > cutscene_duration > 116:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_24)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()
            if 117 > cutscene_duration > 116.5:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_25)
                screen.blit(big_hp_bar.surf, big_hp_bar.rect)
                frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                game_window.blit(frame, frame.get_rect())
                pygame.display.flip()

            if cutscene_duration > 118:
                if fourteenth_viewed:
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
            if cutscene_duration > 14:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        game_window.blit(scene_3, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 22:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        game_window.blit(scene_4, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 30:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        game_window.blit(scene_5, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fifth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 38:
                if not sixth_viewed:
                    for alpha in range(0, 255):
                        scene_6.set_alpha(alpha)
                        game_window.blit(scene_6, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    sixth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 44:
                if not seventh_viewed:
                    for alpha in range(0, 255):
                        scene_7.set_alpha(alpha)
                        game_window.blit(scene_7, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    seventh_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 50:
                if not eighth_viewed:
                    for alpha in range(0, 255):
                        scene_8.set_alpha(alpha)
                        game_window.blit(scene_8, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    eighth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 56:
                if not ninth_viewed:
                    for alpha in range(0, 255):
                        scene_9.set_alpha(alpha)
                        game_window.blit(scene_9, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    ninth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 64:
                if not tenth_viewed:
                    for alpha in range(0, 255):
                        scene_10.set_alpha(alpha)
                        game_window.blit(scene_10, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    tenth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 72:
                if not eleventh_viewed:
                    for alpha in range(0, 255):
                        scene_11.set_alpha(alpha)
                        game_window.blit(scene_11, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    eleventh_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 80:
                if not twelfth_viewed:
                    for alpha in range(0, 255):
                        scene_12.set_alpha(alpha)
                        game_window.blit(scene_12, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    twelfth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 88:
                if not thirteenth_viewed:
                    for alpha in range(0, 255):
                        scene_13.set_alpha(alpha)
                        game_window.blit(scene_13, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    thirteenth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 94:
                if not fourteenth_viewed:
                    for alpha in range(0, 255):
                        scene_14.set_alpha(alpha)
                        game_window.blit(scene_14, (0, 0))
                        game_window.blit(skip_button.surf, skip_button.rect)
                        pygame.display.flip()
                    fourteenth_viewed = True

            if 94.50 > cutscene_duration > 94.25:
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 94.75 > cutscene_duration > 94.50:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_2)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 95 > cutscene_duration > 94.75:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_3)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 95.25 > cutscene_duration > 95:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_4)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 95.50 > cutscene_duration > 95.25:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_5)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 95.75 > cutscene_duration > 95.50:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_6)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 96 > cutscene_duration > 95.75:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_7)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 96.25 > cutscene_duration > 96:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_8)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 96.50 > cutscene_duration > 96.25:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_9)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 96.75 > cutscene_duration > 96.50:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_10)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 97 > cutscene_duration > 96.75:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_11)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 97.25 > cutscene_duration > 97:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_12)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 97.50 > cutscene_duration > 97.25:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_13)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 97.75 > cutscene_duration > 97.50:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_14)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 98 > cutscene_duration > 97.75:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_15)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 98.25 > cutscene_duration > 98:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_16)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 98.50 > cutscene_duration > 98.25:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_17)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 98.75 > cutscene_duration > 98.50:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_18)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 99 > cutscene_duration > 98.75:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_19)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 99.25 > cutscene_duration > 99:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_20)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 99.50 > cutscene_duration > 99.25:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_21)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 99.75 > cutscene_duration > 99.50:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_22)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 100 > cutscene_duration > 99.75:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_23)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 100.25 > cutscene_duration > 100:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_24)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()
            if 100.50 > cutscene_duration > 100.25:
                big_hp_bar.update(big_hp_bar.x_coordinate, big_hp_bar.y_coordinate, big_hp_25)
                game_window.blit(big_hp_bar.surf, big_hp_bar.rect)
                pygame.display.flip()

            if cutscene_duration > 101:
                if fourteenth_viewed:
                    in_cutscene = False

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


def cutscenes_credits(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, cutscene_tic,
                      SCREEN_WIDTH, SCREEN_HEIGHT, game_window):

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    in_cutscene = True
    first_viewed = False
    second_viewed = False
    third_viewed = False
    fourth_viewed = False
    fifth_viewed = False

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(50)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(loops=0)

    while in_cutscene:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                sys.exit()

        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

        if SCREEN_WIDTH != 1280 and SCREEN_HEIGHT != 720:
            # ----------------------------------------------------------------------------------------------------------
            if not first_viewed:
                for alpha in range(0, 255):
                    scene_1.set_alpha(alpha)
                    screen.blit(scene_1, (0, 0))
                    frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    game_window.blit(frame, frame.get_rect())
                    pygame.display.flip()
                first_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 15:
                if not second_viewed:
                    for alpha in range(0, 255):
                        scene_2.set_alpha(alpha)
                        screen.blit(scene_2, (0, 0))
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 30:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        screen.blit(scene_3, (0, 0))
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 45:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        screen.blit(scene_4, (0, 0))
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 60:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        screen.blit(scene_5, (0, 0))
                        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        game_window.blit(frame, frame.get_rect())
                        pygame.display.flip()
                    fifth_viewed = True

            if cutscene_duration > 75:
                if fifth_viewed:
                    in_cutscene = False

        else:
            # ----------------------------------------------------------------------------------------------------------
            if not first_viewed:
                for alpha in range(0, 255):
                    scene_1.set_alpha(alpha)
                    game_window.blit(scene_1, (0, 0))
                    pygame.display.flip()
                first_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 15:
                if not second_viewed:
                    for alpha in range(0, 255):
                        scene_2.set_alpha(alpha)
                        game_window.blit(scene_2, (0, 0))
                        pygame.display.flip()
                    second_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 30:
                if not third_viewed:
                    for alpha in range(0, 255):
                        scene_3.set_alpha(alpha)
                        game_window.blit(scene_3, (0, 0))
                        pygame.display.flip()
                    third_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 45:
                if not fourth_viewed:
                    for alpha in range(0, 255):
                        scene_4.set_alpha(alpha)
                        game_window.blit(scene_4, (0, 0))
                        pygame.display.flip()
                    fourth_viewed = True

            # ----------------------------------------------------------------------------------------------------------
            if cutscene_duration > 60:
                if not fifth_viewed:
                    for alpha in range(0, 255):
                        scene_5.set_alpha(alpha)
                        game_window.blit(scene_5, (0, 0))
                        pygame.display.flip()
                    fifth_viewed = True

            if cutscene_duration > 75:
                if fifth_viewed:
                    in_cutscene = False

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
