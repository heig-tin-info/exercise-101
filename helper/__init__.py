#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from pathlib import Path
from blessings import Terminal
from collections import namedtuple
from methodtools import lru_cache

Outputs = namedtuple('Outputs', ['exit_status', 'stdout', 'stderr'])


class Program:
    def __init__(self, sourcefile):
        self.executable = None
        self.source = Source(sourcefile)
        self.path = Path(sourcefile)

    def build(self):
        result = self.source.build()

        if result == 0:
            out = self.path.absolute().parents[0].joinpath(f'{self.path.stem}.out')
            self.executable = Executable(out)
            self.warnings = self.source.warnings
            self.errors = self.source.errors
        return not result

    def run(self, *args, stdin=None):
        if self.executable:
            self.build()
        return self.executable.run(*args, stdin=stdin)


class Source:
    CC = 'gcc'
    CFLAGS = ["-std=c99", "-g", "-Wall", "-pedantic", "-fdiagnostics-color"]
    LDFLAGS = ["-lm"]

    def __init__(self, filename):
        self.filename = filename
        self.path = Path(self.filename)
        self.execfile = self.path.absolute().parents[0].joinpath(f'{self.path.stem}.out')
        self.warnings = None
        self.errors = None

    def up_to_date(self):
        if not self.execfile.exists():
            return False

        if self.warnings is None or self.errors is None:
            return False

        s = os.path.getmtime(self.path)
        e = os.path.getmtime(self.execfile)

        return e >= s

    def build(self):
        if self.up_to_date():
            return 0


        p = subprocess.Popen([self.CC, *self.CFLAGS, self.filename, f'-o{self.execfile}', *self.LDFLAGS],
            stderr=subprocess.PIPE)

        stdout, stderr = p.communicate()
        stderr = stderr.decode('utf8')
        self.warnings = len(re.findall("warning:", stderr))
        self.errors = len(re.findall("errors:", stderr))

        return p.returncode

    def grep(self, pattern):
        with open(self.filename, 'r') as fp:
            return re.findall(pattern, fp.read())

    def match(self, pattern):
        return len(self.grep(pattern)) > 0


class Executable:
    def __init__(self, filename):
        self.filename = filename

        if not self._is_executable(filename):
            raise ValueError("Program %s is not executable!" % filename)

    #@lru_cache(maxsize=16)
    def run(self, *args, stdin=None):
        p = subprocess.Popen([self.filename, *[str(a) for a in args]],
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        if isinstance(stdin, str):
            stdin = stdin.encode('utf8')
            
        stdout, stderr = p.communicate(input=stdin)
        stdout = stdout.decode('utf8') if stdout else None
        stderr = stderr.decode('utf8') if stderr else None

        return Outputs(p.returncode, GreppableString(stdout), GreppableString(stderr))

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    @staticmethod
    def _is_executable(filename):
        return os.path.isfile(filename) and os.access(filename, os.X_OK)


class GreppableString(str):
    def grep(self, pattern):
        return re.findall(pattern, self)

    def match(self, pattern):
        return len(self.grep(pattern)) > 0


class Test:
    def __init__(self):
        self.t = Terminal()
        self.tests = 0
        self.errors = 0
        for i, test in enumerate(self.collect()):
            self.section = i + 1
            if test.__doc__:
                print(self.t.bold(f'{self.section}. ' + test.__doc__))
            test()
            print("")

        if self.errors == 0:
            print(f"Éxecuté {self.tests} tests avec succès\n\nOK")
            sys.exit(0)
        else:
            s = "s" if self.errors > 1 else ""
            print(
                f"Éxecuté {self.tests - self.errors} sur {self.tests} tests avec succès, {self.errors} erreur{s}\n\nFAIL")
            sys.exit(1)

    def collect(self):
        return [getattr(self, method) for method in dir(self) if method.startswith('test_')]

    def test(self, message, assertion, error_message=None):

        print(f"  {self.section}.{self.tests + 1}. {message}...", end='', flush=True)

        if self._is_lambda(assertion):
            assertion = assertion()

        if assertion:
            print(self.t.green(" ok"), flush=True)
        else:
            self.errors += 1
            print(self.t.red(" erreur"), flush=True)
            if error_message:
                print(self.t.red("   " + error_message))
        self.tests += 1


    @staticmethod
    def _is_lambda(v):
        LAMBDA = lambda:0
        return isinstance(v, type(LAMBDA)) and v.__name__ == LAMBDA.__name__
