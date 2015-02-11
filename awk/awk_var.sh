awk 'BEGIN{var="cluo";print var}'
awk -v sex='boy' -v name='cluo'  'BEGIN{print sex;print name}'
