"""
任务2：嵌套容器与可哈希深度辨析
测试add不同对象，区分可哈希/不可哈希；frozenset作用
"""

print("任务2：嵌套容器与可哈希深度辨析")


s = set()

# 测试1 s.add((1,2,3))
try:
    s.add((1,2,3))
    print("ture add((1,2,3))成功：元组全部元素可哈希，整体可哈希")
except Exception as e:
    print(f"false {(1,2,3)}报错：{e}")

#测试2 s.add((1,[2,3]))
try:
    s.add((1,[2,3]))
    print("ture add((1,[2,3]))成功")
except Exception as e:
    print(f"false add((1,[2,3]))报错:{e}；理由：元组内包含list可变不可哈希，整个元组不可哈希")

#测试3 s.add([1,2])
try:
    s.add([1,2])
    print("ture add([1,2])成功")
except Exception as e:
    print(f"false add([1,2])报错:{e}；理由：list可变，不可哈希，不能放入set")

#测试4 s.add(frozenset({1,2}))
try:
    s.add(frozenset({1,2}))
    print("ture add(frozenset({1,2}))成功：frozenset不可变，可哈希")
except Exception as e:
    print(f"false frozenset报错:{e}")

#测试5 s.add({1,2})
try:
    s.add({1,2})
    print("ture add({1,2})成功")
except Exception as e:
    print(f"false add({{1,2}})普通set报错:{e}；普通set可变不可哈希，不能作为集合元素")

print(f"\n集合s最终内容：{s}")
print("\n思考：集合内存放集合 → 使用 frozenset，固定集合，可哈希")
