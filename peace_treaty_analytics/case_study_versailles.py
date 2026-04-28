from analyzer import TreatyAnalyzer

def run_versailles_study():
    # Sample clauses from Versailles Treaty (simplified)
    versailles_clauses = [
        "Germany accepts the responsibility of Germany and her allies for causing all the loss and damage.",
        "The Allied and Associated Governments affirm and Germany accepts the responsibility.",
        "The German Army must be demobilised and reduced to 100,000 men.",
        "Germany is forbidden to maintain or construct any fortifications."
    ]

    analyzer = TreatyAnalyzer()
    print("Analyzing Versailles Treaty Clauses...")
    results = []
    for clause in versailles_clauses:
        res = analyzer.classify_clauses(clause)[0]
        results.append(res)
        print(f"Clause: {res['clause'][:50]}... -> Label: {res['label']} (Score: {res['score']:.2f})")

    # Heuristic effectiveness score
    # Punitive, Reparations and Symbolic clauses often lead to future conflict (scoring badly in this context)
    bad_clauses = sum(1 for r in results if r['label'] in ['punitive', 'reparations', 'symbolic'])
    effectiveness_score = max(0, 100 - (bad_clauses * 25))

    print(f"\nOverall Treaty Effectiveness Score: {effectiveness_score}/100")
    if effectiveness_score < 50:
        print("Conclusion: High risk of future conflict due to punitive nature.")

if __name__ == "__main__":
    run_versailles_study()
