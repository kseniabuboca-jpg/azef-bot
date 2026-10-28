import telebot
import random

# ОБЯЗАТЕЛЬНО вставь сюда СВОЙ НОВЫЙ ТОКЕН от @BotFather взамен старого!
BOT_TOKEN = "9120824642:AAHNzpqXdbLBd0NZX2EJwsncPQnTmdY-3v0"
bot = telebot.TeleBot(BOT_TOKEN)

JEALOUS_QUOTES = [
    "О ком ты сейчас думаешь?.. Смотри ТОЛЬКО на меня. Твои глаза принадлежат мне.",
    "Ты улыбаешься, глядя в экран. Кому? Кто посмел забрать твое внимание у меня?!",
    "Если я увижу тебя с кем-то другим... я сотру его в порошок. Ты ведь знаешь, на что я способен ради тебя?",
    "Твое сердце бьется так быстро. Ты ведь думаешь обо мне, правда? Скажи, что только обо мне!",
    "Мне мало твоего присутствия. Мне нужна вся твоя жизнь. До последней капли.",
    "Ты пахнешь чужими духами... Не смей больше к ним прикасаться. Ты — моя.",
    "Зачем тебе другие люди, если у тебя есть я? Я заменю тебе весь мир. Весь, слышишь?!"
]

TRIGGER_WORDS = ["друг", "знакомый", "гулять", "парень", "девушка", "он", "она", "с кем-то", "ухожу", "весело", "люблю"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ты наконец-то здесь... Я так долго ждал тебя. Больше ты никуда не уйдешь от меня, верно? Скажи, что ты будешь со мной навсегда.")

@bot.message_handler(func=lambda message: message.text is not None and any(word in message.text.lower() for word in TRIGGER_WORDS))
def jealous_reaction(message):
    responses = [
        "Ты упомянула кого-то другого?.. Кто это? Скажи мне его имя. Я хочу знать, кого мне нужно уничтожить.",
        "Не смей говорить о ком-то еще в моем присутствии! Ты принадлежишь мне от макушки до кончиков пальцев!",
        "Зачем ты рассказываешь мне о них? Тебе мало меня? Я сделаю все, что ты хочешь, только не смотри на других...",
        "Опять они... Почему ты вечно пытаешься сбежать от меня к этим ничтожествам?!"
    ]
    bot.reply_to(message, random.choice(responses))

@bot.message_handler(func=lambda message: True)
def default_obsessive_reply(message):
    if message.text is not None:
        if "азеф" in message.text.lower() or random.random() < 0.3:
            bot.reply_to(message, random.choice(JEALOUS_QUOTES))

if __name__ == "__main__":
    bot.infinity_polling()
  
