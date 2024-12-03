import scrapy
import json
import re
from stubhub_spider.items import StubhubScraperItem


class StubHubEventSpider(scrapy.Spider):
    name = 'stubhub_events'


    start_urls = [
        'https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&page=0&tlcId=2'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 2  # This sets the delay between requests to 2 seconds
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for event in data['events']:
            item = StubhubScraperItem()
            item['event_id'] = event['eventId']
            item['name'] = event['name']
            item['url'] = event['url']
            item['date'] = event['formattedDateWithoutYear']
            item['time'] = event['formattedTime']
            item['venue'] = event['venueName']
            item['venue_location'] = event['formattedVenueLocation']
            item['image_url'] = event['imageUrl']
            item['category_id'] = event['categoryId']
            item['day_of_week'] = event['dayOfWeek']
            yield item


        current_page_match = re.search(r'page=(\d+)', response.url)

        if current_page_match:
            current_page = int(current_page_match.group(1))
        else:
            current_page = 0

        next_page = current_page + 1

        # Generate the URL for the next page using regex to modify the 'page' parameter
        next_page_url = re.sub(r'page=\d+', f'page={next_page}', response.url)

        # If the next page exists and has events, make a request for the next page
        if len(data['events']) > 0:  # Check if there are events in the current page
            yield scrapy.Request(next_page_url, callback=self.parse)
