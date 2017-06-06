    # coding=    UTF-8 #
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from ustc.items import UstcItem
import json

class UstcSpider(BaseSpider):
    name="ustc"
    allowed_domains=["https://www.icourse.club/course/"]
    start_urls=[]

    def start_requests(self):
            url_head="https://www.icourse.club/course/"
            for digit in range(10000,11000):
                digit_str='%d'%digit
                self.start_urls.append(url_head+digit_str)

            for url in self.start_urls:
                yield self.make_requests_from_url(url)

    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        class_name = hxs.xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/span[1]/text()').extract()[0].encode('utf-8')
        class_teacher=hxs.xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/span[2]/text()').extract()[0].encode('utf-8')
        class_time=hxs.xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/span[3]/text()').extract()[0].encode('utf-8')
        #class_college=hxs.xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]').extract()[0].encode('utf-8')
        class_score=hxs.xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/div[1]/span[6]/text()').extract()[0].encode('utf-8')
        #class_score_num=hxs.xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/div[1]/span[7]/text()').extract()[0].encode('utf-8')
        #class_name=class_name.decode('utf8')

        #print class_name,class_time

        item=UstcItem()
        if class_name: item['class_name']=class_name
        if class_teacher: item['class_teacher']=class_teacher
        if class_time: item['class_time']=class_time
        #if class_college: item['class_college']=class_college
        if class_score: item['class_score']=class_score
        #item['class_score_num']=class_score_num
        #items.append(item)

        yield item
        #yield item




