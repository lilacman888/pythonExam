# 조건문 : if else문
# if    조건식 :
#       조건식이 참인 경우에 실행될 문장
#else:
#       조건식이 거짓인 경우에 실행될 문장

# 키보드를 입력한 정수값이 양수인지 음수인지 판별하는 프로그램 작성
n = int(input('정수를입력하세요'))
if n>=0:
    print(n,'은(는) 양수')
else:
    print(n,'은 음수')