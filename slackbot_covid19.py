from datetime import datetime
import requests
import urllib.request
from bs4 import BeautifulSoup

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

myToken='xoxb-'

def run():
    target = urllib.request.urlopen("http://ncov.mohw.go.kr/")
    soup = BeautifulSoup(target, "html.parser")
    nums = []

    for item in soup.select("div.datalist"):
        for data in item.select("span.data"):
            data.string = data.string.replace(',', '')
            nums.append(int(data.string))

    post_message(myToken,"#bot_test",f"오늘 발표된 어제 코로나 확진자수는: {sum(nums)}명입니다.")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        post_message(e)
