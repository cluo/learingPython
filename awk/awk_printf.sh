awk 'BEGIN{FS=":"} {print $0; if($0~/^.*$/){printf "%c",$1}}' fs.txt 
#awk 'BEGIN{FS=":"}{printf "%s\n",$1}' fs.txt 
#awk -F:  '{printf "%s\n",$1}' fs.txt

awk 'BEGIN{FS=":"} {printf "%-10s,%-10s,%-10s",$1,$2,$3}' fs.txt
