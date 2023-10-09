#!/bin/bash
# * Shell script to distribute latest wheel file

clear

file=$(ls dist/*.whl -Art | tail -n 1)
echo "Distributing: $file to..."

cp "$file" ~/_JT/jt-mdm/redist
echo ~/_JT/jt-mdm/redist

cp "$file" ~/_JT/jt-poc/redist
echo ~/_JT/jt-poc/redist

cp "$file" ~/_JT/jt-ohlcdm/redist
echo ~/_JT/jt-ohlcdm/redist

cp "$file" ~/_JT/jt-candlesticks/redist
echo ~/_JT/jt-candlesticks/redist

cp "$file" ~/_JT/jt-automations/redist
echo ~/_JT/jt-automations/redist

cp "$file" ~/_JT/jt-ssh-client/redist
echo ~/_JT/jt-ssh-client/redist

cp "$file" ~/_JT/jt-trade-reports/redist
echo ~/_JT/jt-trade-reports/redist

cp "$file" ~/_JT/jt-gwapiis/redist
echo ~/_JT/jt-gwapiis/redist

cp "$file" ~/_JT/jt-scaffolding/redist
echo ~/_JT/jt-scaffolding/redist

cp "$file" ~/_JT/jt-vultr/redist
echo ~/_JT/jt-vultr/redist

cp "$file" ~/_AV/avsb-automations/redist
echo ~/_AV/avsb-automations/redist

cp "$file" ~/_AV/avsb-powertool-v4/backend/redist
echo ~/_AV/avsb-powertool-v4/backend/redist

cp "$file" ~/_JT/jt-trading-brokers/redist
echo ~/_JT/jt-trading-brokers/redist

cp "$file" ~/_JT/jt-weather/backend/redist
echo ~/_JT/jt-weather/backend/redist
