def shift_n_letters(letter, n):
    num = ord(letter)
    num = num+(n)
    if num in range(ord('a'),ord('z')):
        return chr(num)
    if num > ord('z'):
        more = num - ord('z')
        return chr(ord('a')+(more-1))
    if num < ord('a'):
        num1 = ord('a')-num
        return chr(ord('z')-(num1-1)

# the new function
def rotate (word, rotnum):
    roatetedString = ''
    for char in word:
        # call the function rotate
        rotatedChar = shift_n_letters(char,rotnum)
        roatetedString = roatetedString+rotatedChar
    return roatetedString
    
    
print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'