# 짝수 4 개를 입력 받아 합계를 반환하는 함수

# 함수 정의 
def sum(input1,input2, input3, input4):
    return input1 + input2 + input3 + input4
    
    
# 정수 4개를 입력 받아 평균을 반환하는 함수
def avg(input1, input2, input3, input4):
    return sum(input1, input2, input3, input4) / 4

    
print(sum(2, 2, 1, 3))
print(avg(2, 2, 1, 3))