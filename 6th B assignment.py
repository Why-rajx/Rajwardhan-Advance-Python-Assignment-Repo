def knapsack_bottom_up(weight_list, value_list, capacity):

    item_count = len(weight_list)

    table = [[0 for _ in range(capacity + 1)]
             for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):

        for w in range(1, capacity + 1):

            current_weight = weight_list[i - 1]

            current_value = value_list[i - 1]

            if current_weight <= w:

                include = (
                    current_value +
                    table[i - 1][w - current_weight]
                )

                exclude = table[i - 1][w]

                table[i][w] = max(include, exclude)

            else:

                table[i][w] = table[i - 1][w]

    return table[item_count][capacity]


weight_list = [2, 1, 3, 2]
value_list = [12, 10, 20, 15]

capacity = 5

maximum_value = knapsack_bottom_up(
    weight_list,
    value_list,
    capacity
)

print("Maximum value using Bottom-Up:",
      maximum_value)