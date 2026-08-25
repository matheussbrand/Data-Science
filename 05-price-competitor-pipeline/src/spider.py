import scrapy

class ProductSpider(scrapy.Spider):
    name="products"
    start_urls=["https://example.com/products"]

    def parse(self,response):
        for item in response.css(".product"):
            yield {
                "sku": item.css("::attr(data-sku)").get(),
                "name": item.css(".name::text").get(),
                "price": item.css(".price::text").get(),
            }
