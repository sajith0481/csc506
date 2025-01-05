# Source Code for Sorting Hospital Patient Records

# Sample dataset of patient records
def generate_patient_records():
    return [
        {"patient_id": 101, "name": "Alice", "admission_date": "2023-11-10"},
        {"patient_id": 102, "name": "Bob", "admission_date": "2023-11-12"},
        {"patient_id": 103, "name": "Charlie", "admission_date": "2023-11-11"},
        {"patient_id": 104, "name": "David", "admission_date": "2023-11-10"},
    ]

# Bubble Sort implementation
def bubble_sort(records, key):
    n = len(records)
    for i in range(n):
        for j in range(0, n - i - 1):
            if records[j][key] > records[j + 1][key]:
                records[j], records[j + 1] = records[j + 1], records[j]
    return records

# Merge Sort implementation
def merge_sort(records, key):
    if len(records) > 1:
        mid = len(records) // 2
        left_half = records[:mid]
        right_half = records[mid:]

        # Recursive call on each half
        merge_sort(left_half, key)
        merge_sort(right_half, key)

        # Merging the halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] <= right_half[j][key]:
                records[k] = left_half[i]
                i += 1
            else:
                records[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            records[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            records[k] = right_half[j]
            j += 1
            k += 1

    return records

# Example usage
if __name__ == "__main__":
    # Generate sample patient records
    patient_records = generate_patient_records()

    # Sorting by admission_date using Bubble Sort
    print("Original Records:")
    for record in patient_records:
        print(record)

    print("\nBubble Sort by admission_date:")
    bubble_sorted_records = bubble_sort(patient_records.copy(), "admission_date")
    for record in bubble_sorted_records:
        print(record)

    # Sorting by admission_date using Merge Sort
    print("\nMerge Sort by admission_date:")
    merge_sorted_records = merge_sort(patient_records.copy(), "admission_date")
    for record in merge_sorted_records:
        print(record)
