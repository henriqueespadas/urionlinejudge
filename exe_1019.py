v = int(input())
h = v // 3600
hr = v % 3600
m = hr // 60
mr = hr % 60
s = mr
print(f"{h}:{m}:{s}")
