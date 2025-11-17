import re, os, time

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26047636")
    API_HASH  = os.environ.get("API_HASH", "d8b1ed69ae1f937c5dd4d3cc8c8de440")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    PORT = os.environ.get("PORT", "8080")

    # database config
    DB_NAME = os.environ.get("DB_NAME","botskingdom")
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # other configs
    ADMIN_URL = "https://t.me/Funnytamilan"
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://i.ibb.co/bMFcCB6B/59kLh.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '8367080346').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "public_miracle_bots")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003448988619"))
    FSUB_PIC = os.environ.get("FSUB_PIC", "https://i.ibb.co/bMFcCB6B/59kLh.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Miracle_renamer_bot")

    # webhook config
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):

    START_TXT = """<blockquote>ʜᴇʏ! {}</blockquote>

<blockquote>» ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ! ᴡʜɪᴄʜ ᴄᴀɴ ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇᴍ ᴘᴇʀғᴇᴄᴛʟʏ</blockquote>
<blockquote>✦ <a href="https://t.me/+yW6gjTvSLyU0YWY1">𝙈𝙞𝙧𝙖𝙘𝙡𝙚 𝙗𝙤𝙩𝙨</a></blockquote>"""

    FILE_NAME_TXT = """<b>» <u>sᴇᴛᴜᴘ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ғᴏʀᴍᴀᴛ @BOTSKINGDOMS</u></b>

<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>
➲ ᴇᴘɪꜱᴏᴅᴇ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ
➲ ǫᴜᴀʟɪᴛʏ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ǫᴜᴀʟɪᴛʏ

<b>‣ ꜰᴏʀ ᴇx:- </b> <code> /autorename Your Anime Name Here [S01 - EPepisode - [Quality]  [Dual] @BotsKingdoms </code>

<b>‣ /Autorename: ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ ʙʏ ɪɴᴄʟᴜᴅɪɴɢ 'ᴇᴘɪsᴏᴅᴇ' ᴀɴᴅ 'ǫᴜᴀʟɪᴛʏ' ᴠᴀʀɪᴀʙʟᴇꜱ ɪɴ ʏᴏᴜʀ ᴛᴇxᴛ, ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴇᴘɪsᴏᴅᴇ ᴀɴᴅ ǫᴜᴀʟɪᴛʏ ᴘʀᴇꜱᴇɴᴛ ɪɴ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ꜰɪʟᴇɴᴀᴍᴇ. @BOTSKINGDOMS """

    ABOUT_TXT = f"""<b>❍ ʙᴏᴛ ʙʏ: <a href="https://t.me/ROHITREDDY69">ʀᴏʜɪᴛ</a>
❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/ROHITREDDY69">ʀᴏʜɪᴛ</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ᴘᴜʙʟɪᴄ ʀᴇᴘᴏ : <a href="https://github.com/BOTSKINGDOMS/Auto-Renamer-bot.git">ʀᴇᴘᴏ</a>
❍ ʙᴏᴛsᴋɪɴɢᴅᴏᴍs: <a href="https://t.me/botskingdoms">Bᴏᴛs Kɪɴɢᴅᴏᴍ</a></b>"""

    THUMBNAIL_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ @BOTSKINGDOMS</u></b>
➲ /start: send any photo to save as thumbnail
➲ /del_thumb: delete current thumbnail
➲ /view_thumb: view your thumbnail"""

    CAPTION_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ</u></b>

★ /set_caption  
★ /see_caption  
★ /del_caption"""

    PROGRESS_BAR = """\n<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4}"""

    DONATE_TXT = """<blockquote> ᴛʜᴀɴᴋs ғᴏʀ sᴜᴘᴘᴏʀᴛ 💞 </blockquote>"""

    HELP_TXT = """<b>ʜᴇʟᴘ ᴍᴇɴᴜ  

★ /autorename  
★ /metadata  
★ /help</b>"""

    # ✅ METADATA TEXTS (Correctly placed inside class)
    SEND_METADATA = """
<b>--Metadata Settings:--</b>

★ /metadata: Turn on or off metadata.

<b>Description</b> : Metadata will modify MKV video files including audio, streams & subtitles.
"""

    META_TXT = """
**ᴍᴀɴᴀɢɪɴɢ ᴍᴇᴛᴀᴅᴀᴛᴀ**

- **Title**
- **Author**
- **Artist**
- **Audio**
- **Subtitle**
- **Video**

★ Commands:
    /settitle
    /setauthor
    /setartist
    /setaudio
    /setsubtitle
    /setvideo
    /setencoded_by
    /setcustom_tag

**Example:** /settitle Your Title Here
"""
