class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        target = int(target)
        table = [1 for _ in range(10000)]  # set keeping track of deadends, and visted states
        for deadend in deadends:
            table[int(deadend)] = 0

        # go through possibilites in a queue
        queue = []
        q_pos = 0
        queue.append((0, 0))  # (lock_state, # of turns used), start at (0000, 0)
        while len(queue) > q_pos:
            cur_state = queue[q_pos][0]
            cur_turns = queue[q_pos][1]
            # if target is found
            if cur_state == target:
                return cur_turns
            # if we are not at a deadend or a prev visted state, enqueue all other possible turns
            if table[cur_state]:
                # all possible rotations
                if cur_state >= 9000:
                    queue.append((cur_state - 9000, cur_turns + 1))
                else:
                    queue.append((cur_state + 1000, cur_turns + 1))
                if cur_state % 1000 >= 900:
                    queue.append((cur_state - 900, cur_turns + 1))
                else:
                    queue.append((cur_state + 100, cur_turns + 1))
                if cur_state % 100 >= 90:
                    queue.append((cur_state - 90, cur_turns + 1))
                else:
                    queue.append((cur_state + 10, cur_turns + 1))
                if cur_state % 10 >= 9:
                    queue.append((cur_state - 9, cur_turns + 1))
                else:
                    queue.append((cur_state + 1, cur_turns + 1))
                if cur_state < 1000:
                    queue.append((cur_state + 9000, cur_turns + 1))
                else:
                    queue.append((cur_state - 1000, cur_turns + 1))
                if cur_state % 1000 < 100:
                    queue.append((cur_state + 900, cur_turns + 1))
                else:
                    queue.append((cur_state - 100, cur_turns + 1))
                if cur_state % 100 < 10:
                    queue.append((cur_state + 90, cur_turns + 1))
                else:
                    queue.append((cur_state - 10, cur_turns + 1))
                if cur_state % 10 < 1:
                    queue.append((cur_state + 9, cur_turns + 1))
                else:
                    queue.append((cur_state - 1, cur_turns + 1))
                # mark cur state as visted
                table[cur_state] = 0
            q_pos += 1
        return -1
