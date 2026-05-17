# ПЕРСОНАЖИ

default Roy = Character("Рой", color="#ff0000", image='Roy', callback=name_callback, cb_name="Roy")

default Riley = Character("Райли", image='Riley', callback=name_callback, cb_name="Riley")

default Lily = Character("Лили", image='Lily', callback=name_callback, cb_name="Lily")

default News = Character("Ведущий новостей")

default Mom = Character("Мама", image='Mom', callback=name_callback, cb_name="Mom")

default Rudy = Character("Руди?")

default Daniel = Character("Даниэль", image='Daniel', callback=name_callback, cb_name="Daniel")

default Edward = Character("Эдвард", image='Edward', callback=name_callback, cb_name="Edward")

default Ms_Wolford = Character("Миссис Волфорд", image='Ms_Wolford', callback=name_callback, cb_name="Ms_Wolford")

# ФОНЫ

image Roy_walking = 'images/episode_1/Roy_walking.png'

image Roy_looks_out_the_window = 'images/episode_2/Roy_looks_out_the_window.png'

# СПРАЙТЫ

## Мама Роя 

image Mom funeral = At('images/sprites/Roys_mom/funeral.png', sprite_highlight('Mom'))

image Mom normal = At('images/sprites/Roys_mom/normal.png', sprite_highlight('Mom'))

## Райли

image Riley normal silent = At('images/sprites/Riley/normal_silent.png', sprite_highlight('Riley'))

image Riley normal talking = At('images/sprites/Riley/normal_talking.png', sprite_highlight('Riley'))

image Riley funeral silent = At('images/sprites/Riley/funeral_silent.png', sprite_highlight('Riley'))

image Riley funeral silent sad = At('images/sprites/Riley/funeral_silent_sad.png', sprite_highlight('Riley'))

image Riley funeral sad = At('images/sprites/Riley/funeral_sad.png', sprite_highlight('Riley'))

image Riley funeral angry = At('images/sprites/Riley/funeral_angry.png', sprite_highlight('Riley'))

## Даниэль

image Daniel normal silent = At('images/sprites/Daniel/normal_silent.png', sprite_highlight('Daniel'))

image Daniel normal talking = At('images/sprites/Daniel/normal_talking.png', sprite_highlight('Daniel'))

image Daniel funeral silent = At('images/sprites/Daniel/funeral_silent.png', sprite_highlight('Daniel'))

image Daniel funeral talking = At('images/sprites/Daniel/funeral_talking.png', sprite_highlight('Daniel'))

## Лили 

image Lily normal = At('images/sprites/Lily/normal.png', sprite_highlight('Lily'))

image Lily screamer = At('images/sprites/Lily/screamer.png', sprite_highlight('Lily'))

# Нердик

image Edward funeral silent = At('images/sprites/Nerdik/funeral_silent.png', sprite_highlight('Edward'))

image Edward funeral talking = At('images/sprites/Nerdik/funeral_talking.png', sprite_highlight('Edward'))

image Edward normal silent = At('images/sprites/Nerdik/normal_silent.png', sprite_highlight('Edward'))

image Edward normal talking = At('images/sprites/Nerdik/normal_talking.png', sprite_highlight('Edward'))

image Edward normal angry = At('images/sprites/Nerdik/normal_angry.png', sprite_highlight('Edward'))

image Edward normal rolled eyes = At('images/sprites/Nerdik/normal_rolled_eyes.png', sprite_highlight('Edward'))

# Мама Руди

image Ms_Wolford = At('images/sprites/Rudys_mom/normal.png', sprite_highlight('Ms_Wolford'))