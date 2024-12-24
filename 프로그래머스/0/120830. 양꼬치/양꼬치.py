def solution(n, k):
    service_drinks = n // 10  # 서비스로 제공되는 음료수 개수
    total_price = (n * 12000) + (k * 2000) - (service_drinks * 2000)
    return total_price