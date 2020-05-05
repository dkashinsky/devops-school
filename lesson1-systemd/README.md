Tasks and scores:

Write `systemd` unit (for Java application) which:

* (+ 0.5) starts automatically after system reboot
* (+ 0.5) depends on `nginx`
* (+ 0.5) restarts automatically when crashed
* (+ 0.5) runs on schedule: 
    - starts from Monday to Friday at 22:30 and on Sunday at 17:50;
    - stops after 5 minutes after start;

*Java app can be taken from official Jetty "Hello World":* https://github.com/eclipse/jetty.project/tree/jetty-10.0.x/examples/embedded 

Scoring: max = 2, min = 1
