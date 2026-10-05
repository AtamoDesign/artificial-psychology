"""Dry run of the reference game with fake models: no API calls, no cost.

Shows the experiment shape: accuracy by message length.
"""
from artpsych.adapters import FakeAdapter
from artpsych.reference_game import accuracy, run

speaker = FakeAdapter("fake-speaker")
listener = FakeAdapter("fake-listener", error_rate=0.15, seed=7)
for length in range(1, 7):
    results = run(speaker, listener, rounds=100, message_length=length, seed=length)
    print(f"message length {length}: accuracy {accuracy(results):.2f}")
