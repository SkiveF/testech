import unittest
from main import Auctions


class TestAuctions(unittest.TestCase):
    def setUp(self):
        self.bidders_data = {
            'A': [110, 130],
            'B': [],
            'C': [125],
            'D': [105, 115, 90],
            'E': [132, 135, 140]
        }
        self.reserve_price = 100
        self.auctions = Auctions(
            bidders_data=self.bidders_data, reserve_price=self.reserve_price)
    
    def test_find_eligible_bidders(self):
        result = self.auctions.find_eligible_bidders()
        self.assertEqual(result, ['A', 'C', 'D', 'E'])
    
    def test_find_not_eligible_bidder(self):
        result = self.auctions.find_not_eligible_bidder()
        self.assertEqual(result, (None, self.reserve_price))
    
    def test_winner_auctions(self):
        result = self.auctions.winner_auctions()
        self.assertEqual(result, 'E')
    
    def test_winning_price(self):
        result = self.auctions.winning_price()
        self.assertEqual(result, 130)


if __name__ == '__main__':
    unittest.main()
