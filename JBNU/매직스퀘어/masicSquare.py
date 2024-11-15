class MagicSquare:
    def __init__(self, initial_list=None):
        if initial_list:
            self.line_one_magic = initial_list[:4]
            self.line_two_magic = initial_list[4:]
        else:
            self.line_one_magic = [1, 2, 3, 4]
            self.line_two_magic = [8, 7, 6, 5]

        # 두 줄로 구성된 2차원 리스트 생성
        self.magic = [self.line_one_magic, self.line_two_magic]

    def getMagic(self) -> list:
        return self.magic

    def function_A(self) -> None:
        # 윗줄과 아랫줄을 서로 바꾼다
        self.magic[0], self.magic[1] = self.magic[1], self.magic[0]

    def function_B(self) -> None:
        # 각 줄의 숫자를 오른쪽으로 한 칸씩 이동, 마지막을 첫 번째로
        self.magic[0].insert(0, self.magic[0].pop())
        self.magic[1].insert(0, self.magic[1].pop())

    def function_C(self) -> None:
        # 가운데 4개의 숫자를 반시계 방향으로 회전
        self.magic[0][1], self.magic[0][2], self.magic[1][1], self.magic[1][2] = (
            self.magic[0][2], self.magic[1][2], self.magic[0][1], self.magic[1][1]
        )

    def function_D(self) -> None:
        # 1번 위치와 5번 위치의 숫자를 서로 바꾼다
        self.magic[0][0], self.magic[1][3] = self.magic[1][3], self.magic[0][0]
        
    def copy(self):
        new_magic_square = MagicSquare() # 얇은 복사를 위해 새로운 매직스퀘어 객체 생성
        new_magic_square.magic = [row[:] for row in self.magic]  # 본래의 매직스퀘어를 복사하여 새로운 매직스퀘어 생성
        return new_magic_square # 새로운 매직스퀘어 반환

    def print_square(self):
        print(self.magic)


def bfs_magic_square(initial_square: MagicSquare, goal_square: MagicSquare) -> int:
    queue = [(initial_square, 1)]  # 큐에 (현재 상태, 레벨)을 저장, 레벨은 매직스퀘어 동작 횟수라 볼 수 있음.
    visited = set()  # 방문한 상태 저장
    

    while queue:
        
        current_square, level = queue.pop(0)  # 첫 번째 요소를 꺼냄 (BFS)
        function_order = ["A", "B", "C", "D"]  # 가능한 연산
        # 가능한 연산을 모두 수행하여 새로운 상태 탐색

        for func in function_order:
            new_square = current_square.copy()
        
            # 함수 호출
            if func == "A":
                new_square.function_A()

                # 목표 상태에 도달했는지 확인
                if new_square.getMagic() == goal_square.getMagic():
                    return level
                
                new_square_str = str(new_square.getMagic())

                # 방문한 상태가 아니라면 큐에 추가
                if new_square_str not in visited: 
                    visited.add(new_square_str)
                    queue.append((new_square, level + 1))  # 방문 하지 않았으면, 큐에 추가. 한번 하고 바로 큐에 넣어줘야 BFS 성립

            elif func == "B":
                new_square.function_B()

                # 목표 상태에 도달했는지 확인
                if new_square.getMagic() == goal_square.getMagic():
                    return level
                
                # 방문한 상태라면 큐에 들어가서는 안됨
                new_square_str = str(new_square.getMagic())

                # 방문한 상태가 아니라면 큐에 추가
                if new_square_str not in visited: 
                    visited.add(new_square_str)
                    queue.append((new_square, level + 1))  # 방문 하지 않았으면, 큐에 추가. 한번 하고 바로 큐에 넣어줘야 BFS 성립
                
            elif func == "C":
                new_square.function_C()
                
                # 목표 상태에 도달했는지 확인
                if new_square.getMagic() == goal_square.getMagic():
                    return level
                
                # 방문한 상태라면 큐에 들어가서는 안됨
                new_square_str = str(new_square.getMagic())

                # 방문한 상태가 아니라면 큐에 추가
                if new_square_str not in visited: 
                    visited.add(new_square_str)
                    queue.append((new_square, level + 1))  # 방문 하지 않았으면, 큐에 추가. 한번 하고 바로 큐에 넣어줘야 BFS 성립

            elif func == "D":
                new_square.function_D()                
                
                # 목표 상태에 도달했는지 확인
                if new_square.getMagic() == goal_square.getMagic():
                    return level
                
                # 방문한 상태라면 큐에 들어가서는 안됨
                new_square_str = str(new_square.getMagic())

                # 방문한 상태가 아니라면 큐에 추가
                if new_square_str not in visited: 
                    visited.add(new_square_str)
                    queue.append((new_square, level + 1))  # 방문 하지 않았으면, 큐에 추가. 한번 하고 바로 큐에 넣어줘야 BFS 성립

    return -1  # 목표 상태에 도달할 수 없을 경우


if __name__ == "__main__":
    

    # 입력을 받아서, 공백을 기준으로 int값 할당하여 리스트에 저장
    input_list = list(map(int, input().split()))
    
    magicSquare = MagicSquare()  # 매직 스퀘어 객체        
    magicSquare_goal = MagicSquare(input_list)

    if magicSquare.getMagic() == magicSquare_goal.getMagic():
        print(0)
    else:  
        print(bfs_magic_square(magicSquare, magicSquare_goal))
