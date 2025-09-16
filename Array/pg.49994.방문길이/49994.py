def is_valid_pos(x, y):
    if x >= -5 and x <= 5 and y >= -5 and y <= 5:
        return True
    else:
        return False


def solution(dirs):

    pass_road = set()
    x, y = 0, 0  # 현재 위치
    pass_road_count = 0  # 지나온 길 카운트

    for direction in dirs:
        dx, dy = 0, 0
        if direction == "U":
            dy += 1
        elif direction == "R":
            dx += 1
        elif direction == "L":
            dx -= 1
        elif direction == "D":
            dy -= 1

        if is_valid_pos(x + dx, y + dy) == False:  # 유효한 길인지 검사
            print("유효한 길이 아님")
            pass
        elif ((x, y), (x + dx, y + dy)) in pass_road:  # 이미 지나온 길인지 검사
            print("이미 지나온 길입니다.")
            x += dx  # x좌표 이동
            y += dy  # y좌표 이동
            pass
        else:
            pass_road.add(((x, y), (x + dx, y + dy)))  # (현재 좌표, 이동한 좌표) 추가
            print(f"x:{x} y:{y} 에서 {x+dx}, {y+dy}로 이동")
            pass_road.add(((x + dx, y + dy), (x, y)))  # (이동한 좌표. 현재 좌표) 추가
            pass_road_count += 1
            x += dx  # x좌표 이동
            y += dy  # y좌표 이동

    answer = pass_road_count
    return answer
