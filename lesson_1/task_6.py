a = 2
b = 10
result_days = 1
while a < 10:
    a = a + ((a * 10) / 100)
    result_days += 1
    a = a + ((a * 10) / 100)
    if a >= 10:
        print(f"on {result_days:.0f} days")




