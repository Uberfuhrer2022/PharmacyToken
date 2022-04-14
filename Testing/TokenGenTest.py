from datetime import datetime
import json
from datetime import datetime


def TokenCreate():
    CurrentDay = datetime.today()
    CurrentTime = datetime.now()

    tknDate = CurrentDay.strftime("%d-%b-%Y")
    tknTime = CurrentTime.strftime("%H:%M:%S")

    data = {
        "TokenID": 0,
        "Time": print(tknTime),
        "Date": print(tknDate)
    }

    print(f"Data:", data)

    # printing object as json string
    s = json.dumps(data)
    print(f"JSON Input: ", s)

    # getting python object from json string
    data2 = json.loads(s)
    assert data2 == data

    # writing data to file
    with open('db_Tokens.json', 'w') as f:
        json.dump(data, f)

    # reading data from file
    with open('db_Tokens.json') as f:
        data3 = json.load(f)
    assert data3 == data


if __name__ == '__main__':
    TokenCreate()
