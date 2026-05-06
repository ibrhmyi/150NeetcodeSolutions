class Solution:
    def evalRPN(self, tokens: List[str]) -> int: #MOST OPTIMAL SOLUTION
        stack = []
        for token in tokens:
            if token in {"+","-","/","*"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    num = a + b 
                elif token == "-":
                    num = a - b
                elif token == "/":
                    num = int(a / b)
                elif token == "*":
                    num = a * b

                stack.append(num)
            else:
                stack.append(int(token))

        return stack[0]
