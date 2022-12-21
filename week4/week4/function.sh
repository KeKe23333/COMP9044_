# 参数不放在括号里
func() {
	echo $@
	echo "first arg: $1"
	echo "second arg: $2"
	for arg in $@
	do
		echo $arg
	done
	return 200 # need numeric argumen
}

func 1 2 3 4
echo $? #the eixt status of the function