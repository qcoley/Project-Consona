def character_screen_draw(screen, race, amuna_character_screen, nuldar_character_screen, sorae_character_screen,
                          character_select_overlay, amuna_select_overlay, amuna_character, nuldar_select_overlay,
                          nuldar_character, sorae_select_overlay, sorae_character, amuna_button, nuldar_button,
                          sorae_button, start_button, back_button, name_input, name_input_font, character_name_input,
                          pygame):

    if race == "amuna":
        screen.blit(amuna_character_screen, (0, 0))
        screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        screen.blit(amuna_button.surf, amuna_button.rect)
        screen.blit(nuldar_button.surf, nuldar_button.rect)
        screen.blit(sorae_button.surf, sorae_button.rect)
        screen.blit(amuna_select_overlay.surf, amuna_select_overlay.rect)
        screen.blit(amuna_character.surf, amuna_character.rect)
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(back_button.surf, back_button.rect)
        screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        screen.blit(character_name_surface, (605, 575))

    if race == "nuldar":
        screen.blit(nuldar_character_screen, (0, 0))
        screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        screen.blit(amuna_button.surf, amuna_button.rect)
        screen.blit(nuldar_button.surf, nuldar_button.rect)
        screen.blit(sorae_button.surf, sorae_button.rect)
        screen.blit(nuldar_select_overlay.surf, nuldar_select_overlay.rect)
        screen.blit(nuldar_character.surf, nuldar_character.rect)
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(back_button.surf, back_button.rect)
        screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        screen.blit(character_name_surface, (605, 575))

    if race == "sorae":
        screen.blit(sorae_character_screen, (0, 0))
        screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        screen.blit(amuna_button.surf, amuna_button.rect)
        screen.blit(nuldar_button.surf, nuldar_button.rect)
        screen.blit(sorae_button.surf, sorae_button.rect)
        screen.blit(sorae_select_overlay.surf, sorae_select_overlay.rect)
        screen.blit(sorae_character.surf, sorae_character.rect)
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(back_button.surf, back_button.rect)
        screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        screen.blit(character_name_surface, (605, 575))
