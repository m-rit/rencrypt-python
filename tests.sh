#!/bin/sh

pytest
python examples/encrypt.py
python examples/encrypt_into.py
python examples/encrypt_from.py
python examples/encrypt_file.py
python bench/bench.py