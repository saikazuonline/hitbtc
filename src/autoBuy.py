import hitBtc
import configparser
from module import *

if __name__ == "__main__":
    # START API情報
    conf = configparser.ConfigParser()
    conf.read('../info/setting.conf')
    # publicKey
    public_key = conf.get('INFO', 'API_KEY')
    # secretKey
    secret = conf.get('INFO', 'SECRET_KEY')
    # END API情報

    # 実行情報
    client = hitBtc.Client("https://api.hitbtc.com", public_key, secret)

    afCurrency = getAfterCurrencys(client)
    beCurrency = textReadForCurrency()

    currencys = comparison(afCurrency, beCurrency)

    for currency in currencys:
        orderInfo = calculation(conf, client, currency)
        buy(client, orderInfo)

    textWriteForCurrency(getBalances(client))