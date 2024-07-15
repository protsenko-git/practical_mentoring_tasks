def merge_transform_analyze(list_1, list_2, list_3):
    list_main = list(zip(list_1, list_2, list_3))
    main_dict = {
        "sums": [],
        "products": [],
        "min": [],
        "max": []
    }
    for i in list_main:
        main_dict["sums"].append(sum(i))
    for v in list_main:
        j = 1
        for num in v:
            j *= num
        main_dict["products"].append(j)
    for m in list_main:
        main_dict["min"].append(min(m))
        main_dict["max"].append(max(m))
    return print(main_dict)
