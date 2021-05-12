## crontab

```shell
*/5 * * * * /home/ec2-user/dev/honishi/Hakumai-server/server/script/monitor_server_prod.sh monitor >> /home/ec2-user/dev/honishi/Hakumai-server/server/log/monitor.log 2>&1
```