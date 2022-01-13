from elements import elements
import elements.elements as elements
import os
from tkinter import *
from functools import partial

# function converts atomic no. to symbol for text on the button as well as for performing functions


def NoToSymbol(n):
    l = elements.AllSymbols
    for i in l:
        if getattr(elements, i).AtomicNumber == n:
            w = getattr(elements, i).AtomicMass

            SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

            w = w.replace('amu', '')
            w = w.replace('(', '')
            w = w.replace(')', '')
            w = float(w)
            w = round(w)
            op = (str(n)+i).translate(SUP)+str(w).translate(SUB)

            return op


# function shows message box when button is clicked
def clicked(symbol):
    from tkinter import messagebox
    for i in symbol:
        if i in "⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉":
            symbol = symbol.replace(i, '')
    y = getattr(elements, symbol)
    try:
        """fname = "C:\\mywork\\pythonprgs\\Element_Information\\"+y.Name + \
            '.txt'  # C:\mywork\pythonprgs\Element_Information\fluorine.txt
        """
        fname = os.getcwd() + "\Element_Information\\"+y.Name + \
            '.txt'
        f = open(fname, 'r')
        desc = f.read()
    except:
        desc = y.Name.replace(' ', '#')

    f.close()
    p = " Name: \t\t"+str(y.Name)+"\n Atomic Number: \t"+str(y.AtomicNumber)+"\n Atomic Mass: \t"+str(y.AtomicMass) + \
        "\n Protons/Electrons:" + \
        str(y.Protons_Electrons)+"\n Neutrons:  \t" + \
        str(y.Neutrons) + "\n Description: \n" + desc

    messagebox.showinfo(symbol, p)

# function for deciding the colour for the buttons based on position on the periodic table


def col(i, j):
    colour = "white"

    if j == 0:  # alkali metals group1
        colour = "#FFB619"
    elif j == 17:  # inert gases group18
        colour = "#E8BFDB"
    elif j == 16:
        colour = "#77F227"

    elif j == 1:  # alkaline earth metals group2
        colour = "#FC8E42"
    elif j == 2:
        if i == 4 or i == 5:
            colour = "#1692FF"
        elif i == 6:
            colour = "#16FFA0"
        else:
            colour = "#FFF416"
    elif j >= 3 and j < 12:  # transition metals group 3 to 12
        colour = "#1692FF"
    elif j == 12 or j == 13 or j == 14 or j == 15:  # nonmetals, metalloids and pure metals
        if j-i >= 11:
            colour = "#FF2074"
        elif (j-i) < 9 or j == 12 and i == 3:
            colour = "#C660FF"

        else:
            colour = "#ECE572"

    else:
        colour = "cyan"
    return colour
# function which creates the 112 buttons


def button():

    # group name
    for j in range(18):
        n = str(j+1)

        l = Label(text="""Group
 """+n, bg="white", font=("Times New Roman", 10), borderwidth=1, relief="solid", width=7)
        l.grid(row=0, column=j+1)

    # period 1
    n = 0
    for j in range(18):
        if j >= 1 and j < 17:
            l1 = Label(window, text="   ")
            l1.grid(column=j+1, row=1)
        else:
            if j == 0:
                n = 1
                sym = NoToSymbol(n)
                bt = Button(text=sym, command=partial(
                    clicked, sym), width=6, bg="#FF2074")
                bt.grid(column=1, row=1)
            else:
                n = 2
                sym = NoToSymbol(n)
                bt = Button(text=sym, command=partial(
                    clicked, sym), width=6, bg="#E8BFDB")
                bt.grid(column=18, row=1)


# period 2 and 3

    for i in range(2):
        for j in range(18):
            colour = col(i+2, j)

            if((j < 2) or (j > 11)):
                if j < 2:
                    n = 3+(8*i)+j
                else:
                    n = 3+(8*i)+(j-10)

                sym = NoToSymbol(n)
                bt = Button(text=sym, command=partial(
                    clicked, sym), width=6, bg=colour)
                bt.grid(column=j+1, row=i+2)
            else:
                l1 = Label(window, text="   ")
                l1.grid(column=j+1, row=i+2)

