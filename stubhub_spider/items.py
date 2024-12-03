import scrapy


class StubhubScraperItem(scrapy.Item):
    # Define the fields for the event data you want to scrape
    event_id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    venue = scrapy.Field()
    venue_location = scrapy.Field()
    image_url = scrapy.Field()
    category_id = scrapy.Field()
    day_of_week = scrapy.Field()

