# demonstrating `ShoppingList.__repr__`


def strike(text):
    """Renders string with strike-through characters through it.

    `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'

    Notes
    -----
    \u0336 is a special strike-through unicode character; it
    is not unique to Python."""
    return "".join("\u0336{}".format(c) for c in text)


class ShoppingList:
    """
    Shopping list
    """

    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self) -> str:
        """
        Returns formatted shopping list as a string with
        purchased items crossed out

        Returns
        -------
        str
        """

        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            # You wont find the • character on your keyboard. I simply
            # googled "unicode bullet point" and copied/pasted it here.
        return "• " + "\n• ".join(remaining_items + purchased_items)

    def add_new_items(self, items):
        self._needed.update(items)

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)

    def __add__(self, other):
        """ Add the unpurchased and purchased items from another shopping
            list to the present one.

            Parameters
            ----------
            other : ShoppingList
                The shopping list whose items we will add to the present one.
            Returns
            -------
            ShoppingList
                The present shopping list, with items added to it."""
                
        new_list = ShoppingList([])
        # populate new_list with items from `self` and `other`
        for l in [self, other]:
            new_list.add_new_items(l._needed)

            # add purchased items to list, then mark as purchased
            new_list.add_new_items(l._purchased)
            new_list.mark_purchased_items(l._purchased)
        return new_list



if __name__ == "__main__":
    shopping = ShoppingList(["grapes", "delmonte pineapples", "lemons"])
    shopping.mark_purchased_items(["grapes"])
    shopping.add_new_items(["Bananas"])
    # print(shopping.__repr__())
    print(shopping)
