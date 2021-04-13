'''
1125. Smallest Sufficient Team

In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
'''

## trick!! (refer to Huahua)
## there are at most 16 skills; but 60 people!! If we do setwise computation
## 60 people = 2^60 many cases; 16 skills  = 2^16 many cases
## so, we should use cases to STORE results/run dp
##
## This is also similar to knapsack problems!

class Solution:
    def smallestSufficientTeam_save_space_using_df(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: (1<<i) for i, v in enumerate(req_skills)}

        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= key[skill]

            ## you cannot modify dict in a loop
            dp_tmp = dp.copy()
            for skill_set, need in dp_tmp.items():
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]        
    
    
    def smallestSufficientTeam_reserve_space(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: (1<<i) for i, v in enumerate(req_skills)}
        
        Target = (1<<n )
        dp = [float('inf')]*(Target)
        dp_skills = [()]*(Target)

        prev = 0
        dp[0] = 0
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= key[skill]
                    
            ## use reverse
            ## because with_his_skill has already included his_skill
            ## if the smaller values changed, then it will impact the later (bigger values)
            for sk_r in reversed(range((Target))):
                with_his_skill = (sk_r|his_skill)
                
                if with_his_skill == sk_r: continue
                if dp[with_his_skill]> dp[sk_r] + 1:
                    dp[with_his_skill] = dp[sk_r] + 1
                    dp_skills[with_his_skill] = (sk_r, i)

        res = []
                    
        t = (Target- 1)

        while t:
            res.append(dp_skills[t][1])
            t = dp_skills[t][0]
            
        return res