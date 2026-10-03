class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        res = []
        visit = set()
        done = set()
        def dfs(course):
            if course in visit:
                return False
            if course in done:
                return True
            
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            done.add(course)
            visit.remove(course)
            preMap[course] = []
            res.append(course)
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        