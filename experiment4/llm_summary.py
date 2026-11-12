from openai import OpenAI

def generate_doc_review(top50_words, text_snippet, api_key, base_url="https://api.deepseek.com"):
    """
    生成文档智能审查摘要
    :param top50_words: top50词频列表
    :param text_snippet: 文档文本片段
    :param api_key: deepseek的api-key
    :param base_url: deepseek接口地址
    :return:大模型返回审查报告
    """
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    prompt = f"""
你是本地文档智能审查助手。
【文档高频Top50词汇】：{top50_words}
【文档文本片段】：{text_snippet[:1200]}

任务：
1. 概括这批文档的核心主题；
2. 给出简短文档审查意见；
3. 输出结构化摘要。
输出简洁，适合实验报告。
"""

    resp = client.chat.completions.create(
        model="deepseek-flash",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    result = resp.choices[0].message.content

    # 保存审查报告
    with open("llm_review_report.txt","w",encoding="utf-8") as f:
        f.write(result)
    print("\n====DeepSeek大模型生成文档审查报告已保存 llm_review_report.txt ====")
    print(result)
    return result

if __name__ == "__main__":
    # 测试示例
    test_top50 = [("人工智能", 8), ("大模型",5)]
    test_text = "人工智能与大模型技术发展，实现本地文档智能审查"
    # 把你的key填进去
    #generate_doc_review(test_top50, test_text, api_key="?????")
