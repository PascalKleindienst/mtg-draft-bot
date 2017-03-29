from Strategy import Strategy


class Bomb(Strategy):
    def __init__(self):
        self.abilities = ('Flying', 'Trample', 'Hexproof', 'Fear', 'Intimidate')

    def check(self, card):
        score = self.analyze_content(card['text'], self.abilities)

        return score > 0
