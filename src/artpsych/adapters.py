"""Model adapters: one interface for every model the experiments use.

Real adapters (AI Verde, local open models) go behind the same interface.
FakeAdapter is deterministic and free, for tests and dry runs.
"""
from __future__ import annotations

import random
from typing import Protocol


class ModelAdapter(Protocol):
    name: str

    def complete(self, prompt: str) -> str:
        """Return the model's text reply to a prompt."""
        ...


class FakeAdapter:
    """Deterministic stand-in model.

    As a speaker it repeats the target message; as a listener it picks the
    option that matches the message, with an optional error rate.
    """

    def __init__(self, name: str = "fake", error_rate: float = 0.0, seed: int = 0):
        self.name = name
        self.error_rate = error_rate
        self._rng = random.Random(seed)

    def complete(self, prompt: str) -> str:
        if "TARGET:" in prompt:
            return prompt.split("TARGET:", 1)[1].splitlines()[0].strip()
        if "MESSAGE:" in prompt and "OPTIONS:" in prompt:
            message = prompt.split("MESSAGE:", 1)[1].splitlines()[0].strip()
            options = [
                line.split(")", 1)[1].strip()
                for line in prompt.split("OPTIONS:", 1)[1].splitlines()
                if ")" in line
            ]
            if message in options and self._rng.random() >= self.error_rate:
                return str(options.index(message) + 1)
            return str(self._rng.randrange(len(options)) + 1)
        return ""
