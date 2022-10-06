import math

"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Fraction:

    def __init__(self, num, den):
        # "constructor", more precisely "initializer"
        # initialize Fraction here
        self.num = num
        self.den = den


    def __repr__(self):
        # magic method for text representation
        # return Fraction as a string in `numerator/denominator` format, e.g 1/2, 3/4, 153/468 etc.
        return(f'{self.num}/{self.den}')

    def normalize(self):
        # from this Fraction get normalized Fraction, return normalized Fraction
        gcd = math.gcd(self.num, self.den)
        self.num = int( self.num / gcd )
        self.den = int( self.den / gcd )
        return Fraction(self.num, self.den)

    def __eq__(self, other):
        # magic method for comparison `==`
        # compare two fractions if they are same
        # two Fractions are same if their normalized numerators and denominators are equal respectively
        # example 1/3 is equal to 2/6, 1/3 is not equal to 3/1
        if self.num/self.den == other.num/other.den:
            return True
        else:
            return False

    def __lt__(self, other):
        # magic method for comparison `<`
        # compare two fractions if the first one is less than second one
        # example 1/3 <= 1/2
        if self.num/self.den < other.num/other.den:
            return True
        else:
            return False

    def __le__(self, other):
        # magic method for comparison `<=`
        # compare two fractions if the first one is less than or equal to the second one
        # example 1/3 <= 1/2
        if self.num/self.den <= other.num/other.den:
            return True
        else:
            return False

    def normalize2(num, den): # i call this method 4 times. So, it is necessary
        gcd = math.gcd(int(num), int(den))
        den = den / gcd
        num = num / gcd
        return([num,den])

    def add(self, other):
        # take other Fraction, execute adding, return new Fraction with the result
        new_den = self.den * other.den
        self.num = (self.num * int(new_den/self.den) + other.num*int(new_den/other.den))
        self.den = new_den

        # gcd = math.gcd(int(self.num), int(self.den))
        # print(gcd)
        # self.den = self.den / gcd
        # self.num = self.num / gcd

        self.num, self.den = Fraction.normalize2(self.num,self.den)
        return Fraction(int(self.num), int(self.den))

    def sub(self, other):
        # take other Fraction, execute subtraction, return new Fraction with the result
        new_den = self.den * other.den
        self.num = (self.num * int(new_den / self.den) - other.num * int(new_den / other.den))
        self.den = new_den
        self.num, self.den = Fraction.normalize2(self.num, self.den)
        return Fraction(int(self.num), int(self.den))


    def mul(self, other):
        # take other Fraction, execute multiplication, return new Fraction with the result
        return Fraction(self.num*other.num, self.den*other.den)

    def div(self, other):
        # take other Fraction, execute division, return new Fraction with the result
        return Fraction(self.num*other.den, self.den/other.num)

    def __add__(self, other):
        # magic method for operation `+`
        # same as add()
        new_den = self.den * other.den
        self.num = (self.num * int(new_den / self.den) + other.num * int(new_den / other.den))
        self.den = new_den
        self.num, self.den = Fraction.normalize2(self.num, self.den)
        return Fraction(int(self.num), int(self.den))

    def __sub__(self, other):
        # magic method for operation `-`
        # same as sub()
        new_den = self.den * other.den
        self.num = (self.num * int(new_den / self.den) - other.num * int(new_den / other.den))
        self.den = new_den
        self.num, self.den = Fraction.normalize2(self.num, self.den)
        return Fraction(int(self.num), int(self.den))

    def __mul__(self, other):
        # magic method for operation `*`
        # same as mul()
        return Fraction(self.num*other.num, self.den*other.den)

    def __truediv__(self, other):
        # magic method for operation `/`
        # same as div()
        return Fraction(self.num*other.den, self.den/other.num)


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# constructor
assert Fraction(1, 2).num == 1 and Fraction(1, 2).den == 2

# repr
assert f"{Fraction(1, 2)}" == "1/2"

# normalization
assert Fraction(3, 6).normalize().num == 1 \
       and Fraction(3, 6).normalize().den == 2 \
       and type(Fraction(3, 6).normalize().num) is int \
       and type(Fraction(3, 6).normalize().den) is int

# comparison magic
assert Fraction(1, 3) == Fraction(2, 6)
assert not(Fraction(1, 3) == Fraction(3, 1))
assert Fraction(1, 3) <= Fraction(1, 2)
assert Fraction(1, 3) < Fraction(1, 2)


# operation methods
assert Fraction(1, 2).add(Fraction(1, 3)) == Fraction(5, 6)
assert Fraction(1, 2).sub(Fraction(1, 3)) == Fraction(1, 6)
assert Fraction(2, 2).mul(Fraction(1, 3)) == Fraction(1, 3)
assert Fraction(1, 2).div(Fraction(1, 3)) == Fraction(3, 2)

# operators magic
assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)