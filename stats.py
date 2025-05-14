def number_of_words(text):
    num_words = len(text.split())
    return num_words


def number_of_characters(text):
    result = {}
    text_lower = text.lower()
    for c in text_lower:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def sort_on(dict):
    return dict["num"]


def sort_results(results):
    sorted = []
    for result in results:
        sorted.append({"char": result, "num": results[result]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
