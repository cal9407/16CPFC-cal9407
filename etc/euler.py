# -*-coding:utf8
# 참고문헌 : https://euler.synap.co.kr/prob_detail.php?id=1

"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3,5,7,9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
"""

# sum() 함수와 list comprehension 이름
# S = {i l 0 < i < 1000, i 는 3의 배수 또는 5의 배수인 자연수} 라고 집합을 정의하는 것과 비슷합니다.
print(sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0]))