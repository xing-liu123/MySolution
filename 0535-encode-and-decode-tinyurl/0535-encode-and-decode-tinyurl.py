class Codec:
    def __init__(self):
        self.url_map = {}
        self.characters = string.ascii_letters + string.digits
        self.base = "http://xingliu.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            short_url = ''.join(random.choice(self.characters) for _ in range(6))

            if not short_url in self.url_map:
                self.url_map[short_url] = longUrl
                break
        
        return self.base + short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.replace(self.base, "")

        return self.url_map.get(shortUrl, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))