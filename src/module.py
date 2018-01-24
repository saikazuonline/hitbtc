import hitBtc

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

    for afCurrency in afCurrencys:
        hitFlg = False
        for beCurrency in beCurrencys:
            if(afCurrency == beCurrency):
                hitFlg = True
        if(hitFlg == False):
            print('新通貨があります: ' + afCurrency)
            comparisonFlg = True
    if(comparisonFlg == False):
        print('新通貨はありませんでした。')





