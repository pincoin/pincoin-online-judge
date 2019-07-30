from django.test import TestCase

from . import sandbox


class SandboxTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sandbox_run_date(self) -> None:
        self.assertEquals(sandbox.examine(['/bin/date', ]), 0)
