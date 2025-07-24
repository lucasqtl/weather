import json
from .feedback_model import Feedback

FEEDBACK_FILE = "feedback_data.json" 

def load_feedbacks():
    try:
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            return [Feedback.from_dict(d) for d in raw_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_feedbacks(feedbacks_list):
    serializable_data = [f.to_dict() for f in feedbacks_list]
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(serializable_data, f, indent=4)
    print("Feedbacks salvos com sucesso!")