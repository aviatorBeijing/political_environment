#!/bin/bash

NAME=$1
OCCU=$2
NATION=$3
YEAR=$4
REASON=$5
SOURCE=$6

$PYTHON ../src/unnatural_death/historical.py --name $NAME --occupation $OCCU --nation $NATION --death_date=$YEAR --reason $REASON --source $SOURCE
