class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []
        
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y-x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(y/x)
        }
        
        
        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
                
        return stack.pop()