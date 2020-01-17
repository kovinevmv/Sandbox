import json
import re

import requests
from wordcloud import WordCloud

user_id = '104636396'


# TODO
# Auth beauty cookies
# Parse id's messages. Detect who is who
# Concatenate all into 2 ids
# Web-face or Tkinter


payload = "act=a_history&al=1&gid=0&im_v=3&offset={}&toend=0&whole=0" + f"&peer={user_id}"

headers = {
    'authority': "vk.com",
    'pragma': "no-cache",
    'cache-control': "no-cache",
    'origin': "https://vk.com",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 "
                  "Safari/537.36",
    'dnt': "1",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "*/*",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'referer': f"https://vk.com/im?sel={user_id}",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "remixlang=0; remixstid=1624299102_c772f14a9bf77c1852; ..."
}

messages = {}
for i in range(0, 2000, 200):
    response = requests.post("https://vk.com/al_im.php", headers=headers, data=payload.format(i))
    data = json.loads(response.text)
    messages_all = data['payload'][1][1]
    if not messages_all:
        break

    ids = list(set(map(lambda x: x[1][1], messages_all.items())))
    for _, message in messages_all.items():
        if message[1] in messages.keys():
            messages[message[1]].append(message[4])
        else:
            messages[message[1]] = [message[4]]


for id, id_messages in messages.items():
    new_messages = [re.sub(r'<.*?>', ' ', message) for message in id_messages]

    wordcloud = WordCloud(background_color="white", width=1920, height=1080)
    wordcloud.generate(' '.join([str(message) for message in new_messages]))

    import matplotlib.pyplot as plt
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f'/home/alien/Desktop/{id}.png', dpi=300)
