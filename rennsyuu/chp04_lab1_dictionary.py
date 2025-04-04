# 空の辞書を作成
students = {}

date_count = 0
all_avg = 0

# menuを出力
while True:
    
  print(f"""
      ==================
       1. 학생 성적 입력
       2. 학생 목록 출력 (입력 순)
       3. 프로그램 종료
      
      현 입력데이터 갯수:{date_count}
      전체 학생 평균 값:{all_avg / date_count if date_count > 0 else 0:.2f}
      ================== 
      """)

# menu番号入力受ける
  menu_num = input("메뉴를 선택하세요: ")



# if menu == 1
# 학번, 이름, 성적 입력 받기
  if menu_num == "1":
      student_id = input("학번을 입력하세요: ")
      if student_id in students:
          print("이미 등록된 학번입니다.")
      
      else:
        name = input("이름을 입력하세요: ")
        kor = int(input("국어 성적을 입력하세요: "))
        eng = int(input("영어 성적을 입력하세요: "))
        math = int(input("수학 성적을 입력하세요: "))
          
        total = kor + eng + math
        avg = round(total / 3, 2)
        print(f"총점은 {total}점이고, 평균은 {avg}점입니다.")
          
    # 딕셔너리에 추가
        students[student_id] = {
             "이름": name,
             "국어": kor,
             "영어": eng,
             "수학": math,
             "총점": total,
             "평균": avg
             }
         
        date_count += 1
        all_avg += avg

# elif menu == 2
# 딕셔너리 다 출력
  elif menu_num == "2":
      for student_id, info in students.items():
          print(f"학번:{student_id}, 이름:{info['이름']}, 국어:{info['국어']}, 영어{info['영어']}, 수학{info['수학']}, "
            f"총점{info['총점']}, 평균{info['평균']}")
          
# elif menu == 3
# 프로그램 종료
  elif menu_num == "3":
    print("프로그램을 종료합니다.")
    break

# else 間違った入力
  else:
    print("잘못된 입력입니다.")