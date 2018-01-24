import uuid
import hitBtc
from decimal import *

def getBalances(client):
    # 一覧を取得
    balances = client.get_account_balance()

    return balances

def getAfterCurrencys(client):

    afCurrency = []

    # 一覧を取得
    balances = client.get_account_balance()

    for balance in balances:
        afCurrency.append(balance['currency'])

    return afCurrency

def textWriteForCurrency(balances):

    # ファイル書き込みモード
    fileWriteMode = open('../data/bitcoin.txt', 'w')

    # 通過の部分だけを書き込み
    for balance in balances:
        fileWriteMode.write(balance['currency'] + '\n')

    # ファイルを閉じる
    fileWriteMode.close()

def textReadForCurrency():

    # リスト初期化
    beforeCurrency = []

    # ファイル読み込みモード
    fileReadMode = open('../data/bitcoin.txt', 'r')

    # 改行ごとにリスト型で取得
    currencys = fileReadMode.readlines()

    # \nを取り除きリストに格納
    for currency in currencys:
        beforeCurrency.append(currency.replace("\n", ""))

    # ファイル閉じる
    fileReadMode.close()

    return beforeCurrency

def comparison(afCurrencys, beCurrencys):

    comparisonFlg = False
    currencys = []

    for afCurrency in afCurrencys:
        hitFlg = False
        for beCurrency in beCurrencys:
            if(afCurrency == beCurrency):
                hitFlg = True
        if(hitFlg == False):
            print('新通貨があります: ' + afCurrency)
            comparisonFlg = True
            currencys.append(afCurrency)
    if(comparisonFlg == False):
        print('新通貨はありませんでした。')

    return currencys

def calculation(conf, client, currency):

    symbol = currency + 'BTC'

    orderbook = client.get_orderbook(symbol)

    client_order_id = uuid.uuid4().hex
    btc_usdt = Decimal(conf.get('VALUE', 'BTC_USDT')) # TODO 可変でもってこれるようにする
    best_price = Decimal(orderbook['bid'][0]['price'])
    doller = Decimal(conf.get('VALUE', 'DOLLER'))

    symbolDoll = btc_usdt * best_price
    quentity = round((doller / symbolDoll), 0)

    orderInfo = {'client_order_id':client_order_id, 'symbol':symbol, 'price': best_price, 'quentity': quentity}

    return orderInfo

def buy(client, orderInfo):

    print(orderInfo)

    order = client.new_order(orderInfo['client_order_id'], orderInfo['symbol'], 'buy', orderInfo['quentity'], orderInfo['price'])
    if 'error' not in order:
        if order['status'] == 'filled':
            print("Order filled", order)
        elif order['status'] == 'new' or order['status'] == 'partiallyFilled':
            print("Waiting order...")
            for k in range(0, 3):
                order = client.get_order(client_order_id, 20000)
                print(order)

                if 'error' in order or ('status' in order and order['status'] == 'filled'):
                    break



