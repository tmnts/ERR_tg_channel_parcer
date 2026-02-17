import requests
import time

API_TOKEN = 'YOUR_TOKEN_HERE'
CATEGORIES = ['technology', 'business', 'economy']

def hunt():
    for cat in CATEGORIES:
        print(f"--- Ищу в категории: {cat} ---")
        url = f"https://api.tgstat.ru{API_TOKEN}&category={cat}&subscribers_from=10000&subscribers_to=50000&language=russian"
        
        res = requests.get(url).json()
        if res.get('status') == 'ok':
            # Берем первые 10
            channels = res['response']['items'][:10]
            for ch in channels:
                # В Питоне задержка не вешает поток так, как в Гугле
                time.sleep(2) 
                stat_url = f"https://api.tgstat.ru{API_TOKEN}&channelId={ch['username']}"
                stat = requests.get(stat_url).json()
                
                if stat.get('status') == 'ok':
                    err = stat['response'].get('err_percent', 0)
                    if err >= 15:
                        print(f"🔥 НАЙДЕН: @{ch['username']} | ERR: {err}% | Подписчиков: {ch['participants_count']}")
        print("\n")

hunt()
