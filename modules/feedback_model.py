class Feedback:
    def __init__(self, location, condition, temperature, comment=''):
        self.location = location
        self.condition = condition
        self.temperature = temperature
        self.comment = comment

    def __str__(self):
        return f"Feedback: {self.location} {self.condition} {self.temperature} {self.comment}"
    
    def to_dict(self):
        return {
            "location": self.location,
            "condition": self.condition,
            "temperature": self.temperature,
            "comment": self.comment,
        }

    @classmethod
    def from_dict(cls, data_dict):
        

        return cls(
            location=data_dict['location'],
            condition=data_dict['condition'],
            temperature=data_dict['temperature'],
            comment=data_dict.get('comment', '')
        )