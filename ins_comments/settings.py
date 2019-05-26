# -*- coding: utf-8 -*-

# Scrapy settings for ins_comments project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ins_comments'

SPIDER_MODULES = ['ins_comments.spiders']
NEWSPIDER_MODULE = 'ins_comments.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ins_comments (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
          'cookie': 'mid=XNJdwgAEAAFQhOz5naU7BAY8aA6H; shbid=5093; shbts=1558601300.0202212; rur=FRC; csrftoken=hsQJlkGRAAk6kavxWBCLoaNxm7N1D5GZ; ds_user_id=7965489049; sessionid=7965489049%3AfSfHOXLdld3N7N%3A19; urlgen="{\"118.163.206.2\": 3462}:1hU7LW:bWXRXyg_Q04Q1W0hWztMVmojcQg", mid=XNJdwgAEAAFQhOz5naU7BAY8aA6H; shbid=5093; shbts=1558601300.0202212; rur=FRC; csrftoken=hsQJlkGRAAk6kavxWBCLoaNxm7N1D5GZ; ds_user_id=7965489049; sessionid=7965489049%3AfSfHOXLdld3N7N%3A19; urlgen="{\"118.163.206.2\": 3462}:1hU7LW:bWXRXyg_Q04Q1W0hWztMVmojcQg"; rur=FRC; mid=WyJBLAAEAAGwzHili1LhECwShi6S; mcd=3; csrftoken=XWsn427D8nBvKMTOwgooEn63ccZz5em3; urlgen="{\"118.163.206.2\": 3462}:1hU7Om:EyKO-_AZsDtlRHOrpUtkjiMTM7A"; ds_user_id=7965489049; csrftoken=XWsn427D8nBvKMTOwgooEn63ccZz5em3',
          'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
          'Accept': "*/*",
          'Cache-Control': "no-cache",
          'Postman-Token': "ce2ba0a4-5ecb-4a7e-bf74-7c4f9cfdebff,8b949fa8-5c55-4d6e-98ff-c37a0c17265e",
          'Host': "www.instagram.com",
          'accept-encoding': "gzip, deflate",
          'Connection': "keep-alive",
          'cache-control': "no-cache"
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ins_comments.middlewares.InsCommentsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ins_comments.middlewares.InsCommentsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ins_comments.pipelines.InsCommentsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
