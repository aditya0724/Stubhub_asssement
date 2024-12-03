import requests
import json
import time
import fake_useragent


ua = fake_useragent.UserAgent()


url_template = 'https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&page={page}&tlcId=2'

# Function to scrape events data
def scrape_events():
    all_events = []
    page = 0

    while True:
        url = url_template.format(page=page)

        # Set up a fake user-agent header
        headers = {
            'User-Agent': ua.random 
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            break

        data = response.json()

        if not data.get('events'):
            print(f"No more events found on page {page}. Stopping.")
            break

        for event in data['events']:
            event_data = {
                'event_id': event.get('eventId'),
                'name': event.get('name'),
                'url': event.get('url'),
                'date': event.get('formattedDateWithoutYear'),
                'time': event.get('formattedTime'),
                'venue': event.get('venueName'),
                'venue_location': event.get('formattedVenueLocation'),
                'image_url': event.get('imageUrl'),
                'category_id': event.get('categoryId'),
                'day_of_week': event.get('dayOfWeek')
            }
            all_events.append(event_data)

        # Print status
        print(f"Scraped {len(data['events'])} events from page {page}")

        time.sleep(2)

        page += 1

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(all_events, f, indent=4)

    print(f"Scraping completed. Total events scraped: {len(all_events)}")

if __name__ == '__main__':
    scrape_events()
