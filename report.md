# N-gram Models Assignment Report

## Problem 1: Zipf's Law Analysis

### Methodology

I analyzed four different corpora to investigate Zipf's Law:
- King James Bible (English)
- The Jungle Book (English)
- SETIMES Bulgarian
- SETIMES Turkish

For each corpus, I counted word frequencies and sorted them by descending frequency. The tokenization was done by simply splitting on whitespace. I then created both linear and log-log plots to visualize the frequency distributions.

### Results

The plots are saved in `outputs/plots/`:
- `kjv_zipf.png` - King James Bible
- `junglebook_zipf.png` - The Jungle Book
- `setimes_bg_zipf.png` - SETIMES Bulgarian
- `setimes_tr_zipf.png` - SETIMES Turkish

![KJV Bible Zipf Plot](outputs/plots/kjv_zipf.png)
![Jungle Book Zipf Plot](outputs/plots/junglebook_zipf.png)
![SETIMES Bulgarian Zipf Plot](outputs/plots/setimes_bg_zipf.png)
![SETIMES Turkish Zipf Plot](outputs/plots/setimes_tr_zipf.png)

### Discussion

Looking at the log-log plots, all four corpora show approximately linear trends, which confirms that Zipf's Law holds pretty well across different languages and text types. The log-log plots are mostly straight lines with a negative slope, which is what we'd expect from Zipf's Law.

Some observations:
- The SETIMES corpora have way more unique words (224k for Bulgarian, 264k for Turkish) compared to the English texts (13k for KJV, 10k for Jungle Book). This is probably because SETIMES is a much larger corpus and also because Bulgarian and Turkish might have more morphological variation.
- All corpora show the typical Zipf pattern where a few words appear very frequently (like "the", "and", "of" in English) and most words appear rarely.
- The linear plots show the characteristic hyperbolic curve that drops off quickly for lower ranks.

Overall, Zipf's Law seems to be a pretty universal property of natural language that works across different languages and text types.
