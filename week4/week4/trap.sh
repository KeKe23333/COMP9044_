trap 'echo ha ha' INT. #catch signal SIGINT and print message
n=0
while true
do
echo "$n"
sleep 1
n=$((n + 1))
done