"""
Problem 1: Zipf's Law Analysis

This script analyzes word frequency distributions across multiple corpora
and generates visualizations to investigate Zipf's Law.
"""

import matplotlib.pyplot as plt
from collections import Counter
import nltk
from datasets import load_dataset
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


def count_word_frequencies_from_text(text):
    """
    Count word frequencies from a text string.

    Args:
        text: Text string to analyze

    Returns:
        Counter object with word frequencies
    """
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


def load_setimes_corpus(language):
    """
    Load SETIMES corpus for a specific language from HuggingFace.

    Args:
        language: 'bg' for Bulgarian or 'tr' for Turkish

    Returns:
        Combined text string from all translations
    """
    print(f"  Loading SETIMES dataset (bg-tr pair)...")
    dataset = load_dataset("community-datasets/setimes", "bg-tr", split="train")

    # Extract all sentences for the specified language
    texts = []
    lang_key = "translation"

    for item in dataset:
        if language in item[lang_key]:
            texts.append(item[lang_key][language])

    # Combine all texts
    combined_text = " ".join(texts)
    return combined_text


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

    # Analyze SETIMES Bulgarian
    print("\nAnalyzing SETIMES (Bulgarian)...")
    setimes_bg_text = load_setimes_corpus("bg")
    setimes_bg_freqs = count_word_frequencies_from_text(setimes_bg_text)
    save_frequency_list(setimes_bg_freqs, "outputs/setimes_bg_frequencies.txt")
    print(f"Saved frequency list to outputs/setimes_bg_frequencies.txt ({len(setimes_bg_freqs)} unique words)")

    # Analyze SETIMES Turkish
    print("\nAnalyzing SETIMES (Turkish)...")
    setimes_tr_text = load_setimes_corpus("tr")
    setimes_tr_freqs = count_word_frequencies_from_text(setimes_tr_text)
    save_frequency_list(setimes_tr_freqs, "outputs/setimes_tr_frequencies.txt")
    print(f"Saved frequency list to outputs/setimes_tr_frequencies.txt ({len(setimes_tr_freqs)} unique words)")


if __name__ == "__main__":
    main()
