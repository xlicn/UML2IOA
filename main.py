import argparse


def main(inputFile, outputFile):
    i = 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""UML to I/O Automata translator.""")
    parser.add_argument('-i', dest='inputFile', default="nas.uml", help="uml file to read")
    parser.add_argument('-o', dest='outputFile', default="nas.ioa", help="ioa file to write, default=5GNAS.ioa")
    args = parser.parse_args()
    main(args.inputFile, args.outputFile)