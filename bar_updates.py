import resource_urls


# ----------------------------------------------------------------------------------------------------------------------
# gets current player health and updates hp bar image on screen according to the health value from 0-100
def health_bar_update(character):
    if character.health == 100:
        return resource_urls.hp_100
    if character.health == 99:
        return resource_urls.hp_99
    if character.health == 98:
        return resource_urls.hp_98
    if character.health == 97:
        return resource_urls.hp_97
    if character.health == 96:
        return resource_urls.hp_96
    if character.health == 95:
        return resource_urls.hp_95
    if character.health == 94:
        return resource_urls.hp_94
    if character.health == 93:
        return resource_urls.hp_93
    if character.health == 92:
        return resource_urls.hp_92
    if character.health == 91:
        return resource_urls.hp_91
    if character.health == 90:
        return resource_urls.hp_90
    if character.health == 89:
        return resource_urls.hp_89
    if character.health == 88:
        return resource_urls.hp_88
    if character.health == 87:
        return resource_urls.hp_87
    if character.health == 86:
        return resource_urls.hp_86
    if character.health == 85:
        return resource_urls.hp_85
    if character.health == 84:
        return resource_urls.hp_84
    if character.health == 83:
        return resource_urls.hp_83
    if character.health == 82:
        return resource_urls.hp_82
    if character.health == 81:
        return resource_urls.hp_81
    if character.health == 80:
        return resource_urls.hp_80
    if character.health == 79:
        return resource_urls.hp_79
    if character.health == 78:
        return resource_urls.hp_78
    if character.health == 77:
        return resource_urls.hp_77
    if character.health == 76:
        return resource_urls.hp_76
    if character.health == 75:
        return resource_urls.hp_75
    if character.health == 74:
        return resource_urls.hp_74
    if character.health == 73:
        return resource_urls.hp_73
    if character.health == 72:
        return resource_urls.hp_72
    if character.health == 71:
        return resource_urls.hp_71
    if character.health == 70:
        return resource_urls.hp_70
    if character.health == 69:
        return resource_urls.hp_69
    if character.health == 68:
        return resource_urls.hp_68
    if character.health == 67:
        return resource_urls.hp_67
    if character.health == 66:
        return resource_urls.hp_66
    if character.health == 65:
        return resource_urls.hp_65
    if character.health == 64:
        return resource_urls.hp_64
    if character.health == 63:
        return resource_urls.hp_63
    if character.health == 62:
        return resource_urls.hp_62
    if character.health == 61:
        return resource_urls.hp_61
    if character.health == 60:
        return resource_urls.hp_60
    if character.health == 59:
        return resource_urls.hp_59
    if character.health == 58:
        return resource_urls.hp_58
    if character.health == 57:
        return resource_urls.hp_57
    if character.health == 56:
        return resource_urls.hp_56
    if character.health == 55:
        return resource_urls.hp_55
    if character.health == 54:
        return resource_urls.hp_54
    if character.health == 53:
        return resource_urls.hp_53
    if character.health == 52:
        return resource_urls.hp_52
    if character.health == 51:
        return resource_urls.hp_51
    if character.health == 50:
        return resource_urls.hp_50
    if character.health == 49:
        return resource_urls.hp_49
    if character.health == 48:
        return resource_urls.hp_48
    if character.health == 47:
        return resource_urls.hp_47
    if character.health == 46:
        return resource_urls.hp_46
    if character.health == 45:
        return resource_urls.hp_45
    if character.health == 44:
        return resource_urls.hp_44
    if character.health == 43:
        return resource_urls.hp_43
    if character.health == 42:
        return resource_urls.hp_42
    if character.health == 41:
        return resource_urls.hp_41
    if character.health == 40:
        return resource_urls.hp_40
    if character.health == 39:
        return resource_urls.hp_39
    if character.health == 38:
        return resource_urls.hp_38
    if character.health == 37:
        return resource_urls.hp_37
    if character.health == 36:
        return resource_urls.hp_36
    if character.health == 35:
        return resource_urls.hp_35
    if character.health == 34:
        return resource_urls.hp_34
    if character.health == 33:
        return resource_urls.hp_33
    if character.health == 32:
        return resource_urls.hp_32
    if character.health == 31:
        return resource_urls.hp_31
    if character.health == 30:
        return resource_urls.hp_30
    if character.health == 29:
        return resource_urls.hp_29
    if character.health == 28:
        return resource_urls.hp_28
    if character.health == 27:
        return resource_urls.hp_27
    if character.health == 26:
        return resource_urls.hp_26
    if character.health == 25:
        return resource_urls.hp_25
    if character.health == 24:
        return resource_urls.hp_24
    if character.health == 23:
        return resource_urls.hp_23
    if character.health == 22:
        return resource_urls.hp_22
    if character.health == 21:
        return resource_urls.hp_21
    if character.health == 20:
        return resource_urls.hp_20
    if character.health == 19:
        return resource_urls.hp_19
    if character.health == 18:
        return resource_urls.hp_18
    if character.health == 17:
        return resource_urls.hp_17
    if character.health == 16:
        return resource_urls.hp_16
    if character.health == 15:
        return resource_urls.hp_15
    if character.health == 14:
        return resource_urls.hp_14
    if character.health == 13:
        return resource_urls.hp_13
    if character.health == 12:
        return resource_urls.hp_12
    if character.health == 11:
        return resource_urls.hp_11
    if character.health == 10:
        return resource_urls.hp_10
    if character.health == 9:
        return resource_urls.hp_9
    if character.health == 8:
        return resource_urls.hp_8
    if character.health == 7:
        return resource_urls.hp_7
    if character.health == 6:
        return resource_urls.hp_6
    if character.health == 5:
        return resource_urls.hp_5
    if character.health == 4:
        return resource_urls.hp_4
    if character.health == 3:
        return resource_urls.hp_3
    if character.health == 2: 
        return resource_urls.hp_2
    if character.health == 1:
        return resource_urls.hp_1
    if character.health == 0:
        return resource_urls.hp_0

    else:
        return resource_urls.hp_0


