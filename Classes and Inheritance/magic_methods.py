class book:
    def __init__(self,title,author,cost):
        self.t = title
        self.a = author
        self.c = cost
    #using __str__ to print the book details
    def __str__(self):
          return f"{self.t} by {self.a} costs {self.c}"
    #using __repr__ to print the book details
    def __repr__(self):
        return f"title = {self.t}, author = {self.a}, cost = {self.c}"
b1 = book("Harry Potter","JK Rowling",100)
b2 = book("The Lord of the Rings","Tolkien",200)
print(b1)
print(repr(b2))
print(str(b2))