def transform_and_group(names):
    grouped_names = {}
    for name in names:
        upper_name = name.upper()
        length = len(upper_name)
        if length not in grouped_names:
            grouped_names[length] = []
        grouped_names[length].append(upper_name)
    return dict(sorted(grouped_names.items()))
