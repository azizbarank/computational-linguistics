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


def save_frequency_list(word_counts, output_path):
    """
    Save complete frequency list to a file.

    Args:
        word_counts: Counter object with word frequencies
        output_path: Path to save the frequency list
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for rank, (word, count) in enumerate(word_counts.most_common(), start=1):
            f.write(f"{rank} {word} {count}\n")


def main():
    """
    Main function to run Zipf's Law analysis.
    """
    print("Problem 1: Zipf's Law Analysis")
    print("-" * 40)

    # Analyze KJV Bible
    print("\nAnalyzing King James Bible...")
    kjv_freqs = count_word_frequencies("data/kjv.txt")
    save_frequency_list(kjv_freqs, "outputs/kjv_frequencies.txt")
    print(f"Saved frequency list to outputs/kjv_frequencies.txt ({len(kjv_freqs)} unique words)")

    # Analyze Jungle Book
    print("\nAnalyzing Jungle Book...")
    jb_freqs = count_word_frequencies("data/junglebook.txt")
    save_frequency_list(jb_freqs, "outputs/junglebook_frequencies.txt")
    print(f"Saved frequency list to outputs/junglebook_frequencies.txt ({len(jb_freqs)} unique words)")


if __name__ == "__main__":
    main()
