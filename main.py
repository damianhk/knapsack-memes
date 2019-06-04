from ortools.algorithms import pywrapknapsack_solver
from collections import Counter
from random import randint


def calculate(usb_size, memes):
    """
    Function calculate maximum value of memes wchich could we
    save on usb stick and return set of these memes. 

    calculate(usb_size, memes)
    input:
        usb_size:   int
                    USB capacity in GiB 
                    1 GiB = 1024 MiB

        memes:      List/Tuple[Tuple/List[str, int, int], ]
                    e.g. [('dolan.png', 126, 5)]
                    [(name, size in MiB, price), ...]

    output:
                Tuple[int {str, str, str, ...}]
                (max price, {set of memes names}
    

    """
    # Check input types and values
    if not isinstance(usb_size, (int)):
        raise TypeError("usb_size value must be an int not in {}".format(type(usb_size)))
    if usb_size < 0:
        raise ValueError("usb_size value must be non negative integer")

    if not isinstance(memes, (list, tuple)):
        raise TypeError(
            "memes must be stored in a list or tuple not in {}".format(type(memes))
        )

    for element in memes:
        if not isinstance(element, (list, tuple)):
            raise TypeError(
                "meme must be stored in a tuple or list not in {}".format(type(element))
            )

        if len(element) != 3:
            raise TypeError(
                "not enough arguments for meme, expected 3 get {}".format(len(element))
            )

        if not isinstance(element[0], (str)):
            raise TypeError("name must be a str not in {}".format(type(element[0])))

        if not element[0]:
            raise ValueError("meme name is blank")

        for item in element[1:]:
            if not isinstance(item, (int)):
                raise TypeError("value and weight must be an int")

            if item < 0:
                raise ValueError("value and weigth must be a non negative integer")

    names = [item[0] for item in memes]
    for item in Counter(names).values():
        if item > 1:
            raise ValueError("names have to be unique")

    # Save values and weigts in correct type for feeding solver
    values = [item[2] for item in memes]  
    weights = [[item[1] for item in memes]]
    capacities = [usb_size * 1024]  # Convert GiB to MiB

    # Define Solver
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "Knapsack_branch_and_boud",
    )

    solver.Init(values, weights, capacities)  # Solver feeding
    computed_profit = solver.Solve()  # Compute optimum value

    # Save the best set of memes
    packed_items = {
        names[x] for x in range(0, len(weights[0])) if solver.BestSolutionContains(x)
    }

    # Return tuple of comuted_profit and set of the best memes
    return (computed_profit, packed_items)


if __name__ == "__main__":
    usb_size = 32
    memes = [('meme ' + str(idx), randint(0, 1000), randint(0, 500)) for idx in range(1000)]
    cost, memes = calculate(usb_size, memes)
    print("Set value: ", cost)
    print(memes)