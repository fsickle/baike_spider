import urllib.request

class HtmlDownloader():
    
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        
        
        if response.getcode() != 200:
            print('download failed')
            return None
        
        return response.read()
