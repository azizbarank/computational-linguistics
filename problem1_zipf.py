"""
Problem 1: Zipf's Law Analysis

This script analyzes word frequency distributions across multiple corpora
and generates visualizations to investigate Zipf's Law.
"""

import matplotlib.pyplot as plt
from collections import Counter
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
    with open(output_path, "w", encoding="utf-8") as f:
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
    print("  Loading SETIMES dataset (bg-tr pair)...")
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


def plot_frequency_distribution(freq_file, corpus_name, output_file):
    """
    Create linear and log-log plots for a corpus.

    Args:
        freq_file: Path to frequency list file
        corpus_name: Name of the corpus for the title
        output_file: Path to save the plot
    """
    # Read frequency data
    ranks = []
    freqs = []

    with open(freq_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            rank = int(parts[0])
            freq = int(parts[-1])
            ranks.append(rank)
            freqs.append(freq)

    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Linear plot
    ax1.plot(ranks, freqs)
    ax1.set_xlabel("Rank")
    ax1.set_ylabel("Frequency")
    ax1.set_title(f"{corpus_name} - Linear Scale")
    ax1.grid(True)

    # Log-log plot
    ax2.loglog(ranks, freqs)
    ax2.set_xlabel("Rank (log)")
    ax2.set_ylabel("Frequency (log)")
    ax2.set_title(f"{corpus_name} - Log-Log Scale")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"  Saved plot to {output_file}")


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
    print(
        f"Saved frequency list to outputs/kjv_frequencies.txt ({len(kjv_freqs)} unique words)"
    )

    # Analyze Jungle Book
    print("\nAnalyzing Jungle Book...")
    jb_freqs = count_word_frequencies("data/junglebook.txt")
    save_frequency_list(jb_freqs, "outputs/junglebook_frequencies.txt")
    print(
        f"Saved frequency list to outputs/junglebook_frequencies.txt ({len(jb_freqs)} unique words)"
    )

    # Analyze SETIMES Bulgarian
    print("\nAnalyzing SETIMES (Bulgarian)...")
    setimes_bg_text = load_setimes_corpus("bg")
    setimes_bg_freqs = count_word_frequencies_from_text(setimes_bg_text)
    save_frequency_list(setimes_bg_freqs, "outputs/setimes_bg_frequencies.txt")
    print(
        f"Saved frequency list to outputs/setimes_bg_frequencies.txt ({len(setimes_bg_freqs)} unique words)"
    )

    # Analyze SETIMES Turkish
    print("\nAnalyzing SETIMES (Turkish)...")
    setimes_tr_text = load_setimes_corpus("tr")
    setimes_tr_freqs = count_word_frequencies_from_text(setimes_tr_text)
    save_frequency_list(setimes_tr_freqs, "outputs/setimes_tr_frequencies.txt")
    print(
        f"Saved frequency list to outputs/setimes_tr_frequencies.txt ({len(setimes_tr_freqs)} unique words)"
    )

    # Create plots
    print("\nCreating plots...")
    plot_frequency_distribution(
        "outputs/kjv_frequencies.txt", "KJV Bible", "outputs/plots/kjv_zipf.png"
    )
    plot_frequency_distribution(
        "outputs/junglebook_frequencies.txt",
        "Jungle Book",
        "outputs/plots/junglebook_zipf.png",
    )
    plot_frequency_distribution(
        "outputs/setimes_bg_frequencies.txt",
        "SETIMES Bulgarian",
        "outputs/plots/setimes_bg_zipf.png",
    )
    plot_frequency_distribution(
        "outputs/setimes_tr_frequencies.txt",
        "SETIMES Turkish",
        "outputs/plots/setimes_tr_zipf.png",
    )


if __name__ == "__main__":
    main()
