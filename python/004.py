print max(a*b for a in range(100,999) for b in range(100,999) if str(a*b) == str(a*b)[::-1])