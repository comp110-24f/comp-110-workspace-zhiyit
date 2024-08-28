"""number of people to calculate number of tea bags, treats, expected cost"""

__author__: str = "730736518"


def main_planner(guests: int) -> None:
    """Main function that puts all the following small ones tgt
    the people needs to equal guests since guests is the parameter
    the functions of teabags and treats needs to be called
    return None needs to be at the end of a def for it to run or else returns None
    remember spaces and turning int to str"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """using number of people to find tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """using number of poeple to find treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """finding total cost of tea bags and treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
