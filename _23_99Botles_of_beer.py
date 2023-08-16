"""Exercise Description

Write a program that displays the lyrics to “99 Bottles of Beer.” Each stanza of the song goes like this:

X bottles of beer on the wall,

X bottles of beer,

Take one down,

Pass it around,

X – 1 bottles of beer on the wall,

The X in the song starts at 99 and decreases by one for each stanza. When X is one (and X – 1 is zero), the last line is 
“No more bottles of beer on the wall!” After each stanza, display a blank line to separate it from the next stanza.

You’ll know you have the program correct if it matches the lyrics at https://inventwithpython.com/bottlesofbeerlyrics.txt. It looks like the following:

99 bottles of beer on the wall,

99 bottles of beer,

Take one down,

Pass it around,

98 bottles of beer on the wall,

 

98 bottles of beer on the wall,

98 bottles of beer,

Take one down,

Pass it around,

97 bottles of beer on the wall,

…cut for brevity…

1 bottle of beer on the wall,

1 bottle of beer,

Take one down,

Pass it around,

No more bottles of beer on the wall!

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: for loops, range() with three arguments, print()"""

def run():

    beers = 99

    for beer in range(beers , 0, -1):
        if beer > 1:
            print(f'{beer} bottles of beer on the wall,\n')
            print(f'{beer} bottles of beer,\n')
            print(f'Take one down,\n')
            print(f'Pass it around,\n')
            print(f'{beer - 1} bottles of beer on the wall,\n')
            print('----------------------------') # this is a paragraph separation

        else:
            print('1 bottle of beer on the wall,\n')
            print('1 bottle of beer,\n')
            print('Take one down,\n')
            print('Pass it around,\n')
            print('No more bottles of beer on the wall!')
            

if __name__ == '__main__':
    run()