# -*- coding: gb2312 -*-

'''
Created on 2016-12-15

@author: Sawatari
'''

import string
import sys
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector
from FindGoods.items import FindgoodsItem

class FindGoods(Spider):
    name = "FindGoods"
    download_delay = 4
    allowed_domains = ["tmall.com"]
    start_urls = [
        "https://www.tmall.com/"
    ]

    def parse(self, response):
        # ����ȷ���Ƿ������ɹ�
        if response.url == "https://www.tmall.com/":
            # ��ȡ��ʱ�ļ�
            temp = open('tempgoods.temp', 'r')
            good = temp.read()
            temp.close()
            # ��è��������Ʒ��һҳ
            url = "https://list.tmall.com/search_product.htm?q=" + good + "&type=p&vmarket=&spm=875.7931836%2FA.a2227oh.d100&from=mallfp..pc_1_searchbutton"
            # �ݹ�
            yield Request(url, callback=self.parse)

        else:
            # �����ɹ�
            item = FindgoodsItem()
            sel = Selector(response)
            gifts = sel.xpath('//*[@id="J_ItemList"]/div[@class="product  "]')
            for gift in gifts:
                name = gift.xpath('div/p[@class="productTitle"]/a/@title').extract()
                # ��è������HTML�ṹ��ͬ
                if not name:
                    name = gift.xpath('div/div[@class="productTitle productTitle-spu"]/a[1]/text()').extract()

                shop = gift.xpath('div/div[@class="productShop"]/a[@class="productShop-name"]/text()').extract()
                price = gift.xpath('div/p[@class="productPrice"]/em/@title').extract()
                trading = gift.xpath('div/p[@class="productStatus"]/span[1]/em/text()').extract()
                review = gift.xpath('div/p[@class="productStatus"]/span[2]/a/text()').extract()
                url = gift.xpath('div/p[@class="productTitle"]/a/@href').extract()
                if not url:
                    url = gift.xpath('div/div[@class="productTitle productTitle-spu"]/a[1]/@href').extract()

                # sys.getfilesystemencoding()��ñ��ر��루mbcs���룩
                item['name'] = [na.encode(sys.getfilesystemencoding()) for na in name]

                # ȥ���̵���ĩβ��\n���з���������\n��
                tempshop = str(shop[0].encode(sys.getfilesystemencoding()))
                item['shop'] = tempshop.strip('\n')

                item['price'] = price
                item['url'] = 'https:' + url[0]

                # ��è������������Ʒ�޽�������Ϣ
                tradnum = 0
                if trading:
                    # ������ҳ�޷���ȡ��������ϸ���֣���ת��
                    tradstr = str(trading[0].encode(sys.getfilesystemencoding()))
                    item['trading'] = tradstr
                    # ���ʡ������ַ����е��±�
                    biindex = tradstr.index('\xb1\xca')
                    # ��ȥ���ʡ�
                    tradstr = tradstr[:biindex]
                    # �ж��Ƿ��С�����
                    if '\xcd\xf2' in tradstr:
                        # ���������ַ����е��±�
                        wanindex = tradstr.index('\xcd\xf2')
                        # ��ȥ������
                        tradstr = tradstr[:wanindex]
                        tradnum = tradnum + string.atof(tradstr) * 10000
                    else:
                        # û�С�����
                        tradnum = tradnum + string.atof(tradstr)

                # ��è����������������Ϣ
                revinum = 0
                if review:
                    # ������ҳ�޷���ȡ��������ϸ���֣���ת��
                    revistr = str(review[0].encode(sys.getfilesystemencoding()))
                    item['review'] = revistr
                    # �ж��Ƿ��С�����
                    if '\xcd\xf2' in revistr:
                        # ���������ַ����е��±�
                        wanindex2 = revistr.index('\xcd\xf2')
                        # ��ȥ������
                        revistr = revistr[:wanindex2]
                        revinum = revinum + string.atof(revistr) * 10000
                    else:
                        # û�С�����
                        revinum = revinum + string.atof(revistr)

                # ��������
                score = revinum + (tradnum * 2)
                item['score'] = round(score)
                yield(item)
            # ��ȡ��Ʒ��
            good = response.url[(response.url.index("q=") + 2):response.url.index("&type=p&v")]
            next_page_urls = [
                "https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.0HVJLN&s=60&q=" + good + "&sort=s&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter",
                "https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.Zt2HlG&s=120&q=" + good + "&sort=s&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter"
            ]
            # �ݹ��ȡ����ҳ
            for next_page_url in next_page_urls:
                yield Request(next_page_url, callback=self.parse)