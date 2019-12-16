import time
import sys
from setting import session
from sqlalchemy.sql import text

def main(loop):
    insert_sql = text(f"INSERT INTO test_users (loop_value) VALUES ('loop-{loop}')")
    session.execute(insert_sql)
    session.commit()

    select_sql = text("SELECT NOW() AS now, @@hostname AS hostname")
    for row in session.execute(select_sql):
        print(f"{row['now']} - {row['hostname']}")


if __name__ == '__main__':
    loop = 0
    while (True):
        try:
            main(loop)
        except:
            print(sys.exc_info())
            pass
        finally:
            session.close()
            loop +=1
            time.sleep(1)
