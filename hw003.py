# [3주차 숙제] 캐시 메모리의 FIFO(선입선출) 교체 알고리즘 구현하기
# 3주 차 과제: [메모리] 캐시 메모리 FIFO 교체 알고리즘
# 개념 연결: 캐시 메모리가 가득 찼을 때, 가장 먼저 들어왔던 데이터를 내보내는 FIFO(First-In, First-Out) 알고리즘을 구현합니다.
# 과제 안내문: "파이썬의 리스트를 활용해 캐시 공간을 시뮬레이션하고, 캐시 미스가 발생했을 때 가장 오래된 데이터를 삭제하는 로직을 완성하세요."

def simulate_fifo(page_requests, cache_size):
    cache = []      # 캐시 공간 (최대 크기: cache_size)
    hit_count = 0
    miss_count = 0

    for page in page_requests:
        # -------------------------------------------------------------
        # [TODO] 아래의 조건문을 완성하여 FIFO 캐시 로직을 완성하세요.
        # -------------------------------------------------------------
        # 1. 만약 page가 cache에 이미 존재한다면 (Cache Hit):
        #    - hit_count를 1 증가시킵니다.
        #
        # 2. 만약 page가 cache에 없다면 (Cache Miss):
        #    - miss_count를 1 증가시킵니다.
        #    - 만약 현재 캐시가 가득 찼다면 (len(cache) == cache_size):
        #        -> 캐시의 맨 앞(가장 먼저 들어온 것) 데이터를 제거합니다. (힌트: cache.pop(0))
        #    - 캐시의 맨 뒤에 새로운 page를 추가합니다. (힌트: cache.append(page))
        
        # (테스트를 위한 임시 pass 코드 - 구현 시 삭제하세요)
        pass

        print(f"요청 데이터: {page} -> 현재 캐시 상태: {cache}")

    # 적중률 계산
    hit_rate = (hit_count / len(page_requests)) * 100
    print(f"\n[결과] Hit: {hit_count}, Miss: {miss_count}, 적중률: {hit_rate:.1f}%")

# --- 테스트 코드 ---
# CPU가 요청하는 데이터 번호 순서
requests = [1, 2, 3, 1, 4, 1, 5, 2]
CACHE_SIZE = 3

print(f"=== FIFO 캐시 시뮬레이션 (캐시 크기: {CACHE_SIZE}) ===")
simulate_fifo(requests, CACHE_SIZE)
