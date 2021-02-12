from collections import Counter
import re

def top_3_words(text):
    words = re.findall(r"[\w']+", text.lower().replace('_', ' '))
    top_3 = Counter(word for word in words if re.findall(r'\w+', word))
    return [word[0] for word in top_3.most_common(3)]