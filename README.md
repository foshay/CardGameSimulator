# CardGameSimulator
I had a weird dream of a card game where you drew cards to try and make pairs from a shuffled collection of two decks of cards.


From running the simulation we got the following results:
Lowest number of Cards: 1
Highest number of Cards: 520
Average number of Cards: 51.9273
Median number of Cards: 36.0
Mean Average Deviation: 37.89149236000179
Standard Deviation: 51.12403754311673

So it looks like the odds would have been in my favor of surviving the matching game due to the average being under 52 cards (One deck of cards).

# Notes
I know this is a slow way to do this and creating so many objects is unneeded in a simulation as simple as this, but I wanted to make this as much like a "card drawing game" as possible without a gui lol.

# Notes part 2
I got 'the itch' so implemented the dull way of calculating this via lists instead. Here are the results after running 10 sims of 10,000 sims (100,000 sims total):
Dull:
Time taken: 12.682347130775451
Fancy:
Time taken: 20.735045433044434
Dull is 38.84% faster than Fancy