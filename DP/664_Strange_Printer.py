import re
class Solution(object):
    
    def strangePrinter(self, s):
        cache = dict()

        def solve(s):
            if not s:
                return 0
            if s in cache:
                return cache[s]
            # cost to simply insert last character
            cost = solve(s[0:-1]) + 1
            # what if last character could be inserted for free just by reusing previous step that already prints it?
			# . . . . . A . . . . A
			# |---------| |-----| last character is free
            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[0:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost
        ## solution remains the same if you remove all duplicates
        
        s = re.sub(r'(.)\1+',r'\1',s)
        return solve(s)
    
    def strangePrinter_noRegex(self, s):
        cache = dict()

        def solve(s):
            if not s:
                return 0
            if s in cache:
                return cache[s]
            # cost to simply insert last character
            cost = solve(s[0:-1]) + 1
            # what if last character could be inserted for free just by reusing previous step that already prints it?
			# . . . . . A . . . . A
			# |---------| |-----| last character is free
            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[0:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost
        ## solution remains the same if you remove all duplicates
        
        s = list(s)
        l = 0
        for i in range(len(s)):
            if s[i] == s[l]:
                continue
            l += 1
            s[l] = s[i]
        s = ''.join(s[:l+1])
        
        print(tt)
        return solve(s)