import asyncio
import pyrogram
from cache.admins import admins
from pyrogram import Client, filters
from config import  IMG_3, UPDATES_CHANNEL
from time import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from driver.filters import command, other_filters


 @Client.on_message(command(["الاوامر", "اوامر", "الاوامر", "م", f"start@{BOT_USERNAME}]) & filters.group & ~filters.edited)
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
   
   
