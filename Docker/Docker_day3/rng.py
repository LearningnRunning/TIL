from random import randint

min_numer = int(input("최솟값을 넣어주세요: "))
max_numer = int(input("최댓값을 넣어주세요: "))

if max_numer < min_numer:
    print("잘못된 정보를 입력하였습니다. 죄송합니다.")
else:
    rnd_number = randint(min_numer, max_numer)
    print(rnd_number)
