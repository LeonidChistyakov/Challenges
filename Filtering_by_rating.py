def filter_by_rating(d: dict, rating: str):
    fdict = dict()
    for (key, value) in d.items():
        if rating == value:
            fdict[key] = rating
    if fdict:
        return fdict
    else:
        return "No results found"

hotels = {
    "Continental Hotel": "****",
    "Big Street Hotel": "**",
    "Corner Hotel": "**",
    "Trashviews Hotel": "*",
    "Hazbins": "*****",
}

filtered = filter_by_rating(hotels, "**")
print(filtered)
