# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Project_Eterna.py'],
             pathex=[],
             binaries=[],
             datas=[('resources/art/*','resources/art'), ('resources/art/character_art/NPCs/*.png','resources/art/character_art/NPCs'), ('resources/art/character_art/player_character/default/battle/*.png','resources/art/character_art/player_character/default/battle'), ('resources/art/character_art/player_character/default/*.png','resources/art/character_art/player_character/default'), ('resources/art/enemy_art/battle/*.png','resources/art/enemy_art/battle'), ('resources/art/enemy_art/*.png','resources/art/enemy_art'), ('resources/art/environment_art/background_textures/*.png','resources/art/environment_art/background_textures'), ('resources/art/environment_art/buildings/*.png','resources/art/environment_art/buildings'), ('resources/art/environment_art/*.png','resources/art/environment_art'), ('resources/art/item_art/*.png','resources/art/item_art'), ('resources/art/screens/*.png','resources/art/screens'), ('resources/art/ui_elements/bars/energy/*.png','resources/art/ui_elements/bars/energy'), ('resources/art/ui_elements/bars/health/*.png','resources/art/ui_elements/bars/health'), ('resources/art/ui_elements/bars/xp/*.png','resources/art/ui_elements/bars/xp'), ('resources/art/ui_elements/buttons/battle_screen/*.png','resources/art/ui_elements/buttons/battle_screen'), ('resources/art/ui_elements/buttons/shop/*.png','resources/art/ui_elements/buttons/shop'), ('resources/art/ui_elements/buttons/*.png','resources/art/ui_elements/buttons'), ('resources/art/ui_elements/notifications/*.png','resources/art/ui_elements/notifications'), ('resources/art/ui_elements/status/*.png','resources/art/ui_elements/status'), ('resources/art/ui_elements/*.png','resources/art/ui_elements'), ('resources/art/critter_art/*.png','resources/art/critter_art')],                                                                                                       
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Project_Eterna',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
