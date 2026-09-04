# Sign Language Pattern Association System

## Problem Statement

A sign-language system stores relationships between hand-pattern
representations and their corresponding command symbols.

This project analyzes training pairs of hand patterns and command
symbols, identifies the association between them, predicts the
corresponding command for a new input pattern, and detects incorrect
associations.

## Objective

The main objectives of this project are:

1. To store hand-pattern and command-symbol training pairs.
2. To identify the relationship between hand patterns and commands.
3. To predict the command for a new hand-pattern input.
4. To identify incorrect or mismatched associations.
5. To visualize and analyze the learned associations.

## Concept Used

The main concept used in this project is Pattern Association.

Pattern association means finding a relationship between an input
pattern and its corresponding output.

For example:

Hand Pattern → Command

OPEN_HAND → HELLO
FIST → STOP
THUMBS_UP → YES

If a new input is OPEN_HAND, the expected command is HELLO.

## Methodology

The project follows these steps:

1. Create training data containing hand patterns and command symbols.
2. Load the training dataset using Python.
3. Analyze the relationships between patterns and commands.
4. Store the learned associations.
5. Give a new hand pattern as input.
6. Find the corresponding command.
7. Compare the predicted command with the expected command.
8. Identify incorrect associations.
9. Display the results using simple visualizations.

## Tools and Libraries

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
