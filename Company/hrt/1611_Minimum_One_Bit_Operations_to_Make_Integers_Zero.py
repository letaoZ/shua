'''
1611. Minimum One Bit Operations to Make Integers Zero
Hard

272

260

Add to List

Share
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

 

Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
 

Constraints:

0 <= n <= 109
'''

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ## if 11000 ->1+op(1000 )
        ## for 2^k, it takes 2^(k+1) - 1 many moves
        ## eg 1000, 1001, 1011, 1010, 1110, 1111, 1101,1100,0100 -->2^3 moves to arrive at 2^2 etc.
        ## the transformation covered ALL numbers between   2^(3+1)-1 to 0
        ## given n, n written as 1xxxx,
        ## minMoves from 1xxxx to 10000 is the min moves from xxxx to 0000
        ## AND we know 1xxxx is in one of the steps from 10000 to 0 i.e. 10000->...->n->...0
        ## SO: minMoves from 1xxxx to 10000 = minimumOneBitOperations(10000) - minimumOneBitOperations(1xxxx)
        ## SO: minimumOneBitOperations(left most of n 0000) - minimumOneBitOperations(n) = minimumOneBitOperations(n remove left most bit)
        
        
        track_moves = {0:0,1:1}
        def bit_to_0(k):
            num = 1<<k
            if num in track_moves:
                return track_moves[1<<k]
            
            track_moves[num] = ((bit_to_0(k-1) + 1)<<1) -1
            # return 1<<(k+1) - 1
            return track_moves[num]
        
        def minmoves(n):
            ## minmoves(highestbit) - minmovs(n removes highest bit)
            if n in track_moves:
                return track_moves[n]
            highestbit = int(math.log2(n))
            remove_bit = (n ^ (1<<highestbit)) ## remove the higest bit
            # print("remove_bit, ",remove_bit)
            # print("highestbit", highestbit)
            track_moves[n] = bit_to_0(highestbit) - minmoves(remove_bit)
            return track_moves[n]
        
        res = minmoves(n)
        # print(track_moves)
        return res