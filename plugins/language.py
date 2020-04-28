from mmpy_bot.bot import respond_to, listen_to
from mmpy_bot.dispatcher import Message
from polyglot.detect import Detector
from polyglot.detect.base import UnknownLanguage

@respond_to('.*')
def give_me(message: Message):
    try:
        detector = Detector(message.get_message())
        message.reply_thread(str(detector))
    except UnknownLanguage:
        message.react('-1')

@listen_to('.*')
def to_english(message: Message):
    url_name = message.get_channel_name()
    is_direct_message = message.is_direct_message()
    if (not is_direct_message) and url_name != "town-square":
        try:
            detector = Detector(message.get_message())
            if detector.reliable is True:
                if detector.language.code == 'de' and detector.language.confidence > 0.9:
                    if len(message.get_message().split(" ")) > 3:
                        message.react("uk")
        except Exception:
            return
        #message.reply_thread(", ".join(map(str,langs)))
