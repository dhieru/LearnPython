# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

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
        return chr(ord('z')-(num1-1))

print shift_n_letters('a', -1)
print shift_n_letters('z', 1)
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i