
#while문을 사용해서 구구단 프로그램을 만들어 봅시다.
# 실행하면 아래와 같은 결과물이 출력되어야 합니다.



i = 1

while i <= 9:
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, j * i))
        j += 1

    i += 1
