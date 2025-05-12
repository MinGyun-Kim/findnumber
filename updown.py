# 랜덤으로 숫자 1~100의 숫자 선정
import random
correct = random.randrange(1,100)

# 사용자가 숫자를 입력 받고 correct함수와 비교해서 up down을 출력하고 정답이면 정답을 출력
# 정답 작성한 횟수도 코딩
# 20회만 가능 20회 시 코드 멈춤
challenge_number = 0 # 사용자가 입력한 도전 횟수를 알려주는 변수
while True:          
    challenge_number += 1 # while문이 돈만큼 challenge_number의 값에 1을 증가 시킨다.
    answer = int(input("답 : ")) # 사용자가 변수 입력
    if correct > answer: # correct가 answer 보다 크면 print up 출력
        print("Up")
    elif correct < answer: # correct가 answer 보다 작은면 print down 출력
        print("Down")
    else:                   # 위 두개의 조건이 아닐경우 print 정답 출력 하고 while문 정지
        print("정답")
        break
    if challenge_number == 20: # 만약 challenge_number 도전 횟수가 20이 되면 아래 print출력 하고 while문 정지
        print(f"20번이 끝났습니다 정답은{correct}입니다.")
        break
    print(f"{challenge_number}번 했습니다.") # 사용자의 도전 횟수 출력
