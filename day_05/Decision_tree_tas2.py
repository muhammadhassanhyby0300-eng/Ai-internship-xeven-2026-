def loan_approval(age, income, credit_score):
    decision_path = []
    
    if age < 18:
        decision_path.append("Age < 18 → Reject")
        return "Rejected", decision_path
    else:
        decision_path.append("Age ≥ 18")
    
    if income < 30000:
        decision_path.append("Income < 30000 → Reject")
        return "Rejected", decision_path
    else:
        decision_path.append("Income ≥ 30000")
    
    if credit_score < 600:
        decision_path.append("Credit Score < 600 → Reject")
        return "Rejected", decision_path
    else:
        decision_path.append("Credit Score ≥ 600 → Approve")
        return "Approved", decision_path

# Example run
result, path = loan_approval(age=25, income=40000, credit_score=650)
print("Decision:", result)
print("Path:", " → ".join(path))
