import sys
import io

file_path = sys.argv[1]

CARRIAGE_RETURN_LINE_FEED = "\r\n"

with open(file_path, 'r') as fin:
    with open('hosts_win32','w') as fout:
        for line in fin:
            if not line.startswith('#') and not line.isspace():
                fout.write(line.rstrip('\n') + CARRIAGE_RETURN_LINE_FEED)
    fout.close()
fin.close()


