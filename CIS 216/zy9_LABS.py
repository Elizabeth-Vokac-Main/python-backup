# zy9_labs
'''
class FoodItem:
    def __init__(self, item_name='Water', amount_fat=0, amount_carbs=0, amount_protein=0):
        self.name = item_name
        self.fat = amount_fat
        self.carbs = amount_carbs
        self.protein = amount_protein
     
    #       attributes (name, fat, carbs, protein)
       
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
       
    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'  Fat: {self.fat:.2f} g')
        print(f'  Carbohydrates: {self.carbs:.2f} g')
        print(f'  Protein: {self.protein:.2f} g')

if __name__ == "__main__":
       
    item_name = input('input apple')
    if item_name == 'Water' or item_name == 'water':
        food_item = FoodItem()
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       
    
    else:
        amount_fat = float(input(20))
        amount_carbs = float(input(100))
        amount_protein = float(input(30))
        num_servings = float(input(3))
        
        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')


        #zy9 Artist

class Artist:
    def __init__(self, artist_name='unknown', birth_year=-1, death_year=-1):
        self.name = artist_name
        self.birth_year = birth_year
        self.death_year = death_year
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def print_info(self):
    #    if (self.birth_year > 0) and (self.death_year > 0):
        print(f'Artist: {self.name} {self.birth_year} to {self.death_year}')
    # TODO: Define print_info() method

      
class Artwork:
    def __init__(self, title='unknown', year_created=-1, artist_name='unknown'):
        artist_name = Artist()
        self.artist_name = artist_name
        self.title = title
        self.year_created = year_created
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    def print_info(self):
        print(f'Title: {self.title}, {self.year_created}')
        
        
    # TODO: Define print_info() method


if __name__ == "__main__":
    user_artist_name = input('artist')
    user_birth_year = int(input('birth year'))
    user_death_year = int(input('death year'))
    user_title = input('great gatsby')
    user_year_created = int(input('1920'))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created)
    
    user_artist.print_info()
    new_artwork.print_info()

'''

class Pet:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self, breed=''):
        Pet.__init__(self) 
        self.breed = breed
'''       
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')
        print(f'   Breed: { self.breed }')
'''
my_pet = Pet()
my_cat = Cat()


pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()

pet1 = Pet()
pet1.name = pet_name
pet1.age = pet_age
pet1.print_info()


cat1 = Cat()
cat1.name = cat_name
cat1.age = cat_age
cat1.breed = cat_breed
cat1.print_info()
print(f'   Breed: { cat1.breed }')
'''
Dobby
2
Kreacher
3
Scottish Fold
'''

# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()

# TODO: Create cat pet (using cat_name, cat_age, cat_breed) and then call print_info()

# TODO: Use my_cat.breed to output the breed of the cat

#format lines 120 - 131 like 160 and 163 below to see if that works....
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