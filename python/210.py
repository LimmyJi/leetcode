class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # graph[i][1] = 1 iff j is a prereq for i
        graph = [[0 for i in range(numCourses)] for j in range(numCourses)]
        # prereq_num[i] = num of prereqs i has
        prereq_num = [0 for i in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[0]][prereq[1]] = 1
            prereq_num[prereq[0]] += 1

        # use bfs, start at classes with no prereq
        queue = []
        q_pos = 0
        for i in range(len(prereq_num)):
            if prereq_num[i] == 0:
                queue.append(i)
        # take class next in queue, remove it as a prereq from all classes,
        #   then add classes that have 0 prereq into the queue
        while len(queue) > q_pos:
            cur = queue[q_pos]
            for j in range(len(graph)):
                if graph[j][cur] == 1:
                    graph[j][cur] = 0
                    prereq_num[j] -= 1
                    if prereq_num[j] == 0:
                        queue.append(j)
            q_pos += 1
        # if we no longer have any prereqs, we have taken all courses, return queue as it
        #   is in a valid order
        if sum(prereq_num) == 0:
            return queue
        return []
