class Codec:
    def __init__(self):
        self.d = {}
        self.r = {}

    def encode(self, longUrl):
        self.d[longUrl] = longUrl.__hash__()
        self.r[longUrl.__hash__()] = longUrl
        return longUrl.__hash__()

    def decode(self, shortUrl):
        return self.r[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
