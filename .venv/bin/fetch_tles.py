#!/Users/lindsaymcrory/Dev/SailPerf_N2K/.venv/bin/python3.12
# -*- coding: utf-8 -*-
import re
import sys
from pyorbital.fetch_tles import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())
