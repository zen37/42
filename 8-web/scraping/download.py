import requests 

WEBSITE = 'https://Xautomatetheboringstuff.com/files/rj.txt'
TIMEOUT_SEC = 10

def download():

    try:
        res = requests.get(WEBSITE, timeout=TIMEOUT_SEC)
        print("status code: ", res.status_code)
        #print(type(res))
        print(res.text[:25])
    except Exception as e:
        print('There was a problem: %s' % (e))

if __name__ ==  "__main__":
    download()