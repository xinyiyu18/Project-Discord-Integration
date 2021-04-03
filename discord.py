import getopt
import sys
import os
import requests


def helper(x):
    r = requests.get('https://animechan.vercel.app/api/quotes/anime', params={'title': x})
    if r.status_code != 200:
        print("Error message: no quotes is found. Try another. "
              "Example input: Inuyasha, Jitsu wa Watashi wa, Gantz, The Heroic Legend of Arslan")
        sys.exit()
    q = r.json()[0]['quote']
    data = {
        "content": q,
        "username": "SpongeBob",
        # "avatar_url":"",
    }
    url = "https://discord.com/api/webhooks/808788725890941008/" + os.getenv("WEBHOOK_TOKEN")
    response = requests.post(url, json=data)
    print(response)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "i:h")
    except getopt.GetoptError:
        print('discord -i <input>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-i':
            helper(arg)
            sys.exit()
        if opt == '-h':
            print('HELP: You can input the animate title to fetch its quote. For example: \ndiscord -i <input>;'
                  ' Example input: Inuyasha, Jitsu wa Watashi wa, Gantz, The Heroic Legend of Arslan')
            sys.exit()
    print('HELP: You can input the animate title to fetch its quote. For example: \ndiscord -i <input>; '
          ' Example input: Inuyasha, Jitsu wa Watashi wa, Gantz, The Heroic Legend of Arslan')


if __name__ == "__main__":
    main(sys.argv[1:])
