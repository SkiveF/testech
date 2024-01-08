def auctions(bidders_data, reserve_price):
    """this function is an auction simulation.
       It takes two parameters: the bids and the default price.
    """
    # filter eligible bidder which offer is >= reserve_price.
    eligible_bidders = [bidder for bidder, bids in bidders_data.items() if
                        bids and max(bids) >= reserve_price]
    
    # if offer of eligible_bidders <= reserve_price
    if not eligible_bidders:
        return None, reserve_price
    
    # sort bidders according to their offer
    eligible_bidders.sort(key=lambda bidder: max(bidders_data[bidder]),
                          reverse=True)
    winner = eligible_bidders[0]
    winning_price = max(bidder for bidder, bids in bidders_data.items() if
                        bidder != winner and bids and max(
                            bids) >= reserve_price)
    # result
    return winner, winning_price


if __name__ == '__main__':
    # usage case
    bidders_data = {
        'A': [110, 130],
        'B': [],
        'C': [125],
        'D': [105, 115, 90],
        'E': [132, 135, 140]
    }
    
    reserve_price = 100
    
    winner, winning_price = auctions(bidders_data, reserve_price)
    
    print("L'enchère gagnante est :", winner)
    print("Le prix de l'enchère gagnante est de:", winning_price)
