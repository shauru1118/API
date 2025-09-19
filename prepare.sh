#!/bin/bash

clear

echo ""
echo "    ---- > git fetch --all < ----"
echo ""
git fetch --all
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

echo ""
echo "    ---- > git status < ----"
echo ""
git status
echo ""