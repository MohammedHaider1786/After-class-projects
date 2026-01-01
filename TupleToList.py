class TupleToList:
    def __init__(self, data):
        self.data = data

    def convert(self):
        return list(self.data)


def main():
    # Input tuple
    my_tuple = (10, 20, 30, 40, 50)

    converter = TupleToList(my_tuple)
    my_list = converter.convert()

    print("Original Tuple:", my_tuple)
    print("Converted List:", my_list)


main()
