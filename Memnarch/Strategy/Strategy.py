from abc import ABCMeta


class Strategy:
    __metaclass__ = ABCMeta

    def check(self):
        raise NotImplementedError

    @classmethod
    def analyze_content(cls, text, kwic):
        """
        Analyze card text for keywords
        :param text: string
        :param kwic: list
        :return: int
        """
        text = text.lower().split()
        score = 0

        for token in text:
            for kw in kwic:
                if kw == token:
                    score = score + 1

        return score
