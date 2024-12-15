class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if len(deck) < 3:
            return deck

        deck.sort()
        queue = [deck[-1]]
        q_pos = 0
        # for the n-th largest card in the deck, the last n elements in queue in reverse
        #   will represent an ordering of a deck consisting of the n largest cards, which
        #   will reveal said cards in increasing order
        for card in deck[-2::-1]:
            card2 = queue[q_pos]
            queue.append(card2)
            queue.append(card)
            q_pos += 1        
        # return reversed
        return queue[-1:-len(deck)-1:-1]
