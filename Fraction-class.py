import math

class Fraction:
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum
        
    def __add__(self, fraction):
       return self.simplify_fraction(Fraction(self.num * fraction.denum + self.denum * fraction.num, self.denum * fraction.denum))
       
    def __sub__(self, fraction):
       return self.simplify_fraction(Fraction(self.num*fraction.denum - self.denum*fraction.num, self.denum * fraction.denum))
       
    def __mul__(self,fraction):
         return self.simplify_fraction(Fraction(self.num * fraction.num,self.denum * fraction.denum))
         
     def __truediv__(self,fraction):
        return Fraction(self.num * fraction.denum,self.denum * fraction.num)
        
    def __str__(self):
        return str( self.num) + "/" + str(self.denum)
        
    def simplify_fraction(self,fraction):
        common_divisor = math.gcd(fraction.num, fraction.denum)
        (reduced_num, reduced_den) = (fraction.num / common_divisor, fraction.denum / common_divisor)
        if reduced_den == 1:
            fraction.num = reduced_num
            return fraction
        elif common_divisor == 1:
            return fraction
        else:
            fraction.num = reduced_num
            fraction.denum = reduced_den
            return fraction