import requests
import time


class Bot:
    @classmethod
    def initialize(cls):
        cls.__read_keys()
        cls.last_error = ''
        print('initialized LineNotification')

    @classmethod
    def __read_keys(cls):
        file = open('./ignore/line.txt', 'r')  # 読み込みモードでオープン
        cls.token = file.readline().split(':')[1]
        file.close()

    @classmethod
    def send_message(cls, message):
        url2 = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + cls.token}
        payload = {"message": message}
        try:
            res = requests.post(url2, headers=headers, data=payload)
        except Exception as e:
            print('Line notify error!={}'.format(e))

if __name__ == '__main__':
    Bot.initialize()
    for i in range(10):
        Bot.send_message('\r\n' + 'call no.='+str(i))
        time.sleep(10)

