'''
Give a binary string consisting of 0's and 1's only. E.g., 0100101. We are allowed to pick
any two indexes and swap them. We have to return the minimum number of swaps required to make
it a palindrome or -1 if it cannot. The string 0100101 can be made a palindrome by swapping
(3,4)-> 0101001 and swapping (0,1) -> 1001001 which is a palindrome. In this case, the
correct answer is 2.

'''

def numswaps(binary):
    n = len(binary)
    count = 0 
    for i in range(n // 2):
        if binary[i] != binary[n - i - 1]:
            count += 1
    if count % 2 == 1 and n % 2 == 0:
        return -1
    return (count + 1) // 2