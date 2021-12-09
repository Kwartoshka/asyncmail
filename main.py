import asyncio
import sqlite3
from email.message import EmailMessage

import aiosmtplib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_emails():
    connection = sqlite3.connect(r'contacts.db')
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM contacts;").fetchall()
    print(result)
    return result


async def send_message(subject):
    message = EmailMessage()
    message["From"] = "root@localhost"
    print()
    message["To"] = subject[3]
    message["Subject"] = "RE"
    message.set_content(f"Уважаемый {subject[1]} {subject[2]}\! Спасибо, что пользуетесь нашим сервисом объявлений\.")
    await aiosmtplib.send(message, hostname="127.0.0.1", port=1025)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(aiosmtplib.send(message, hostname="127.0.0.1", port=25))
    #


subjects = get_emails()


async def main():
    for subject in subjects:
        await send_message(subject)


asyncio.run(main())
