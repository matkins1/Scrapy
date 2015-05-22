import scrapy

from realtor.items import RealtorItem

class RealtorSpider(scrapy.Spider):
    name = "realtor"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.realtor.com/realestateandhomes-search/Austin_TX/type-single-family-home,condo-townhome-row-home-co-op/price-200000-550000",
        "http://www.realtor.com/realestateandhomes-search/Austin_TX/type-single-family-home,condo-townhome-row-home-co-op/price-200000-550000/pg-2"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
	for sel in response.xpath('/html/body/div[5]/div[7]/div[2]/div[1]/div[4]/div'):
			item = RealtorItem()
			item['address'] = sel.xpath('/html/body/div[5]/div[7]/div[2]/div[1]/div[4]/div/div[1]/div/div/ul/li[1]/a/span[1]').extract()								  					
			item['city'] = sel.xpath('/html/body/div[5]/div[7]/div[2]/div[1]/div[4]/div/div[1]/div/div/ul/li[1]/a/span[2]').extract()
			item['price'] = sel.xpath('/html/body/div[5]/div[7]/div[2]/div[1]/div[4]/div/div[1]/div/div/ul/li[2]/span[1]').extract()
			yield item
