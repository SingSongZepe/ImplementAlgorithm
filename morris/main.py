

from typing import List, Optional

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

        self.morris_traversal_result = []

    def morris_traversal(self) -> List[int]:
        if not hasattr(self, 'morris_traversal_result'):
            self.morris_traversal_result = []

        curr = self
        while curr:
            if curr.left is None:
                self.morris_traversal_result.append(curr.data)
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right and tmp.right != curr:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = curr
                    curr = curr.left
                else:
                    tmp.right = None
                    self.morris_traversal_result.append(curr.data)
                    curr = curr.right

        return self.morris_traversal_result


def build_tree(arr: List[int]) -> Optional[BinaryTreeNode]:
    def build_helper(arr: List[int], idx: int) -> Optional[BinaryTreeNode]:
        if idx >= len(arr) or arr[idx] is None:
            return None
        node = BinaryTreeNode(arr[idx])
        node.left = build_helper(arr, 2*idx+1)
        node.right = build_helper(arr, 2*idx+2)
        return node
    return build_helper(arr, 0)

def test1():
    arr = [1, 2, 3, 4, 5, 6, 7] # three levels
    root = build_tree(arr)
    print(root.morris_traversal())


def main() -> None:
    test1()




if __name__ == '__main__':
    main()

