print('THE WIZZARD. THE TEXT QUAST.')
print('Это игра текстовый квест.')
print('Для начала ознакомтесь с правилами:')
print('1. Для выбора надо вводить действия надо ввести число указанное рядом')
print('Пример: ――> 1 <―― . Использовать')
print('Теперь начнём введение.')
print('Вы - новичок зельевар-волщебник, который только начиная свой путь')
print('заболевает страшной болезнью. Чтобы излечится вам понадобится')
print('сварить снадобье.')
print('для этого снадобья вам понадобиться 3 ингридиента:')
print('корень Мандрагоры, яд Паука-Людоеда и Гриб-Дьявол.')
print('Так-же у вас есть инвентарь. Сейчас у вас есть:')
print('5 злотых, Палка-Копалка(Палочка).')
inventory = ['Палочка']
money = 5
print('Это конец введения, так что удачи!')
print('Но запомните - часики тикают')
name = input(print('Кстати говоря, введите ваше имя: '))
print('И наконец начинается приключение великого(может и нет)', name)
print('Выберите действие:')
print('1. Идти в Мастерскую')
print('2. Идти на Склад')
print('3. Идти в Зельеварочную')
print('4. Идти в Подземелье')
print('5. Идти на Рынок')
print('6. Отдохнуть немного')
choise = int(input())
if choise == 1:
  print('Вы отправляетесь в Мастерскую')
  print('Здесь вы можете улучшить вашу Палочку до 1-го уровня')
  print('Для этого вам понадобится:')
  print('3 кусочка коры, 1-ин зелёный камушек.')
  print('Так как вы можете найти всё это на улице вы идёте туда.')
  print('И вот вы вышли на улицу')
