

import re

from cal import PostfixEvaluator

# def infix_to_postfix(infix_expr):
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
#     output = []
#     operator_stack = []
#
#     tokens = re.findall(r'[A-Za-z0-9]+|[+*/()-]', infix_expr)
#
#     for token in tokens:
#         if token.isalnum():
#             output.append(token)
#         elif token == '(':
#             operator_stack.append(token)
#         elif token == ')':
#             while operator_stack and operator_stack[-1] != '(':
#                 output.append(operator_stack.pop())
#             operator_stack.pop()
#         else:
#             while (operator_stack and operator_stack[-1] != '(' and
#                    precedence[operator_stack[-1]] >= precedence[token]):
#                 output.append(operator_stack.pop())
#             operator_stack.append(token)
#
#     while operator_stack:
#         output.append(operator_stack.pop())
#
#     return ' '.join(output)

class PostfixConverter:

    @staticmethod
    def infix_to_postfix(infix_expr):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        op_stack = []

        # a token is like AAA ABD 1 134
        tokens = re.findall(r'[A-Za-z0-9]+|[+*/()-]', infix_expr)

        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                op_stack.pop()  # throw '('
            else:  # '+-*/'
                while op_stack and op_stack[-1] != '(' \
                    and precedence[op_stack[-1]] >= precedence[token]:
                    output.append(op_stack.pop())
                op_stack.append(token)

        while op_stack:
            output.append(op_stack.pop())

        return ' '.join(output)



def t(expression: str) -> str:
    res = PostfixConverter.infix_to_postfix(expression)
    print(res)
    return res

def test1() -> None:
    expression = "A * B + C"
    t(expression)

def test2() -> None:
    expression = "A*(B+C)+D/C"
    t(expression)

def test3() -> None:
    expression = "A * ( B + C ) + D / C"
    t(expression)

def test4() -> None:
    expression = "10 * ( 103 + 9 ) + 5 / 10"
    postfix_res = t(expression)
    res = PostfixEvaluator.evaluate(postfix_res)
    print(res)

def main():
    # test1()
    # test2()
    # test3()
    test4()


if __name__ == '__main__':
    main()
