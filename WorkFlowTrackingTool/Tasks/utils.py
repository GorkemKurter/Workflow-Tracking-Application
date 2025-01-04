import requests
from django.utils.text import slugify
import os

def send_telegram_message(message):
    bot_token = '7778529175:AAG07DGCZSP-uVqn4vQILVqC7N7xH_lj2fU'
    chat_id = '-4611990013'
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    proxies = {
    'http': 'http://10.146.55.60:8080',
    'https': 'http://10.146.55.60:8080',
    }

    try:
        response = requests.post(api_url, data={'chat_id': chat_id, 'text': message},proxies=proxies,verify=False)
        if response.status_code != 200:
            print(f"Failed to send message: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
#send_telegram_message('Port Number Test')

def order_upload_to(instance, filename):
    topic_slug = slugify(instance.Topic)
    return os.path.join(f'orders/{topic_slug}', filename)

def emc_upload_to(instance, filename):
    emc_slug = slugify(instance.Topic)
    return os.path.join(f'emc/{emc_slug}', filename)

def e_lab_upload_to(instance, filename):
    e_lab_slug = slugify(instance.Topic)
    return os.path.join(f'Tests/{e_lab_slug}', filename)

