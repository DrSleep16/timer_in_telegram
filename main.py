import os
from dotenv import load_dotenv
import ptbot as alien_bot
from pytimeparse import parse


def start_countdown(chat_id, text):
    time = parse(text)
    message_id = bot.send_message(chat_id, f'Осталось {time}')
    bot.create_countdown(
        time,
        update_telegram_message,
        chat_id=chat_id,
        id=message_id,
        start_time=time
    )
    bot.create_timer(time, send_finish, chat_id=chat_id)


def send_finish(chat_id):
    bot.send_message(chat_id,'Время вышло!')


def update_telegram_message(secs_left,chat_id,id,start_time):
    bot.update_message(
        chat_id,
        id,
        f'Осталось {secs_left}'
        f'\n{render_progressbar(start_time,start_time-secs_left)}'
    )


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    bot = alien_bot.Bot(tg_token)
    bot.reply_on_message(start_countdown)
    bot.run_bot()
