import math
from fractions import Fraction


class TheMath:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def calc(self):
        a = int(self.__a)
        b = int(self.__b)
        c = int(self.__c)

        d = ((b ** 2) - (4 * a * c))

        if d < 0:
            d_abs = abs(d)
        else:
            d_abs = d

        rad1 = int(d_abs)
        workrad1 = rad1
        sqrnum = 1

        for i in range(2, rad1):
            mexp = 1
            while i ** mexp <= workrad1:
                if workrad1 % i ** mexp == 0:
                    mexp = mexp + 1
                else:
                    break
            if mexp > 2:
                sqrfac = i ** (int((mexp - 1) / 2))
                sqrnum = sqrnum * sqrfac
                workrad1 = workrad1 / (sqrfac ** 2)

        outsidenum = int(sqrnum)
        insidenum = int(rad1 / (sqrnum ** 2))

        if insidenum == 1:
            if d < 0:
                rad = (str(outsidenum) + "i")
            else:
                rad = (str(outsidenum))
        else:
            if outsidenum == 1:
                if d < 0:
                    rad = ("i√" + str(insidenum))
                else:
                    rad = ("√" + str(insidenum))
            else:
                if d < 0:
                    rad = (str(outsidenum) + "i" + "√" + str(insidenum))
                else:
                    rad = (str(outsidenum) + "√" + str(insidenum))

        # if "i" in rad and "√" in rad:
        #     return "(" + str(-b) + " ± " + rad + ") / (" + str(2 * a) + ")"
        # elif "√" in rad:
        #     return "(" + str(-b) + " ± " + rad + ") / (" + str(2 * a) + ")"
        # elif "i" in rad:
        #     return "(" + str(-b) + " ± " + rad + ") / (" + str(2 * a) + ")"
        if 'i' in rad or '√' in rad:
            return "(" + str(-b) + " ± " + rad + ") / (" + str(2 * a) + ")"
        else:
            x1 = float(str(((-1 * b) + int(rad)) / (2 * a)))
            x2 = float(str(((-1 * b) - int(rad)) / (2 * a)))

            if x1.is_integer() and x2.is_integer():
                return "X = " + str(x1), "X = " + str(x2)
            else:
                return "X = " + str(Fraction(x1).limit_denominator()), \
                       "X = " + str(Fraction(x2).limit_denominator())