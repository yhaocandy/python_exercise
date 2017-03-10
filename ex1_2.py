import postgresql
import postgresql.driver as pg_driver
import uuid


db = pg_driver.connect(user = 'postgres',password = 'xxxxx',host = 'xxxx',
port = 5432,
database = 'xxx'
)

def create_code(n, length):   #生成”n“个激活码，每个激活码含有”length“位
    result = []

    while True:
        jihuoma = uuid.uuid4()
        list = str(jihuoma).replace('-', '')[:length]
        if not list in result:
            result.append(list)
        if len(result) == n:
            break
    return result
temp = (create_code(10, 8))
print(temp)


for c in range(0, 10):
    a = temp[c]
    sql_a = "insert into pyex5(ide) values ('{}')".format(a)
    try:
        db.query(sql_a)
    except postgresql.exceptions.UniqueError:
        pass



