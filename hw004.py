# 4주 차 과제: [보조기억장치] 하드디스크 FCFS 스케줄러
# 개념 연결: 하드디스크의 디스크 헤드가 요청이 들어온 순서대로 트랙을 이동하는 FCFS(First-Come, First-Served) 알고리즘의 이동 거리를 계산합니다.
# 과제 안내문: "디스크 헤드의 현재 위치와 요청된 트랙 순서가 주어질 때, 헤드가 움직인 총 거리를 계산하는 프로그램을 작성하세요."
# [4주차 숙제] 디스크 스케줄링 FCFS(선입선출) 이동 거리 계산기

def calculate_fcfs_distance(head_start, track_requests):
    current_head = head_start
    total_distance = 0
    
    print(f"디스크 헤드 시작 위치: {current_head}")
    
    for track in track_requests:
        # -------------------------------------------------------------
        # [TODO] 디스크 헤드의 이동 거리를 누적하는 로직을 완성하세요.
        # -------------------------------------------------------------
        # 1. 현재 헤드 위치(current_head)와 가야 할 트랙(track) 사이의 거리를 계산합니다.
        #    (주의: 거리는 항상 양수여야 하므로 파이썬의 abs() 함수를 사용하세요)
        # 2. 계산한 거리를 total_distance에 더해줍니다.
        # 3. 디스크 헤드의 위치(current_head)를 방금 방문한 트랙 위치로 갱신합니다.
        
        distance = 0 # 이 부분을 수정하세요.
        
        print(f"-> 트랙 {track} 이동 (이동 거리: {distance})")
        
    return total_distance

# --- 테스트 코드 ---
start_position = 53
requests = [98, 183, 37, 122, 14]

print("=== FCFS 디스크 스케줄링 시작 ===")
total = calculate_fcfs_distance(start_position, requests)
print(f"\n[결과] 디스크 헤드의 총 이동 거리: {total} 트랙")
# 예상 정답 총 이동 거리: 640
