BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ROBOTSTXT_OBEY = True
LOG_FILE = "spider.log"

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 0