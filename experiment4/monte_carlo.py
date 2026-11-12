import random

def monte_carlo_keyword_simulation(word_list, target_keyword, sample_times=10000):
    """
    蒙特卡洛模拟：估算目标关键词在词库中出现概率
    :param word_list: 全部分词列表
    :param target_keyword: 要查询的关键词（自己输入）
    :param sample_times: 采样次数
    :return: 估算概率
    """
    if not word_list:
        print("词列表为空，无法模拟！")
        return 0

    hit = 0
    for _ in range(sample_times):
        pick = random.choice(word_list)
        if pick == target_keyword:
            hit += 1
    prob = hit / sample_times
    print(f"\n【蒙特卡洛模拟】关键词：{target_keyword}")
    print(f"采样次数：{sample_times}，估算出现概率：{prob:.4f}")
    return prob


if __name__ == "__main__":
    # 单独运行这个文件时，手动输入关键词测试
    words_test = ["人工智能", "大模型", "文档", "Agent", "监控"]
    kw = input("请输入要查询的关键词：")
    monte_carlo_keyword_simulation(words_test, kw, sample_times=10000)
