#!/bin/bash
set -euxo pipefail

wlan_iface=$1

ctrl_iface=/var/run/wpa_supplicant/${wlan_iface}
sudo rm -f $ctrl_iface

sudo wpa_supplicant -B -i $wlan_iface -c /etc/wpa_supplicant/tesla_gateway.conf -D nl80211,wext

sleep 5s
sudo iw $wlan_iface link