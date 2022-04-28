class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
    
    def add(self, frac):
        result = Fraction(1, 1)
        result.numerator = ( self.numerator * frac.denominator) + (frac.numerator * self.denominator)
        result.denominator = self.denominator * frac.denominator
        return result

    def sub(self, frac):
        result = Fraction(1, 1)
        result.numerator = (self.numerator * frac.denominator) - (frac.numerator * self.denominator)
        result.denominator = self.denominator * frac.denominator
        return result

    def mul(self, frac):
        result = Fraction(1, 1)
        result.numerator = self.numerator * frac.numerator
        result.denominator = self.denominator * frac.denominator
        return result

    def div(self, frac):
        result = Fraction(1, 1)
        result.numerator = self.numerator * frac.denominator
        result.denominator = self.denominator * frac.numerator
        return result

    def simplify(self):
        while(True):
            if self.numerator % 2 == 0 and self.denominator % 2 == 0:
                self.numerator //= 2
                self.denominator //= 2

            elif self.numerator % 3 == 0 and self.denominator % 3 == 0:
                self.numerator //= 3
                self.denominator //= 3

            elif self.numerator % 5 == 0 and self.denominator % 5 == 0:
                self.numerator //= 5
                self.denominator //= 5

            elif self.numerator % 7 == 0 and self.denominator % 7 == 0:
                self.numerator //= 7
                self.denominator //= 7
            
            else:
                break
    
    def show(self):
        print(self.numerator, "/", self.denominator)

f1 = Fraction(2, 4)
f2 = Fraction(2, 3)

# result = f1.add(f2)
# result.show()

f1.simplify()
f1.show()
