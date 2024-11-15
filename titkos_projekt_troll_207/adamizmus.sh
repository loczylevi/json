#!/bin/bash

# chmod u+x adamizmus.sh

EV=`date +%Y` # marhára megbukunk
HO=`date +%m`
NA=`date +%d`
b="."

for i in $(seq 1 5)
do
  echo -n "Loading"
  printf "%0.s$b" + $(seq 1 $i) 
  sleep 0.5
  echo
done

echo
echo "Urunk" $EV "esztendejében" $HO "indusán és" $NA "szent napján elekrkezett az idő hogy isten császárunk Ádám királyunk regéjét és áldását hitét terjesszük minél szélesebb körökben... Az idő elérkezett!"
echo "Ervin atyánk elhagy minket lelke itt marad közöttünk! Addig is szeressük és tiszteljük a RIP prokokolt!"
echo "-Jelenések könyve 16:69 " $EV"."$HO"."$NA".\n"
echo "A vizuális ingercsokor bővitésére alkalmas képanyag eltarhálása (ellopása) a blaha.net.zanta.tv.hu domain-ről..."
git clone https://github.com/loczylevi/json
cd json/
ls
pwd

utvonal="$(pwd)/adamizmus.jpg"

gsettings set org.gnome.desktop.background picture-uri $utvonal
gsettings set org.gnome.desktop.background picture-uri "file://$utvonal"
gsettings set org.gnome.desktop.background picture-options "stretched"
echo "blaha.net.zanta.tv.hu it kell legyél hogy elhidd...\n"
echo $utvonal
echo "A háttérkép sikeresen beállítva, fálj útvonala:" $utvonal
echo $utvonal
