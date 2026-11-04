"""
任务5 综合选课统计
class1 = [101,103,105,107,109,103,101]
class2 = [102,104,106,108,109,107,102]

"""

print("任务5：综合选课统计")


class1 = [101,103,105,107,109,103,101]
class2 = [102,104,106,108,109,107,102]

#①保序去重
c1_unique = list(dict.fromkeys(class1))
c2_unique = list(dict.fromkeys(class2))
print(f"①1班保序去重 {c1_unique}")
print(f"①2班保序去重 {c2_unique}")

s1 = set(class1)
s2 = set(class2)

#②同时选两门课（交集）
both = s1 & s2
print(f"②同时选两门课学生编号 {both}")

#③只选其中一门（对称差）
only_one = s1 ^ s2
print(f"③只选一门课学生编号 {only_one}")

#④选1班，没有选2班
only_c1 = s1 - s2
print(f"④选1班但不选2班 {only_c1}")

#⑤交集转为元组
t_both = tuple(both)
print(f"⑤交集转为元组 {t_both}")
print("解释：集合元素可哈希，转元组后元组全部元素可哈希，元组整体可存入集合。")

#拓展：嵌套列表去重 nest = [[1,2],[3,4],[1,2],[5,6]]
print("\n-----拓展嵌套列表去重-----")
nest = [[1,2],[3,4],[1,2],[5,6]]
#内层list不可哈希，先转元组放入集合去重，再转回list
temp = {tuple(item) for item in nest}
nest_dedup = [list(x) for x in temp]
print(f"原始嵌套列表 {nest}")
print(f"嵌套去重结果 {nest_dedup}")
