from pyrogram import Client, filters 
from config import ADMIN, DOWNLOAD_LOCATION
import os

dir = os.listdir(DOWNLOAD_LOCATION)

@Client.on_message(filters.private & filters.photo & filters.user(ADMIN))                            
async def set_tumb(bot, msg):       
    if len(dir) == 0:
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        return await msg.reply(f"<b>Yᴏᴜʀ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Is Sᴀᴠᴇᴅ Iɴ Dɪᴄᴛɪᴏɴᴀʀʏ ✅️ \nIғ Yᴏᴜ Cʜᴀɴɢᴇ Yᴜʀ Sᴇʀᴠᴇʀ Oʀ Rᴇᴄʀᴇᴀᴛᴇ Tʜᴇ Sᴇʀᴠᴇʀ Aᴘᴘ Tᴏ Aɢᴀɪɴ Rᴇsᴇᴛ Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ ⚠️</b>")            
    else:    
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")               
        return await msg.reply(f"<b>Yᴏᴜʀ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Is Sᴀᴠᴇᴅ Iɴ Dɪᴄᴛɪᴏɴᴀʀʏ ✅️ \nIғ Yᴏᴜ Cʜᴀɴɢᴇ Yᴜʀ Sᴇʀᴠᴇʀ Oʀ Rᴇᴄʀᴇᴀᴛᴇ Tʜᴇ Sᴇʀᴠᴇʀ Aᴘᴘ Tᴏ Aɢᴀɪɴ Rᴇsᴇᴛ Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ ⚠️</b>")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def view_tumb(bot, msg):
    try:
        await msg.reply_photo(photo=f"{DOWNLOAD_LOCATION}/thumbnail.jpg", caption="<b>Tʜɪs Is Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ</b>")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="<b>Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Tʜᴜᴍʙɴᴀɪʟ</b>")

@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    try:
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await msg.reply_text("<b>Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ Wᴀs Rᴇᴍᴏᴠᴇᴅ 🚫</b>")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="<b>Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Tʜᴜᴍʙɴᴀɪʟ</b>")
    
