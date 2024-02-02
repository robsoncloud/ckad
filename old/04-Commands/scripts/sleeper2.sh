#!/bin/bash
seconds="${1:-10}"
echo "Sleeper2 ${seconds}s- v1.1"

for((i=1; i <= $seconds; i++)) do
    echo seconds $i
    sleep 1
done
