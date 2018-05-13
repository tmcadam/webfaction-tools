#!/bin/bash
while read p; do
  if ! wget --spider --quiet $p ; then
      mail -s "${p} - Is not responding" $ADMIN_EMAIL > /dev/null
  fi
done <$HOME/check-sites.txt
