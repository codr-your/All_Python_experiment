import requests
from bs4 import BeautifulSoup

import pandas as pd
url = "http://read.nlc.cn/yuewen/index"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
html = resp.text
soup = BeautifulSoup(html, "html.parser")

# 1. 找到放所有图书的ul
book_ul = soup.find("ul", class_="WLWX2023_home_list")
# 2. 在ul里面找到全部li（每一本书）
all_book = book_ul.find_all("li")

data = []
for box in all_book:
    a_tag = box.find("a", class_="book")
    if a_tag:
        href = a_tag["href"]
        book_link = "https://www.nlc.cn/web/index.shtml" + href  # 换成你的网站域名
    else:
        book_link = ""

    book_name = ""
    category = ""
    author = ""
    desc = ""

    right = box.find("span", class_="right")
    if right:
        # 书名：tt
        tt_tag = right.find("span", class_="tt")
        book_name = tt_tag.get_text(strip=True) if tt_tag else ""

        # txt1 里面：分类lab + 作者
        txt1_tag = right.find("span", class_="txt1")
        if txt1_tag:
            lab_tag = txt1_tag.find("i", class_="lab")
            category = lab_tag.get_text(strip=True) if lab_tag else ""
            # 取txt1全部文字，去掉分类文字，剩下作者
            txt1_all = txt1_tag.get_text(strip=True)
            author = txt1_all.replace(category, "").strip(' "') # 去掉引号和空格

        # 简介：txt2
        txt2_tag = right.find("span", class_="txt2")
        desc = txt2_tag.get_text(strip=True) if txt2_tag else ""

    data.append({
        "书名": book_name,
        "分类": category,
        "作者": author,
        "简介": desc,
        "详情链接": book_link
    })


df = pd.DataFrame(data)
df.to_csv("book.csv", index=False, encoding="utf-8-sig")
print("保存完成 book.csv")
