Imagine "TBFSBS", a text-based format for storing biological sequences with a numeric value annotation. 

Each sequence is preceded by a "header". 

The TBFSBS header is a *single line* that begins with the `%` character, followed by:

- any number of spaces
- the identifier: string (without whitespaces)
- any number of spaces
- a numeric target value: integer or float or null (null/NULL/NaN/-)
- any number of spaces
- the description: string (can contain whitespace)

The sequence follows the header line, and can be split into multiple lines.

Example:
```
% MyID1 1.25424 My first text description
ACTGACTGACTGACTGACTGACTGACAACTTGACTGACTGACTGAAACTGACTG
GAACTGACGTTGTGACTGACTGACTGACTGACTGACTGACTTTGACTGACTGAC
ACTGACTGGGACTGACTGACTGACTGACAACTTGACTAAGACT
% MyID2 0.22145 My second text description
ACTGACTG...
```

Write a simple parser in Python that reads a TBFSBS file and prints the following for each input sequence:

```
ID: MyID1
Value: 1.3 (print only one digit after decimal point)
Description: My first text description
Sequence length: 151

ID: MyID2
Value: 0.2
Description: My second text description
Sequence length: 123
...
```

Requirements:

- Do not install any extra Python packages, import default libraries only (hint: you don't need to implement your own commandline arg parser, it's included as a default library)
- Provide the solution as an executable Python script that can be executed as: `./parse.py MySequences.txt`
- Publish the solution on GitHub or any other git-based software hosting site
- Don't worry too much about documentation or extendability, the goal is to get the job done using simple clean code
- (Bonus 1) Allow parsing multiple files, print filename before parsing each input file.
- (Bonus 2) Implement a TBFSBS writer that writes the TBFSBS sequences back into an output file, with configurable maximum length of the sequence line (line wrap). Usage `./parse.py MySequences.txt --output MyOutput.txt --wrap 80`
