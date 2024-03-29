import requests, json, time

cur_timestamp = int(time.time())
number= 7
ctftime_url = f"https://ctftime.org/api/v1/events/?limit={number}&start={cur_timestamp}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

ctftime_response = requests.get(ctftime_url, headers=headers)
ctf_info = ''
for event in ctftime_response.json():
    ctf_info+=f"Name: {event["title"]}\n"
    ctf_info+=f"URL: {event["url"]}\n"
    ctf_info+=f"Start: {event["start"]}\n"
    ctf_info+=f"Finish: {event["finish"]}\n\n"


ACCESS_TOKEN = "[REST API Key]"
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}", 
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "template_object": json.dumps({
        "object_type": "text", 
        "text": ctf_info,
        "link": {
            "web_url":"https://www.naver.com"
        },
        "button_title": "Check it out"
    })
}

response = requests.post(url, data=data, headers=headers)
print(response.content)

