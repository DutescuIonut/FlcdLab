from Scanner import Scanner


def print_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(str(content))
    except FileNotFoundError as e:
        print(e)


def run(file_path):
    scanner = Scanner(file_path)
    scanner.scan()
    pif = scanner.get_pif()
    print_to_file(file_path.replace(".txt", "tables.txt"),str(scanner.get_identifiersST())+"\n CONSTANT STARTS HERE \n"+str(scanner.get_constantST()))
    print_to_file(file_path.replace(".txt", "spif.txt"), pif.__str__())


if __name__ == "__main__":
    run("p1.txt")
    # run("p2.txt")
    # run("p3.txt")
    # run("pERR.txt")
