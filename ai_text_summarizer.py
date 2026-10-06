import re
from collections import Counter


def summarize_text(text, max_sentences=3):
    """Create an extractive summary using word-frequency scoring."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = [sentence for sentence in sentences if sentence]

    if len(sentences) <= max_sentences:
        return sentences

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    stop_words = {
        "the", "is", "a", "an", "and", "or", "of", "to", "in",
        "on", "for", "with", "this", "that", "are", "was", "were",
        "as", "by", "it", "from", "at", "be", "has", "have"
    }

    useful_words = [word for word in words if word not in stop_words]
    frequency = Counter(useful_words)

    scored = []

    for index, sentence in enumerate(sentences):
        sentence_words = re.findall(
            r"\b[a-zA-Z]+\b", sentence.lower()
        )
        score = sum(frequency[word] for word in sentence_words)
        scored.append((score, index, sentence))

    selected = sorted(scored, reverse=True)[:max_sentences]
    selected.sort(key=lambda item: item[1])

    return [item[2] for item in selected]


def main():
    print("\n==============================")
    print("       AI TEXT SUMMARIZER")
    print("==============================")
    print("Enter your text below.")
    print("Press Enter on an empty line when finished.\n")

    lines = []

    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    text = " ".join(lines).strip()

    if not text:
        print("Please enter some text.")
        return

    try:
        number = input(
            "Number of summary sentences (default 3): "
        ).strip()

        max_sentences = int(number) if number else 3

        if max_sentences <= 0:
            print("Please enter a positive number.")
            return

        summary = summarize_text(text, max_sentences)

        print("\n========== SUMMARY ==========")
        for sentence in summary:
            print(sentence)

        total_sentences = len(
            re.split(r"(?<=[.!?])\s+", text)
        )

        print("\nOriginal sentences :", total_sentences)
        print("Summary sentences  :", len(summary))

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
