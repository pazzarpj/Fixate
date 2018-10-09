from fixate.core.common import TestClass
from fixate.core.ui import user_ok, user_info
from fixate.core.checks import *

__version__ = "1"


class SimpleTest(TestClass):
    """Simple passing test"""
    retry_type = TestClass.RT_FAIL

    def test(self):
        chk_true(False, "It is True!")


TEST_SEQUENCE = [SimpleTest()]