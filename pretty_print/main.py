
class PrettyPrinter:
    @staticmethod
    def delete_redundant_parentheses(ipt: str) -> str:



        pass


def test1():
    ipt = 'F + ( A * ( B + C ) ) + ( D / C ) * G'
    res = PrettyPrinter.delete_redundant_parentheses(ipt)
    print(res)

def test2():
    ipt = '( A * ( B + C ) )'
    res = PrettyPrinter.delete_redundant_parentheses(ipt)
    print(res)


def main():
    test1()
    test2()

if __name__ == '__main__':
    main()

