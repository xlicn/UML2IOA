# UML2IOA

Translate UML to I/O Automata

# UML format
    We use the uml format in plantuml (https://plantuml.com/). A uml can be a sequence diagram for interaction between two components or a state diagram inside of a component.

# IOA format
    An automaton consists of a set of signatures, state and transactions(https://www.cs.yale.edu/homes/aspnes/pinewiki/IOAutomata.html).
    The state is represented by a set of variables.
    A transaction consists of an action (input or output), a precondition (for input action, it is empty), and an effect (for output action, it can be empty)