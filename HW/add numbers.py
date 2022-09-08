def calculate_eight_year_gain(fname):
    '''
    Calculates the stock gain from 9-1-2000 Open price to 3-7-2008 close price for
    10 shares of stock
    input:
        fname - str, aapl stock price filename
    output:
        gain - float, monetary gain during period
    '''
    # open file
    with open(fname) as f:
        # read in lines
        lines = f.readlines()
        # get 9-1-2000 open price
        open_price = float(lines[0].split(',')[1])
        # get 3-7-2008 close price
        close_price = float(lines[-1].split(',')[4])
    # calculate gain
    gain = (close_price - open_price) * 10
    return gain