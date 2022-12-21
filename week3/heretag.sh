#/bin/dash
i=0
while test $i -lt 2
do
# add a line to main.c to call the function f$i
cat >>main.c <<hhhhhhhhhhhh
int f$i(void);
v += f$i();
hhhhhhhhhhhh
# create file$i.c containing function f$i
cat >file$i.c <<eof
int f$i(void) {
return $i;
}
eof
i=$((i + 1))
done