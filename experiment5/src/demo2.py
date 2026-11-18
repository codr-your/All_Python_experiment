import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

class NewsCrawler:
    def __init__(self, target_url, retries=3, sleep_sec=2, timeout=12):
        self.target_url = target_url
        self.retries = retries
        self.sleep_sec = sleep_sec
        self.timeout = timeout
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.result_list = []

    def fetch_html(self):
        """发送请求获取网页html，带重试"""
        for attempt in range(self.retries):
            try:
                resp = requests.get(
                    self.target_url,
                    headers=self.headers,
                    timeout=self.timeout
                )
                resp.raise_for_status()
                time.sleep(self.sleep_sec)
                return resp.text
            except Exception as err:
                print(f"请求失败 第{attempt+1}/{self.retries}次：{err}")
                time.sleep(self.sleep_sec)
        return None

    def parse(self, html_text):
        """修复ssr4.scrape.center的标签选择器"""
        soup = BeautifulSoup(html_text, "html.parser")
        # 正确：卡片class是 item
        items = soup.find_all("div", class_="item")
        for item in items:
            # 标题
            title_tag = item.find("h2")
            title = title_tag.get_text(strip=True) if title_tag else ""
            # 链接
            a_tag = item.find("a")
            link = "https://ssr4.scrape.center" + a_tag["href"] if a_tag else ""
            # 导演（作者）
            author = ""
            info_tags = item.find_all("div", class_="info")
            if info_tags:
                author = info_tags[0].get_text(strip=True)
            # 上映时间（发布时间）
            pub_time = ""
            if len(info_tags)>=2:
                pub_time = info_tags[1].get_text(strip=True)

            self.result_list.append({
                "title": title,
                "publish_time": pub_time,
                "author": author,
                "link": link
            })
        print("解析得到前3条数据样例：")
        for row in self.result_list[:3]:
            print(row)

    def save_csv(self, filename="result.csv"):
        df = pd.DataFrame(self.result_list)
        df.to_csv(filename, index=False, encoding="utf-8-sig")

    def run(self):
        """爬虫总执行入口"""
        html = self.fetch_html()
        if not html:
            print("网页获取失败，爬虫终止")
            return
        self.parse(html)
        self.save_csv()
        print(f"抓取完成，共获取 {len(self.result_list)} 条数据，已保存至result.csv")

if __name__ == "__main__":
    crawler = NewsCrawler(target_url="https://ssr4.scrape.center/page/2")
    crawler.run()
