# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000

# 코드를 입력하세요.


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 125


# 코드를 입력하세요.


# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))

# amounts를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.

# 달러($)로 각각 얼마인가요?
i = 0
while i < len(amounts):
    amounts[i] = round(krw_to_usd(amounts[i]), 1)
    i += 1
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.

# 엔화(￥)으로 각각 얼마인가요?
n = 0
while n < len(amounts):
    amounts[n] = round(usd_to_jpy(amounts[n]), 1)
    n += 1
print("일본 화폐: " + str(amounts))
