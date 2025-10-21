"""
Problem 1: Zipf's Law Analysis

This script analyzes word frequency distributions across multiple corpora
and generates visualizations to investigate Zipf's Law.
"""

import matplotlib.pyplot as plt
from collections import Counter
import nltk
from utils import load_corpus


def count_word_frequencies(corpus_path):
    """
    Count word frequencies in a corpus.

    Args:
        corpus_path: Path to the corpus file

    Returns:
        Counter object with word frequencies
    """
    text = load_corpus(corpus_path)

    # Split on whitespace to get tokens
    words = text.split()

    # Count frequencies
    word_counts = Counter(words)

    return word_counts


def main():
    """
    Main function to run Zipf's Law analysis.
    """
    print("Problem 1: Zipf's Law Analysis")
    print("-" * 40)

    # Load and analyze KJV Bible
    print("\nAnalyzing King James Bible...")
    kjv_freqs = count_word_frequencies("data/kjv.txt")

    # Get most common words
    most_common = kjv_freqs.most_common(20)

    print("\nTop 20 most frequent words:")
    for word, count in most_common:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
