class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # total is # of students who want square
        total = sum(students)
        # count is total # of all students
        count = len(students)
        pos_sand = 0
        pos_students = 0
        while count > 0:
            # if all students want square, but circle is at front
            if total == count and sandwiches[pos_sand] == 0:
                return count
            # if all students want circle, but square is at front
            if total == 0 and sandwiches[pos_sand] == 1:
                return count
            # if we can match student at front to sandwich at front
            if students[pos_students] == sandwiches[pos_sand]:
                total -= students[pos_students]  # will go down if student took a square
                count -= 1
                pos_sand += 1
                pos_students += 1
            else:
                # else we will move to back and continue
                students.append(students[pos_students])
                pos_students += 1
        return 0
