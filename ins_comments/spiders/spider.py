from scrapy import Request,Spider
from ..items import InsCommentsItem
from json import loads,dumps
from urllib import parse
import logging
import re


class InsSpider(Spider):
      name = 'ins_comments'
      logger = logging.getLogger(__name__)
      h_s = '<script type="text/javascript">window.__initialDataLoaded(window._sharedData)'
      base_url = "https://www.instagram.com/graphql/query/"
      variables = '{"shortcode":"%s","first":12,"after":"{\"cached_comments_cursor\":+\"%s\",+\"bifilter_token\":+\"%s\"}"}'
      querystring = {
                     "query_hash": "97b41c52301f77ce508f55e66d17620e",
                     "variables": '{variables}'
                    }
      
      def __init__(self,post_url):
          if not post_url:
              return
          self.start_urls = ['{}'.format(post_url)]
     
          
      def parse(self, response):
          post_id = response.url.split('/')[-2]
          result = re.search(r'<script type="text/javascript">window._sharedData = (.*);</script>', response.text, re.S)
          if result:
              result = result.group(1).strip(self.h_s).replace(';</script>', '')
          result = loads(result)
          # yield from self.parse_data(result)
          yield from self.fetch_next(result,post_id)
          
          
          
      def parse_comments(self, response):
          post_id = response.meta['post_id']
          result = loads(response.text)
          # yield from self.parse_data(result)
          yield from self.fetch_next(result,post_id)
      
      
      
      def fetch_next(self, result, post_id):
          print(result)
          cached_comments_cursor = re.search(r'"cached_comments_cursor": "(\d+)"', str(result),re.S)
          bifilter_token = re.search(r'"bifilter_token": "([\d\w\-\_\=]*)"', str(result),re.S)
          if cached_comments_cursor:
              cached_comments_cursor = cached_comments_cursor.group(1)
          if bifilter_token:
              bifilter_token = bifilter_token.group(1)
          # v = self.variables % (post_id, cached_comments_cursor, bifilter_token)
          self.querystring['variables'] = self.variables % (post_id, cached_comments_cursor, bifilter_token)
          print(self.querystring)
          # url = self.url.format(parse.urlencode(self.querystring))
          self.logger.info('<====== fetch next page {} ======>'.format(self.querystring))
          yield Request(url=self.base_url, method='GET',body=dumps(self.querystring),callback=self.parse_comments,meta={'post_id':post_id})
          
      
          
      def parse_data(self, result):
          print(result.keys())
