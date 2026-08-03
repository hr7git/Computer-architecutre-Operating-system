
# [5주차 숙제] 가상 메모리 페이징(Paging) 주소 변환 시스템

# 가상 페이지 번호를 물리 프레임 번호로 매핑해주는 '페이지 테이블' (딕셔너리 자료형)
# 예: 0번 페이지는 5번 프레임에, 1번 페이지는 2번 프레임에 있음
page_table = {
    0: 5,
    1: 2,
    2: 8,
    3: 1
}

PAGE_SIZE = 4096 # 페이지 크기: 4KB (4096 바이트)

def translate_address(logical_address):
    # -------------------------------------------------------------
    # [TODO] 논리 주소를 페이지 번호와 변위(Offset)로 나누고 물리 주소를 구하세요.
    # -------------------------------------------------------------
    # 1. 페이지 번호(page_num) 구하기: logical_address를 PAGE_SIZE로 나눈 '몫'입니다.
    # 2. 변위(offset) 구하기: logical_address를 PAGE_SIZE로 나눈 '나머지'입니다.
    
    page_num = 0  # 이 부분을 수정하세요.
    offset = 0    # 이 부분을 수정하세요.
    
    # 페이지 테이블에 해당 페이지 번호가 있는지 확인
    if page_num not in page_table:
        return "Page Fault! (테이블에 없는 가상 주소 접근)"
    
    # 3. 물리 프레임 번호 찾기
    frame_num = page_table[page_num]
    
    # 4. 최종 물리 주소(physical_address) 계산하기
    #    공식: (프레임 번호 * PAGE_SIZE) + 변위
    physical_address = 0 # 이 부분을 수정하세요.
    
    return f"가상주소 {logical_address} -> [페이지: {page_num}, 변위: {offset}] -> 실제 물리주소: {physical_address}"

# --- 테스트 코드 ---
print("=== 페이징 주소 변환 테스트 ===")
# 1. 0번 페이지의 500번째 변위 주소 변환 테스트 (예상 물리 주소: 5 * 4096 + 500 = 20980)
print(translate_address(500))

# 2. 1번 페이지의 1000번째 변위 주소 변환 테스트 (예상 물리 주소: 2 * 4096 + 1000 = 9192)
print(translate_address(5096)) 
