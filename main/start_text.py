from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="This is personal use bot 🙏. Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Bᴏᴛ? 👇 Cʟɪᴄᴋ Tʜᴇ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ Tᴏ Dᴇᴘʟᴏʏ"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TN69Links-Saravana/Simple-Rename-Bot")
        ],[
        InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Dᴇᴘʟᴏʏ", url="https://youtube.com/@TN69Links")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"hai {msg.from_user.mention} I Aᴍ Sɪᴍᴘʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Pᴇʀsᴏɴᴀʟ Usᴀɢᴇ.\nTʜɪs Bᴏᴛ Is Mᴀᴅᴇ Bʏ <b><a href=https://t.me/Cute_Boy_Saravana</a></b>"                                     
    button= [[
        InlineKeyboardButton("🦋 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🦋", url="https://t.me/TN69Links")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Mᴀsᴛᴇʀ=f"<a href=https://t.me/Cute_Boy_Saravana>Ƭɴ69 ×͜× Sᴀʀᴀᴠᴀɴᴀ࿐</a> & <a href=https://t.me/TN69Vikram>ᥫ᭡፝֟፝֟ Vikram࿐</a>"  
    Sᴏᴜʀᴄᴇ="<a href=https://github.com/TN69Links-Saravana/Simple-Rename-Bot>Click Here</a>"
    txt=f"<b>Bᴏᴛ Nᴀᴍᴇ: {me.mention}\nDᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/TN69Links</a>\n🦋 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🦋: <a href=https://youtube.com/@TN69Links>🌸 YᴏᴜTᴜʙᴇ Cʜᴀɴɴᴇʟ 🌸</a>\n😈 Mʏ Mᴀsᴛᴇʀ's 😈: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


