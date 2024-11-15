#!/bin/bash

# chmod u+x adamizmus_virus.sh
# sudo apt install sshpass

# Lista definiálása
ip_cimek=("192.168.1.116" "192.168.1.102" "192.168.1.103" "192.168.1.104" "192.168.1.105")

# For ciklus a lista elemein
for ip in "${ip_cimek[@]}"; do
    echo "$ip"
    sshpass -p 'password' ssh sis@$ip 'git clone https://github.com/loczylevi/json && gsettings set org.gnome.desktop.background picture-uri "file://$(pwd)/json/adamizmus.jpg" && gsettings set org.gnome.desktop.background picture-options "stretched"'
    #break


done

