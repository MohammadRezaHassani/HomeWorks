# adding a class as super class for class Z and A

class T:
    def do_job(self,**kwargs):
        # do nothing actually 
        pass

class A(T):
    def do_job(self,**kwargs):
        super().do_job(**kwargs)
        print('I am walking ...')


class Z(T):
    def do_job(self, n,**kwargs):
        super(Z, self).do_job(**kwargs)
        print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')





class B(A):
    def do_job(self, s,**kwargs):
        super().do_job(**kwargs)
        print(f'I am printing your string : "{s}"')


class C(A,Z):
    def do_job(self,**kwargs):
        super().do_job(**kwargs)
        print('I am jumping ...')


class D(B):
    def do_job(self,**kwargs):
        super().do_job(**kwargs)
        print('I am speaking ...')


class E(D, C):
    def do_job(self,**kwargs):
        super().do_job(**kwargs)
        print('I am laughing ...')


class F(Z,B):
    def do_job(self,**kwargs):
        super().do_job(**kwargs)
        # goes to z with super
        print('I am playing ...')


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(3)
# print(E.__mro__)
# print(F.__mro__)
print()

obje = E()
my_dict1={"n":5,"s":"Python"}
obje.do_job(**my_dict1)

print()
objf = F()
my_dict2={"n":6,"s":"Python"}
objf.do_job(**my_dict2)
