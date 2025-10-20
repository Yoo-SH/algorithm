from collections import defaultdict

def solution(enroll, referral, seller, amount):
    # 부모 매핑 생성
    parent_mapping = {child: parent for child, parent in zip(enroll, referral)}
    # 각 판매원의 이익 저장
    profits = defaultdict(int)
    
    def distribute_profit(seller, profit):
        # 현재 판매원에게 분배할 금액의 10%를 계산 (원 단위 절사)
        parent_share = profit // 10
        # 현재 판매원이 가질 금액
        my_share = profit - parent_share
        
        # 현재 판매원의 이익에 추가
        profits[seller] += my_share
        
        # 부모가 있고, 분배할 금액이 1원 이상인 경우
        if parent_share >= 1 and seller in parent_mapping:
            parent = parent_mapping[seller]
            # 부모가 "-"가 아닌 경우 (즉, 실제 부모가 있는 경우)
            if parent != "-":
                distribute_profit(parent, parent_share)
    
    # 각 판매 기록에 대해 이익 분배
    for s, a in zip(seller, amount):
        total_profit = a * 100
        distribute_profit(s, total_profit)
    
    # enroll 순서대로 결과 반환
    return [profits[e] for e in enroll]