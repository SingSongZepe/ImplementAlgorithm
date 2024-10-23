def find_duplicate(nums):
    # Step 1: Initialize slow and fast pointers
    slow = nums[0]  # Start slow at the first number
    fast = nums[0]  # Start fast at the first number

    # Step 2: Finding the intersection point
    while True:
        slow = nums[slow] if slow < len(nums) else len(nums) - 1  # Move slow pointer by 1 step
        fast = nums[nums[fast] if fast < len(nums) else 0] if fast < len(nums) else len(nums) - 1  # Move fast pointer by 2 steps
        if slow == fast:
            break

    # Step 3: Find the entrance to the cycle
    slow = nums[0]  # Reset slow pointer to the beginning
    while slow != fast:
        slow = nums[slow] if slow < len(nums) else len(nums) - 1  # Move slow pointer by 1 step
        fast = nums[fast] if fast < len(nums) else len(nums) - 1  # Move fast pointer by 1 step

    return slow  # return the duplicate value


def test1() -> None:
    arr = [1, 2, 3, 2]
    res = find_duplicate(arr)
    print(res)  # Output: 2

def test2() -> None:
    arr = [1, 2, 3, 1]
    res = find_duplicate(arr)
    print(res)  # Output: None

def test3() -> None:
    arr = [9, 1, 7, 8, 9, 2, 3, 4, 6]
    res = find_duplicate(arr)
    print(res)  # Output: 9

def main() -> None:
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()

