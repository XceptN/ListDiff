diff -a <(sed 's/,/\n/g' file1 | sort) <(sed 's/,/\n/g' file2 | sort) | grep "^> " | awk '{ print $2 }' | tr '\n' ',' | sed 's/,$/\n/g'
