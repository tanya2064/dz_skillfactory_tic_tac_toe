import itertools

# Создаём игровое поле
field = [['-' for _ in range(3)] for _ in range(3)]


# Функция отрисовки поля
def create_field():
    print("  0 1 2")  # Верхняя ось X
    for i in range(3):
        print(i, ' '.join(field[i]))  # Ос Y + сам ряд


# Функция хода игрока
def course_of_game(player_name, player_symbol):
    while True:
        try:
            print(f"{player_name}, ваш ход! ({player_symbol})")
            x, y = map(int, input("Введите координаты (строка и столбец) через пробел: ").split())

            # Проверяем корректность хода
            if 0 <= x < 3 and 0 <= y < 3 and field[x][y] == '-':
                field[x][y] = player_symbol  # Устанавливаем символ игрока
                break
            else:
                print("Некорректный ход, попробуйте снова.")
        except ValueError:
            print("Ошибка ввода! Введите два числа через пробел.")


# Функция проверки победителя
def check_winner():
    win_lines = (
        # Горизонтальные линии
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        # Вертикальные линии
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        # Диагонали
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    )

    for line in win_lines:
        symbols = [field[x][y] for x, y in line]
        if symbols[0] != '-' and symbols.count(symbols[0]) == 3:
            return symbols[0]  # Возвращаем победный символ ('X' или 'O')

    return None  # Если победителя нет


# Основная функция игры
def play_game():
    # Вводим имена игроков
    name1 = input('Введите имя первого игрока: ')
    name2 = input("Введите имя второго игрока: ")

    # Привязываем символы к игрокам
    player_symbols = {name1: 'X', name2: 'O'}
    players = [name1, name2]  # Очередность ходов
    move_count = 0  # Счетчик ходов

    create_field()  # Отрисовываем начальное поле

    while move_count < 9:  # Максимум 9 ходов (если ничья)
        current_player = players[move_count % 2]  # Меняем игрока по очереди
        course_of_game(current_player, player_symbols[current_player])
        create_field()  # Показываем обновленное поле

        # Проверяем, есть ли победитель
        winner_symbol = check_winner()
        if winner_symbol:
            for name, symbol in player_symbols.items():
                if symbol == winner_symbol:
                    print(f"Поздравляем, {name}! Вы победили!")
                    return

        move_count += 1  # Увеличиваем счетчик ходов

    print("Ничья! Игра окончена.")


# Запускаем игру
play_game()