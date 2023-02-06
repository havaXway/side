import pytest

from kid import reverse

def test_reverse():
    assert reverse('abc') == 'cba'