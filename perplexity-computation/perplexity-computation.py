import math
def perplexity(prob_distributions, actual_tokens):
    prob_li=[]
    for i in range(len(actual_tokens)):
        row = prob_distributions[i]
        idx = actual_tokens[i]
        prob = row[idx]
        prob_li.append(prob)
    log_sum=0
    for p in prob_li:
        log_sum+=math.log(p) 
    cross_entropy = -log_sum/len(prob_li)
    perplexity_value = math.exp(cross_entropy)
    return perplexity_value
