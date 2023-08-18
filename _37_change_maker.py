"""Write a makeChange() function with an amount parameter. 
The amount parameter contains an integer of the number of 
cents to make change for. For example, 
30 would represent 30 cents and 125 would 
represent $1.25. This function should return 
a dictionary with keys 'quarters', 'dimes', 'nickels', and 'pennies', 
where the value for a key is an integer of the number of this type of coin.

The value for a coin’s key should never be 0. Instead, 
the key should not be present in the dictionary. 
For example, makeChange(5) should return {'nickels': 1} 
and not {'quarters’: 0, 'dimes': 0, 'nickels': 1, 'pennies': 0}.

For example, makeChange(30) would returns the dictionary 
{'quarters': 1, 'nickels': 5} to represent the 
coins used for 30 cents change. 
The function should use the minimal number of 
coins. For example, makeChange(10) should return 
{'dimes': 1} and not {'nickels': 2}, even though they both add up to 10 cents.

These Python assert statements stop the program if their condition is False. 
Copy them to the bottom of your solution program. Your solution is 
correct if the following assert statements’ conditions are all True:

assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}"""

def makeChange(num):
    dic = {}

    
    if num >= 25:
        dic['quarters'] = num // 25
        num = num % 25
    if num >= 10:
        dic['dimes'] = num // 10
        num = num % 10
        
    if num >= 5:
        dic['nickels'] = num // 5
        num = num % 5
    
    if num >= 1:
        dic['pennies'] = num // 1
            
    return dic

assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}

makeChange(100000000000)

