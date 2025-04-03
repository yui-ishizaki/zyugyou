# 짝수 4 개를 입력 받아 합계를 반환하는 함수


# 함수 정의 
def prt_even_odd(arg_input):
    if arg_input % 2 == 0:
        msg = "짝수"
        
    else:
        msg = "홀수"
        
    print(f"{msg} 입니다.")        

# 정의된 호출
prt_even_odd(2) # 짝수 입니다
prt_even_odd(3) # 홀수 입니다