# player energy bar update
def energy_bar_update(character):
    if character.energy == 100:
        return resource_urls.en_100
    if character.energy == 99:
        return resource_urls.en_99
    if character.energy == 98:
        return resource_urls.en_98
    if character.energy == 97:
        return resource_urls.en_97
    if character.energy == 96:
        return resource_urls.en_96
    if character.energy == 95:
        return resource_urls.en_95
    if character.energy == 94:
        return resource_urls.en_94
    if character.energy == 93:
        return resource_urls.en_93
    if character.energy == 92:
        return resource_urls.en_92
    if character.energy == 91:
        return resource_urls.en_91
    if character.energy == 90:
        return resource_urls.en_90
    if character.energy == 89:
        return resource_urls.en_89
    if character.energy == 88:
        return resource_urls.en_88
    if character.energy == 87:
        return resource_urls.en_87
    if character.energy == 86:
        return resource_urls.en_86
    if character.energy == 85:
        return resource_urls.en_85
    if character.energy == 84:
        return resource_urls.en_84
    if character.energy == 83:
        return resource_urls.en_83
    if character.energy == 82:
        return resource_urls.en_82
    if character.energy == 81:
        return resource_urls.en_81
    if character.energy == 80:
        return resource_urls.en_80
    if character.energy == 79:
        return resource_urls.en_79
    if character.energy == 78:
        return resource_urls.en_78
    if character.energy == 77:
        return resource_urls.en_77
    if character.energy == 76:
        return resource_urls.en_76
    if character.energy == 75:
        return resource_urls.en_75
    if character.energy == 74:
        return resource_urls.en_74
    if character.energy == 73:
        return resource_urls.en_73
    if character.energy == 72:
        return resource_urls.en_72
    if character.energy == 71:
        return resource_urls.en_71
    if character.energy == 70:
        return resource_urls.en_70
    if character.energy == 69:
        return resource_urls.en_69
    if character.energy == 68:
        return resource_urls.en_68
    if character.energy == 67:
        return resource_urls.en_67
    if character.energy == 66:
        return resource_urls.en_66
    if character.energy == 65:
        return resource_urls.en_65
    if character.energy == 64:
        return resource_urls.en_64
    if character.energy == 63:
        return resource_urls.en_63
    if character.energy == 62:
        return resource_urls.en_62
    if character.energy == 61:
        return resource_urls.en_61
    if character.energy == 60:
        return resource_urls.en_60
    if character.energy == 59:
        return resource_urls.en_59
    if character.energy == 58:
        return resource_urls.en_58
    if character.energy == 57:
        return resource_urls.en_57
    if character.energy == 56:
        return resource_urls.en_56
    if character.energy == 55:
        return resource_urls.en_55
    if character.energy == 54:
        return resource_urls.en_54
    if character.energy == 53:
        return resource_urls.en_53
    if character.energy == 52:
        return resource_urls.en_52
    if character.energy == 51:
        return resource_urls.en_51
    if character.energy == 50:
        return resource_urls.en_50
    if character.energy == 49:
        return resource_urls.en_49
    if character.energy == 48:
        return resource_urls.en_48
    if character.energy == 47:
        return resource_urls.en_47
    if character.energy == 46:
        return resource_urls.en_46
    if character.energy == 45:
        return resource_urls.en_45
    if character.energy == 44:
        return resource_urls.en_44
    if character.energy == 43:
        return resource_urls.en_43
    if character.energy == 42:
        return resource_urls.en_42
    if character.energy == 41:
        return resource_urls.en_41
    if character.energy == 40:
        return resource_urls.en_40
    if character.energy == 39:
        return resource_urls.en_39
    if character.energy == 38:
        return resource_urls.en_38
    if character.energy == 37:
        return resource_urls.en_37
    if character.energy == 36:
        return resource_urls.en_36
    if character.energy == 35:
        return resource_urls.en_35
    if character.energy == 34:
        return resource_urls.en_34
    if character.energy == 33:
        return resource_urls.en_33
    if character.energy == 32:
        return resource_urls.en_32
    if character.energy == 31:
        return resource_urls.en_31
    if character.energy == 30:
        return resource_urls.en_30
    if character.energy == 29:
        return resource_urls.en_29
    if character.energy == 28:
        return resource_urls.en_28
    if character.energy == 27:
        return resource_urls.en_27
    if character.energy == 26:
        return resource_urls.en_26
    if character.energy == 25:
        return resource_urls.en_25
    if character.energy == 24:
        return resource_urls.en_24
    if character.energy == 23:
        return resource_urls.en_23
    if character.energy == 22:
        return resource_urls.en_22
    if character.energy == 21:
        return resource_urls.en_21
    if character.energy == 20:
        return resource_urls.en_20
    if character.energy == 19:
        return resource_urls.en_19
    if character.energy == 18:
        return resource_urls.en_18
    if character.energy == 17:
        return resource_urls.en_17
    if character.energy == 16:
        return resource_urls.en_16
    if character.energy == 15:
        return resource_urls.en_15
    if character.energy == 14:
        return resource_urls.en_14
    if character.energy == 13:
        return resource_urls.en_13
    if character.energy == 12:
        return resource_urls.en_12
    if character.energy == 11:
        return resource_urls.en_11
    if character.energy == 10:
        return resource_urls.en_10
    if character.energy == 9:
        return resource_urls.en_9
    if character.energy == 8:
        return resource_urls.en_8
    if character.energy == 7:
        return resource_urls.en_7
    if character.energy == 6:
        return resource_urls.en_6
    if character.energy == 5:
        return resource_urls.en_5
    if character.energy == 4:
        return resource_urls.en_4
    if character.energy == 3:
        return resource_urls.en_3
    if character.energy == 2:
        return resource_urls.en_2
    if character.energy == 1:
        return resource_urls.en_1
    if character.energy == 0:
        return resource_urls.en_0

    else:
        return resource_urls.en_0


