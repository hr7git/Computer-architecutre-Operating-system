# [2주차 숙제] 가상 CPU의 명령어 실행(Execute) 루틴 완성하기
# 2주 차 과제: [CPU/명령어] 폰 노이만 시뮬레이터 완성
# 개념 연결: 교재에 나오는 '명령어 인출(Fetch) \(\rightarrow \) 명령어 해석/실행(Execute)' 사이클을 눈으로 확인합니다.
# 과제 안내문: "가상의 CPU 레지스터와 메모리를 이용해, 컴퓨터 내부에서 산술 연산 명령어들이 어떻게 처리되는지 조건문으로 구현해 오세요."

# 가상 메모리: [명령어(Opcode), 데이터(Operand)]
memory = [
    ["LOAD", 10],  # 레지스터에 10을 가져와 저장
    ["ADD",  20],  # 레지스터에 원래 있던 값에 20을 더함
    ["SUB",  5],   # 레지스터에 원래 있던 값에서 5를 뺌
    ["END",  0]    # 프로그램 종료
]

class MicroCPU:
    def __init__(self):
        self.PC = 0         # 프로그램 카운터 (다음 실행할 메모리 주소)
        self.register = 0   # 누산기 레지스터 (연산 결과를 임시 저장)
        self.is_running = True

    def fetch(self):
        """메모리에서 명령어를 가져오고 PC를 증가시킵니다."""
        instruction = memory[self.PC]
        self.PC += 1
        return instruction

    def execute(self, instruction):
        """가져온 명령어를 해석하고 실행합니다."""
        opcode, operand = instruction
        print(f"[PC: {self.PC-1}] 명령어 인출 완료 -> 연산코드: {opcode}, 오퍼랜드: {operand}")
        
        # -------------------------------------------------------------
        # [TODO] 아래의 조건문(if-elif)을 완성하여 CPU의 동작을 구현하세요.
        # -------------------------------------------------------------
        # 규칙 1: opcode가 "LOAD"이면 -> self.register에 operand 값을 그대로 대입합니다.
        # 규칙 2: opcode가 "ADD"이면  -> self.register에 operand 값을 더합니다.
        # 규칙 3: opcode가 "SUB"이면  -> self.register에서 operand 값을 뺍니다.
        # 규칙 4: opcode가 "END"이면  -> self.is_running을 False로 변경합니다.
        
        # 여기에 코드를 작성하세요.
        pass

# --- 시뮬레이션 가동 ---
cpu = MicroCPU()
print("=== 가상 CPU 제어 루프 시작 ===")

while cpu.is_running:
    current_instr = cpu.fetch()
    cpu.execute(current_instr)
    print(f"-> 현재 레지스터(값) 상태: {cpu.register}\n")

print("=== 프로그램이 안전하게 종료되었습니다 ===")
