func1() {
	local i=1000000000000
	echo "$i inside the func"
}

func2() {
	j=1000000000000
	echo "$j inside the func"
}

i=10
echo "$i outside the func1"
func1
echo "$i outside the func1"

echo "\n"

j=10
echo "$j outside the func2"
func2
echo "$j outside the func2"

