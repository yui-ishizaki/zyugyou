# [직원 출퇴근 관리 프로그램]
# select = 出勤時間更新するかどうか

# 빈 딕셔너리 작성
employees = {}

# 지원수 초기화
employee_count = 0

while True: 
# 메뉴를 출력
 print(f"""
              ======================
              1. 직원 출근 시간 기록
              2. 직원 퇴근 시간 시록
              3. 직원 목록 출력
              4. 프로그램 출력
              
              현재 등록된 지원 수: {employee_count}
              ======================
              """)

# 사용자로부터 메뉴 번호를 입력 받기
 menu_num = input("메뉴를 선택하세요: ")
 
# 1-4: 정보 입력 받기
# if 1번 선택: 사번을 입력 받기
 if menu_num == "1":
     emp_id = input("사번을 입력하세요: ")
     
  # if-if 이미 등록된 경우:출근 시간을 변경합니까?
     if emp_id in employees:
         while True:
             select = input("이미 등록된 사번 입니다. 출근 시간을 변경합니까? (yes or no)")
        
             # if-if-if: "yes" 출근 시간 변경함
             if select == "yes":
              start_time = input("출근 시간을 입력하세요: ")
              employees[emp_id]["출근"] = start_time
              break
             # if-if-elif: "no" 변경 않함 
             elif select == "no":
              break #メニューに戻る
           
             # if-if-else: 에러
             else:
              print("잘못된 입력입니다. 다시 입력하세요: ")     
              
  # if-else: 사번 등록 없음
     else:       
  # 이름, 출근 시간을 입력 받기
      name = input("이름을 입력하세요: ")
      start_time = input("출근 시간을 입력하세요: ")
  # 딕셔너리에 추가  
      employees[emp_id] = {
          "이름": name,
          "출근": start_time,
          "퇴근": ""
      }
  # 지원 수 += 1
      employee_count += 1

# elif 2번 선택: 사번을 입력 받고 퇴근 시간을 입력 받기
# 사번을 입력 받기
 elif menu_num == "2":
     emp_id = input("사번을 입력하세요: ")

  # if 등록 있음: 퇴근 시간 입력 받기
     if emp_id in employees:
         end_time = input("퇴근 시간을 입력하세요: ")
         employees[emp_id]['퇴근'] = end_time
  # else: 에러
     else:
         print("등록되지 않은 사번입니다.") ## １番に飛ぶように修正

# elif 3번 선택: 직원 목록 출력
 elif menu_num == "3":
      for emp_id, info in employees.items():
          print(f"사번: {emp_id}, 이름: {info['이름']}, 출근 시간: {info['출근']}, 퇴근 시간: {info['퇴근']}")
# elif 4번 선택: 프로그램 종료 break
 elif menu_num == "4":
     print("프로그램을 종료합니다.")
     break
# else: 에러
 else:
     
     print("잘못된 입력입니다.")
