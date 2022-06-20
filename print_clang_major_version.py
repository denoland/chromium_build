#!/usr/bin/env python

import re
import subprocess
import sys


def main():
  clang_bin = sys.argv[1]
  output = subprocess.check_output([clang_bin, "--version"])
  major_version = int(re.search(b"version (\d+)\.\d+\.\d+", output)[1])
  print(major_version)


if __name__ == '__main__':
  sys.exit(main())
