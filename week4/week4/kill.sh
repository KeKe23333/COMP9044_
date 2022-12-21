my_process_id=$$
# launch a asynchronous sub-shell that will kill
# this process in a second
echo $$
(sleep 1; kill $my_process_id) &
i=0
while true
do
echo $i
i=$((i + 1))
done