# Вариант 9
tab="   "
reset = f"\x1b[0m"
white = f"\x1b[47m{tab}"
black = f"\x1b[40m{tab}"
yellow = f"\x1b[43m{tab}"
blue = f"\x1b[44m{tab}"
delete = "\033[H"
import time
import os
def clear():
    os.system("cls")



# Задание 1 (Флаг)
def flag():
    l, h = 1,1

    clear()

    linewbw = f"{white*5*l}{blue*3*l}{white*10*l}{reset}\n"*4*h
    lineb = f"{blue*18*l}{reset}\n"*3*h
    print(f"{linewbw}{lineb}{linewbw}")



# # Задание 2 (Узор)
def uzor():
    amt = 4
    R = 7

    clear()
    
    def line(R,colored,amt):
        notcolored = (2*R-colored)//2
        return f"{white*notcolored}{black*colored}{white*notcolored}{reset}"*amt
    
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
        print(delete)
        print(f"{black}{yellow*3}{black*8}{reset}\n"
        f"{yellow*5}{black*7}{reset}\n"
        f"{yellow*5}{black*4}{white}{black*2}{reset}\n"
        f"{yellow*5}{black*7}{reset}\n"
        f"{black}{yellow*3}{black*8}{reset}"
        )

        time.sleep(0.2)
        print(delete)
        print(f"{black*5}{yellow*3}{black*4}{reset}\n"
        f"{black*4}{yellow*3}{black*5}{reset}\n"
        f"{black*4}{yellow*2}{black*3}{white}{black*2}{reset}\n"
        f"{black*4}{yellow*3}{black*5}{reset}\n"
        f"{black*5}{yellow*3}{black*4}{reset}"
        )

        time.sleep(0.2)
        print(delete)
        print(f"{black*8}{yellow*3}{black*1}{reset}\n"
        f"{black*7}{yellow*5}{reset}\n"
        f"{black*7}{yellow*5}{reset}\n"
        f"{black*7}{yellow*5}{reset}\n"
        f"{black*8}{yellow*3}{black*1}{reset}"
        )

        time.sleep(0.2)
        print(delete) 
        print(f"{black*12}{reset}\n"
        f"{black*11}{yellow*1}{reset}\n"
        f"{black*11}{yellow*1}{reset}\n"
        f"{black*11}{yellow*1}{reset}\n"
        f"{black*12}{reset}"
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
    print(f'{yellow*(int(aper))}{reset}{aper}%\n{blue*(int(bper))}{reset}{bper}%')



# Задание 5
def graph():
    h = 12

    clear()

    res = "Y\n\u2191\n"
    for y in range(h,-1,-1):
        x = 2*y
        line = f"│{white*x}{black*2}{reset}{white*(2*h-x)}{reset}\n"
        res += line
    OX = f"0{f'\u203e'*3*2*(h+1)}\u2192X"
    res += OX
    
    print(res)



#flag()
#uzor()
#animation()
#diagram()
#graph()