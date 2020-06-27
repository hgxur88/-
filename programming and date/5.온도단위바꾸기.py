#화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.
#섭씨와 화씨의 관계식은 다음과 같습니다:
#화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요.
#이 함수를 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
i = 0
def fahrenheit_to_celsius(fahrenheit):
      return (fahrenheit - 32) * 5 / 9
    # 코드를 입력하세요.


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.

while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1# 섭씨 온도 출력

print("섭씨 온도 리스트: " + str(temperature_list))
