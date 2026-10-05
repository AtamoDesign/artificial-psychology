import unittest

from artpsych.adapters import FakeAdapter
from artpsych.reference_game import accuracy, run
from artpsych.visual_code import (
    MAX_MESSAGE_LENGTH, MAX_VOCABULARY, SYMBOLS, format_message, parse_message,
)


class VisualCodeTests(unittest.TestCase):
    def test_vocabulary_fits_working_memory(self):
        self.assertLessEqual(len(SYMBOLS), MAX_VOCABULARY)

    def test_names_colors_and_shapes_are_unique(self):
        for field in ("name", "hex", "shape"):
            values = [getattr(s, field) for s in SYMBOLS]
            self.assertEqual(len(values), len(set(values)), field)

    def test_parse_round_trips(self):
        msg = "blue green red"
        self.assertEqual(format_message(parse_message(msg)), msg)

    def test_rejects_unknown_symbol(self):
        with self.assertRaises(ValueError):
            parse_message("blue teal")

    def test_rejects_messages_over_limit(self):
        with self.assertRaises(ValueError):
            parse_message(" ".join(["blue"] * (MAX_MESSAGE_LENGTH + 1)))


class ReferenceGameTests(unittest.TestCase):
    def test_perfect_fake_pair_is_accurate(self):
        results = run(FakeAdapter("a"), FakeAdapter("b"), rounds=30, seed=1)
        self.assertEqual(accuracy(results), 1.0)

    def test_runs_are_reproducible(self):
        a = run(FakeAdapter("a"), FakeAdapter("b", error_rate=0.3, seed=2), rounds=30, seed=3)
        b = run(FakeAdapter("a"), FakeAdapter("b", error_rate=0.3, seed=2), rounds=30, seed=3)
        self.assertEqual([r.correct for r in a], [r.correct for r in b])


if __name__ == "__main__":
    unittest.main()
