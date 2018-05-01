
class Show:
    """カードを画面に写す"""
    def display_deck(self):
        display_d = self.dealer.display()
        display_p = self.player.display()
        return display_d + "\n" + display_p
