import hitBtc
from module import *

# このファイルが実行された時のみ実行
if __name__ == "__main__":

    # START API情報
    conf = configparser.ConfigParser()
    conf.read('../info/setting.conf')
    # publicKey
    public_key = conf.get('INFO', 'API_KEY')
    # secretKey
    secret = conf.get('INFO', 'SECRET_KEY')
    # END

    # 実行情報
    client = hitBtc.Client("https://api.hitbtc.com", public_key, secret)

    beforeCurrency = []

    textWriteForCurrency(getBalances(client))