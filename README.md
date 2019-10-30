# Exercices 101

Cette série d'exercices est destinée à vous familiariser davantage avec le C
et vous préparer pour le prochain travail écrit.

Le corrigé de ces exercices se trouve dans la branche `solution`.

Le programme de test essaie automatiquement de compiler tous les programmes et vous indique
le nombre de points obtenus.

## Tests

Pour tester votre progression: 

```sh
$ make test
```

Pour tout compiler:

```sh
$ make build
```

## Compilation et test manuel du programme ?

Facile, voici l'exemple pour `printf/1.c`:

```sh
$ gcc -std=c99 -Wall printf/1.c
$ ./a.out
```

