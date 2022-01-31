class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        stack = []
        cur_passengers = 0

        for i in range(len(trips)):
            while stack and trips[stack[-1]][2] <= trips[i][1]:
                cur_passengers -= trips[stack[-1]][0]
                stack.pop()

            if cur_passengers + trips[i][0] > capacity:
                return False

            if stack and trips[stack[-1]][1] == trips[i][1] or stack and trips[i][2] > trips[stack[-1]][2]:
                temp_stack = []
                while stack and trips[stack[-1]][2] < trips[i][2]:
                    temp_stack.append(stack.pop())
                stack.append(i)
                cur_passengers += trips[i][0]
                while temp_stack:
                    stack.append(temp_stack.pop())
                continue
            stack.append(i)
            cur_passengers += trips[i][0]
        return True
