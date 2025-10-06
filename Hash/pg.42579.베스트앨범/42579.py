from collections import defaultdict

def solution(genres, plays):
    genre_to_songs_dict = defaultdict(list)
    genre_to_total_plays_dict = defaultdict(int)
    result =[]

    # 장르를 키로 하고, (재생 횟수, 고유번호) 튜플의 리스트를 값으로 가지는 딕셔너리 생성
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_to_songs_dict[genre].append((play, index))

    #  장르를 키로 하고, 총 재생 횟수를 값으로 가지는 딕셔너리 생성 + 각 장르 내에서 노래를 재생 횟수 기준으로 정렬하고, 재생 횟수가 같은 경우 고유번호 기준으로 정렬합니다.
    for genre, play_list in genre_to_songs_dict.items():
        genre_to_total_plays_dict[genre] = sum(play for play, _ in play_list)
        play_list.sort(key=lambda x: x[0], reverse=True) # 큰 순서대로 내림차순 정렬

    #  총 재생 횟수를 기준으로 장르를 내림차순으로 정렬합니다
    genre_sorted_list = sorted(genre_to_total_plays_dict.items(), key=lambda x: x[1], reverse=True)

    # 각 장르에서 최대 두 개의 노래를 선택하여 인덱스 번호를 결과 리스트에 추가합니다.
    for genre, _ in genre_sorted_list:
        for i in range(min(2, len(genre_to_songs_dict[genre]))):  # 장르에 노래가 1개만 있을 수도 있음
            result.append(genre_to_songs_dict[genre][i][1])

    return result