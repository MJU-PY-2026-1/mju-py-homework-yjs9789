

current_calories=0

def record_diet():
    global current_calories
    target_calories=2500
    calories=float(input('\n섭취한 칼로리:'))
    current_calories+=calories

    print(f'현재 총 섭취량:{current_calories} / {target_calories}kal')



def cal_exercises_volume():
    total_volume=0  
    sets=int(input('세트 수'))

    if sets<=0 :
        return 0            
    for i in range(1, sets+1):
        weight_num=input(f'{i}세트의 무게와 횟수를 띄어쓰기로 입력 ').split()
        
        weight=float(weight_num[0])
        num=int(weight_num[1])
        if weight<=0 or num<=0:
            break
        total_volume+= weight*num
    return total_volume
        

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


while True:
    print('\n -----메뉴----')
    print('1. 식단기록')
    print('2. 운동기록')
    print('3. 신체 정보 업데이트')
    print('4. 오늘의 루틴 체크')
    print('5. 운동루틴 확인 ')
    print('6. 종료')

    menu=input('메뉴 선택(1~6):')

    if menu=='1':
        record_diet()

        
    elif menu=='2':
        mon_exercises=[1,2]

        exercises_volume=[] 
        for i in range(len(mon_exercises)): 
            exercise=input('\n운동 종목:')      
            volume=cal_exercises_volume()
            exercises_volume.append([exercise, volume])
        
        print()
        for n in exercises_volume:
            print(f'{n[0]}, {n[1]}')

    
    elif menu=='3' :
        bodyheight_cm=float(input('키를 입력하시오:'))
        bodyweight=float(input('몸무게를 입력하시오:'))
        bmi, my_bmi= cal_bmi(bodyheight_cm, bodyweight)
        print(f'\nbmi={bmi: .2f}, {my_bmi}입니다')

    
    elif menu=='6':
        print('종료')
        break

    else:
        print('1~6선택')