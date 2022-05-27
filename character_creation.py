import resource_urls


def character_screen_draw(race, amuna_character_screen, nuldar_character_screen, sorae_character_screen,
                          character_select_overlay, amuna_select_overlay, amuna_character, nuldar_select_overlay,
                          nuldar_character, sorae_select_overlay, sorae_character, amuna_button, nuldar_button,
                          sorae_button, start_button, name_input, name_input_font, character_name_input, pygame):

    if race == "amuna":
        resource_urls.screen.blit(amuna_character_screen, (0, 0))
        resource_urls.screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        resource_urls.screen.blit(amuna_button.surf, amuna_button.rect)
        resource_urls.screen.blit(nuldar_button.surf, nuldar_button.rect)
        resource_urls.screen.blit(sorae_button.surf, sorae_button.rect)
        resource_urls.screen.blit(amuna_select_overlay.surf, amuna_select_overlay.rect)
        resource_urls.screen.blit(amuna_character.surf, amuna_character.rect)
        resource_urls.screen.blit(start_button.surf, start_button.rect)
        resource_urls.screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        resource_urls.screen.blit(character_name_surface, (605, 575))

    if race == "nuldar":
        resource_urls.screen.blit(nuldar_character_screen, (0, 0))
        resource_urls.screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        resource_urls.screen.blit(amuna_button.surf, amuna_button.rect)
        resource_urls.screen.blit(nuldar_button.surf, nuldar_button.rect)
        resource_urls.screen.blit(sorae_button.surf, sorae_button.rect)
        resource_urls.screen.blit(nuldar_select_overlay.surf, nuldar_select_overlay.rect)
        resource_urls.screen.blit(nuldar_character.surf, nuldar_character.rect)
        resource_urls.screen.blit(start_button.surf, start_button.rect)
        resource_urls.screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        resource_urls.screen.blit(character_name_surface, (605, 575))

    if race == "sorae":
        resource_urls.screen.blit(sorae_character_screen, (0, 0))
        resource_urls.screen.blit(character_select_overlay.surf, character_select_overlay.rect)
        resource_urls.screen.blit(amuna_button.surf, amuna_button.rect)
        resource_urls.screen.blit(nuldar_button.surf, nuldar_button.rect)
        resource_urls.screen.blit(sorae_button.surf, sorae_button.rect)
        resource_urls.screen.blit(sorae_select_overlay.surf, sorae_select_overlay.rect)
        resource_urls.screen.blit(sorae_character.surf, sorae_character.rect)
        resource_urls.screen.blit(start_button.surf, start_button.rect)
        resource_urls.screen.blit(name_input.surf, name_input.rect)
        character_name_surface = name_input_font.render(character_name_input, True, (255, 255, 255))
        resource_urls.screen.blit(character_name_surface, (605, 575))

    pygame.display.flip()
