import json


with open("rules.json", "r") as f:
    rules = json.load(f)

def analyze_skill_gaps(payload):
   
    tech = payload["technical_score"]
    comm = payload["communication_score"]
    dsa = payload["dsa_score"]
    ml = payload["ml_score"]
    proj = payload["project_explanation_score"]
    weak_kw = payload["weak_keywords"]
    strong_kw = payload["strong_keywords"]

  
    def get_label(score):
        for r in rules["score_ranges"]:
            low, high = map(int, r.split('-')) if '-' in r else (int(r), int(r))
            if low <= score <= high:
                return rules["score_ranges"][r]["label_suffix"]
        return "unknown"

    weaknesses = []
    if dsa <= 4:
        weaknesses.append("DSA fundamentals")
    if proj <= 4:
        weaknesses.append("Project clarity")
    if comm <= 4:
        weaknesses.append("Communication")

  
    for w in weak_kw:
        if w in rules["keyword_topic_map"]:
            weaknesses.append(rules["keyword_topic_map"][w])

    strengths = []
    for s in strong_kw:
        if s in rules["keyword_topic_map"]:
            strengths.append(rules["keyword_topic_map"][s])

    priority_topics = sorted(set(weaknesses))[:2]

    roadmap = {
        "day_1_3": f"{priority_topics[0]} practice" if len(priority_topics) > 0 else "Skill revision",
        "day_4_7": f"{priority_topics[1]} deep dive" if len(priority_topics) > 1 else "Mock interview prep",
        "day_8_10": "ML revision",
        "day_11_14": "Mock interviews"
    }

    
    resources = [
        {"topic": "DSA", "link": "https://www.geeksforgeeks.org/data-structures/"},
        {"topic": "ML", "link": "https://www.coursera.org/learn/machine-learning"}
    ]

    output = {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "priority_topics": priority_topics,
        "roadmap_2_weeks": roadmap,
        "resources": resources
    }

    return output


if __name__ == "__main__":
    sample_input = {
        "technical_score": 6,
        "communication_score": 5,
        "dsa_score": 4,
        "ml_score": 7,
        "project_explanation_score": 3,
        "weak_keywords": ["normalization", "time complexity"],
        "strong_keywords": ["cnn", "regression"]
    }

    result = analyze_skill_gaps(sample_input)
    print(json.dumps(result, indent=2))
