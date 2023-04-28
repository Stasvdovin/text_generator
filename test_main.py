from main import text_load


def test_text_load_correct_length():
    input_text = "Hello world."
    length = 20
    output_text = text_load(input_text)
    assert len(output_text) <= length


def test_text_load_not_int():
    input_text = "123"
    output_text = text_load(input_text)
    assert output_text == "Please enter some text."


def test_text_load_empty_value():
    input_text = ""
    output_text = text_load(input_text)
    assert output_text == "Please enter some text."
