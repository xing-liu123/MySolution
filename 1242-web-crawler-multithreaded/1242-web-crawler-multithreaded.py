# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from collections import deque
import threading

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Extract hostname from startUrl
        hostname = urlparse(startUrl).netloc
        
        # Use Set with thread lock to store visited URLs
        visited = set()
        lock = threading.Lock()
        
        def get_hostname(url):
            return urlparse(url).netloc
        
        def is_same_hostname(url):
            return get_hostname(url) == hostname
        
        def crawl_url(url):
            # Get all URLs from current page
            urls = htmlParser.getUrls(url)
            
            # Filter URLs and add to result
            next_urls = []
            for next_url in urls:
                if is_same_hostname(next_url):
                    # Thread-safe way to check and add to visited
                    with lock:
                        if next_url not in visited:
                            visited.add(next_url)
                            next_urls.append(next_url)
            
            return next_urls
        
        # Start with the initial URL
        with lock:
            visited.add(startUrl)
        
        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=16) as executor:
            # Start with initial URL
            task_queue = deque([startUrl])
            
            # Process URLs until no more left
            while task_queue:
                # Get next batch of URLs to process
                current_batch = []
                while task_queue and len(current_batch) < 16:
                    current_batch.append(task_queue.popleft())
                
                if not current_batch:
                    break
                    
                # Submit all URLs in batch to thread pool
                future_to_url = {
                    executor.submit(crawl_url, url): url 
                    for url in current_batch
                }
                
                # Process completed tasks and add new URLs to queue
                for future in as_completed(future_to_url):
                    next_urls = future.result()
                    task_queue.extend(next_urls)
        
        return list(visited)
        