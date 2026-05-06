class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]: #O(n) BEST
        n = len(temps)
        result = [0] * n
        stack = []

        for today in range(n):
            while stack and temps[today] > temps[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = today - prev_day
            stack.append(today)

        return result


  def dailyTemperatures2(self, temps: List[int]) -> List[int]: #BRUTE FORCE
      days = len(temps)
      output = []
      for today in range(days):
          count = 1       
          tomorrow = today + 1       # Start checking next day
          while tomorrow < days:
              if temps[tomorrow] > temps[today]:  # Found warmer day
                  break
              tomorrow += 1
              count += 1
          # If reached end without finding warmer day
          count = 0 if tomorrow == days else count
          output.append(count)
      return output

  
