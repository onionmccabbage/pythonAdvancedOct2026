# Some useful features of Python:
# - the double-ended queue deque
# - zip (not for compression)

from collections import deque
# a normal list has append, pop etc.
# a deque can also appendleft and  popleft

def checkPalindrome(word):
    '''Palindrome is any word or phrase the same in both directions
    madam, racecar etc.'''
    dq = deque(word) #
    # print(dq, type(dq))
    while len(dq)>1:
        left  = dq.popleft()
        right = dq.pop()
        if left != right:
            return False
    return True

def main():
    '''explore zip: combine several data sets into one'''
    days_l   = ['Mon', 'Tue', 'Weds', 'Thur', 'Fri']
    fruit_t  = ('Banana', 'Orange', 'Durian', 'Kiwi')
    drinks_s = {'Coffee', 'Tea', 'Water'} # zip will stop at the shortest data set
    z=  zip(days_l, fruit_t, drinks_s)
    for (day, fruit, drink) in z:
        print(f'On {day} we eat {fruit} with {drink}')
    print(z, type(z))

if __name__ == '__main__':
    print( checkPalindrome('madam') ) # True
    print( checkPalindrome('tenet') ) # True
    print( checkPalindrome('done') ) # False
    main()
