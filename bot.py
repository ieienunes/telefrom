#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("28950191", default=None, cast=int)
API_HASH = config("5703eecea6a40b91f651a16e0a53d70d", default=None)
SESSION = config("1AZWarzUBu2KFO131lECd8y56_41QfGxXfWm03EJtt4iK4Ihk7fnBn8gnFI6hMKgbO_i4XovhQ6A37Wy6b_k12WlMzRENXXz0VfdW0taidBv7nCn1DfADDNoxu8BKVJcHWhw3HIl2IDf9OnQRUJa2FXiRGJqTMBibESt06MrTAyzZkWotym54PQF4TMt0F1cPASXMGXtiPEHflEqMEGSRXMtwW02P3H58opuXtZEGrjz1lrNkuEeQfH8yTfBmWfr7mzLkLWaFSXteGWfnEBgVIcLJZEj1Dg3mlCmnJ5mgpctTj0bQVtE1ICjFwHyADtHh8uO9Dqk9UwYqp_1FRaRmtmTlK3vU8ns=")
FROM_ = config("-1001722050407")
TO_ = config("-1001845061551")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            message = await event.get_reply_message()
            input_msg = await BotzHubUser.input(f"Digite a mensagem para enviar para {i}:")
            msg = input_msg.stringify().replace('message=', '')
            
            # Remover links da mensagem
            msg = re.sub(r'http\S+', '', msg, flags=re.MULTILINE)
            
            if message:
                msg = msg + f"\n\n{message.sender.first_name}: {message.text}"
            edited = await BotzHubUser.input(f"Editar mensagem para {i}: {msg}")
            await BotzHubUser.send_message(i, edited)
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()




















