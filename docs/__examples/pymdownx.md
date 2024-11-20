---
date:
  created: 2024-11-15
readtime: 15
pin: true
categories:
  - Holidays
tags:
  - new year
  - hogmanay
  - festive season
authors:
  - team
---


<!-- more -->

# Exemple de Markdown avec fonctionnalités avancées

## Table des matières
La table des matières est générée automatiquement grâce à l'extension `toc`.

---

## 📘 Introduction

Bienvenue dans cet exemple ! Ce document met en avant différentes extensions Markdown pour enrichir votre documentation.

---

## 💡 Admonitions

Les admonitions permettent de mettre en avant des blocs spécifiques :

!!! note "Note importante"
    Ce bloc est utilisé pour insister sur des points spécifiques, comme une note.

!!! warning "Attention"
    Soyez vigilant lorsque vous utilisez cette fonction ! Elle pourrait causer des erreurs si elle est mal configurée.

!!! tip "Astuce"
    Vous pouvez utiliser cette fonctionnalité pour donner des astuces aux utilisateurs.

---

## 🧩 Blocs de code avancés avec onglets

Grâce à `pymdownx.superfences`, vous pouvez créer des blocs de code regroupés sous forme d'onglets :

With title bar
```python {title="My Cool Header"}
import foo.bar
import boo.baz
import foo.bar.baz
```

With console result
```pycon
>>> 3 + 3
6
```

With highlight line
```python {hl_lines="1-2 5 7-8"}
import foo
import boo.baz
import foo.bar.baz

class Foo:
   def __init__(self):
       self.foo = None
       self.bar = None
       self.baz = None
```

## 🔁 Inclusion de snippets

Incluez des fichiers externes pour réutiliser du contenu avec `pymdownx.snippets` :

--8<--
docs/blog/snippet.md
--8<--

## 🔁 Inclusion de table avec `pymdownx.superfences`

Incluez des tables :


| id | name | email                      | password |
|----|------|----------------------------|----------|
| 1  | ath  | ath.francophonia@gmail.com | ******** |
| 2  | rob  | rob.francophonia@gmail.com | ******** |

# Exemple avec pymdownx.tabbed

Grâce à `pymdownx.superfences`, vous pouvez créer des blocs de code regroupés sous forme d'onglets :

/// tab | Tab A title
```python
def HelloWorld(name):
    if name is None:
        return "Hello World!"
    else:
        return "Hello " + name + "!"
```
///

/// tab | Tab B title
```python
def hello_world(name: str = "World"):
    return f"Hello, {name}!"
```
///

/// tab | Tab C Title
    new: true

Will be part of a separate, new tab group. 🤗
///