from unittest import TestCase

from django.test import override_settings

from graph_app.management.commands.give_me_the_odds import compute_odds
from graph_app.utils.file import read_json_file


class TestCases(TestCase):
    @override_settings(DEBUG=True)
    def test_case(self):
        for case in range(1, 5):
            with self.subTest(case=case):
                computed_odd = compute_odds(
                    f"./tests/cases/case{case}/millennium-falcon.json",
                    f"./tests/cases/case{case}/empire.json",
                )
                answer_file = read_json_file(f"./tests/cases/case{case}/answer.json")
                assert computed_odd == answer_file["odds"]
