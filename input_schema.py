INPUT_SCHEMA = {
    "query": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Query"]
    },
    "paragraphs": {
        'datatype': 'STRING',
        'required': True,
        'shape': [None],  # Allow multiple paragraphs
        'example': ["Paragraph1", "Paragraph2", "Paragraph3"]  # Example list of paragraphs
    }
}
