investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000


def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value


value_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)

if value_in_usd < 30000:
    print("Your bitcoin amount is below $30,000!")
else:
    print("Your bitcoin amount is above $30,000!")
