from ..day3 import Day3
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestDay3(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(Day3, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")
