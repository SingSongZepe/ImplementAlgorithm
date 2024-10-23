#
# def evaluate_postfix(postfix_expr):
#     stack = []
#
#     tokens = postfix_expr.split()
#
#     for token in tokens:
#         if token.isnumeric():
#             stack.append(int(token))
#         elif token.isalnum():
#             stack.append(ord(token) - ord('A') + 1)
#         else:
#             right = stack.pop()
#             left = stack.pop()
#
#             if token == '+':
#                 result = left + right
#             elif token == '-':
#                 result = left - right
#             elif token == '*':
#                 result = left * right
#             elif token == '/':
#                 result = left / right
#             else:
#                 raise ValueError(f"未知的操作符: {token}")
#
#             stack.append(result)
#
#     return stack.pop()



class PostfixEvaluator:
    @staticmethod
    def evaluate(postfix_expr: str):
        stack = []
        for token in postfix_expr.split():
            if token.isnumeric():
                stack.append(int(token))
            # elif // other token like A n x
            elif token in '+-*/':
                right = stack.pop()
                left = stack.pop()
                match token:
                    case '+':
                        stack.append(left + right)
                    case '-':
                        stack.append(left - right)
                    case '*':
                        stack.append(left * right)
                    case '/':
                        stack.append(left / right)
            else:
                raise ValueError(f"未知的操作符: {token}")
        return stack.pop()
