def knapsack_top_down(weights_list, values_list, items, capacity, memory):

    if items == 0 or capacity == 0:
        return 0

    if memory[items][capacity] != -1:
        return memory[items][capacity]

    if weights_list[items - 1] > capacity:

        memory[items][capacity] = knapsack_top_down(
            weights_list,
            values_list,
            items - 1,
            capacity,
            memory
        )

    else:
        include = values_list[items - 1] + knapsack_top_down(
            weights_list,
            values_list,
            items - 1,
            capacity - weights_list[items - 1],
            memory
        )

        exclude = knapsack_top_down(
            weights_list,
            values_list,
            items - 1,
            capacity,
            memory
        )

        memory[items][capacity] = max(include, exclude)

    return memory[items][capacity]


weights_list = [2, 1, 3, 2]
values_list = [12, 10, 20, 15]

capacity = 5
items = len(weights_list)

memory = [[-1 for _ in range(capacity + 1)]
          for _ in range(items + 1)]

maximum_value = knapsack_top_down(
    weights_list,
    values_list,
    items,
    capacity,
    memory
)

print("Maximum value using Top-Down:", maximum_value)