# period 4 5  6
    for i in range(3):

        for j in range(18):
            colour = col(i+4, j)
            if i == 2 and j >= 3:
                n = 69+j
                sym = NoToSymbol(n)

                bt = Button(text=sym, command=partial(
                    clicked, sym), width=6, bg=colour)
                bt.grid(column=j+1, row=i+4)
            else:
                n = 19+(18*i)+j

                sym = NoToSymbol(n)

                bt = Button(text=sym, command=partial(
                    clicked, sym), width=6, bg=colour)
                bt.grid(column=j+1, row=i+4)


# 7
    for j in range(12):
        colour = col(7, j)
        if j < 3:
            n = 87+j
        else:
            n = 101+j
        sym = NoToSymbol(n)
        bt = Button(text=sym, command=partial(
            clicked, sym), width=6, bg=colour)
        bt.grid(column=j+1, row=6+1)

    l = Label(text="")
    l.grid(column=1, row=8)


#actinides and lactindes
    for j in range(14):
        n = 58+j
        sym = NoToSymbol(n)
        bt = Button(text=sym, command=partial(
            clicked, sym), bg="#16FFA0", width=6)
        bt.grid(column=(3+j), row=9)
    for j in range(14):
        n = 90+j
        sym = NoToSymbol(n)
        bt = Button(text=sym, command=partial(
            clicked, sym), bg="#FFF416", width=6)
        bt.grid(column=(3+j), row=10)
# period name
    for i in range(11):
        px = 0
        py = 0
        txt = ''
        if i >= 1 and i <= 7:
            txt = "Period "+str(i)
            px = 10
            py = 2
        elif i == 9:
            txt = "Actinides"
            px = 7
            py = 0
        elif i == 10:
            txt = "Lanthanides"
            px = 0
            py = 0

        else:
            txt = ''
            l = Label(text=txt)
            l.grid(column=0, row=i)
            continue
        l = Label(text=txt, font=("Times new roman", 12), bg="white",
                  borderwidth=1, relief="solid", padx=px, pady=py)
        l.grid(column=0, row=i)
# key
    nonmetal = Label(window, text='KEY:', font=("Arial Bold", 14))
    nonmetal.grid(column=0, row=15)

    nonmetal = Label(window, text='''Non
Metals''', font=("Arial Bold", 7), borderwidth=1, relief="solid", bg='#FF2074', padx=20, pady=8)
    nonmetal.grid(column=0, row=16, rowspan=3)

    alkm = Label(window, text='''Alkali
Metals''', font=("Arial Bold", 7), borderwidth=1, relief="solid", bg='#FFB619', padx=9, pady=8)
    alkm.grid(column=1, row=16, rowspan=3)

    alkem = Label(window, text='''Alkaline
Earth
Metals''', font=("Arial Bold", 7), borderwidth=1, relief="solid", bg='#FC8E42', padx=4, pady=2.5)
    alkem.grid(column=2, row=16, rowspan=3)

    trans = Label(window, text='''Transition
Elements''', font=("Arial Bold", 7), borderwidth=1, relief="solid", bg='#1692FF', pady=8)
    trans.grid(column=3, row=16, rowspan=3)

    pm = Label(window, text='''Pure
Metals''', font=("Arial Bold", 7), borderwidth=1, relief="solid", bg='#C660FF', padx=8, pady=8)
    pm.grid(column=4, row=16, rowspan=3)

    mtld = Label(window, text='Metalloids', font=("Arial Bold", 7),
                 borderwidth=1, relief="solid", bg='#ECE572', pady=14)
    mtld.grid(column=5, row=16, rowspan=3)

    hl = Label(window, text='Halogens', font=("Arial Bold", 7),
               borderwidth=1, relief="solid", bg='#77F227', pady=14)
    hl.grid(column=6, row=16, rowspan=3)

    nert = Label(window, text='''Noble
Gases''', font=("Arial Bold", 7), borderwidth=1, relief="solid", bg='#E8BFDB', pady=8, padx=10)
    nert.grid(column=7, row=16, rowspan=3)

    act = Label(window, text='Actinides', font=("Arial Bold", 7),
                borderwidth=1, relief="solid", bg='#16FFA0', pady=14)
    act.grid(column=8, row=16, rowspan=3)

    lan = Label(window, text='Lanthanides', font=("Arial Bold", 6),
                borderwidth=1, relief="solid", bg='#FFF416', pady=14)
    lan.grid(column=9, row=16, rowspan=3)

    window.mainloop()


# main
window = Tk()
window.title("Periodic Table")
button()
