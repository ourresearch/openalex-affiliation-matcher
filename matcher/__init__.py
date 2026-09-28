"""OpenAlex affiliation matcher: candidates -> student p -> chooser.

    retrieve.py    institution cards and the lexical candidate search
    candidates.py  the four candidate generators and the pool
    student.py     the student cross-encoder that scores (string, card) pairs
    decider.py     the chooser's features and its apply step
    gbt.py         the chooser's trees as JSON, evaluated with numpy
    batch.py       the chooser over many strings at once
    score.py       exact match, precision, recall and hallucination against the labels
    training/      reference code that trained the student and the chooser
"""
