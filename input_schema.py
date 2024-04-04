INPUT_SCHEMA = {
    "query": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Can you provide information about the history of artificial intelligence?"]
    },
    "paragraphs": {
        'datatype': 'STRING',
        'required': True,
        'shape': [10],  # Allow multiple paragraphs
        'example': ["Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior.", "The history of AI can be traced back to ancient civilizations", "In the 20th century, the formalization of the concepts behind AI began to take shape.","Alan Turing proposed the Turing Test in 1950 as a way to evaluate a machine's ability to exhibit intelligent behavior", "The field experienced significant ups and downs, known as 'AI winters,' where funding and interest in AI research waned.", "However, breakthroughs in machine learning, particularly deep learning, have revitalized the field in recent years", "Today, AI is applied in various domains, including healthcare, finance, transportation, and entertainment.", "It powers virtual assistants, recommendation systems, autonomous vehicles, and much more.", "Looking ahead, AI holds the promise of revolutionizing industries and reshaping society.", "However, it also raises ethical and societal concerns that must be addressed"]  # Example list of paragraphs
    }
}
