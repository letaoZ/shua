'''
582. Kill Process
Medium

809

16

Add to List

Share
You have n processes forming a rooted tree structure. Y
ou are given two integer arrays pid and ppid, 
where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. 
Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, 
return a list of the IDs of the processes that will be killed. You may return the answer in any order.

 

Example 1:


Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.
Example 2:

Input: pid = [1], ppid = [0], kill = 1
Output: [1]
'''

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        dict_ids = collections.defaultdict(list) ## parent id->decendent id
        for i in range(len(pid)):
            dict_ids[ppid[i]].append(pid[i])
        queue = collections.deque()
        queue.append(kill)## kill is ID
        res  = [kill]
        while queue:
            cur = queue.popleft()
            ## find whose parent has ID == cur
            res.extend(dict_ids[cur])
            for nn in dict_ids[cur]:
                queue.append(nn)
        return res