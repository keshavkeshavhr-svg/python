class Heroine:
    def __init__(self):
        self.name="rukku"
        self.age=27
        self.numOfMovies=7
    def act(self):
        print("rukku is good actors")
h1=Heroine()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.address="karanataka"
print(h1.address)
h1.age=28
print(h1.age)
del h1.numOfMovies
print(h1.numOfMovies)