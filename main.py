import api,cash_on_hand,overheads, profit_loss

# create a function to run api, cash_on_hand, overheads and profit_loss
def main():
    # extract the realtime currency exchange rate from api
    forex = api.exchange_rate()
    # the result of overhead, cash_on_hand and profit_loss will convert to SGD
    overheads.overheadfunction(forex)
    cash_on_hand.coh_function(forex)
    profit_loss.profit_loss_function(forex)

# run the function
main()