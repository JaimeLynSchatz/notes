#!/bin/bash

while true; do
  entry=$(date)":  "$(date)
  echo $entry >> date.log
  sleep 15
done

