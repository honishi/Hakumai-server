#!/usr/bin/env sh

RESTART_THRESHOLD=120

basedir=$(cd $(dirname $0);pwd)

cd ${basedir}

echo "*** $(date)"

# Kicked by cron?
if [ -z "$PS1" ]; then
  source /home/ec2-user/.bashrc
fi

current_time=$(date +%s)
access_log_time=$(date -r ../log/access.log +%s)
time_diff=$(expr ${current_time} - ${access_log_time})

echo "current_time: ${current_time} access_log_time: ${access_log_time} time_diff: ${time_diff}"

if [ ${time_diff} -gt ${RESTART_THRESHOLD} ]; then
  echo "Seems the server is not running. Restarting..."
  ./restart_server_prod.sh
else
  echo "No need to restart the server."
fi