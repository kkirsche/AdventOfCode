from pkgutil import get_data


def load_puzzle(day: int, example: bool = False, filter_none: bool = True) -> list[str]:
    suffix = "-example" if example else ""
    content = get_data(
        "adventofcode",
        f"inputs/day{day}{suffix}.txt",
    )
    if not content:
        return []
    content_list = content.decode("utf-8").splitlines()
    if filter_none:
        return list(filter(None, content_list))
    return content_list
