from __future__ import annotations


def build_question_identifier(stimulus_id, snippet_no, condition_no, question_no) -> str:
    """Build the unique page identifier for a comprehension question.

    The parts are stored as separate columns and can be read back as floats
    (for example when the source table has a stray non-empty bottom row), so
    they are coerced to integers before concatenation to avoid decimal points
    leaking into the identifier.
    """
    return (
        str(int(stimulus_id))
        + str(int(snippet_no))
        + str(int(condition_no))
        + str(int(question_no))
    )
