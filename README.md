# Introduction

This command aims to retrieve information from a social graph.

## Data

A JSON file with the following structure:
```
[
  {
    "id": 1,
    "firstName": "Paul",
    "surname": "Crowe",
    "age": 28,
    "gender": "male",
    "friends": [
      2
    ]
  },
  ...
]```

Link between friends consist in an adjacency list of ids, defined with the `friends` attribute.

## Objective

The solution must allow to retrieve the following information:

- Direct friends: Return those people who are directly connected to the chosen person.
- Friends of friends: Return those who are two steps away, but not directly connected to the chosen person.
- Suggested friends: Return people in the group who know 2 or more direct friends of the chosen person, but are not directly connected to her.


# Solution

The solution is based on python, built around a command line tool. 
I focused on providing a solution within 3 hours, without wasting time in managing HTTP request 
for a REST API or defining a database model, which is not required to solve this problem.

# Installation

## Requirements

- python, >=2.7
- pip package manager, >=7.0.3

## Source

## Setup

- for production  
  `pip install `

- for development   
  ```
  git clone git@github.com:zazabe/cargo.tar.gz /opt/source/cargo
  cd /opt/source/cargo 
  pip install -e .
  ```

Notes: 
- the code has only been tested on Ubuntu 14.04, but should work on any unix distribution supporting at least python 2.7.
- to run unit tests, you must at least clone the repository and run tests from the root of the repo.


# Usage

The command support a `--help` option for each sub-command.

## Get direct friends of a person

```
cargo social <JSON_DATA_FILE> direct <PERSON_ID>

$ cargo social tests/fixtures.json direct 2
2 friend(s) found for Rob Fitz
- Paul Crowe
- Ben O'Carolan
```

## Get people with a 2 steps relation with a person

```
cargo social <JSON_DATA_FILE> steps <PERSON_ID> --steps [NB_STEPS] (default: 2)

$ cargo social tests/fixtures.json steps 2
4 relation with 2 steps for Rob Fitz
- Rob Fitz
- Victor
- Peter Mac
- Sarah Lane
```

## Suggestion people with at least 2 common friends for a person

```
cargo social <JSON_DATA_FILE> suggest <PERSON_ID>

$ cargo social tests/fixtures.json suggest 5
1 friend(s) suggestion for Peter Mac
- Katy Couch
```

# Tests

[Unit tests][test_source] are written with [py.test][py_test], you must clone the source code to have all required files (fixtures, etc...) and run test properly.

Run all tests (at the root of the repository folder):
```
$ py.test tests/social.py
```

Additionnally, tests are run by [Travis CI][travis] at every commit.


  [py_test]: http://pytest.org/latest/
  [test_source]: 
  [travis]: https://travis-ci.org/
