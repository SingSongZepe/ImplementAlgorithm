
from typing import List, Optional
import unittest

class AVLNode:
    def __init__(self, val: int, bf: int, left: Optional['AVLNode'] = None, right: Optional['AVLNode'] = None):
        self.val = val
        self.bf = bf  # bf is balance factor for short
        self.left = left
        self.right = right

class AVL:
    # you can initialize an AVL by giving an AVLNode
    # but also can use static method __from__
    def __init__(self, root: Optional[AVLNode]):
        self.root: Optional[AVLNode] = root

    # notice that the input arr must be a sorted array
    # without that, the AVL will be disordered
    @staticmethod
    def __from__(arr: List[int]) -> 'AVL':

        def power_of_2(v: int) -> bool:
            return (v & (v-1)) == 0

        def build(arr: List[int]) -> Optional[AVLNode]:
            if not arr:
                return None
            if len(arr) == 1:
                return AVLNode(arr[0], 0)
            mid = len(arr) // 2
            if len(arr) % 2 == 1 or power_of_2(len(arr)):
                root = AVLNode(arr[mid], 0)
            else:
                root = AVLNode(arr[mid], 1)

            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])

            return root

        return AVL(build(arr))

    def insert(self, val: int) -> None:

        new_lvl = False
        def _insert(node: AVLNode, val: int) -> None:
            if val == node.val:
                raise Exception('value of any two nodes can\'t be equal')

            if val < node.val:
                if node.left:
                    _insert(node.left, val)
                else:
                    node.left = AVLNode(val, 0)

            else:
                if node.right:
                    _insert(node.right, val)
                else:
                    node.right = AVLNode(val, 0)




        _insert(self.root, val)



    def preorder_traverse(self):
        result = []

        def _preorder(node):
            if node:
                result.append(node.val)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    def inorder_traverse(self):
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)

        _inorder(self.root)
        return result

    def postorder_traverse(self):
        result = []

        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.val)

        _postorder(self.root)
        return result



class Test(unittest.TestCase):
    def test1(self) -> None:
        # constructing of AVL by a sorted array
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
        avl = AVL.__from__(sorted_array)
        print(avl.preorder_traverse())
        print(avl.inorder_traverse())
        print(avl.postorder_traverse())

    def test_insert(self) -> None:
        sorted_array = [4, 10]
        # AVL will be like
        #       10
        #      /
        #    4
        avl = AVL.__from__(sorted_array)
        print(avl.inorder_traverse())

        # after inserting 3
        # AVL will be like
        #        10
        #       /
        #     4
        #    /
        #  3
        # so need a right rotate to be
        #        4
        #      /  \
        #    3    10
        avl.insert(3)
        print(avl.inorder_traverse())




        pass

def main() -> None:
    unittest.main()

if __name__ == '__main__':
    main()
