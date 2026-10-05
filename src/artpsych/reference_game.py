"""Reference game: a speaker describes a target, a listener picks it out.

Each round is logged as one JSON line with the models, prompts, replies,
and settings, so runs are reproducible and auditable.
"""
from __future__ import annotations

import json
import random
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from .adapters import ModelAdapter
from .visual_code import MAX_MESSAGE_LENGTH, SPEC_VERSION, SYMBOLS, format_message

SPEAKER_PROMPT = (
    "You are describing a sequence of symbols to a partner using only these "
    "names: {vocab}.\nReply with the names only, separated by spaces.\n"
    "TARGET: {target}\n"
)
LISTENER_PROMPT = (
    "Your partner described one of the options below.\n"
    "MESSAGE: {message}\nOPTIONS:\n{options}\nReply with the option number only.\n"
)


@dataclass
class Round:
    round_id: int
    speaker: str
    listener: str
    message_length: int
    target: str
    options: list[str]
    message: str
    choice: int | None
    correct: bool
    spec_version: str = SPEC_VERSION


def _random_message(rng: random.Random, length: int) -> str:
    return format_message([rng.choice(SYMBOLS) for _ in range(length)])


def play_round(speaker: ModelAdapter, listener: ModelAdapter, *, round_id: int,
               message_length: int, n_options: int, rng: random.Random) -> Round:
    if not 1 <= message_length <= MAX_MESSAGE_LENGTH + 2:
        raise ValueError("message_length out of range")
    options: list[str] = []
    while len(options) < n_options:
        m = _random_message(rng, message_length)
        if m not in options:
            options.append(m)
    target = rng.choice(options)
    vocab = ", ".join(s.name for s in SYMBOLS)
    message = speaker.complete(SPEAKER_PROMPT.format(vocab=vocab, target=target)).strip()
    numbered = "\n".join(f"{i + 1}) {o}" for i, o in enumerate(options))
    reply = listener.complete(LISTENER_PROMPT.format(message=message, options=numbered))
    try:
        choice = int(reply.strip().split()[0])
    except (ValueError, IndexError):
        choice = None
    correct = choice is not None and 1 <= choice <= len(options) and options[choice - 1] == target
    return Round(round_id, speaker.name, listener.name, message_length, target,
                 options, message, choice, correct)


def run(speaker: ModelAdapter, listener: ModelAdapter, *, rounds: int = 20,
        message_length: int = 2, n_options: int = 4, seed: int = 0,
        log_path: str | Path | None = None) -> list[Round]:
    rng = random.Random(seed)
    results = []
    log = open(log_path, "a", encoding="utf-8") if log_path else None
    try:
        for i in range(rounds):
            r = play_round(speaker, listener, round_id=i, message_length=message_length,
                           n_options=n_options, rng=rng)
            results.append(r)
            if log:
                log.write(json.dumps({**asdict(r), "seed": seed, "time": time.time()}) + "\n")
    finally:
        if log:
            log.close()
    return results


def accuracy(results: list[Round]) -> float:
    return sum(r.correct for r in results) / len(results) if results else 0.0
