import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from main import analyze_documents

DOC_FOLDER = "./docs"

class DocFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # 文件发生变化，排除文件夹本身
        if not event.is_directory and event.src_path.endswith(".txt"):
            print(f"\n检测到文档变更：{event.src_path}，自动启动文档分析……")
            try:
                analyze_documents(
                    folder_path="./docs",
                    font_path=r"./simhei.ttf",
                    stopwords_file="./stopwords.txt",
                    user_dict="./user_dict.txt"
                )
            except Exception as e:
                print(f"自动分析出错：{e}")

    def on_created(self, event):
        self.on_modified(event)


if __name__ == "__main__":
    event_handler = DocFileHandler()
    observer = Observer()
    observer.schedule(event_handler, DOC_FOLDER, recursive=False)
    observer.start()
    print(f"正在监控文件夹 {DOC_FOLDER}，放入/修改txt文档会自动分析，Ctrl+C退出")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
