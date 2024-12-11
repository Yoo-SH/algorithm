from collections import deque


class TransformSolver:
    START = "12348765"
    TRANSFORM_TYPE_RULE = [
        [4, 5, 6, 7, 0, 1, 2, 3],  # funtion A
        [3, 0, 1, 2, 7, 4, 5, 6],  # funtion B
        [0, 2, 6, 3, 4, 1, 5, 7],  # funtion C
        [7, 1, 2, 3, 4, 5, 6, 0],  # funtion D
    ]

    def __init__(self, goal):
        self.goal = goal

    def transform(self, state, rule_index):
        return "".join(state[self.TRANSFORM_TYPE_RULE[rule_index][i]] for i in range(8))

    def find_minimum_transforms(self):
        visited = set()
        queue = deque([(self.START, 0)])  # (state, count)
        visited.add(self.START)

        while queue:
            current, count = queue.popleft()

            if current == self.goal:
                return count

            for rule_index in range(4):
                next_state = self.transform(current, rule_index)
                # 이미 방문한 상태는 다시 방문하지 않는다.
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, count + 1))

        return -1  # 변환 불가능한 경우


def parse_input():
    import sys

    input_data = sys.stdin.read().strip()
    chars = input_data.split()
    goal = chars[:4] + chars[4:][::-1]
    return "".join(goal)


if __name__ == "__main__":

    goal_state = parse_input()
    solver = TransformSolver(goal_state)
    result = solver.find_minimum_transforms()
    print(result)
