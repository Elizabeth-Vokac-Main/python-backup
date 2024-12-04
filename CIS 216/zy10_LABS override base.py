#10.1_Derived_Classes

class PersonData:
    def __init__(self):
        self.last_name = ''
        self.age_years = 0

    def set_name(self, user_name):
        self.last_name = user_name

    def set_age(self, num_years):
        self.age_years = num_years

    # Other parts omitted

    def print_all(self):
        output_str = f'Name: {self.last_name}, Age: {self.age_years}'
        return output_str


class StudentData(PersonData):
    def __init__(self):
        PersonData.__init__(self)  # Call base class constructor
        self.id_num = 0

    def set_id(self, student_id):
        self.id_num = student_id

    def get_id(self):
        return self.id_num


course_student = StudentData()

course_student.last_name = 'Smith'
course_student.age_years = 20
course_student.id_num = '9999'

print(f'{course_student.print_all()}, ID: {course_student.get_id()}')



# fix the below 
import unittest

class Parity:
    def __init__(self, numbers):
        self.numbers = numbers
    def evens(numbers):
        """Return the even values in numbers"""
        return [i for i in numbers if (i % 2 == 0)]

    def odds(numbers):
        """Return the odd values in numbers"""
        return [i for i in numbers if (i % 2 == 1)]


class TestNumbers(unittest.TestCase):
    test_nums = [1, 3, 5, 6, 8, 2, 1]

    def test_evens(self): 
        e = Parity(numbers)
        self.assertIn((e.evens(numbers)), test_nums)

    def test_odds(self):
        o = Parity(numbers)
        self.assertIn((o.odds(numbers)), test_nums)


if __name__ == "__main__":
    unittest.main()



#zy lab 10.10 overriding base class methods (the below got 10/10 all tests passed)
# 
class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')


class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition='', num_pages=0):
        Book.__init__(self, title, author, publisher, publication_date)
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.edition = edition
        self.num_pages = num_pages
    
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_pages
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')
        print(f'   Edition: {self.edition}')
        print(f'   Number of Pages: {self.num_pages}')
        
    
    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Book class

if __name__ == "__main__":
    title = input()
    author = input()
    publisher = input()
    publication_date = input()
    
    e_title = input()
    e_author = input()
    e_publisher = input()
    e_publication_date = input()
    edition = input()
    num_pages = int(input())
    
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()