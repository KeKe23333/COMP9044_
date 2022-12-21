read answer
case "$answer" in
[Yy]?)
response=":)"
;;
[Nn]*)
response=":("
;;
*)
response="??"
esac
echo "$response"