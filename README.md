Process of Scraping:
(Scrapy)
Step 1:
To begin, I identified the API endpoint that provides the required data. I ensured that the data returned by the API matches what is displayed on the UI, confirming the API’s relevance and accuracy for the task.

Step 2:
I used Scrapy to send requests to the identified API and retrieve the data. To mitigate the risk of being blocked or rate-limited, I implemented a fake User-Agent in the middleware. This helps mask the requests and simulate legitimate browser traffic.

Step 3:
To prevent overwhelming the server, I incorporated a 2-second delay between each request using Scrapy's DOWNLOAD_DELAY setting. This ensures that the scraping process remains respectful of the server's resources.

Step 4:
Since the data is spread across multiple pages, I also implemented pagination in the spider. This logic extracts the current page number from the API response, increments it, and continues to scrape additional pages until all relevant data has been retrieved.

Step 5:
To save the scraped data, I configured Scrapy's output settings by specifying the following:

FEED_FORMAT = 'json': This setting ensures that the output is saved in JSON format, making it easy to store and process the data.
FEED_URI = 'events.json': The data is saved to a file named events.json on the local system. You can also use other formats like CSV or XML if needed by adjusting the FEED_FORMAT.
____________________________________________________________________________________________________________________________________________________________________________
Note - Using Requests library I have also uploaded a .py file
