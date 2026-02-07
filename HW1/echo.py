#echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitates a real-world echo."""
    echo = text[-repetitions:]
    print(echo)
    for i in range(repetitions-1):
        echo = echo[1:]
        print(echo)
    print(".")

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    echo(text)