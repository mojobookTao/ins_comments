import requests

url = "https://www.instagram.com/graphql/query/"

querystring = {"query_hash":"97b41c52301f77ce508f55e66d17620e","variables":"%7B%22shortcode%22%3A%22Bx8OM-lgcDj%22%2C%22first%22%3A12%2C%22after%22%3A%22%7B%5C%22cached_comments_cursor%5C%22%3A+%5C%2217992640746232530%5C%22%2C+%5C%22bifilter_token%5C%22%3A+%5C%22KDYBDABYACAAGAAQAAgACAB_7__Pnz_UvP_eb26jad9_y7be197_-V-v_v7__z47O7u1XGJAiJAA%5C%22%7D%22%7D"}

headers = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "79e00d52-c69a-49e5-8f8c-ae9d2b260b14,b6a5a7a8-d09a-41c4-ad8f-d301f73b460f",
    'Host': "www.instagram.com",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)