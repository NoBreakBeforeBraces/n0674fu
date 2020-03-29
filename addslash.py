import glob
import re


def process(l):
    o = []
    slash = False
    level = None
    duplicate = None
    for i in l:
        if i.startswith("%   "):
            duplicate = i[2:]
            o.append(i)
        elif i.startswith("% ") and i.endswith("\\\\"):
            slash = True
            o.append(i)
        elif i.endswith(":名もない探索者"):
            level = re.search(r"\d{1,3}", i)[0]
            o.append(i)
        elif slash:
            o.append(i + "\\\\")
            slash = False
        elif level:
            o.append(f"{level}:无名的探索者")
            level = None
        elif duplicate:
            if i:
                o.append(i)
            else:
                o.append(duplicate)
            duplicate = None
        else:
            o.append(i)
    return o


if __name__ == '__main__':
    fl = glob.glob("*.tex")
    for j in fl:
        s = open(j, "rb").read().decode().split('\n')
        if s[0] == '% Auto-slash processed':
            continue
        r = ['% Auto-slash processed']
        r += process(s)
        open(j, "wb").write('\n'.join(r).encode())
