#!/usr/bin/python3.5
import argparse
import xml.etree.ElementTree as ET
import plantuml

def parseUML(umlFile):
    # uml can be a sequence diagram or a state diagram

    tree = ET.parse(umlFile)


def main(inputFile, outputFile):
    # generate a figure of uml iva plantuml
    #pl = plantuml.PlantUML()
    #pl.processes(inputFile)
    i = 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""UML to I/O Automata translator.""")
    parser.add_argument('-i', dest='inputFile', default="nas.uml", help="uml file to read")
    parser.add_argument('-o', dest='outputFile', default="nas.ioa", help="ioa file to write, default=5GNAS.ioa")
    args = parser.parse_args()
    main(args.inputFile, args.outputFile)