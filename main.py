from src.factorial import factorial


def main() -> None:
    for n in range(6):
        print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()
