#!/bin/bash
seconds="${1:-10}"
echo "Sleep2 - v1.0"
echo "Sleeping in $seconds seconds ..."
	
for ((i=1; i <= $seconds; i++))	do
	echo "second - ($i)"
	sleep 1
done
