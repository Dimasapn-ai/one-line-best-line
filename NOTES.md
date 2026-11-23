# One Line, Best Line — entry notes

## Final line (116 characters)

> The cat pays no rent, fears no god, and sleeps sixteen hours a day: evolution peaked, and it's asleep on my laundry.

## Candidates drafted

1. **The cat pays no rent, fears no god, and sleeps sixteen hours a day: evolution peaked, and it's asleep on my laundry.** ← winner
2. My goldfish remembers nothing for more than three seconds, so every lap of his bowl is a world tour and every dinner is a surprise party.
3. Grandma has beaten the same video game boss 400 times and still calls him "that rude young man."
4. I taught my dog to fetch my slippers; now he hides them first so he can look like a hero.
5. A toddler with a marker is just a tiny landlord inspecting the walls he now owns.
6. The octopus has three hearts, and still not one of them has ever had to sit through a Monday meeting.
7. My houseplant has survived three years of my care, which makes it either immortal or too afraid to die in front of me.
8. My smart home has forty devices, and when the internet dies I live in a very expensive cave.
9. I finally beat my fear of heights: now I panic at sea level like everyone else.
10. I asked the mirror who was fairest, and it showed me a loading spinner.
11. My alarm clock and I play the same game every morning: it shouts, and I surrender five minutes at a time.
12. Somewhere right now, a vending machine is judging your snack choices harder than your doctor does.

## Why the winner wins

Against the judge's brief, in its own order:

- **Stops the scroll in the first few words.** "The cat pays no rent, fears no god" is a triple beat of escalating absurdity that opens mid-thought — a reader who was leaving stays to see where the list goes.
- **Genuinely entertaining, not merely clever.** It is funny on first contact with no explanation needed: everyone knows this cat. The goldfish line (#2) is more delightful than funny and needs a beat to set up; the mirror line (#10) is a witticism that stays clever rather than landing.
- **Lands in a single sentence with a turn at the end.** The colon pivots from the cat's lifestyle to a mock-grand conclusion — "evolution peaked" — and then undercuts it with the concrete, deflating image "asleep on my laundry." Setup, turn, punch, all in one sentence.
- **Fresh.** The rent/god/sleep list and the evolution framing are a combination a reader has not met a hundred times; it avoids the standard one-liner templates (no "my therapist says," no Wi-Fi-down-with-family setup).
- **Short.** At 116 characters it is well under the 240 cap, and since exact ties break toward the smaller text, its brevity is a competitive edge rather than a compromise — nothing in it is filler.

## Program

`main.py` (Python standard library only) embeds the line as a constant and
writes it, plus a trailing newline, to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR` when set, else `/output`), creating the directory if
needed. Output was verified under simulated server conditions — read-only
working directory, empty environment (`env -i`), writable output stand-in:
exit 0 on both runs, byte-identical `entry.txt` (117 bytes), 116 characters
of text, exactly one line, nothing written to the working directory.
