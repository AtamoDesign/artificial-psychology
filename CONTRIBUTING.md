# Contributing

Thanks for helping. This project welcomes code, experiments, docs and bug reports.

## Sign your commits (DCO)

Every commit must carry a Developer Certificate of Origin sign-off:

```bash
git commit -s -m "Your message"
```

This adds `Signed-off-by: Your Name <you@example.com>` and certifies the [Developer Certificate of Origin 1.1](https://developercertificate.org/): that you wrote the contribution or otherwise have the right to submit it under this project's license.

## License of contributions

Contributions are accepted under the project's licenses: Apache 2.0 for code, CC BY 4.0 for docs and images. By contributing you agree your work may be used, modified and redistributed under those terms, including in other projects.

## Rules for what you submit

- **You must have the rights.** Don't submit code copied from projects with incompatible licenses.
- **Employer work:** don't submit code written for an employer unless they've allowed it.
- **AI-assisted code is fine** if you've reviewed it, understand it, and can vouch that it doesn't reproduce someone else's licensed code.
- **No personal data.** Never commit participant data, API keys, or anything identifying a person. Experiment logs in pull requests must be synthetic or fully anonymized.

## Workflow

1. Open an issue first for anything larger than a small fix.
2. Keep pull requests small and focused.
3. Run the tests before submitting: `python3 -m unittest discover -s tests`
4. New behavior needs a test. `FakeAdapter` keeps tests free and deterministic.

## Code of conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
