import requests

from config import (
    EVOLUTION_API_URL,
    EVOLUTION_INSTANCE_NAME,
    EVOLUTION_AUTHENTICATION_API_KEY,
)

def send_whatsapp_message(number, text):
    url = f'{EVOLUTION_API_URL}/message/sendText/{EVOLUTION_INSTANCE_NAME}'
    headers = {
        'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
        'Content-Type': 'application/json',
    }

    payload = {
        'number': number,
        'text': text,
    }
    requests.post(
        url=url,
        json=payload,
        headers=headers,
    )

def mark_message_as_read(remote_jid, message_id):
    url = f'{EVOLUTION_API_URL}/chat/markAsRead/{EVOLUTION_INSTANCE_NAME}'
    headers = {
        'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
        'Content-Type': 'application/json',
    }

    payload = {
        'lastMessage': {
            'key': {
                'remoteJid': remote_jid,
                'fromMe': True,
                'id': message_id
            }
        }
    }

    response = requests.post(
        url=url,
        json=payload,
        headers=headers,
    )
    return response.json()
