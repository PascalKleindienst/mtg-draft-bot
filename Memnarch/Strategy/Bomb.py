from Strategy import Strategy


class Bomb(Strategy):
    def check(self, card):
        """
        Checks for big creature that is difficult to block / remove OR if the card provides somes card advantage 
            OR if the card is a planeswalker (usually they fall into the bomb category)
        :param card: 
        :return: bool
        """
        #
        return self.is_big_creature(card) or self.provides_card_advantage(card) or 'Planeswalker' in card['types']

    def is_big_creature(self, card):
        """
        Checks for a big creature (e.g cmc >= 4 and power/toughness > 4 which is
        difficult to block or hard to remove
        :param card: dict
        :return: bool
        """
        if 'Creature' not in card['types']:
            return False

        abilities = ('Flying', 'Hexproof', 'Shroud', 'Fear', 'Intimidate', 'Indestructible')
        score = self.analyze_content(card['text'], abilities)

        return score > 1 and card['cmc'] >= 4 and (card['power'] + card['toughness']) / 2 >= 4

    def provides_card_advantage(self, card):
        """
        
        :param card: 
        :return: bool
        """
        pass
