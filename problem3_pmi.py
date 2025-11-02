"""
Problem 3: PMI (Pointwise Mutual Information) Analysis

This script calculates PMI for word pairs in a corpus and finds
the highest and lowest scoring pairs.
"""

import math
from collections import Counter
from utils import load_corpus


def calculate_pmi(corpus_path, min_word_count=10):
    """
    Calculate PMI for all word pairs in the corpus.

    PMI formula: log[C(w1,w2) * N / (C(w1) * C(w2))]
    """
    # Load and tokenize corpus
    text = load_corpus(corpus_path)
    words = text.split()

    # Count individual word frequencies
    word_counts = Counter(words)

    # Filter out words that appear less than min_word_count times
    filtered_words = [w for w in words if word_counts[w] >= min_word_count]

    print(f"Total words: {len(words)}")
    print(f"Words after filtering (count >= {min_word_count}): {len(filtered_words)}")
    print(f"Unique words after filtering: {len(set(filtered_words))}")

    # Count bigrams (successive word pairs)
    bigrams = []
    for i in range(len(filtered_words) - 1):
        bigrams.append((filtered_words[i], filtered_words[i + 1]))

    bigram_counts = Counter(bigrams)

    # Total number of words (N in the formula)
    N = len(filtered_words)

    # Calculate PMI for each bigram
    pmi_scores = {}
    for (w1, w2), bigram_count in bigram_counts.items():
        c_w1 = word_counts[w1]
        c_w2 = word_counts[w2]
        c_w1_w2 = bigram_count

        # PMI = log[C(w1,w2) * N / (C(w1) * C(w2))]
        pmi = math.log((c_w1_w2 * N) / (c_w1 * c_w2))
        pmi_scores[(w1, w2)] = pmi

    return pmi_scores


def main():
    corpus_path = "data/kjv.txt"

    print("Calculating PMI for word pairs...")
    print()

    pmi_scores = calculate_pmi(corpus_path)

    # Sort by PMI score
    sorted_pmi = sorted(pmi_scores.items(), key=lambda x: x[1], reverse=True)

    # Top 20 highest PMI
    print("\n=== Top 20 Highest PMI Pairs ===")
    for (w1, w2), pmi in sorted_pmi[:20]:
        print(f"{w1:20} {w2:20} PMI: {pmi:.4f}")

    # Top 20 lowest PMI
    print("\n=== Top 20 Lowest PMI Pairs ===")
    for (w1, w2), pmi in sorted_pmi[-20:]:
        print(f"{w1:20} {w2:20} PMI: {pmi:.4f}")


if __name__ == "__main__":
    main()
