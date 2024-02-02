class Auctions:
    """_summary_"""

    def __init__(self, bidders_data, reserve_price):
        self.bidders_data = bidders_data
        self.reserve_price = reserve_price

    def find_eligible_bidders(self):
        eligible_bider = [
            bidder
            for bidder, bids in self.bidders_data.items()
            if bids and max(bids) >= self.reserve_price
        ]
        return eligible_bider

    def find_not_eligible_bidder(self):
        return None, self.reserve_price

    def winner_auctions(self):
        eligible_bidders = self.find_eligible_bidders()
        if eligible_bidders:
            eligible_bidders.sort(
                key=lambda bidder: max(self.bidders_data[bidder]), reverse=True
            )
            winner = eligible_bidders[0]
            return winner
        else:
            return None

    def winning_price(self):
        winner = self.winner_auctions()
        if winner:
            winning_price_ = max(
                max(bids)
                for bidder, bids in self.bidders_data.items()
                if bidder != winner and bids and max(bids) >= self.reserve_price
            )

            return winning_price_
        else:
            return 0


if __name__ == "__main__":
    bidders_data = {
        "A": [110, 130],
        "B": [],
        "C": [125],
        "D": [105, 115, 90],
        "E": [132, 135, 140],
    }

    reserve_price = 100
    auctions = Auctions(bidders_data=bidders_data, reserve_price=reserve_price)
    winner_x = auctions.winner_auctions()
    winning_price = auctions.winning_price()
    print("L'enchère gagnante est :", winner_x)
    print("Le prix de l'enchère gagnante est de:", winning_price)
