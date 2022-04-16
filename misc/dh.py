class Person:
    def __init__(self, private: int, g: int, n: int) -> None:
        self.private = private
        self.g = g
        self.n = n
        self.shared = pow(g, private, n)
    
    def gen_key(self, shared: int) -> int:
        return pow(shared, self.private, self.n)


g = 4
n = 23


p1 = Person(4, g, n)

p2 = Person(3, g, n)

print(p1.gen_key(p2.shared), p2.gen_key(p1.shared))

