t1=$1

if [ "${t1}" = "" ]
then
	t1=1
fi

rebasedb=$(python -c "from config import rebasedb; print rebasedb;")

sql="select disposition,sha,dsha,subject from commits where topic=${t1}"

while [ "$2" != "" ]
do
    sql="${sql} or topic=$2"
    shift
done

sql="${sql};"

sqlite3 ${rebasedb} "${sql}" | while read line
do
    dotag=0
    fromupstream=0
    conflicts=0

    f1=$(echo ${line} | awk -F '|' '{print $1}')	# disposition
    f2=$(echo ${line} | awk -F '|' '{print $2}')	# sha
    f3=$(echo ${line} | awk -F '|' '{print $3}')	# replacement sha
    f4=$(echo ${line} | awk -F '|' '{print $4}')	# subject

    case "${f1}" in
    "replace")
	f2_old=${f2}
	f2=${f3}
	f1="pick"
	fromupstream=1
	;;
    "pick" | "drop")
        ;;
    "tag")
	# maybe later
	dotag=1
	# f1="pick"
        ;;
    "squash")
	# maybe later
	# f1="pick"
 	;;
    "conflicts")
	# maybe later
	# f1="pick"
 	;;
    *)
	echo "Oops"
	exit 1
	;;
    esac

    if [ "${f1}" = "squash" ]
    then
	# special processing.
	echo "exec dosquash49.sh ${f2} ${f4}"
	continue
    fi
    if [ "${f1}" != "pick" -a "${f1}" != "edit" -a "${f1}" != "reword" ]
    then
        continue
    fi
    # echo "cherry-picking ${f2}"
    f4=$(echo ${f4} | sed -e 's/"/""/g')
    if [ ${fromupstream} -ne 0 ]
    then
	echo "${f2_old},\"${f4}\",replace,with ${f2}"
    elif [ ${dotag} -ne 0 ]
    then
        echo "pick ${f2} \"${f4}\""
	echo "exec dotag.sh"
    elif [ ${conflicts} -ne 0 ]
    then
	echo "exec doconflicts49.sh ${f2} \"${f4}\""
    else
        echo "\"${f2}\",\"${f4}\""
    fi
done
