# Raw data
def analyze_skills(input_data: dict) -> dict:
    """
    Mock engine that simulates logic based on the
    example input/output format s.
    """
    print(f"Mock Engine Received: {input_data}")
    
    # Check if a specific keyword is present to simulate a different response
    if "normalization" in input_data.get("weak_keywords", []):
        return {
          "strengths": ["ML basics", "CNN theory"],
          "weaknesses": ["Time complexity", "Project clarity", "Data Normalization"],
          "priority_topics": ["DSA fundamentals", "Explainability", "Normalization Techniques"],
          "roadmap_2_weeks": {
            "day_1_3": "DSA basics + time complexity",
            "day_4_7": "Project explanation practice",
            "day_8_10": "Normalization and feature scaling",
            "day_11_14": "Mock interviews"
          },
          "resources": [
            {"topic": "DSA", "link": "https://example.com/dsa"},
            {"topic": "Normalization", "link": "https://example.com/ml-normalization"}
          ]
        }
    
    # Default mock response
    return {
      "strengths": ["Basic Python", "Git"],
      "weaknesses": ["Advanced Algorithms", "System Design"],
      "priority_topics": ["Data Structures", "API Design"],
      "roadmap_2_weeks": {
        "day_1_3": "Review Arrays and Strings",
        "day_4_7": "Study Hashmaps and Trees",
        "day_8_10": "REST API principles",
        "day_11_14": "System Design basics"
      },
      "resources": [
        {"topic": "Data Structures", "link": "https://example.com/ds"},
        {"topic": "API Design", "link": "https://example.com/api"}
      ]
    }