# holding file for cis unittest file

#Three functions w function stub return None etc

'''


def test_convert_types(self):
        unicode = ['\u00b5', '\u003D', '\u221E']
        animals = ['lions', 'tigers', 'bears']
        letters = ['A', 'B', 'C']
        numbers = ['1', '2', '3']
        symbols = ['µ', '=', '∞']
        self.assertEqual((list(unicode)), (list(symbols)))
        self.assertEqual((list(unicode)), (list(symbols)))

def palindrome_repeats(string, int):
    string = input('Enter a string')
    int = int(input('Enter a positive integer'))
    
    return None

def myabsval(input_int):
        if input_int < 0:
            input_int = -input_int
        return input_int



def celsius_to_kelvin(c_float):
#    k_float = c_float - 273.15
def age_to_seconds(year_int):
#    age_seconds = year_int * 365 * 24 * 3600
def palindrome_repeats(string, int):
    string = input('Enter a string')
    int = int(input('Enter a positive integer'))



    def test_celsius_to_kelvin(self):
        self.assertEqual(celsius_to_kelvin(-273), 0)
        self.assertEqual(celsius_to_kelvin(500), 773)
        self.assertEqual(celsius_to_kelvin(0), 273)


    def test_age_to_seconds(self):
        self.assertEqual(age_to_seconds(1), 31536000)
        self.assertEqual(age_to_seconds(0), 0)
        self.assertEqual(age_to_seconds(-5), None)





def myabsval(input_int):
        if input_int < 0:
            input_int = -input_int
        return input_int

def absolute_val(int_list):
    int_list = [-3, -2, -1, 0, 1, 2, 3]
    for int in int_list:
        if int < 0:
            int = -int 

'''


c_float = float(input('Please enter a value greater than or equal '
                          'to -273.15. '))
def celsius_to_kelvin(c_float):
    if c_float >= -273:
        k_float = c_float + 273.15
        print(k_float)
    else:
        c_float = input('Enter a value greater than or equal to '
                        '-273 because Kelvin scale is all positive.')
celsius_to_kelvin(c_float)
    
