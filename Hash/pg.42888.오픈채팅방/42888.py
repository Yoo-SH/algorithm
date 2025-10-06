def solution(record):

    user_dict :dict = {}
    result = []

    # 유저 최종 닉네임 확인
    for i in record:
        parts = i.split()
        command = parts[0]
        user_id = parts[1]

        if command in ["Enter", "Change"]:
            nick_name = parts[2]
            user_dict[user_id] = nick_name


    # 유저 채팅방 결과 생성
    for i in record:
        parts = i.split()
        command = parts[0]
        user_id = parts[1]

        if command == "Enter":
            result.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{user_dict[user_id]}님이 나갔습니다.")
    
    
    return result