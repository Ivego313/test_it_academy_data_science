def calculate_cosine_difference(vector_a: list, vector_b: list):
    if len(vector_a) != len(vector_b):
        print("Vectors have different dimensionality!")
        return
    elif len(vector_a) == 0:
        print("Vectors must be not zero vectors!")
        return
    dot_product = sum(vector_a[i] * vector_b[i] for i in range(len(vector_a)))
    product_vector_lengths = get_vector_length(vector_a) * get_vector_length(vector_b)
    cosine_difference = 1 - dot_product / product_vector_lengths
    print(f"Cosine difference is {round(cosine_difference, 5)}")


def get_vector_length(vector: list) -> int:
    return sum(vector[i] ** 2 for i in range(len(vector))) ** 0.5


a = [1, 1, 1, 1, 0]
b = [1, 1, 0, 0, 1]
calculate_cosine_difference(a, b)
