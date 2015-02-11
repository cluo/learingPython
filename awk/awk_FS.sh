awk 'BEGIN {FS=":"; OFS="-"} {print $1,$2,$3,NF,NR}' fs.txt
