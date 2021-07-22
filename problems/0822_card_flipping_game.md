# Card Flipping Game
> Medium

You are given `n` cards, with a positive integer printed on the front and back of each card (possibly different). You can flip any number of cards (possibly zero).

After choosing the front and the back of each card, you will pick each card, and if the integer printed on the back of this card is not printed on the front of any other card, then this integer is **good**.

You are given two integer array fronts and backs where `fronts[i]` and `backs[i]` are the integers printer on the front and the back of the `ith` card respectively.

Return the smallest good and integer after flipping the cards. If there are no good integers, return `0`.

**Note** that a **flip** swaps the front and back numbers, so the value on the front is now on the back and vice versa.

## Examples
```
Input: fronts = [1, 2, 4, 4, 7], backs = [1, 3, 4, 1, 3]
Output: 2
```

## Solution
Thoughts:

If fronts[i] == backs[i], the number cannot be good number if flipped or not. For other numbers, we only need to find the smallest value because we only need to flip that card to make the number as a good number

``` python
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_card = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same_card.add(fronts[i])
        output = min([x for x in fronts + backs if x not in same_card], default=0)
        return output
```