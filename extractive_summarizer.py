import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


def summarize_text(text: str, summary_ratio: float = 0.3) -> str:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    stopwords = list(STOP_WORDS)
    word_frequencies = {}

    for token in doc:
        token_text = token.text.lower()
        if token_text not in stopwords and token_text not in punctuation:
            word_frequencies[token_text] = word_frequencies.get(token_text, 0) + 1

    if not word_frequencies:
        return ""

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}

    for sent in sentence_tokens:
        for word in sent:
            token_text = word.text.lower()
            if token_text in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[token_text]

    select_length = max(1, int(len(sentence_tokens) * summary_ratio))
    best_sentences = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    summary = " ".join([sent.text.strip() for sent in best_sentences])
    return summary


if __name__ == "__main__":
    sample_text = """
    Maria Sharapova has basically no friends as tennis players on the WTA Tour. The Russian player has no problems in openly speaking about it and in a recent interview she said: 'I don't really hide any feelings too much.
    I think everyone knows this is my job here. When I'm on the courts or when I'm on the court playing, I'm a competitor and I want to beat every single person whether they're in the locker room or across the net.
    So I'm not the one to strike up a conversation about the weather and know that in the next few minutes I have to go and try to win a tennis match.
    I'm a pretty competitive girl. I say my hellos, but I'm not sending any players flowers as well. Uhm, I'm not really friendly or close to many players.
    I have not a lot of friends away from the courts.' When she said she is not really close to a lot of players, is that something strategic that she is doing? Is it different on the men's tour than the women's tour? 'No, not at all.
    I think just because you're in the same sport doesn't mean that you have to be friends with everyone just because you're categorized, you're a tennis player, so you're going to get along with tennis players.
    I think every person has different interests. I have friends that have completely different jobs and interests, and I've met them in very different parts of my life.
    I think everyone just thinks because we're tennis players we should be the greatest of friends. But ultimately tennis is just a very small part of what we do.
    There are so many other things that we're interested in, that we do.'
    """

    print("Original Text:\n")
    print(sample_text)
    print("\nExtractive Summary:\n")
    print(summarize_text(sample_text, summary_ratio=0.3))
