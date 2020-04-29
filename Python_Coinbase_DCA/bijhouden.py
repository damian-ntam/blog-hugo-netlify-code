from coinbase.wallet.client import Client


API_VERSION = '2020-04-18'
currency = 'EUR'

buy_price_threshold_min  = 4000
btcToBuyInEUR=2;

client = Client(API_KEY, API_SECRET, api_version=API_VERSION)

accounts = client.get_accounts()


for account in accounts:
    print(f"Accounts: {account['data']['name']}" )



#account = client.get_primary_account()
#print(f"Primary Account: {account}" )
#payment_methods = client.get_payment_methods()
#print(f"Payment Method: {payment_methods}" )

def main():
    for method in payment_methods.data:
        if (method.name == "EUR Wallet"):
            payment_method = method.id

    print("Getting latest BTC price...");
    buy_price  = client.get_buy_price(currency=currency)
    print("Latest BTC price in " + currency + ": " + buy_price.amount)
    btcToBuy=round(btcToBuyInEUR/float(buy_price.amount), 8);
    print("You want to buy " + str(btcToBuyInEUR) + buy_price.currency + " in BTC. Therefore you will buy " + str(btcToBuy) + " BTC")
    checkBalance(accounts)
    performBTCBuy(account, payment_method, buy_price, buy_price_threshold_min, btcToBuy )
    checkBalance(accounts)

def performBTCBuy(account, payment_method, buy_price, buy_price_threshold_min, btcToBuy):
    #print(str(buy_price.amount))
    #print(str(buy_price_threshold_min))

    if float(buy_price.amount) <= buy_price_threshold_min:
        try:
            print("Executing the buy")
            #buy = account.buy(
            #        amount=btcToBuy,
            #        currency="BTC",
            #        payment_method=payment_method
            #)
            print("Purchase was successfull")
        except:
            print("Purchase was not successfull")
    else:
        print("Could not buy BTC as the curreny BTC price is above " + str(buy_price_threshold_min))


        #print("Purchase was successfull")

def checkBalance(accounts):
    for account in accounts.data:
        if (account.name == "EUR Wallet" or account.name == "BTC Wallet"):
            print("Balance for account " + account.name + ": "+ str(account.balance) )

if __name__ == "__main__": main()


