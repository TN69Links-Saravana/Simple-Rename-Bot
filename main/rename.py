import time, os
from pyrogram import Client, filters, enums
from config import DOWNLOAD_LOCATION, CAPTION, ADMIN
from main.utils import progress_message, humanbytes

@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    if len(msg.command) < 2 or not reply:
       return await msg.reply_text("Pʟᴇᴀsᴇ Rᴇᴘʟʏ Tᴏ Aɴ Fɪʟᴇ Oʀ Vɪᴅᴇᴏ Oʀ Aᴜᴅɪᴏ Wɪᴛʜ FɪʟᴇNᴀᴍᴇ + .extension Exᴀᴍᴘʟᴇ :-(`.mkv` or `.mp4` or `.zip`)")
    media = reply.document or reply.audio or reply.video
    if not media:
       await msg.reply_text("Pʟᴇᴀsᴇ Rᴇᴘʟʏ Tᴏ Aɴ Fɪʟᴇ Oʀ Vɪᴅᴇᴏ Oʀ Aᴜᴅɪᴏ Wɪᴛʜ FɪʟᴇNᴀᴍᴇ + .extension Exᴀᴍᴘʟᴇ :-(`.mkv` or `.mp4` or `.zip`)")
    og_media = getattr(reply, reply.media.value)
    new_name = msg.text.split(" ", 1)[1]
    sts = await msg.reply_text("Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ.....")
    c_time = time.time()
    downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ.....", sts, c_time)) 
    filesize = humanbytes(og_media.file_size)                
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            return await sts.edit(text=f"Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Eʀʀᴏʀ Uɴᴇxᴘᴇᴄᴛᴇᴅ Kᴇʏᴡᴏʀᴅ ●> ({e})")           
    else:
        cap = f"{new_name}\n\n💽 size : {filesize}"

    # this idea's back end is TN69Links brain 🧠

    dir = os.listdir(DOWNLOAD_LOCATION)
    if len(dir) == 0:
        file_thumb = await bot.download_media(og_media.thumbs[0].file_id)
        og_thumbnail = file_thumb
    else:
        try:
            og_thumbnail = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"
        except Exception as e:
            print(e)        
            og_thumbnail = None
        
    await sts.edit("Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅɪɴɢ")
    c_time = time.time()
    try:
        await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Uᴘʟᴏᴀᴅᴇ Sᴛᴀʀᴛᴇᴅ.....", sts, c_time))        
    except Exception as e:  
        return await sts.edit(f"Error {e}")                       
    try:
        if file_thumb:
            os.remove(file_thumb)
        os.remove(downloaded)      
    except:
        pass
    await sts.delete()





