from database import models
from database.models import create_connection
import time, datetime

# типо создали таблицы, далее ебашим INSERT
create_user = lambda name, priority, phone_number, user_tg_id: f"""
INSERT INTO users (name, priority, phone_number, user_tg_id) 
VALUES ('{name}', '{priority}', '{phone_number}', '{user_tg_id}');
"""

create_visit = lambda user_tg_id, option_id, poll_id, date, price: f"""
INSERT INTO visits (user_tg_id, option_id, poll_id, date, price) 
VALUES ('{user_tg_id}', '{option_id}', '{poll_id}', '{date}', '{price}')
"""

create_user_visit = lambda user_tg_id, date: f"""
INSERT INTO
    users_visits (user_tg_id, date)
VALUES
    ({user_tg_id}, '{date}')
"""


# SELECT
def select_users(path):
    select = "SELECT * FROM users"
    users = models.execute_read_query(create_connection(path), select)
    return users


def select_user(path, tg_id):
    select = f"""
    SELECT 
        name, phone_number 
    FROM 
        users 
    WHERE 
        user_tg_id = '{tg_id}'"""
    user = models.execute_read_query(create_connection(path), select)
    return user


def select_visits(path):
    select = "SELECT * FROM visits"
    visits = models.execute_read_query(create_connection(path), select)
    return visits


def insert_user_from_register(name, priority, user_tg_id, phone_number):
    # ---вручную---
    connection = models.create_connection(models.path)
    models.execute_query(connection, create_user(name, priority, phone_number, user_tg_id))


def insert_vote_in_table(user_tg_id, poll_id, option_id, date):
    # ---вручную---
    connection = models.create_connection(models.path)
    if option_id == [0]:
        models.execute_query(connection, create_visit(user_tg_id, option_id, poll_id, date, 6670 / 12))
        models.execute_query(connection, create_user_visit(user_tg_id, date))



async def create_poll_(bot):
    drop_table = """DROP TABLE users_visits"""
    connection = models.create_connection(models.path)
    models.execute_query(connection, drop_table)
    models.execute_query(connection, models.create_users_visits_table)
    next_train = str(next_saturday_day_in_a_month())
    return await bot.send_poll(chat_id='641371845',
                               question=f'Тренировка на {next_train} 11:00',
                               options=['Приду', 'Не смогу', 'Просто чекнуть проголосовавших'],
                               is_anonymous=False)


def next_saturday_day_in_a_month():
    number_of_day_in_a_week = int(time.strftime('%w'))
    count = 0
    if number_of_day_in_a_week <= 5:
        count = 5 - number_of_day_in_a_week
    elif number_of_day_in_a_week == 6:
        count = 6
    day_of_a_month_next_saturday = datetime.datetime.now() + datetime.timedelta(days=count)
    return day_of_a_month_next_saturday.strftime('%Y-%m-%d')
