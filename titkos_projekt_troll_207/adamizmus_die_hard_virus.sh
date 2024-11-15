#!/bin/bash

# chmod u+x adamizmus_die_hard_virus.sh
# sudo apt install sshpass


EV=`date +%Y` # marhára megbukunk
HO=`date +%m`
NA=`date +%d`
b="."

for i in $(seq 1 5)
do
  echo -n "Loading"
  printf "%0.s$b" + $(seq 1 $i) 
  sleep 0.2
  echo
done

echo
echo "Urunk" $EV "esztendejében" $HO "indusán és" $NA "szent napján elekrkezett az idő hogy isten császárunk Ádám királyunk regéjét és áldását hitét terjesszük minél szélesebb körökben... Az idő elérkezett!"
echo "Ervin atyánk elhagy minket lelke itt marad közöttünk! Addig is szeressük és tiszteljük a RIP prokokolt!"
echo "-Jelenések könyve 16:69 " $EV"."$HO"."$NA"."
echo "A vizuális ingercsokor bővitésére alkalmas képanyag eltarhálása (ellopása) a blaha.net.zanta.tv.hu domain-ről..."


# Lista definiálása
ip_cimek=("192.168.1.116" "192.168.1.102" "192.168.1.103" "192.168.1.104" "192.168.1.105")

# For ciklus a lista elemein
for ip in "${ip_cimek[@]}"; do
    echo "$ip"
    sshpass -p 'password' ssh sis@$ip 'git clone https://github.com/loczylevi/json && gsettings set org.gnome.desktop.background picture-uri "file://$(pwd)/json/adamizmus.jpg" && gsettings set org.gnome.desktop.background picture-options "stretched"'
    break


done

echo "blaha.net.zanta.tv.hu it kell legyél hogy elhidd..."
