from method import method


def main():
    invest = 8

    if invest < 0:
        print("Invest count must be 0 or higher")

    table = [
        # [[2, 0.5], [2, 0.4], [4, 1.4], [5, 1.5], [3, 0.8]],
        # [[3, 0.8], [4, 0.8], [1, 0.4], [2, 0.6], [3, 0.8]],
        # [[1, 0.3], [4, 0.8], [1, 0.4], [3, 0.9], [5, 1.3]],
        [[2, 0.5], [3, 0.6], [3, 1.1], [3, 0.9], [3, 0.8]],
        [[1, 0.3], [4, 0.8], [3, 1.1], [5, 1.5], [4, 1.0]],
        [[1, 0.3], [4, 0.8], [3, 1.1], [5, 1.5], [5, 1.3]],
    ]
    path, incomes = method(table, invest)
    print("\n---------------------------------------------------------------------")
    for i, j in path:
        print(f"\nIt's necessary to invest {j} conventional units in company {i}.")
    print("\n---------------------------------------------------------------------")
    print(f"\nTotal income : {incomes}")

if __name__ == "__main__":
    main()

