# Вариант 9
TAB="   "
RESET = f"\x1b[0m"
WHITE = f"\x1b[47m{TAB}"
BLACK = f"\x1b[40m{TAB}"
YELLOW = f"\x1b[43m{TAB}"
BLUE = f"\x1b[44m{TAB}"
DELETE = "\033[H"
import time
import os
def clear():
    os.system("cls")



# Задание 1 (Флаг)
def flag():
    l, h = 1,1

    clear()

    linewbw = f"{WHITE*5*l}{BLUE*3*l}{WHITE*10*l}{RESET}\n"*4*h
    lineb = f"{BLUE*18*l}{RESET}\n"*3*h
    print(f"{linewbw}{lineb}{linewbw}")



# # Задание 2 (Узор)
def uzor():
    amt = 4
    R = 7

    clear()
    
    def line(R,colored,amt):
        notcolored = (2*R-colored)//2
        return f"{WHITE*notcolored}{BLACK*colored}{WHITE*notcolored}{RESET}"*amt
    
    for i in range(0,R*2+1):
        x = R - i
        colored = 2*(int((R**2 - x**2)**0.5))
        print(line(R,colored,amt))



# Задание 3 (Анимация)
def animation():
    cycles = 3

    clear()

    for i in range(cycles):
        time.sleep(0.2)
        print(DELETE)
        print(f"{BLACK}{YELLOW*3}{BLACK*8}{RESET}\n"
        f"{YELLOW*5}{BLACK*7}{RESET}\n"
        f"{YELLOW*5}{BLACK*4}{WHITE}{BLACK*2}{RESET}\n"
        f"{YELLOW*5}{BLACK*7}{RESET}\n"
        f"{BLACK}{YELLOW*3}{BLACK*8}{RESET}"
        )

        time.sleep(0.2)
        print(DELETE)
        print(f"{BLACK*5}{YELLOW*3}{BLACK*4}{RESET}\n"
        f"{BLACK*4}{YELLOW*3}{BLACK*5}{RESET}\n"
        f"{BLACK*4}{YELLOW*2}{BLACK*3}{WHITE}{BLACK*2}{RESET}\n"
        f"{BLACK*4}{YELLOW*3}{BLACK*5}{RESET}\n"
        f"{BLACK*5}{YELLOW*3}{BLACK*4}{RESET}"
        )

        time.sleep(0.2)
        print(DELETE)
        print(f"{BLACK*8}{YELLOW*3}{BLACK*1}{RESET}\n"
        f"{BLACK*7}{YELLOW*5}{RESET}\n"
        f"{BLACK*7}{YELLOW*5}{RESET}\n"
        f"{BLACK*7}{YELLOW*5}{RESET}\n"
        f"{BLACK*8}{YELLOW*3}{BLACK*1}{RESET}"
        )

        time.sleep(0.2)
        print(DELETE) 
        print(f"{BLACK*12}{RESET}\n"
        f"{BLACK*11}{YELLOW*1}{RESET}\n"
        f"{BLACK*11}{YELLOW*1}{RESET}\n"
        f"{BLACK*11}{YELLOW*1}{RESET}\n"
        f"{BLACK*12}{RESET}"
        )



# Задание 4
def diagram():
    clear()

    file = open('sequence.txt', 'r')
    a = []
    b = []
    for i in file:
        if 5<=float(i)<=10:
            a.append(i)
        if -10<=float(i)<=-5:
            b.append(i)
    file.close()

    alen, blen=len(a), len(b)
    aper,bper=alen*100/(alen+blen),blen*100/(alen+blen)
    print(f'{YELLOW*(int(aper))}{RESET}{aper}%\n{BLUE*(int(bper))}{RESET}{bper}%')



# Задание 5
def graph():
    h = 12

    clear()

    res = "Y\n\u2191\n"
    for y in range(h,-1,-1):
        x = 2*y
        line = f"│{WHITE*x}{BLACK*2}{RESET}{WHITE*(2*h-x)}{RESET}\n"
        res += line
    OX = f"0{f'\u203e'*3*2*(h+1)}\u2192X"
    res += OX
    
    print(res)



#flag()
#uzor()
#animation()
#diagram()
#graph()
