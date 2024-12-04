#zy11_LABS 

prize1, prize2, prize3 = input('one, two, three').split()
prizes_left = {prize1, prize2, prize3}

try:
    prize_claimed = input('two')
    prizes_left.remove(prize_claimed)
    
    print(f'Selected: {prize_claimed}')
    
    if prize_claimed not in prizes_left:
        raise KeyError('is unavailable')
    
except KeyError as excpt1:
    print(f'{prize_claimed} {excpt1}') 


#zy LAB 11.10
#things to note = the value error auto prints like this below because
#of using valueerror as excpt (aka as a variable excpt) and needs the
#double quotes
#prints as... Input Exception: invalid literal for int() with base 10: '15.5'
user_num = input()
div_num = input()

try:
    quotient = int(int(user_num) / int(div_num))
    print(f'{quotient}')
    
except ValueError as excpt:
    print(f"Input Exception: {excpt}")
except ZeroDivisionError:
    print(f'Zero Division Exception: integer division or modulo by zero')
    