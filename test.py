#!/usr/bin/env python3
from random import randint
from numpy import mean
from helper import Executable, Test, Source, Program
from itertools import permutations

import codecs

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

    def test_printf_4(self):
        "printf/4.c"
        p = Program('printf/4.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\%\d+\.\d+[Ffg]'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("042.12 sur stdout ?", p.run().stdout.match(r'042.12'))

    def test_printf_5(self):
        "printf/5.c"
        p = Program('printf/5.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\\t'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Sortie standard correcte ?", p.run().stdout.match(r'23\t3.14150*\t6.280*\t99'))

    def test_printf_6(self):
        "printf/6.c"
        p = Program('printf/6.c')
        self.test("Ne pas utilser sprintf ?", not p.source.grep(r'sprintf'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Question 1 ?", p.run().stdout.match(r'Q1.+\'(z)7\1 {5}7\1\\n'))
        self.test("Question 2 ?", p.run().stdout.match(r'Q2.+\'7{2}\.0{6}\\n'))
        self.test("Question 3 ?", p.run().stdout.match(r'Q3.+\'36[,]1e[,]1E\\n'))
        self.test("Question 4 ?", p.run().stdout.match(r'Q4.+\'77\\n'))

    def test_printf_7(self):
        "printf/7.c"
        p = Program('printf/7.c')
        self.test("Utiliser printf ?", p.source.grep(r'printf'))
        self.test("Variable birth year correcte ?", p.source.grep(r'char\s+birth_year\s*=\s*\d{1,2}\s*;'))
        self.test("Plus de points de suspension ?", not p.source.grep(r'\.{3}'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Nom présent sur stdout ?", p.run().stdout.match(r'Name:\s+\S+'))
        self.test("Année de naissance sur stdout ?", p.run().stdout.match(r'Birth Year:\s+(19|20)\d{2}'))
        self.test("Mobile sur stdout ?", p.run().stdout.match(r'Mobile:\s+\+\d{2} (\d{2,3} ?)*\d{2,3}'))
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
