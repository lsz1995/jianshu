from scrapy import Spider,Request
from jianshu.items import JianshuItem
from lxml import etree
import re


class JianshuSpider(Spider):
    name = 'jianshu'
    init_following_url = 'https://www.jianshu.com/users/2399ca214fbd/following'

    def start_requests(self):
        yield Request(url=self.init_following_url,callback=self.parse_following)
    def parse_following(self,response):
        '''
        提取用户数据
        提取用户关注者页码
        '''

        selector = etree.HTML(response.text)
         # 下面是解析用户信息，用户信息全部在第一页进行解析
        item = JianshuItem()#初始化
        id = selector.xpath('//div[@class="title"]/a/@href')[0]
        item['id'] = item['id'] = re.search('/u/(.*)', id).group(1)
        item['name'] = selector.xpath('//div[@class="title"]/a/text()')
        item['followings'] =selector.xpath('//div[@class="meta-block"]/a/p/text()')[0]
        item['followers'] =selector.xpath('//div[@class="meta-block"]/a/p/text()')[1]
        item['words'] =selector.xpath('//div[@class="meta-block"]/p/text()')[0]
        item['likes'] =selector.xpath('//div[@class="meta-block"]/p/text()')[1]
        item['articles'] =selector.xpath('//div[@class="meta-block"]/a/p/text()')[2]
        yield item

        page_all = page_all = selector.xpath('//div[@class="main-top"]/div[@class="info"]/ul/li[1]//p/text()')[0]
        page_all = int(page_all)
        if page_all% 9 ==0:
            page_num = int(page_all / 9)
        else:
            page_num = int(page_all / 9)+1

        for i in  range(page_num):
            url = response.url + '?page={}'.format(str(i+1))

            yield Request(url=url,callback=self.parse_info)


    def parse_info(self, response):
        selector = etree.HTML(response.text)
        id_list = selector.xpath('//div[@class="info"]/a/@href')
        for id in id_list:
            id = re.search('/u/(.*)', id).group(1)
            url = 'http://www.jianshu.com/users/{}/following'.format(id)
            yield Request(url=url, callback=self.parse_following)



