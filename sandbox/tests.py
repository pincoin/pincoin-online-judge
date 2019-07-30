from django.test import TestCase


class SandboxTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_something_that_will_pass(self) -> None:
        self.assertFalse(False)

    def test_something_that_will_fail(self) -> None:
        self.assertTrue(False)
