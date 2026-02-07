from collections import Counter

def random_forest_vote(predictions):
    output = []
    
    n_samples = len(predictions[0])
    n_trees = len(predictions)

    for i in range(n_samples):
        votes = []
        
        # collect votes from all trees for sample i
        for t in range(n_trees):
            votes.append(predictions[t][i])

        counts = Counter(votes)

        # max frequency
        max_vote = max(counts.values())

        # tie break → smallest label
        winner = min(label for label, c in counts.items() if c == max_vote)

        output.append(winner)

    return output
