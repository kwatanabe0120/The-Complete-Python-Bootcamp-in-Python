my_list = [1,2,3]
print(len(my_list))

class Sample():
    pass
my_sample = Sample()

print(len(my_sample))
print(my_sample)


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book is deleted')
    
my_book = Book('Flutter book','John',400)

print(my_book)
print(len(my_book))

del my_book

