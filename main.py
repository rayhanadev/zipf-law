# %%

import string
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# %%

with open("corpus.txt", "r") as file:
    content = file.read()

# %%

words = content.translate(str.maketrans("", "", string.punctuation)).split()
word_counts = Counter(words)
total_words = sum(word_counts.values())
relative_frequencies = {
    word: count / total_words for word, count in word_counts.items()
}

# %%

sorted_counts = sorted(relative_frequencies.values(), reverse=True)
ranks = np.arange(1, len(sorted_counts) + 1)

plt.figure(figsize=(6, 6))
plt.scatter(ranks, sorted_counts, alpha=0.7, color="blue", s=10)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Word Rank")
plt.ylabel("Relative Frequency")
plt.title("Word Frequency Distribution (Zipf's Law)")
plt.xticks([1, 10, 100, 1000, 10000], labels=["1", "10", "100", "1000", "10000"])
plt.yticks(
    [0.00001, 0.0001, 0.001, 0.01, 0.1],
    labels=["0.00001", "0.0001", "0.001", "0.01", "0.1"],
)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
