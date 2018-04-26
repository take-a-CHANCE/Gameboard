#!/bin/bash

rm Game.py
git fetch --all
git reset --hard origin/master
rm Game.py
mv Game.1.py Game.py