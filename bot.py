from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
import asyncio
from random import randint,random
import time
import json


print("Use api_id,api_hash,text from last session?\n (y/n)")
check=input().lower()

if check=="n":
    data={}
    print("Write API ID:")
    api_id=input()
    data["api_id"]=api_id
    
    print("Write API HASH:")
    api_hash=input()
    data["api_hash"]=api_hash

    print("Write Text:")
    mes_text=input()
    data['text']=mes_text

    with open("data\\config.json","w", encoding="utf-8") as file :
        json.dump((data),file,indent=4,ensure_ascii=False)

if check=="y":
    data={}
    with open("data\\config.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    api_id=data["api_id"]
    api_hash=data["api_hash"]
    mes_text=data["text"]

client = Client(name="data\\my_client",api_id=api_id,api_hash=api_hash)
@client.on_message(filters.channel)
def all_message(client:Client,message:Message):
    if randint(1,99)%2==0:
        delay=random()*3
        print(f"delay {round(delay,1)}s.")
        time.sleep(delay)

        
    print("---------------------------------------------------")
    mes=client.get_discussion_message(message.chat.id,message.id)
    client.send_message(chat_id=mes.chat.id,text=mes_text)
print(f"start work|api_id:{api_id}")
client.run()
