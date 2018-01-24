import hitBtc
from module import *

# このファイルが実行された時のみ実行
if __name__ == "__main__":

    # publicKey
    public_key = "76d97819b9ee9ac6d677ba6f6af1d0f7"
    # secretKey
    secret = "f9a571b58d61f8d4ca4eb615962eba12"

    # 実行情報
    client = hitBtc.Client("https://api.hitbtc.com", public_key, secret)

    beforeCurrency = []

    textWriteForCurrency(getBalances(client))