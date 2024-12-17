if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        applicants = []  # 각 테스트 케이스마다 초기화
        passedApplicants = 0
        N = int(input())

        for _ in range(N):
            documentRank, interviewRank = map(int, input().split())
            applicants.append((documentRank, interviewRank))

        applicants.sort(key=lambda x: x[0])  # 서류 등수 기준 정렬
        minInterviewRank = N  # 최솟값 초기화

        for documentRank, interviewRank in applicants:
            if interviewRank <= minInterviewRank:
                minInterviewRank = interviewRank
                passedApplicants += 1

        print(passedApplicants)
