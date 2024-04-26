def get_words_count_distribution_percentage(strings: list[str]) -> dict[int, int]:
    strings_count = len(strings)
    distribution = dict()
    for s in strings:
        words_count = len(s.split())
        if words_count in distribution:
            distribution[words_count] += 1
        else:
            distribution[words_count] = 1

    for count, count_occurrences in distribution.items():
        distribution[count] = (count_occurrences / strings_count) * 100

    return distribution


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing",
                  "foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]
words_count_distribution = get_words_count_distribution_percentage(search_queries)

for quantity, percentage in sorted(words_count_distribution.items()):
    print(f"{quantity} слово: {round(percentage, 2)}%")
