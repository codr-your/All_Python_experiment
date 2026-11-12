import matplotlib
matplotlib.use('Agg')

import os
import jieba
import csv
from collections import Counter
from wordcloud import WordCloud
# ==========【新增导入，先注释，不启用】==========
#from monte_carlo import monte_carlo_keyword_simulation
#from llm_summary import generate_doc_review


def analyze_documents(folder_path, font_path, stopwords_file=None, user_dict=None):
    # 加载自定义专业词典
    if user_dict and os.path.exists(user_dict):
        jieba.load_userdict(user_dict)

    # 加载停用词
    stopwords = set()
    if stopwords_file and os.path.exists(stopwords_file):
        with open(stopwords_file, 'r', encoding='utf-8') as f:
            stopwords = set([line.strip() for line in f])
    else:
        # 内置默认停用词
        stopwords = {"的", "了", "和", "在", "是", "我", "你", "他", "我们", "他们",
                     "为", "以", "等", "并", "对", "与", "这", "那", "也", "就"}

    all_words = []

    # 批量遍历读取docs文件夹下txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    all_text += text + "\n"
                # jieba精确模式分词
                words = jieba.lcut(text)
                # 过滤单字符、过滤停用词
                filtered_words = [w for w in words if len(w) > 1 and w not in stopwords]
                all_words.extend(filtered_words)
                print(f"成功处理文件: {filename}")
            except Exception as e:
                print(f"处理文件{filename} 时发生错误: {e}")

    # 判断是否提取到有效词汇
    if not all_words:
        print("⚠️未提取到有效词汇，请检查docs路径、文档内容或者文档编码(必须UTF‑8)。")
        return

    # 统计词频，取Top50高频词
    word_counts = Counter(all_words)
    top_50_words = word_counts.most_common(50)
    print("\n======== Top50高频词 ========")
    for word, cnt in top_50_words:
        print(f"{word} : {cnt}")

    # 导出CSV汇总报告
    with open("word_freq_report.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["词语", "词频"])
        writer.writerows(top_50_words)
    print("\n词频报告已保存：word_freq_report.csv")


    # ======================
    # 【进阶功能区：全部注释，拿到API KEY再解开】
    # ======================
    # # 1. 蒙特卡洛模拟，手动输入关键词版本
    target_kw = input("请输入蒙特卡洛要查询的关键词：")
    monte_carlo_keyword_simulation(all_words, target_kw, sample_times=10000)

    # # 2. DeepSeek 大模型摘要
    #api_key = "我的apikey"
    #generate_doc_review(top_50_words, all_text, api_key=api_key)
    # ======================


    # 生成词云对象
    wc = WordCloud(
        font_path=font_path,
        width=1000,
        height=800,
        background_color='white',
        max_words=50,
        collocations=False
    )
    try:
        wc.generate_from_frequencies(dict(top_50_words))
        output_png = "document_wordcloud.png"
        wc.to_file(output_png)
        print(f"\n词云图片已保存：{output_png}")
    except Exception as e:
        print(f"\n❌词云生成失败：{e}")


if __name__ == "__main__":
    analyze_documents(
        folder_path="./docs",
        font_path=r"./simhei.ttf",
        stopwords_file="./stopwords.txt",
        user_dict="./user_dict.txt"
    )
