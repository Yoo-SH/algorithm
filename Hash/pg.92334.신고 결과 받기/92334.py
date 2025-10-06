from collections import defaultdict

def solution(id_list, report, k):

    reported_dict = defaultdict(set)
    id_mail_dic = defaultdict(int)
    result = []

    # `report` 리스트를 순회하며, 각 신고 기록을 파싱하여 `reported_dict`에 신고당한 사람을 키로, 신고한 사람을 값으로 추가 (중복 제거 위해 집합 사용)
    for r in report:
        reporter, reported = r.split()
        reported_dict[reported].add(reporter)
    
    # `reported_dict`의 리스트 크기를 확인하여, 각 사람이 몇 번 신고당했는지 계산
    for reported, reporter_set in reported_dict.items():
        if len(reporter_set) >= k:
            for reporter in reporter_set:
                id_mail_dic[reporter] += 1
        
        
    # `id_list` 순서대로 결과 리스트를 생성하여 반환
    for id in id_list:
        result.append(id_mail_dic[id])


    

    return result