

current_calories=0
exercises_volume=[] 
routine_list={'월': ['벤치프레스', '인클라인 벤치프레스', '딥스'], '화':['바벨로우', '랫풀다운', '턱걸이'], 
              '수': ['바벨컬', '트라이셉스 익스텐션', '해머컬', '케이블 푸시다운'], '목': ['스쿼트', '레그프레스']}

def record_diet():
    global current_calories
    target_calories=2500
    
    try:
        calories=float(input('\n섭취한 칼로리:'))
        current_calories+=calories
        print(f'현재 총 섭취량:{current_calories} / {target_calories}kal')
    except ValueError:
        print('\n칼로리는 숫자로 입력')



def cal_exercises_volume():
    volume=0
    sets=0 
  
    try:
            exercise= routine_list[day][i]
            sets=input(f'\n{exercise}의 세트 수 입력:')          
            sets= int(sets)
            
            for n in range(1, sets+1):
                weight,num=input(f'{n}세트의 무게와 횟수를 띄어쓰기로 입력 ').split()
                    
                weight=float(weight)
                num=int(num)
                if weight<=0 or num<=0:
                    break
                volume+= weight*num
    except ValueError:
        print('\n세트 수, 무게, 횟수를 숫자로 입력')
    return exercise, sets, volume




def cal_bmi (bodyheight_cm, bodyweight):
        bodyheight_m = bodyheight_cm /100
        bmi=bodyweight/(bodyheight_m**2)
        if bmi <=18.5:
            my_bmi='저체중'
        elif bmi>18.5 and bmi<=23:
            my_bmi='정상체중'
        elif bmi>23 and bmi<=25:
            my_bmi='과체중'
        else: 
            my_bmi='비만'
        return bmi, my_bmi





def routine():
    day=input('오늘의 요일 입력:')
    if day in routine_list:
        print(f'{day}    {routine_list[day]}')
    else:
        print('해당 요일이 없습니다')




        
def save_exercises():
        
    print('\n----------------------------------------------------------------')
    print(f'\n운동종목    |     세트수     |     볼륨     ')
    for info in exercises_volume:
        print(f'\n{info[0]}     |     {info[1]}     |     {info[2]}     ')
    print('\n----------------------------------------------------------------')

    with open('exercises_record.txt', 'w', encoding='utf-8')as file:
        for info in exercises_volume:
            file.write(f'\n {info[0]}     |     {info[1]}     |     {info[2]}     ')


while True:
    print('\n -----메뉴----')
    print('1. 식단기록')
    print('2. 운동기록')
    print('3. 신체 정보 업데이트')
    print('4. 오늘의 루틴 체크')
    print('5. 운동기록 확인, 저장 ')
    print('6. 종료')

    menu=input('메뉴 선택(1~6):')

    if menu=='1':
        record_diet()

        
    elif menu=='2':
        day=input('오늘의 요일 입력:')
        if day in routine_list:
            for i in range(len(routine_list[day])):
                exercise, sets, volume=cal_exercises_volume()
                exercises_volume.append([exercise, sets, volume])
        else:
            print('해당 요일이 없습니다')

        

    
    elif menu=='3' :
        try:
            bodyheight_cm=float(input('키를 입력하시오:'))
            bodyweight=float(input('몸무게를 입력하시오:'))
            bmi, my_bmi= cal_bmi(bodyheight_cm, bodyweight)
        except ValueError:
            print('\n키와 몸무게를 숫자로 입력')
        print(f'\nbmi={bmi: .2f}, {my_bmi}입니다')


    elif menu=='4':
        routine()



    elif menu=='5':
        if not exercises_volume:
            print('운동기록 데이터가 없습니다')
            continue
        save_exercises()
    
    
    
    elif menu=='6':
        print('종료')
        break

    
    else:
        print('1~6선택')