# player xp bar update
def xp_bar_update(character):
    if character.experience == 100:
        return resource_urls.xp_100
    if character.experience == 99:
        return resource_urls.xp_99
    if character.experience == 98:
        return resource_urls.xp_98
    if character.experience == 97:
        return resource_urls.xp_97
    if character.experience == 96:
        return resource_urls.xp_96
    if character.experience == 95:
        return resource_urls.xp_95
    if character.experience == 94:
        return resource_urls.xp_94
    if character.experience == 93:
        return resource_urls.xp_93
    if character.experience == 92:
        return resource_urls.xp_92
    if character.experience == 91:
        return resource_urls.xp_91
    if character.experience == 90:
        return resource_urls.xp_90
    if character.experience == 89:
        return resource_urls.xp_89
    if character.experience == 88:
        return resource_urls.xp_88
    if character.experience == 87:
        return resource_urls.xp_87
    if character.experience == 86:
        return resource_urls.xp_86
    if character.experience == 85:
        return resource_urls.xp_85
    if character.experience == 84:
        return resource_urls.xp_84
    if character.experience == 83:
        return resource_urls.xp_83
    if character.experience == 82:
        return resource_urls.xp_82
    if character.experience == 81:
        return resource_urls.xp_81
    if character.experience == 80:
        return resource_urls.xp_80
    if character.experience == 79:
        return resource_urls.xp_79
    if character.experience == 78:
        return resource_urls.xp_78
    if character.experience == 77:
        return resource_urls.xp_77
    if character.experience == 76:
        return resource_urls.xp_76
    if character.experience == 75:
        return resource_urls.xp_75
    if character.experience == 74:
        return resource_urls.xp_74
    if character.experience == 73:
        return resource_urls.xp_73
    if character.experience == 72:
        return resource_urls.xp_72
    if character.experience == 71:
        return resource_urls.xp_71
    if character.experience == 70:
        return resource_urls.xp_70
    if character.experience == 69:
        return resource_urls.xp_69
    if character.experience == 68:
        return resource_urls.xp_68
    if character.experience == 67:
        return resource_urls.xp_67
    if character.experience == 66:
        return resource_urls.xp_66
    if character.experience == 65:
        return resource_urls.xp_65
    if character.experience == 64:
        return resource_urls.xp_64
    if character.experience == 63:
        return resource_urls.xp_63
    if character.experience == 62:
        return resource_urls.xp_62
    if character.experience == 61:
        return resource_urls.xp_61
    if character.experience == 60:
        return resource_urls.xp_60
    if character.experience == 59:
        return resource_urls.xp_59
    if character.experience == 58:
        return resource_urls.xp_58
    if character.experience == 57:
        return resource_urls.xp_57
    if character.experience == 56:
        return resource_urls.xp_56
    if character.experience == 55:
        return resource_urls.xp_55
    if character.experience == 54:
        return resource_urls.xp_54
    if character.experience == 53:
        return resource_urls.xp_53
    if character.experience == 52:
        return resource_urls.xp_52
    if character.experience == 51:
        return resource_urls.xp_51
    if character.experience == 50:
        return resource_urls.xp_50
    if character.experience == 49:
        return resource_urls.xp_49
    if character.experience == 48:
        return resource_urls.xp_48
    if character.experience == 47:
        return resource_urls.xp_47
    if character.experience == 46:
        return resource_urls.xp_46
    if character.experience == 45:
        return resource_urls.xp_45
    if character.experience == 44:
        return resource_urls.xp_44
    if character.experience == 43:
        return resource_urls.xp_43
    if character.experience == 42:
        return resource_urls.xp_42
    if character.experience == 41:
        return resource_urls.xp_41
    if character.experience == 40:
        return resource_urls.xp_40
    if character.experience == 39:
        return resource_urls.xp_39
    if character.experience == 38:
        return resource_urls.xp_38
    if character.experience == 37:
        return resource_urls.xp_37
    if character.experience == 36:
        return resource_urls.xp_36
    if character.experience == 35:
        return resource_urls.xp_35
    if character.experience == 34:
        return resource_urls.xp_34
    if character.experience == 33:
        return resource_urls.xp_33
    if character.experience == 32:
        return resource_urls.xp_32
    if character.experience == 31:
        return resource_urls.xp_31
    if character.experience == 30:
        return resource_urls.xp_30
    if character.experience == 29:
        return resource_urls.xp_29
    if character.experience == 28:
        return resource_urls.xp_28
    if character.experience == 27:
        return resource_urls.xp_27
    if character.experience == 26:
        return resource_urls.xp_26
    if character.experience == 25:
        return resource_urls.xp_25
    if character.experience == 24:
        return resource_urls.xp_24
    if character.experience == 23:
        return resource_urls.xp_23
    if character.experience == 22:
        return resource_urls.xp_22
    if character.experience == 21:
        return resource_urls.xp_21
    if character.experience == 20:
        return resource_urls.xp_20
    if character.experience == 19:
        return resource_urls.xp_19
    if character.experience == 18:
        return resource_urls.xp_18
    if character.experience == 17:
        return resource_urls.xp_17
    if character.experience == 16:
        return resource_urls.xp_16
    if character.experience == 15:
        return resource_urls.xp_15
    if character.experience == 14:
        return resource_urls.xp_14
    if character.experience == 13:
        return resource_urls.xp_13
    if character.experience == 12:
        return resource_urls.xp_12
    if character.experience == 11:
        return resource_urls.xp_11
    if character.experience == 10:
        return resource_urls.xp_10
    if character.experience == 9:
        return resource_urls.xp_9_
    if character.experience == 8:
        return resource_urls.xp_8_
    if character.experience == 7:
        return resource_urls.xp_7_
    if character.experience == 6:
        return resource_urls.xp_6_
    if character.experience == 5:
        return resource_urls.xp_5_
    if character.experience == 4:
        return resource_urls.xp_4_
    if character.experience == 3:
        return resource_urls.xp_3_
    if character.experience == 2:
        return resource_urls.xp_2_
    if character.experience == 1:
        return resource_urls.xp_1_
    if character.experience == 0:
        return resource_urls.xp_0_

    else:
        return resource_urls.xp_0
