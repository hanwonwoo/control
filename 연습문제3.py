# # #1. 임의의 값을 받아서
# # data=input("값을 입력하세요:")
# #
# # #2. 해당 수가 5초과 10미만사이에 있다
# #
# # data_2= input(5<data<10)
# #
# # if data_2<10
# # #3. 'ok'를 출력하고
# # #4. 그렇지 않은 경우 'no'를 출력
#
#
# x = 4
# if 5 < x < 10:
#     print(x)
#
#
# elif 15<= x:
#     print(x)
# else :
#     print("no")
#
#
# # and, or  연산자
# apple ='사과'
# banana ='감자'
#
# if apple =='사과' or banana =='바나나':
#     print("문자열이 모두 정확합니다.")
# #
# #
# #
# #
# # var =[1,2,3]
# # if 찾고자 하는 요소 in 변수:
# #     print("숫자 3이 var 변수에 있습니다.")
#
#
#
# # fruit = ["사과", "포도", "홍시"]
# # if "사과" in fruit:
# #     print("정답입니다")
#
# #1. 사용자로부터 입력받아
# text = input("조회할 요소를 입력하세요:")
# #2. fruit 변수는 리스트
# fruit=["사과", "포도","홍시"]
# #3. 입력받은 값이 fruit에 요소로 있는지 확인
# if text in fruit:
#     print("정답입니다.")
# else :
#     print("오답입니다.")
#
#


text = input("조회할 요소를 입력하세요")
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if text in fruit.values():
    print("정답입니다.")
else :
    print("오답입니다.")








