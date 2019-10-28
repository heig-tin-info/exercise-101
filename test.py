#!/usr/bin/env python3
from random import randint
from numpy import mean
from . import Executable, Test
from itertools import permutations

class TestArguments(Test):

    def test_arguments(self):
        "Exercices sur les arguments (argc, argv)"

        # arguments/1
        P = Executable('arguments/1.out')
        n = 5
        args = map(str, range(n))
        self.test("./1.out %s" % (" ".join(args)) , int(P(args)).stdout == n)

        # arguments/2
        P = Executable('arguments/2.out')
        n = 5
        args = ["foo", "bar", "baz", "42"]
        self.test("./2.out %s" % (" ".join(args)), 
            [P(args).stdout.match(r'%d*?\b%s\b' % (n + 1, s)) for n, s in enumerate(args)])        

        # arguments/3
        P = Executable('arguments/3.out')
        args = [randint(2048) for i in range(7)]
        self.test("./3.out %s" % (" ".join(map(str, args))), 
            P(args).stdout.match(str(min(args))))

        # arguments/4
        P = Executable('arguments/4.out')
        n = 5
        args = [randint(2048) for i in range(10)]
        self.test("./4.out %s" % (" ".join(map(str, args))), 
            P(args).stdout.match(str(mean(args))))
