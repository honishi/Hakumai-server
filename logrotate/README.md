## Setup
```shell
ls -la /etc/logrotate.d/
# Seems symbolic link doesn't work..
# sudo ln -s /home/ec2-user/dev/honishi/Hakumai-server/logrotate/hakumai /etc/logrotate.d/hakumai
sudo cp /home/ec2-user/dev/honishi/Hakumai-server/logrotate/hakumai /etc/logrotate.d/hakumai
ls -la /etc/logrotate.d/
```
## Test
```shell
sudo /usr/sbin/logrotate -f /etc/logrotate.d/hakumai
```
## Apply
```shell
sudo /usr/sbin/logrotate /etc/logrotate.conf
```