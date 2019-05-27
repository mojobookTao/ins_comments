from scrapy import Request,Spider
from json import loads
import logging
import re
import traceback


class InsSpider(Spider):
      name = 'ins_comments'
      logger = logging.getLogger(__name__)
      h_s = '<script type="text/javascript">window.__initialDataLoaded(window._sharedData)'
      api = 'https://www.instagram.com/graphql/query/?query_hash=97b41c52301f77ce508f55e66d17620e&variables=%7B%22shortcode%22%3A%22{0}%22%2C%22first%22%3A12%2C%22after%22%3A%22%7B%5C%22cached_comments_cursor%5C%22%3A+%5C%22{1}%5C%22%2C+%5C%22bifilter_token%5C%22%3A+%5C%22{2}%5C%22%7D%22%7D'
      base_url = "https://www.instagram.com/graphql/query/?%s"
      file_path = './ins_comments.txt'
      
      
      def __init__(self,post_url):
          if not post_url:
              return
          self.start_urls = ['{}'.format(post_url)]
     
          
      def parse(self, response):
          try:
              post_id = response.url.split('/')[-2]
              ret = re.search(r'<script type="text/javascript">window._sharedData = (.*);</script>', response.text, re.S)
              if ret:
                  ret = ret.group(1).strip(self.h_s).replace(';</script>', '')
              ret = loads(ret)
              self.parse_data(ret)
              cached_comments_cursor = re.search(r'"cached_comments_cursor": "(\d+)"', str(ret), re.S)
              bifilter_token = re.search(r'"bifilter_token": "([\d\w\-\_\=]*)"', str(ret), re.S)
              if not cached_comments_cursor or not bifilter_token:
                  self.logger.info('<==== fail {}'.format(ret))
                  return
              cached_comments_cursor = cached_comments_cursor.group(1)
              bifilter_token = bifilter_token.group(1)
              url = self.api.format(post_id, cached_comments_cursor, bifilter_token)
              self.logger.info('<====== parse comments ======>')
              yield Request(url=url, callback=self.parse_comments, meta={'post_id': post_id})
          except Exception as e:
              self.logger.error('%s %s' % (e,traceback.print_exc()))
          
          
          
      def parse_comments(self, response):
          try:
              if 'fail' in response.text:
                  self.logger.info('<==== fail {}'.format(response.text))
                  return
              post_id = response.meta['post_id']
              ret = loads(response.text)
              self.parse_data(ret)
              has_next_page = ret['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']
              if not has_next_page == True:
                  self.logger.info('<==== has_next_page {}'.format(has_next_page))
                  return
              end_cursor = loads(ret['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor'])
              cached_comments_cursor = end_cursor.get('cached_comments_cursor')
              bifilter_token = end_cursor.get('bifilter_token')
              if not cached_comments_cursor:
                  self.logger.info('<==== no more comment ====>')
                  return
              url = self.api.format(post_id, cached_comments_cursor, bifilter_token)
              self.logger.info('<====== fetch next {} ======>'.format(url))
              yield Request(url=url, callback=self.parse_comments, meta={'post_id': post_id})
          except Exception as e:
              self.logger.error('%s %s' % (e,traceback.print_exc()))
             
    
      
      def parse_data(self, ret):
          l = []
          if 'entry_data' in ret.keys():
             for data in ret['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']:
                 l.append(data['node'])
          elif 'data' in ret.keys():
              for data in ret['data']['shortcode_media']['edge_media_to_parent_comment']['edges']:
                  l.append(data['node'])
          else:
              print(ret)
          print(len(l))
          with open(self.file_path,'a') as f:
              f.write('\n {} \n'.format(l))
      
          
      def parse_reply_from_comment(self, comment_id):
          return
      
if __name__ == '__main__':
    from scrapy import cmdline
    post_url = 'https://www.instagram.com/p/Bx0OSIVnqMS/'
    c_l = 'scrapy crawl ins_comments -a post_url={}'.format(post_url)
    cmdline.execute(c_l.split())