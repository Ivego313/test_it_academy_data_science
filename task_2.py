def calculate_cosine_difference(vector_a: list, vector_b: list):
    if len(vector_a) != len(vector_b):
        print(f"Vectors have different dimensionality! Vector_a length: {len(vector_a)}, vector_b length: {len(vector_b)}.")
        return
    if not vector_a:
        print("Vectors are empty!")
        return
    if is_zero_vector(vector_a):
        print("Vector_a must be non-zero vector!")
        return
    if is_zero_vector(vector_b):
        print("Vector_b must be non-zero vector!")
        return

    dot_product = sum(vector_a[i] * vector_b[i] for i in range(len(vector_a)))
    product_vectors_lengths = get_vector_length(vector_a) * get_vector_length(vector_b)
    cosine_difference = 1 - dot_product / product_vectors_lengths
    print(f"Cosine difference is {round(cosine_difference, 5)}")


def is_zero_vector(lst: list) -> bool:
    return all(x == 0 for x in lst)


def get_vector_length(vector: list) -> int:
    return sum(vector[i] ** 2 for i in range(len(vector))) ** 0.5


a = [1, 1, 1, 1, 0]
b = [1, 1, 0, 0, 1]
calculate_cosine_difference(a, b)
