def character_screen_draw(screen, race, gender, amuna_character_screen, nuldar_character_screen, sorae_character_screen,
                          character_select_overlay, amuna_select_overlay, amuna_male_character, amuna_female_character,
                          nuldar_select_overlay, nuldar_male_character, nuldar_female_character, sorae_select_overlay,
                          sorae_alpha_character, sorae_beta_character, amuna_button, nuldar_button, sorae_button,
                          start_button, back_button, name_input, name_input_font, character_name_input,
                          amuna_male_button, amuna_female_button, nuldar_male_button, nuldar_female_button,
                          sorae_alpha_button, sorae_beta_button):

    if race == "amuna":
        screen.blit(amuna_character_screen, (0, 0))
        screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        screen.blit(amuna_button.surf, amuna_button.rect)
        screen.blit(amuna_male_button.surf, amuna_male_button.rect)
        screen.blit(amuna_female_button.surf, amuna_female_button.rect)
        screen.blit(nuldar_button.surf, nuldar_button.rect)
        screen.blit(nuldar_male_button.surf, nuldar_male_button.rect)
        screen.blit(nuldar_female_button.surf, nuldar_female_button.rect)
        screen.blit(sorae_button.surf, sorae_button.rect)
        screen.blit(sorae_alpha_button.surf, sorae_alpha_button.rect)
        screen.blit(sorae_beta_button.surf, sorae_beta_button.rect)
        screen.blit(amuna_select_overlay.surf, amuna_select_overlay.rect)
        if gender == "male":
            screen.blit(amuna_male_character.surf, amuna_male_character.rect)
        if gender == "female":
            screen.blit(amuna_female_character.surf, amuna_female_character.rect)
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(back_button.surf, back_button.rect)
        screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        screen.blit(character_name_surface, (605, 569))

    if race == "nuldar":
        screen.blit(nuldar_character_screen, (0, 0))
        screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        screen.blit(amuna_button.surf, amuna_button.rect)
        screen.blit(amuna_male_button.surf, amuna_male_button.rect)
        screen.blit(amuna_female_button.surf, amuna_female_button.rect)
        screen.blit(nuldar_button.surf, nuldar_button.rect)
        screen.blit(nuldar_male_button.surf, nuldar_male_button.rect)
        screen.blit(nuldar_female_button.surf, nuldar_female_button.rect)
        screen.blit(sorae_button.surf, sorae_button.rect)
        screen.blit(sorae_alpha_button.surf, sorae_alpha_button.rect)
        screen.blit(sorae_beta_button.surf, sorae_beta_button.rect)
        screen.blit(nuldar_select_overlay.surf, nuldar_select_overlay.rect)
        if gender == "male":
            screen.blit(nuldar_male_character.surf, nuldar_male_character.rect)
        if gender == "female":
            screen.blit(nuldar_female_character.surf, nuldar_female_character.rect)
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(back_button.surf, back_button.rect)
        screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        screen.blit(character_name_surface, (605, 569))

    if race == "sorae":
        screen.blit(sorae_character_screen, (0, 0))
        screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        screen.blit(amuna_button.surf, amuna_button.rect)
        screen.blit(amuna_male_button.surf, amuna_male_button.rect)
        screen.blit(amuna_female_button.surf, amuna_female_button.rect)
        screen.blit(nuldar_button.surf, nuldar_button.rect)
        screen.blit(nuldar_male_button.surf, nuldar_male_button.rect)
        screen.blit(nuldar_female_button.surf, nuldar_female_button.rect)
        screen.blit(sorae_button.surf, sorae_button.rect)
        screen.blit(sorae_alpha_button.surf, sorae_alpha_button.rect)
        screen.blit(sorae_beta_button.surf, sorae_beta_button.rect)
        screen.blit(sorae_select_overlay.surf, sorae_select_overlay.rect)
        if gender == "male":
            screen.blit(sorae_alpha_character.surf, sorae_alpha_character.rect)
        if gender == "female":
            screen.blit(sorae_beta_character.surf, sorae_beta_character.rect)
        screen.blit(start_button.surf, start_button.rect)
        screen.blit(back_button.surf, back_button.rect)
        screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        screen.blit(character_name_surface, (605, 569))
