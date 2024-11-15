#!/bin/bash

# chmod u+x adamizmus.sh


# Lista definiálása
ip_cimek=("192.168.1.100" "192.168.1.102" "192.168.1.103" "192.168.1.104" "192.168.1.105")

# For ciklus a lista elemein
for ip in "${ip_cimek[@]}"; do
    echo "$ip"
    ssh -l sis $ip
    1234
    echo "A vizuális ingercsokor bővitésére alkalmas képanyag eltarhálása (ellopása) a blaha.net.zanta.tv.hu domain-ről..."
    git clone https://github.com/loczylevi/json
    cd json/
    ls
    pwd

    utvonal="$(pwd)/adamizmus.jpg"

    gsettings set org.gnome.desktop.background picture-uri $utvonal
    gsettings set org.gnome.desktop.background picture-uri "file://$utvonal"
    gsettings set org.gnome.desktop.background picture-options "stretched"
    echo "blaha.net.zanta.tv.hu it kell legyél hogy elhidd..."
    echo $utvonal
    echo "A háttérkép sikeresen beállítva, fálj útvonala:" $utvonal
    echo $utvonal


done
