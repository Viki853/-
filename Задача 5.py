color_a=input('Выберите первый цвет из возможных (красный, синий или желтый): ').lower()
color_b=input('Выберите второй цвет из возможных (красный, синий или желтый): ').lower()

if color_a or color_b == 'красный' or 'синий' or 'желтый':
    if color_a == color_b:
        print(f'Цвет не поменялся - {color_a}')
    else:
        if ('красный' in (color_a, color_b)) and ('синий' in (color_a, color_b)):
            print('У вас получится - фиолетовый')
        elif ('красный' in (color_a,color_b)) and ('желтый' in (color_a, color_b)):
            print('У вас получится - оранжевый')
        elif ('синий' in (color_a,color_b)) and ('желтый' in (color_a, color_b)):
            print('У вас получится - зеленый')
else:
    print('Ошибка: выберите цвет из предложенных!')