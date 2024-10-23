

from typing import List

def boyer_moore_majority_vote(arr: List[int]) -> int:
    candidate = None
    vote = 0

    for n in arr:
        if vote == 0:
            candidate = n
        vote += 1 if n == candidate else -1

    return candidate


def test1() -> None:
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(boyer_moore_majority_vote(arr))


def main() -> None:
    test1()


if __name__ == '__main__':
    main()

