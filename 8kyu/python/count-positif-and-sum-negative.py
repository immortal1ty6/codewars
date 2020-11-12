def count_positives_sum_negatives(arr):
        if not arr:
            return []
        positive = 0
        negative = 0
        for a in arr:
            if a>=1:
                positive += 1
            else:
                negative += a
        return [positive, negative]
