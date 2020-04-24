from mmpy_bot.bot import respond_to, listen_to
from langdetect import detect_langs
from mmpy_bot.dispatcher import Message
from langdetect.lang_detect_exception import LangDetectException

@respond_to('.*')
def give_me(message: Message):
    try:
        langs = detect_langs(message.get_message())
        message.reply_thread(", ".join(map(str, langs)))
    except LangDetectException:
        message.react('-1')

@listen_to('.*')
def to_english(message: Message):
    url_name = message.get_channel_name()
    is_direct_message = message.is_direct_message()
    if (not is_direct_message) and url_name != "town-square":
        try:
            langs = detect_langs(message.get_message())
            if len(langs) == 1:
                if langs[0].lang == 'de' and langs[0].prob > 0.99:
                    if len(message.get_message().split(" ")) > 3:
                        message.react("uk")
        except LangDetectException:
            return
        #message.reply_thread(", ".join(map(str,langs)))
