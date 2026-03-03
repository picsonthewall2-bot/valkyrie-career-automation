import re
from collections import Counter

def extract_keywords(job_text):
    # Basic cleaning
    words = re.findall(r'\b[a-zA-Z]+\b', job_text.lower())
    
    # Remove common filler words
    stopwords = set([
        "the","and","to","of","a","in","for","with","on",
        "is","are","as","an","by","be","or","from","at",
        "this","that","will","we","you","our","your"
    ])
    
    filtered = [word for word in words if word not in stopwords and len(word) > 3]
    
    frequency = Counter(filtered)
    
    # Top 20 repeated keywords
    return frequency.most_common(20)


if __name__ == "__main__":
    print("Paste job description below:\n")
    job_input = input()
    
    keywords = extract_keywords(job_input)
    
    print("\nTop Extracted Keywords:\n")
    for word, count in keywords:
        print(f"{word}: {count}")
