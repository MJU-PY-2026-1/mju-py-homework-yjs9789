while True:
    print('\n -----메뉴----')
    print('1. 식단기록')
    print('2. 운동기록')
    print('3. 신체 정보 업데이트')
    print('4. 오늘의 루틴 체크')
    print('5. 운동루틴 확인 ')
    print('6. 종료')

    menu=input('메뉴 선택(1~6):')

    def cal_exercises_volume():
        total_volume=0
        sets=int(input('세트 수:'))
        if sets<=0 :
            return 0            
        for n in range(1, sets+1):
            weight=float(input('무게:'))
            num=int(input('횟수:'))  
            if weight <= 0 or num<=0:
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



    if menu=='2':
        mon_exercises=[1,2]

        exercises_volume=[] 
        for i in range(len(mon_exercises)):
            exercise=input("\n종목:")
            volume=cal_exercises_volume()
            exercises_volume.append([exercise, volume])
        for n in exercises_volume:
            print(f'{n[0]}, {n[1]}')


    elif menu=='3' :
        bodyheight_cm=float(input('키를 입력하시오:'))
        bodyweight=float(input('몸무게를 입력하시오:'))
        bmi, my_bmi= cal_bmi(bodyheight_cm, bodyweight)
        print(f'bmi={bmi: .2f}, {my_bmi}입니다')

    elif menu=='6':
        print('종료')
        break

    else:
        print('없는 메뉴')