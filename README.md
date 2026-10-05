# Artificial Psychology

Tools for building machine perception around human limits: a minimal visual code that people and AI models can read equally well, and experiments that test it.

![The six symbols on a neutral background](docs/symbols-light.png)

## The idea

People hold about four items in working memory. AI models don't have that limit, so in most human-AI communication the machine has an unfair advantage. This project designs a shared code that stays inside human limits:

- **6 symbols**, each a fixed color + shape pair (colorblind-safe Okabe-Ito colors, shape as a backup channel)
- **A neutral background** so color reads the same everywhere
- **Messages of 4 symbols or fewer**, so the whole message fits in working memory

Then it tests whether people and different AI models decode the code equally well, and where that breaks down.

Full spec: [docs/visual-code-spec.md](docs/visual-code-spec.md)

## Quick start

```bash
python3 -m pip install -e ".[render]"
python3 -m unittest discover -s tests
python3 examples/render_symbols.py   # writes docs/symbols-*.png
python3 examples/fake_game.py        # dry-run experiment, no API calls
```

## What's here

| Module | Purpose |
|---|---|
| `artpsych.visual_code` | The symbol set and working-memory rules |
| `artpsych.render` | Draws symbols with Pillow |
| `artpsych.adapters` | One interface for every model; `FakeAdapter` for free, deterministic tests |
| `artpsych.reference_game` | Speaker/listener game with JSON-lines logging |

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md); every commit needs a DCO sign-off (`git commit -s`).

## License

Code: [Apache License 2.0](LICENSE). Spec, docs and symbol images: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Names and logos: see [TRADEMARKS.md](TRADEMARKS.md).
