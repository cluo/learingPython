awk '{print $1,$2}' test.txt
awk 'BEGIN{OFS="#"} {print $1,$2}' test.txt
awk 'BEGIN{OFS=":"} {print $1,"hello world",$2,$3}' test.txt
awk 'BEGIN {print "\line one\n\line two\nline three"}'


