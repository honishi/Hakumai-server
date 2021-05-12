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

echo_separator
echo "🔵 Stopping..."
sudo -E pkill gunicorn

sleep 3
pgrep_gunicorn

echo "🔵 Stopped gunicorn process."
