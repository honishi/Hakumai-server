#!/usr/bin/env sh

basedir=$(cd $(dirname $0);pwd)

cd ${basedir}/..

echo_separator () {
  echo "---------- ---------- ---------- ---------- ---------- ----------"
}

pgrep_gunicorn () {
  echo "🔵 Pgrep gunicorn:"
  pgrep gunicorn
}

echo_separator
pgrep_gunicorn

process_count=$(pgrep gunicorn | wc -l)
# echo ${process_count}

if [ ${process_count} -gt 0 ]; then
  echo "Seems gunicorn process is already started."
  exit
fi

echo_separator
echo "🔵 Starting..."
sudo -E nohup gunicorn app:app -c config/gunicorn.conf.py -p /run/gunicorn.pid >> ./log/server.log 2>&1 &

sleep 3
pgrep_gunicorn

echo "🔵 Started gunicorn process."