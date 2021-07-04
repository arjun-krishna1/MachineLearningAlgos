def get_statistics(input_list):
    Z_SCORE = 1.96
    result = {
        "mean": 0,
        "median": 0,
        "mode": 0,
        "sample_variance": 0,
        "sample_standard_deviation": 0,
        "mean_confidence_interval": [0, 0],
    }

    input_list.sort()

    n = len(input_list)
    result["mean"] = sum(input_list) / n

    # median: equal number of nums above median as below median
    if n % 2 != 0:
        result["median"] = input_list[n // 2]

    else:
        result["median"] = (input_list[n // 2 - 1] + input_list[n // 2]) / 2

    # mode: get value that occurs the most often
    max_val = input_list[0]
    max_count = 1

    prev_val = input_list[0]
    count = 1

    for i in range(1, n):
        if input_list[i] == prev_val:
            count += 1

        else:
            if count > max_count:
                max_val = prev_val
                max_count = count

            prev_val = input_list[i]
            count = 1

    result["mode"] = max_val

    # sample variance: spread of sample
    result["sample_variance"] = float(sum([(y - result["mean"])**2 for y in input_list]))/(n - 1)

    # sample std dev:
    result["sample_standard_deviation"] = result["sample_variance"] ** 0.5

    spread_interval = (Z_SCORE * result["sample_standard_deviation"]) / (n ** 0.5)
    result["mean_confidence_interval"] = [result["mean"] - spread_interval, result["mean"] + spread_interval]

    return result

# mode is wrong, std_dev is wrong, sample_variance is wrong
if __name__ == "__main__":
    print(get_statistics([2, 1, 3, 4, 4, 5, 6, 7]))
