import requests
  
url = "https://www.fast2sms.com/dev/bulkV2"
  
querystring = {
    "authorization": "odM59gKcv1xiYXUT6aNQyVROP4kthS0bAuCDBeEIps8LJFwnm3VUhaZ4EA9r0HNDPXFizYOIf1mcGwyR",
    "message": "This is test Message sent from \
         Python Script using REST API.",
    "language": "english",
    "route": "q",
    "numbers": "8905429708"}
  
headers = {
    'cache-control': "no-cache"
}
try:
    response = requests.request("GET", url,
                                headers = headers,
                                params = querystring)
      
    print("SMS Successfully Sent")
except:
    print("Oops! Something wrong")