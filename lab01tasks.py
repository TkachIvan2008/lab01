import os
import time


# Вариант 9
TAB = "   "
RESET = "\x1b[0m"
WHITE = f"\x1b[47m{TAB}"
BLACK = f"\x1b[40m{TAB}"
YELLOW = f"\x1b[43m{TAB}"
BLUE = f"\x1b[44m{TAB}"
DELETE = "\033[H"


def clear():
    os.system("cls")


# Задание 1 (Флаг)
def flag():
    length = 1
    height = 1

    clear()

    linewbw = f"{WHITE * 5 * length}{BLUE * 3 * length}{WHITE * 10 * length}{RESET}\n" * 4 * height
    lineb = f"{BLUE * 18 * length}{RESET}\n" * 3 * height
    print(f"{linewbw}{lineb}{linewbw}")


# Задание 2 (Узор)
def uzor():
    amount = 4
    radius = 7

    clear()

    def line(radius, colored, amount):
        not_colored = (2 * radius - colored) // 2
        return f"{WHITE * not_colored}{BLACK * colored}{WHITE * not_colored}{RESET}" * amount

    for i in range(0, radius * 2 + 1):
        x = radius - i
        colored = 2 * (int((radius**2 - x**2) ** 0.5))
        print(line(radius, colored, amount))


# Задание 3 (Анимация)
def animation():
    cycles = 3

    clear()

    for i in range(cycles):
        time.sleep(0.2)

        print(DELETE)

        print(
            f"{BLACK}{YELLOW * 3}{BLACK * 8}{RESET}\n"
            f"{YELLOW * 5}{BLACK * 7}{RESET}\n"
            f"{YELLOW * 5}{BLACK * 4}{WHITE}{BLACK * 2}{RESET}\n"
            f"{YELLOW * 5}{BLACK * 7}{RESET}\n"
            f"{BLACK}{YELLOW * 3}{BLACK * 8}{RESET}"
        )

        time.sleep(0.2)

        print(DELETE)

        print(
            f"{BLACK * 5}{YELLOW * 3}{BLACK * 4}{RESET}\n"
            f"{BLACK * 4}{YELLOW * 3}{BLACK * 5}{RESET}\n"
            f"{BLACK * 4}{YELLOW * 2}{BLACK * 3}{WHITE}{BLACK * 2}{RESET}\n"
            f"{BLACK * 4}{YELLOW * 3}{BLACK * 5}{RESET}\n"
            f"{BLACK * 5}{YELLOW * 3}{BLACK * 4}{RESET}"
        )

        time.sleep(0.2)

        print(DELETE)

        print(
            f"{BLACK * 8}{YELLOW * 3}{BLACK * 1}{RESET}\n"
            f"{BLACK * 7}{YELLOW * 5}{RESET}\n"
            f"{BLACK * 7}{YELLOW * 5}{RESET}\n"
            f"{BLACK * 7}{YELLOW * 5}{RESET}\n"
            f"{BLACK * 8}{YELLOW * 3}{BLACK * 1}{RESET}"
        )

        time.sleep(0.2)

        print(DELETE)

        print(
            f"{BLACK * 12}{RESET}\n"
            f"{BLACK * 11}{YELLOW * 1}{RESET}\n"
            f"{BLACK * 11}{YELLOW * 1}{RESET}\n"
            f"{BLACK * 11}{YELLOW * 1}{RESET}\n"
            f"{BLACK * 12}{RESET}"
        )


# Задание 4
def diagram():
    clear()

    file_sequence = open("sequence.txt", "r")
    group_a = []
    group_b = []
    for i in file_sequence:
        if 5 <= float(i) <= 10:
            group_a.append(i)
        if -10 <= float(i) <= -5:
            group_b.append(i)
    file_sequence.close()

    a_length = len(group_a)
    b_length = len(group_b)
    a_percentage = a_length * 100 / (a_length + b_length)
    b_percentage = b_length * 100 / (a_length + b_length)
    print(f"{YELLOW * (int(a_percentage))}{RESET}{a_percentage}%\n{BLUE * (int(b_percentage))}{RESET}{b_percentage}%")


# Задание 5
def graph():
    height = 12

    clear()

    res = "Y\n\u2191\n"
    for y in range(height, -1, -1):
        x = 2 * y
        line = f"│{WHITE * x}{BLACK * 2}{RESET}{WHITE * (2 * height - x)}{RESET}\n"
        res += line
    ox = f"0{f'\u203e' * 3 * 2 * (height + 1)}\u2192X"
    res += ox

    print(res)


# flag()
# uzor()
# animation()
# diagram()
# graph()