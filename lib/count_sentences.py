#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value if isinstance(value, str) else ''
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            self._value = ''
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        import re
        # Split the string on sentence-ending punctuation marks
        sentence_endings = re.split(r'[.!?]', self.value)
        # Filter out empty strings from the resulting list
        sentences = [s.strip() for s in sentence_endings if s.strip()]
        return len(sentences)
