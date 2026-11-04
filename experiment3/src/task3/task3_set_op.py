"""
任务3：集合运算 + 集合推导式
A = {2,4,6,8,10,12}, B={3,6,9,12,15}
"""

print("任务3：集合运算 + 集合推导式")


A = {2,4,6,8,10,12}
B = {3,6,9,12,15}

print(f"A = {A}")
print(f"B = {B}")
print(f"交集 A & B ：{A & B}")
print(f"并集 A | B ：{A | B}")
print(f"A‑B（A有B没有）：{A - B}")
print(f"B‑A（B有A没有）：{B - A}")
print(f"对称差集 A ^ B：{A ^ B}")

#集合推导式生成1‑30能被4整除
set_div4 = {x for x in range(1,31) if x % 4 ==0}
print(f"\n集合推导式：1~30能被4整除集合 {set_div4}")
