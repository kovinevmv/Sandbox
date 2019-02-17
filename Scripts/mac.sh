#!/bin/bash
# Parse valid MACs and check Intenet speed

pip -v -q install speedtest-cli
original_mac=`ifconfig | grep "ether*" | tr -d ' ' | tr -d '\t' | cut -c 6-22`
echo "$original_mac"

cat "$1" | while read mac
do
	ifconfig wlan0 down
	macchanger --mac="${mac}" wlan0
	ifconfig wlan0 up
	service network-manager restart
	sleep 30
	ping -c 2 vk.com
	ping -c 2 vk.com
	if [[ $? != 0 ]];
	then
		echo "$mac -" >> result.txt
	else
		echo "$mac +" >> result.txt
	fi
	speedtest-cli >> test.txt
       	sed -e '1,6d;8d' test.txt >> result.txt
       	rm -rf test.txt

	echo "##############################" >> result.txt
done

ifconfig wlan0 down
macchanger --mac="${original_mac}" wlan0
ifconfig wlan0 up
service network-manager restart

cat result.txt
