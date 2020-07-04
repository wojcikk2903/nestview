import pytest

from nestview.nv import nestview


@pytest.fixture
def simple_nested_dict():
    return {"a": 1, "b": {"ba": "21", "bb": "22"}, "c": 3}


@pytest.fixture
def multi_nested_dict():
    return {
        "a": 1,
        "b": {"ba": "21", "bb": {"bba": "221", "bbb": "222", "bbc": "223"}},
        "c": 3,
    }


@pytest.fixture
def dict_list():
    return {"a": 1, "b": ["ba", "bb", "bc"], "c": 3}


def test_single_level_nested_dict(simple_nested_dict):
    assert nestview(simple_nested_dict) == {"a": 1, "b": "{2}", "c": 3}


def test_multi_level_nested_dict_low_level(multi_nested_dict):
    assert nestview(multi_nested_dict) == {"a": 1, "b": "{4}", "c": 3}


def test_multi_level_nested_dict__high_level(multi_nested_dict):
    assert nestview(multi_nested_dict, level=2) == {
        "a": 1,
        "b": {"ba": "21", "bb": "{3}"},
        "c": 3,
    }


def test__list__show_summary(dict_list):
    assert nestview(dict_list, level=1) == {"a": 1, "b": "[3]", "c": 3}


def test_dict_in_list():
    assert nestview(
        {"a": 1, "b": [1, 2, {"ba": "21", "bb": "22"}], "c": 3}, level=1
    ) == {"a": 1, "b": "[4]", "c": 3}


def test_list_top_level():
    assert nestview(["a", {"ba": "21", "bb": "22", "bc": "23"}, "c"], level=1) == [
        "a",
        "{3}",
        "c",
    ]


def test_nested_list():
    assert nestview(["a", ["ba", "bb", "bc"], "c"], level=1) == ["a", "[3]", "c"]


def test_deeply_nested_list():
    assert nestview(["a", ["ba", "bb", ["bca", "bcb", "bcc"]], "c"], level=1) == [
        "a",
        "[5]",
        "c",
    ]


def test_deeply_nested_list_low_level():
    assert nestview(["a", ["ba", "bb", ["bca", "bcb", "bcc"]], "c"], level=2) == [
        "a",
        ["ba", "bb", "[3]"],
        "c",
    ]


def test_sets():
    assert nestview({1, 2, 3}) == {1, 2, 3}


def test_sets_and_tuples():
    assert nestview({1, 2, (4, 5, 6)}) == {1, 2, "(3)"}
    assert nestview((1, 2, {4, 5, 6})) == (1, 2, "set(3)")


def test__short_dicts__show_literal():
    pass
