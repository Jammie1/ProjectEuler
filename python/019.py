from datetime import date

ans = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if date(y, m, 1).weekday() == 6:
            ans += 1

print(ans)