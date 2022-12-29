# Scrapy settings for scrapy_test2_car project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_test2_car'

SPIDER_MODULES = ['scrapy_test2_car.spiders']
NEWSPIDER_MODULE = 'scrapy_test2_car.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_test2_car (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Cookie ASP.NET_SessionId=5x0yetaczdrkz0nmhyz1bbak; ahpvno=9; fvlid=1672054893618zqVwVY7i1w; __ah_uuid_ng=c_401E76FD-BE75-4A1B-B146-6CFA7371D4BA; sessionip=39.171.214.42; sessionid=401E76FD-BE75-4A1B-B146-6CFA7371D4BA%7C%7C2022-12-26+19%3A41%3A35.071%7C%7Cwww.baidu.com; autoid=9cf0b0186215f3de73fcef9731ceb782; v_no=9; visit_info_ad=401E76FD-BE75-4A1B-B146-6CFA7371D4BA||4E95B824-005B-4888-AA79-BF46DC92F50E||-1||-1||9; ref=www.baidu.com%7C0%7C0%7C0%7C2022-12-26+19%3A44%3A17.254%7C2022-12-26+19%3A41%3A35.071; sessionvid=4E95B824-005B-4888-AA79-BF46DC92F50E; area=330681; sessionuid=401E76FD-BE75-4A1B-B146-6CFA7371D4BA%7C%7C2022-12-26+19%3A41%3A35.071%7C%7Cwww.baidu.com; pvidchain=3311667,3311273,3311667,3311667,104399,8,104399,3311224; ahsids=66; tm_lastshows6685=1;': 'pvidlist=76868cdb-9b29-424f-8dc9-b464bfd2ac0b4:529863:833081:121159200:4:4302482',
    'Host': 'www.autohome.com.cn',
    'Referer': 'https://www.baidu.com/link?url=eLK8NsXm2lCZ1xnodnP7mh2AptWfE-XhoRWilSQDQNFyuDHmQWQ2U4J4kpBb7jKe&wd=&eqid=ada0388d000c22430000000563a98869',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101': 'Firefox/104.0',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_test2_car.middlewares.ScrapyTest2CarSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_test2_car.middlewares.ScrapyTest2CarDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy_test2_car.pipelines.ScrapyTest2CarPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
