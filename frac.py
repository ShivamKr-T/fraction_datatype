class Fraction:

    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):
        res_num=self.num * other.den + other.num * self.den
        res_den=self.den * other.den

        [a,b]=self.simplify(res_num,res_den)
        return "{}/{}".format(a,b)

    def __sub__(self,other):
        res_num=self.num * other.den - other.num * self.den
        res_den=self.den * other.den

        [a,b]=self.simplify(res_num,res_den)
        return "{}/{}".format(a,b)

    def __mul__(self,other):
        res_num=self.num * other.num
        res_den=self.den * other.den

        [a,b]=self.simplify(res_num,res_den)
        return "{}/{}".format(a,b)

    def __truediv__(self,other):
        res_num=self.num * other.den
        res_den=self.den * other.num

        [a,b]=self.simplify(res_num,res_den)
        return "{}/{}".format(a,b)

    def simplify(self,n,d):
        i=2
        while i<=min(abs(n),abs(d)):
            if n%i==0 and d%i==0:
                n=n//i
                d=d//i
            else:
                i+=1

        return [n,d]
            
