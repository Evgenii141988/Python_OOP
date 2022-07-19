class PrimaryKey:
    def __enter__(self):
        print("вход")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)

        return True


if __name__ == '__main__':
    with PrimaryKey() as pk:
        raise ValueError
