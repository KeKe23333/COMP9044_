# setting the special variable IFS to the empty string
while IFS= read -r line
do
echo "$line"
done <$1