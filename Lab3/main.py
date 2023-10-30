from Scanner import Scanner



def run(file_path):
    scanner = Scanner(file_path)
    scanner.scan()
    pif = scanner.get_pif()
    with open(file_path+".pif.txt", 'w') as file:
        for element in pif:
            file.write(str(element) + '\n')


if __name__ == "__main__":
    run("p1.txt")
    # run("p2.txt")
    # run("p3.txt")
    # run("pERR.txt")

