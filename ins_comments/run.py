from scrapy import cmdline
post_url = 'https://www.instagram.com/p/Bx8OM-lgcDj/'
c_l = 'scrapy crawl ins_comments -a post_url={}'.format(post_url)
cmdline.execute(c_l.split())