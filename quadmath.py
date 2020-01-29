import math
from fractions import Fraction


class TheMath:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def calc_zeros(self):
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

        if 'i' in rad or '√' in rad:
            return "(" + str(-b) + " ± " + rad + ") ÷ (" + str(2 * a) + ")"
        else:
            x1 = float(str(((-1 * b) + int(rad)) / (2 * a)))
            x2 = float(str(((-1 * b) - int(rad)) / (2 * a)))

            if x1.is_integer() and x2.is_integer():
                return "x = " + str(x1), "X = " + str(x2)
            else:
                return "x = " + str(Fraction(x1).limit_denominator()), \
                       "x = " + str(Fraction(x2).limit_denominator())

    def convrt_vertex(self):
        a = float(self.__a)
        b = float(self.__b)
        c = float(self.__c)

        h = (-b) / (2 * a)

        k = (a * h ** 2) + (b * h) + c

        # if there is a better way to do this
        # but format it the same, leave a comment
        a = str(round(a, 2))
        h = str(round(h, 2))
        k = str(round(k, 2))

        a_string = a
        h_string = h
        k_string = k

        if '.0' in a_string:
            a_string = a_string.replace('.0', '')

        if '-1' in a_string:
            a_string = a_string.replace('1', '')

        if '.0' in h_string:
            h_string = h_string.replace('.0', '')

        if '.0' in k_string:
            k_string = k_string.replace('.0', '')

        if h[0] == '-':
            h_string = h_string.replace('-', '')
            h_string = ' + ' + h_string
        else:
            h_string = ' - ' + h_string

        if k[0] == '-':
            k_string = k_string.replace('-', '')
            k_string = ' - ' + k_string
        else:
            k_string = k_string.replace('-', '')
            k_string = ' + ' + k_string

        # i hate this part
        if float(a) == 1 and float(h) == 0 and float(k) == 0:
            return 'y = (x)²'
        elif float(a) == 1 and float(h) == 0:
            return 'y = (x)²' + k_string
        elif float(a) == 1 and float(k) == 0:
            return 'y = (x' + h_string + ')²'
        elif float(k) == 0 and float(h) == 0:
            return 'y = ' + a_string + '(x)²'
        elif float(k) == 0:
            return 'y=' + a_string + '(x' + h_string + ')²'
        elif float(h) == 0:
            return 'y = ' + a_string + '(x)²' + k_string
        elif float(a) == 1:
            return 'y = ' + '(x' + h_string + ')²' + k_string
        else:
            return 'y = ' + a_string + '(x' + h_string + ')²' + k_string


# print(TheMath(5, -40, 67).convrt_vertex())
