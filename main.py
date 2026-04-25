#운동
mon_exercises=[1,2]

exercises_volume=[] 
for i in range(len(mon_exercises)):
    exercise=input("\n종목:")
    sets=int(input('세트 수:'))
    if sets<=0 :
        break
    
    volume=0
    for n in range(1, sets+1):
        weight=float(input('무게:'))
        num=int(input('횟수:'))
        if num <= 0 or weight <=0:
            break
        volume+=weight*num

    exercises_volume.append([exercise, volume])
print(f"{exercises_volume=}")

#신체정보
bodyheight_cm=float(input('키를 입력하시오:'))
bodyheight_m = bodyheight_cm /100
bodyweight=float(input('몸무게를 입력하시오:'))
bmi=bodyweight/(bodyheight_m*bodyheight_m)
if bmi <=18.5:
    mybmi='저체중'
elif bmi>18.5 and bmi<=23:
    mybmi='정상체중'
elif bmi>23 and bmi<=25:
    mybmi='과체중'
else: 
    mybmi='비만'
print(f'bmi={round(bmi, 2)}, {mybmi}입니다')