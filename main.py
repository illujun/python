a = [1,2,3,4,5,6]

print(a[:3]) #0 생략하고 3 전까지 슬라이싱
print(a[3:7]) # 0부터 시작하니 0,1,2,3 의 요소인 4부터 6까지(7위치) 슬라이싱
print(a[-2:]) #-2 면 -1이 6, -2가 5이니 5부터 끝까지 슬라이싱

if 7 in a: 
    print("들어있습니다") #in으로 a 리스트 안 값 찾기
else:
    print("미포함입니다")

text = "junyac" #text 만들기
finder = text.find('a') #find함수의 값을 받는 함수 만들기
if finder == -1: #미포함일시에 -1의 값이 나옴
    print("미포함입니다")
else:
    print("포함입니다")

b = [2,2,2,2,2,2]

if 2 in a:
    print("들어있습니다")
else:
    print("미포함입니다")

second = "223232322"

while (len(second) > 0): #second 문자열의 길이가 0 전까지 올때까지 반복
    cnt =second.find('2') #2 찾기
    if cnt == -1:
        print("미포함입니다") #원래는 len(second) >= 0으로 해놓고 break했는데 초과로 해놓으면 상관없을듯
    else:
        print("포함입니다")
        second = second[cnt:-1] #막혔던 곳인데 리스트가 0~8 크기니까 cnt: 비워놓으면 마지막 지정이 안되고 8로 해놓으면 슬라이싱 후 크기가 작아진 리스트땜에 무한반복이니 -1로 마지막을 받아줘야함