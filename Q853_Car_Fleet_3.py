class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: #THIS WOULD ONLY WORK IF CARS MOVED 1 UNIT AT A TIME, O(T+n) time complexity
        output = len(position)

        while min(position) < target:
            position = [p + s for p, s in zip(position, speed)]

            seen = {}
            to_remove = set()

            for i, pos in enumerate(position):
                if pos in seen:
                    j = seen[pos]
                    if speed[i] > speed[j]:
                        to_remove.add(i)
                    else:
                        to_remove.add(j)
                        seen[pos] = i  # update slowest at that position
                else:
                    seen[pos] = i

            # rebuild the lists 
            if to_remove:
                output -= len(to_remove)
                position, speed = zip(*[
                    (p, s) for i, (p, s) in enumerate(zip(position, speed)) if i not in to_remove
                ])
                position, speed = list(position), list(speed)

        return output
      

    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int: #SIMPLIFIED
        n = len(position)
        arrivaltime = [(target - x) / y for x,y in zip(position, speed)]
        mylist = sorted(zip(arrivaltime, position), key=lambda x : x[1], reverse=True)
        stack = []

        for s,p in mylist:
            if not stack or s > stack[-1]:
                stack.append(s)
            
        return len(stack)

  
    def carFleet3(self, target: int, position: List[int], speed: List[int]) -> int: #OPTIMAL SOLUTION
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
  
