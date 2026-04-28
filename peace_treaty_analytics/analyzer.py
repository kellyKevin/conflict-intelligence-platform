import spacy
from transformers import pipeline

class TreatyAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        # Using a zero-shot classifier as a simple way to classify clauses
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def classify_clauses(self, text):
        doc = self.nlp(text)
        clauses = [sent.text for sent in doc.sents]

        labels = ["preventive", "symbolic", "punitive", "administrative", "reparations"]
        results = []

        for clause in clauses:
            res = self.classifier(clause, candidate_labels=labels)
            results.append({
                "clause": clause,
                "label": res['labels'][0],
                "score": res['scores'][0]
            })

        return results

if __name__ == "__main__":
    analyzer = TreatyAnalyzer()
    sample_text = "The parties shall refrain from the use of force. We gathered here to express our mutual love for peace."
    print(analyzer.classify_clauses(sample_text))
