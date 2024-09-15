import feedparser
import ssl
import certifi
import urllib.request
import yaml
import csv
from datetime import datetime, timezone
from email.utils import parsedate_tz, mktime_tz
from pprint import pprint



def get_feed(feed_url, author, retrieve_by, date=None, max_count=None, csv_writer=None):
    # Create an SSL context using certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    try:
        # Use urllib to open the URL with the SSL context
        with urllib.request.urlopen(feed_url, context=ssl_context) as response:
            data = response.read()
            #print(data)
        
        #return

        # Parse the downloaded feed data
        feed = feedparser.parse(data)
    
        #print_metadata(feed)

        # Initialize a counter for the number of entries processed
        entry_count = 0

        # Loop through feed entries (articles/items)
        for entry in feed.entries:
            print(entry.author, entry.author_detail)
            print(entry.published, entry.title)
            """
            if entry.author == author :
                print("FOUND")
            else:
                #entry_count += 1
                #print(entry_count)
                continue
            """

            # Parse the published date from RFC 822 format
            entry_date_tuple = parsedate_tz(entry.published)
            if entry_date_tuple:
                # Convert to datetime and then to date
                entry_date = datetime.fromtimestamp(mktime_tz(entry_date_tuple)).date()
                #print(f"Parsed Entry Date: {entry_date}")

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

            # Write the entry to the CSV file
            csv_writer.writerow([author, entry.link, entry.title, entry.summary, entry.published])

            # Output the entry details to the console
            print(f"Author {entry.author}")
            print(f"Author detail: {entry.author_detail}")
            print(f"Authors: {entry.authors}")
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Published: {entry.published}")
            print(f"Published parsed: {entry.published_parsed}")
            print(f"Summary: {entry.summary}")
            print("-" * 40)

            entry_count += 1

            # Exit after processing the specified number of entries (max_count)
            if retrieve_by == 'count' and entry_count >= max_count:
                print(f"Reached {max_count} entries. Exiting...")
                break

        print("ENTRY_COUNT: ", entry_count)

    except Exception as e:
        print(f"Failed to fetch the feed. Error: {e}")


def read_config(file_path):
    # Load the configuration from the YAML file
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    # Get the values from the YAML file
    retrieve_by = config.get('retrieve_by', 'count')
    date_str = config.get('date', None)
    count = config.get('count', None)
    file_feeds = config.get('file_feeds', 'feed_urls.txt')
    file_output = config.get('file_output', 'feed_data.txt')
    file_output_delimiter = config.get('file_output_delimiter', ',')

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
            print("COUNT:", count)
        except ValueError:
            print(f"Count value error: {count}. It should be an integer.")

    return retrieve_by, date, count, file_feeds, file_output, file_output_delimiter


def read_feed_urls(file_path):
    # Open and read the file containing feed URLs (name, URL per line)
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # Return a list of tuples (author, url)
    return [(line.split(',', 1)[0].strip(), line.split(',', 1)[1].strip()) for line in urls if ',' in line]


def process_feeds(config_file):
    # Read configuration
    retrieve_by, date, count, urls_file, output_csv, delimiter = read_config(config_file)

    # Get the current UTC timestamp using timezone-aware datetime
    timestamp = datetime.now(timezone.utc).strftime('_%Y%m%d-%H%M%S')
    
    # Append the timestamp to the output file name
    output_csv_with_timestamp = f"{output_csv.rstrip('.txt')}{timestamp}.txt"

    # Open the output file for writing with the specified delimiter
    with open(output_csv_with_timestamp, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=delimiter)
        # Write the CSV header
        csv_writer.writerow(['Author', 'Link', 'Title', 'Summary', 'Published'])

        # Loop through each URL and author
        for author, url in read_feed_urls(urls_file):
            print(f"Fetching feed from: {url} by {author}")
            # Call the get_feed function with the correct parameters
            get_feed(url, author, retrieve_by, date=date, max_count=count if retrieve_by == 'count' else None, csv_writer=csv_writer)
            print("=" * 40)  # Separator between different feeds

def print_metadata(feed):
    
    pprint(feed.feed)
    print("-" * 40)
    
    if feed.entries:
        
        first_entry = feed.entries[0]
            
        # Print the fields (keys) of the first entry
        print("Fields in the first entry:")
        
        for field in first_entry.keys():
                print(field)


if __name__ == "__main__":
    # Specify the path to your configuration file
    config_file = 'config.yaml'

    # Process feeds using the configuration
    process_feeds(config_file)
