import url_manager_spider, html_downloader_spider
import html_parser_spider, html_outputer_spider

class SpiderMain():
    def __init__(self):
        self.urls = url_manager_spider.UrlManager()
        self.downloader = html_downloader_spider.HtmlDownloader()
        self.parser = html_parser_spider.HtmlPaser()
        self.outputer = html_outputer_spider.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s'%(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                # 可修改爬取次数
                if count == 1000:
                    break
                count = count + 1
            except:
                print('craw failed')
        
        print('craw finished')
        self.outputer.output_html()
        
    

if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
