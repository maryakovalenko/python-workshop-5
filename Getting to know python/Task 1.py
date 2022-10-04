import re

def read_file(file_name):
    path = file_name
    f = open(path, "r")
    result = f.read().replace(" ", "")
    f.close()
    return result

def convert_pol(pol):
    pol = pol + "+"
    temp = []
    x = 0
    for i in re.finditer("\+|-", pol):
        temp.append(pol[x : i.start()])
        x = i.start()

    temp1 = []
    for i in temp:
        zx = i.find("x")
        if zx != -1:
            if zx == len(i) - 1:
                a = (i[0 : (zx - 1)], 1)
            else:
                a = ((i[0 : (zx - 1)]), (i[(zx + 2) : (len(i))]))
        else:
            a = ((i[0 : len(i)]), "0")
        temp1.append(a)
    return temp1

def fold_pols(pol1, pol2):
    res = []
    for i in range(len(pol1)):
        a = (pol1[i][0], pol1[i][1])
        for j in range(len(pol2)):
            if pol1[i][1] == pol2[j][1] != "":
                a = (eval(pol1[i][0] + "+" + pol2[j][0]), pol1[i][1])
        res.append(a)

    return res

def create_formula(input):
    temp = []
    for i in input:
        a = ["+", str(i[0]), "*", "x", "^", i[1]]
        temp.append(a)

    result = ""
    for i in temp:
        for j in i:
            result += str(j)

    if result[0] == "+":
        result = result[1 : len(result)]
    result = result.replace("*x^0", "")
    result = result.replace("++", "+")
    result = result.replace("+-", "-")
    result = result.replace("x^1", "x")

    return result

polynom1 = read_file("polynom1.txt")
polynom2 = read_file("polynom2.txt")
print("Formula N 1: {}".format(polynom1))
print("Formula N 2: {}".format(polynom2))

polynom11 = convert_pol(polynom1)
polynom21 = convert_pol(polynom2)

pol = fold_pols(polynom11, polynom21)

formula = create_formula(pol)

print("Result formula: {}".format(formula))
