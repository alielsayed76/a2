import asyncio
import pyrogram
from cache.admins import admins
from pyrogram import Client, filters
from config import  IMG_3, UPDATES_CHANNEL
from time import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from driver.filters import command


 @Client.on_message(command(["الاوامر", "اوامر", "الاوامر", "م", f"nftb@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def nftb(client: Client, message: Message):
    await message.reply_photo(
        photo=f"IMG3",
        caption=f""""🌀 ها هي الاوامر :
الاوامر تكتب كما هي بدون شرط او اي شيء
━━━━━━━━━━━━
⇦اوامر تشغيل البوت في المجموعات⇨
⇦ ✪『  تشغيل 』✪➢ ➕ 「اسم الأغنية او / رابط」تشغيل الصوت mp3
⇦ ✪『  فديو 』✪➢ ➕ 「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
⇦ ✪『  تشغيل 』✪➢ ➕  「رابط 」تشغيل صوت
 ⇦ ✪『  فديو 』✪➢ ➕  「رابط」 تشغيل فيديو مباشر من اليوتيوب
⇦ ✪『 ايقاف او انهاء』✪➢ ☆ لايقاف التشغيل
⇦ ✪『  وقف 』✪➢ ☆ ايقاف التشغيل موقتآ 
⇦ ✪『 تقدم 』✪➢ ☆ تخطي الئ التالي
⇦ ✪『   مواصله  』✪➢ ☆ استئناف التشغيل 
⇦ ✪『   كتم او سكوت 』✪➢ ☆ لكتم البوت
⇦ ✪『 الغاء الكتم』✪➢ ☆ لرفع كتم البوت
━━━━━━━━━━━━
⇦اوامر التحكم بلبوت خارج وداخل المجموعات⇨
⇦ ✪『   تحكم 』✪➢ ☆ ↤ تظهر لك قائمة التشغيل
⇦ ✪『   تنزيل 』✪➢ ➕ «اسم الفديو» لتنزيل فديو من اليوتيوب 
⇦ ✪『   تحميل 』✪➢ ➕ «اسم الاغنيه» لتحميل اغنيه من اليوتيوب 
⇦ ✪『   بحث 』✪➢ ➕ «اي شيء تريد البحث عنه بليوتيوب»
⇦ ✪『   الصوت 』✪➢ ➕ «كتابه» الرقم لضبط مستوئ الصوت
⇦ ✪『   تحديث 』✪➢ ☆ لتحديث البوت و قائمة المشرفين
⇦ ✪『   انضم 』✪➢ ☆ لاستدعاء حساب المساعد
⇦ ✪『   غادر 』✪➢ ☆ لطرد حساب المساعد 
⇦ ✪『   بينج 』✪➢ ☆ - إظهار حالة البوت بينغ
⇦ ✪『   الوقت 』✪➢ ☆ - اظهار الوقت
⇦ ✪『   السورس 』✪➢ ☆  إظهار معلومات البوت  (في المجموعة)
━━━━━━━━━━━━
⇦اوامر تحكم المطور⇨
⇦ ✪『   مسح  』✪➢ ☆ لمسح جميع الملفات المستخدمه
⇦ ✪『   تنظيف  』✪➢ ☆ لتنظيف جميع الملفات المحمله
⇦ ✪『   معلومات  』✪➢ ☆ لرؤيه معلومات النظام 
⇦ ✪『  ترقيه 』✪➢ ☆ لترقيه البوت لاخر اصدار من السورس
⇦ ✪『  تنصيب 』✪➢ ☆ لاعاده التشغيل من هيركو
⇦ ✪『  غادرالجميع 』✪➢ ☆ لمغادره الحساب المساعد لجميع الدردشات
━━━━━━━━━━━━━━
"𝆥  ⚡️ ??قناة البوت @{UPDATES_CHANNEL}"),
"""
        ),
    )
    
@Client.on_message(command(["uptime","لوقت", f"uptime@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
    async def get_uptime(client: Client, message: Message):
        current_time = datetime.utcnow()
        uptime_sec = (current_time - START_TIME).total_seconds()
        uptime = await _human_time_duration(int(uptime_sec))
        await message.reply_text(
            "🤖 bot status:\n"
            f"• **uptime:** `{uptime}`\n"
            f"• **start time:** `{START_TIME_ISO}`"
         
            )
      @Client.on_message(
    command(["ورتي","وري"])
    & filters.group
    & ~filters.edited
)
async ah madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""صورتك عفنت غيرها بقا😂""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],[
                    InlineKeyboardButton(
                        "SOURCE", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
            ]
        ),
    )
