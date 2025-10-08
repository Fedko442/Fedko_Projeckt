#Дано целое число N (> 0). Найти сумму 1^N + 2^N-1 + ... + N^n

try:
    N = int(input("Введите целое число N (>0): "))
    
    s = 0
    for i in range(1, N + 1):
        s += i ** i   # прибавляем i^i к сумме
        
        print(f"Сумма 1^1 + 2^2 + ... + N^N при N={N}: {s}")
except ValueError:
    print('Ошибка!')