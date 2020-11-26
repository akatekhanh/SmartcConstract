from ..life_cycle import LifeCycle
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestLifeCycle(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(LifeCycle, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")
