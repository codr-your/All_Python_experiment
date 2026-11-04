"""
任务4：去重算法对比
data = [5,2,7,2,5,9,7,3,9,1]
方案1 list(set(data))乱序；方案2手写循环保序；dict.fromkeys保序
"""

print("任务4：去重算法对比")


data = [5,2,7,2,5,9,7,3,9,1]
print(f"原始data：{data}")

#方案1 set去重，丢失顺序
res_set = list(set(data))
print(f"方案1‑set去重（乱序） {res_set}")

#方案2手写保序去重
res_hand = []
for num in data:
    if num not in res_hand:
        res_hand.append(num)
print(f"方案2‑手写循环保序去重 {res_hand}")

#方案3 dict.fromkeys保序去重（python3.7+字典key有序）
res_dict = list(dict.fromkeys(data))
print(f"方案3‑dict.fromkeys保序去重 {res_dict}")

print("\n对比：")
print("list(set)优点代码简短；缺点：集合无序，丢失原始出现顺序")
print("手写循环：保留顺序，逻辑直观；缺点：in查询列表，大数据效率低")
print("dict.fromkeys：保序，底层哈希查询效率高，简洁一行代码")
