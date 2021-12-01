cost = int(input("Enter cost your company "))
proceeds = int(input("Enter proceeds your firm "))
if proceeds > cost:
    print("The company works for profit")
    profitability = proceeds / cost
    print(f"profitability = {profitability:.3f}")
    workers = int(input("Enter the number of workers in your company "))
    print(f"profit per worker was: {profitability / workers:.2f}")
elif proceeds == cost:
    print("company works in zero")
else:
    print("The company is operating at a loss")

