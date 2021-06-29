# TC: O(N) as we process all the functions given in the input. 
# SC: O(N) since every function is stored in the stack until processed completely. 

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not logs or len(logs) == 0: 
            return
        
        stack = []
        result = [0]*n
        curr = prev = 0
        for i in range(len(logs)): 
            id, start_end, timestamp = logs[i].split(":")
            curr = int(timestamp)
            if start_end == "start":
                if stack: 
                    result[stack[-1]] += curr - prev
                prev = curr
                stack.append(int(id))
            elif start_end == "end": 
                if stack: 
                    result[stack.pop()] += curr - prev + 1
                prev = curr + 1
        
        return result
