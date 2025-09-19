#!/bin/bash

clear

echo ""
echo "    ---- > git stash < ----"
echo ""
git stash
echo ""

echo ""
echo "    ---- > git pull < ----"
echo ""
git pull
echo ""

echo ""
echo "    ---- > tree < ----"
echo ""
tree 
echo ""

chmod +x prepare.sh

echo ""
echo "    ---- > git status < ----"
echo ""
git status
echo ""