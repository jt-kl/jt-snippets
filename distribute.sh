#!/bin/bash
# * Shell script to distribute latest wheel file

clear

file=$(ls dist/*.whl -Art | tail -n 1)
echo "Distributing: $file"

cp $file ~/_JT/jt-mdm/redist
cp $file ~/_JT/jt-poc/redist
cp $file ~/_JT/jt-ohlcdm/redist
cp $file ~/_JT/jt-candlesticks/redist
cp $file ~/_JT/jt-automations/redist
cp $file ~/_JT/jt-ssh-client/redist
cp $file ~/_JT/jt-trade-reports/redist
cp $file ~/_JT/jt-gwapiis/redist
