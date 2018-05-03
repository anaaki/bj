
class Display:
    """カードを画面に写す"""
    def display_deck(self, final_judge=False):
        display_d = self.dealer.display(final_judge=final_judge)
        display_p = self.player.display()
        return display_d + "\n" + display_p
