from frame_types import Type

class SlotQuestions:
    def __init__(self, texts: list, patterns: list):
        # Initialize with lists of texts and patterns to ask for slot value
        self._texts = texts
        self._patterns = patterns
    
    @property
    def texts(self):
        # Getter method for list of texts
        return self._texts
    
    @property
    def patterns(self):
        # Getter method for list of patterns
        return self._patterns


class Slot:
    def __init__(self, name: str, type: Type, questions: SlotQuestions):
        # Initialize slot with a name, data type, and questions to ask
        self._name = name
        self._type = type
        self._questions = questions

    @property
    def name(self):
        # Getter method for slot name
        return self._name

    @property
    def type(self):
        # Getter method for slot data type
        return self._type

    @property
    def questions(self):
        # Getter method for slot questions
        return self._questions
