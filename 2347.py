class PokerHand:
    def __init__(self, numbers, suits):
        self.numbers = numbers
        self.suits = suits
    
    def get_hand_rank(self):
        #checks for flush
        if len(set(self.suits)) == 1:
            return "Flush"

        #checks for three of a kind
        counts = [0] * 14
        for num in self.numbers:
            counts[num] += 1
        if 3 in counts or 4 in counts or 5 in counts:
            return "Three of a Kind"

        #check for pair(two cards with the same number)
        if 2 in counts:
            return "Pair"
        
        return "High Card"

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # I AM USING CHATGPT TO HELP ME CREATE A STARTING CODE TO CREAT A CLASS.
        # CHAT DOES IS NOT PERFECT, BUT IT'S AN AWESOME START...
        # I AM AMAZED. 
        init = PokerHand(ranks, suits)
        return init.get_hand_rank()