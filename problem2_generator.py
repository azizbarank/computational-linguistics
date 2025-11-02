"""
Problem 2: Random Text Generation using N-gram Models

This script implements a "Dissociated Press" text generator using n-gram models.
"""

import random
from ngram_model import BasicNgram, goodturing_estimator
from utils import load_corpus


def generate_text(ngram_model, num_words=100):
    """
    Generate text using an n-gram model.

    Args:
        ngram_model: Trained BasicNgram instance
        num_words: Number of words to generate

    Returns:
        Generated text as a string
    """
    # Start with a random context from available contexts
    contexts = ngram_model.contexts()
    # Filter out contexts with start symbols only
    valid_contexts = [c for c in contexts if c[0] != ngram_model._start_symbol]

    if not valid_contexts:
        # Fallback to start symbol context
        context = tuple([ngram_model._start_symbol] * (ngram_model._n - 1))
    else:
        context = random.choice(valid_contexts)

    generated = []

    for _ in range(num_words):
        # Get probability distribution for current context
        prob_dist = ngram_model[context]

        # Generate next word
        next_word = prob_dist.generate()

        # Stop if we hit end symbol
        if next_word == ngram_model._end_symbol:
            break

        generated.append(next_word)

        # Update context (shift window)
        context = context[1:] + (next_word,)

    return " ".join(generated)


def main():
    """
    Main function to run n-gram text generation.
    """
    print("Problem 2: N-gram Text Generation")
    print("-" * 40)

    # Load corpus
    print("\nLoading corpus...")
    text = load_corpus("data/kjv.txt")
    words = text.split()
    print(f"Corpus loaded: {len(words)} words")

    # Generate for n = 2, 3, 4
    for n in [2, 3, 4]:
        print(f"\n--- N-gram size: {n} ---")
        print(f"Training {n}-gram model...")

        # Train model
        ngram = BasicNgram(n, words, estimator=goodturing_estimator)

        # Generate 3 samples
        for i in range(1, 4):
            print(f"  Generating sample {i}...")
            generated_text = generate_text(ngram, num_words=100)

            # Save to file
            output_path = f"outputs/generated_text/n{n}_sample{i}.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(generated_text)

            print(f"  Saved to {output_path}")

    print("\nDone!")


if __name__ == "__main__":
    main()
