import asyncio
from os import link
from pickle import TRUE
from turtle import down
from pyrogram import Client

api_id=7427530
api_hash='86945cc35c57c8131c16566cb37f0249'

app = Client("new7",api_hash=api_hash,api_id=api_id)





async def main(ID):
    async with app:

        

        # "me" refers to your own chat (Saved Messages)
        async def getChatFiles(id):
            PRINT_INF=False

            count = 0
            size = 0
            links = []
            data = app.get_chat_history(id)
            async for message in data:
                if message.document:
                    count+=1
                    size+=round(float(message.document.file_size)/1024/1024/1024,3)
                    links.append(message)
                    
                    #links.append([message.document.file_id,message.document.file_name,message.document.date,message.document.file_size])
                    #links.append(FileT(message.document.file_name,message.document.file_id,message.document.date))
                    #print(message.document)
            
            if PRINT_INF:
                print(f'Total file count:{count}')
                print(f'Total file size:{round(size,2)} GB')

            return links
        
        async def downloader(arr):
            size = 0
            for i in arr:
                size+=i.document.file_size

            
            print(f'Total file size:{round(size/1024/1024/1024,2)} GB')

            for i in arr:
                print(f'Start download: {i.document.file_name}')

                #track of the progress while downloading
                async def progress(current, total):
                    total=i.document.file_size
                    print(f"Current progress: {current * 100 / total:.1f}% ",end='')
                    print('\r', end='')
                    
                    
                await app.download_media(i, progress=progress)
                print(f'Finish downloaded: {i.document.file_name} {i}/{len(arr)}')

        
        arr = await getChatFiles(ID)
        arr = arr[0:8]
        
        #for i in arr:
            #print(i.document.file_name)

        await downloader(arr)
        #print(round(float(arr[0].document.file_size)/1024/1024/1024,3),'GB')

        
        

        
                
        



        

        


        

app.run(main(-1001759499767))