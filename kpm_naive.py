import time
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)
    return matches


def compute_failure_function(pattern):
    m = len(pattern)
    failure = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j
    return failure

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    failure = compute_failure_function(pattern)
    j = 0
    matches = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = failure[j - 1]
    return matches


def performance_test(text, pattern):
    start_time = time.time()
    naive_matches = naive_search(text, pattern)
    naive_time = time.time() - start_time

    start_time = time.time()
    kmp_matches = kmp_search(text, pattern)
    kmp_time = time.time() - start_time

    return naive_matches, kmp_matches, naive_time, kmp_time


text = input("Enter the text: ")
pattern = input("Enter the pattern to search for: ")

naive_matches, kmp_matches, naive_time, kmp_time = performance_test(text, pattern)

print("\nResults:")
print("Naive search algorithm matches:", naive_matches)
print("KMP algorithm matches:", kmp_matches)
print("Naive search algorithm time:", naive_time)
print("KMP algorithm time:", kmp_time)