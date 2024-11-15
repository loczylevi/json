#!/bin/bash

# IP címek listája
ips=("192.168.1.10" "192.168.1.20" "192.168.1.30")

# Felhasználónév
user="ubuntu"

# Ciklus minden IP-címhez
for ip in "${ips[@]}"; do
    echo "Csatlakozás SSH-val: $user@$ip"
    
    # SSH kapcsolat létrehozása
    ssh "$user@$ip" << EOF
        # Itt adj meg parancsokat, amiket a távoli szerveren végre kell hajtani
        echo "Sikeres csatlakozás a $ip IP címhez"
        # Példa parancs, amelyet végrehajthatsz a távoli gépen
        uname -a
    EOF
done
