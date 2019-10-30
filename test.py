#!/usr/bin/env python3
from random import randint
from numpy import mean
from helper import Executable, Test, Source, Program
from itertools import permutations

class TestArguments(Test):

    def test_printf_1(self):
        "printf/1.c"
        p = Program('printf/1.c')
        self.test("Utilisation de printf ?", lambda: p.source.grep(r'printf.+[Hh]ello,?\s+[Ww]orld'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Hello, World sur stdout ?", p.run().stdout.match(r'[Hh]ello,?\s+[Ww]orld'))

    def test_printf_2(self):
        "printf/2.c"
        p = Program('printf/2.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\%d'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("42 sur stdout ?", p.run().stdout.match(r'42'))

    def test_printf_3(self):
        "printf/3.c"
        p = Program('printf/3.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\%l?[Ffg]'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("pi sur stdout ?", p.run().stdout.match(r'3.141592'))


    #     # arguments/1
    #     P = Executable('arguments/1.out')
    #     n = 5
    #     args = map(str, range(n))
    #     self.test("./1.out %s" % (" ".join(args)) , int(P(args)).stdout == n)

    #     # arguments/2
    #     P = Executable('arguments/2.out')
    #     n = 5
    #     args = ["foo", "bar", "baz", "42"]
    #     self.test("./2.out %s" % (" ".join(args)),
    #         [P(args).stdout.match(r'%d*?\b%s\b' % (n + 1, s)) for n, s in enumerate(args)])

    #     # arguments/3
    #     P = Executable('arguments/3.out')
    #     args = [randint(2048) for i in range(7)]
    #     self.test("./3.out %s" % (" ".join(map(str, args))),
    #         P(args).stdout.match(str(min(args))))

    #     # arguments/4
    #     P = Executable('arguments/4.out')
    #     n = 5
    #     args = [randint(2048) for i in range(10)]
    #     self.test("./4.out %s" % (" ".join(map(str, args))),
    #         P(args).stdout.match(str(mean(args))))

TestArguments()
