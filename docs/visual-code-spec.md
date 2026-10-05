# Visual Code Spec v0.1

A minimal visual vocabulary that people and AI systems can decode equally well.

Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Design rules

1. **Fit working memory.** Vocabulary of at most 7 symbols (currently 6). Messages of at most 4 symbols (Cowan, 2001).
2. **One symbol, one color, one shape.** Color and shape always travel together. A color-shape pair counts as one object in visual working memory (Luck & Vogel, 1997), so the shape adds redundancy without adding load.
3. **Familiar categories.** Colors use basic color terms people already know (Berlin & Kay, 1969), so nothing needs memorizing.
4. **Colorblind-safe.** Colors come from the Okabe-Ito palette. Shape carries the meaning when color fails.
5. **Neutral ground.** Symbols sit on an untinted background so surrounding color doesn't shift perception.
6. **Flat rendering.** No gradients, textures or outlines.

## Symbols

| Name | Hex | Shape |
|---|---|---|
| blue | `#0072B2` | circle |
| orange | `#E69F00` | square |
| green | `#009E73` | triangle |
| yellow | `#F0E442` | diamond |
| red | `#D55E00` | cross |
| pink | `#CC79A7` | star |

## Backgrounds

| Theme | Hex |
|---|---|
| Light | `#F2F2F2` |
| Dark | `#2B2B2B` |

## Messages

A message is 1 to 4 symbol names separated by spaces, e.g. `blue green red`. Longer messages are invalid in the standard code. Experiments may test longer messages on purpose, to find where human accuracy drops.

## Open questions

- Does accuracy stay equal for people and AI models up to 4 symbols, and diverge after?
- Do different models (and vision vs. text input) decode the code the same way?
- How robust is the code to screen color shifts, compression, and simulated color-vision deficiency?

## References

- Berlin, B., & Kay, P. (1969). *Basic Color Terms.*
- Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences.*
- Luck, S. J., & Vogel, E. K. (1997). The capacity of visual working memory for features and conjunctions. *Nature.*
- Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review.*
- Okabe, M., & Ito, K. (2002). *Color Universal Design.*
