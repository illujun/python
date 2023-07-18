try:
    4/0 #되겠냐?
except ZeroDivisionError as t: #발생오류 as 오류변수
    print(t)   

# print(4/0) 하면 zerodivisionerror 어쩌구저쩌구 division by zero가 나온다,,

try:
    a = [1,2]
    print(a[3]) #요소가 0, 1인 리스트에서 3 출력하기
    4/0 # 0으로 나누기
except ZeroDivisionError as e:
    print(e) #리스트에러가 먼저 발생하여 division by zero는 출력되지 않음
except IndexError as e:
    print(e) #먼저 발생한 indexerror가 먼저 인식되어 list index out of range가 출력

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e: #이렇게 줄여서 써도 된다!
    print(e)

try:
    age = int(input('나이를 입력하세요: ')) #나이 받아주고
except:
    print("나이가 정확하지 않습니다.") #정수 말고 다른 입력값이 들어와 오류 발생시키면 except 구문 실행
else: #오류가 발생하지 않으면 else 실행
    if age <= 18:
        print("미성년자는 출입 금지입니다.")
    else:
        print("출입 가능합니다!") #여기는 그냥 일반적인 if문

