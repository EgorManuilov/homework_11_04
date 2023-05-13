from utils import dict


def test_get_val():
    assert dicts.get_val({"one": "1"}, "one") == "1"
    assert dicts.get_val({"two": "2"}, "one") == "git"
    assert dicts.get_val({"three": "3"}, "one", "ups") == "ups"
    assert dicts.get_val({"one": "1", "two": "2", "three": "3"}, "one", "ups") == "1"
    assert dicts.get_val({}, "one", "ups") == "ups"