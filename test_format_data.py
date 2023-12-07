# test_format_data.py
import pytest

from format_data import format_data_for_display, format_data_for_excel


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def test_format_data_for_excel(example_people_data):
    output = (
        "given,family,title\n"
        "Alfonsa,Ruiz,Senior Software Engineer\n"
        "Sayid,Khan,Project Manager\n"
    )

    assert format_data_for_excel(example_people_data) == output
