import sys

class TBFSBS_parser:
    """Parser reads a TBFSBS file."""

    def __init__(self, files):
        self.files = files
        self.id = None
        self.value = None
        self.description = ""
        self.seq_length = 0

    def __header(self, line):
        """Process header."""

        header = line.split(' ')
        self.id = header[0]
        try:
            if header[1].isdigit():
                self.value = int(header[1])
            elif float(header[1]):
                self.value = '%.1f'%float(header[1])
            elif header[1]=='NULL' or header[1]=='null' or header[1]=='-':
                self.value = header[1]
        except ValueError:
            print("Wrong numeric target value. Supported types: float, integer, NaN, NULL, null and -.")

        self.description = " ".join(header[2:])

    def __summary(self):
        """Print summary of input sequence."""

        if self.id is None:
            pass
        else:
            print("ID: {0} \nValue: {1} \nDescription: {2} \nSequence length: {3}\n".format(self.id, self.value, self.description, self.seq_length))


    def parse(self):
        """Parse input sequence."""

        for arg in self.files:
            print("FILE: {}\n=============".format(arg))
            try:
                with open(arg, 'r') as f:

                    for line in f:

                        line = line.strip()
                        if line.startswith("%"):
                            TBFSBS_parser.__summary(self)
                            self.seq_length = 0
                            TBFSBS_parser.__header(self, line[1:].strip())
                            
                        else:
                            self.seq_length += len(line)

                    TBFSBS_parser.__summary(self)
                    self.id = None

            except FileNotFoundError:
                print("File doesn't exist.\n")

if __name__ == "__main__":
    parser = TBFSBS_parser(sys.argv[1:])   
    parser.parse() 