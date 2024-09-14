import feedparser
import ssl
import certifi
import urllib.request
import yaml
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz

def get_feed(feed_url, retrieve_by, date=None, max_count=None):
    # Create an SSL context using certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    try:
        # Use urllib to open the URL with the SSL context
        with urllib.request.urlopen(feed_url, context=ssl_context) as response:
            data = response.read()

        # Parse the downloaded feed data
        feed = feedparser.parse(data)

        # Print feed details
        if 'title' in feed.feed:
            print(f"Feed Title: {feed.feed.title}")
        if 'link' in feed.feed:
            print(f"Feed Link: {feed.feed.link}")
        if 'description' in feed.feed:
            print(f"Feed Description: {feed.feed.description}")
        print()

        # Initialize a counter for the number of entries processed
        entry_count = 0

        # Loop through feed entries (articles/items)
        for entry in feed.entries:
            # Debugging information
            print(f"Raw Published Date: {entry.published}")

            # Parse the published date from RFC 822 format
            entry_date_tuple = parsedate_tz(entry.published)
            if entry_date_tuple:
                # Convert to datetime and then to date
                entry_date = datetime.fromtimestamp(mktime_tz(entry_date_tuple)).date()
                print(f"Parsed Entry Date: {entry_date}")

                # Check if we are retrieving by date
                if retrieve_by == 'date' and date:
                    # Ensure the date variable is also a date object
                    if isinstance(date, datetime.date):
                        # Only process entries newer than the specified date
                        if entry_date < date:
                            print(f"Skipping entry with date: {entry_date} (older than {date})")
                            continue
                    else:
                        print(f"Date comparison issue: date variable is not of type datetime.date")

            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Published: {entry.published}")
            print(f"Summary: {entry.summary}")
            print("-" * 40)

            entry_count += 1

            # Exit after processing the specified number of entries (max_count)
            if retrieve_by == 'count' and entry_count >= max_count:
                print(f"Reached {max_count} entries. Exiting...")
                break

    except Exception as e:
        print(f"Failed to fetch the feed. Error: {e}")

# Other functions (read_config, read_feed_urls, process_feeds) remain the same


def read_config(file_path):
    # Load the configuration from the YAML file
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    # Get the values from the YAML file
    retrieve_by = config.get('retrieve_by', 'count')
    date_str = config.get('date', None)
    count = config.get('count', None)

    # Initialize date variable
    date = None

    # If the 'retrieve_by' is date and date_str is provided, parse the date
    if retrieve_by == 'date' and isinstance(date_str, str):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print(f"Date format error: {date_str}. Expected format is YYYY-MM-DD.")
    elif retrieve_by == 'count' and count is not None:
        try:
            count = int(count)
        except ValueError:
            print(f"Count value error: {count}. It should be an integer.")

    return retrieve_by, date, count


def read_feed_urls(file_path):
    # Open and read the file containing feed URLs (name, URL per line)
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # Return URLs, extracting the part after the comma and stripping extra whitespace
    return [line.split(',', 1)[1].strip() for line in urls if ',' in line]

def process_feeds(config_file, urls_file):
    # Read configuration and feed URLs
    retrieve_by, date, count = read_config(config_file)
    urls = read_feed_urls(urls_file)

    # Loop through each URL
    for url in urls:
        print(f"Fetching feed from: {url}")
        # Call the get_feed function with the correct parameters
        get_feed(url, retrieve_by, date=date, max_count=count if retrieve_by == 'count' else None)
        print("=" * 40)  # Separator between different feeds

if __name__ == "__main__":
    # Specify the paths to your configuration and feed URLs files
    config_file = 'config.yaml'
    urls_file = 'feed_urls.txt'
    process_feeds(config_file, urls_file)
