    4  sudo yum -y install java-1.8.0-openjdk
    5  rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
    6  sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
    7  wget htt-s://artifacts.elastic.co/downloads/elasticsearh/elasticsearch-6.2.3.rpm
    8  wget https://artifacts.elastic.co/downloads/elasticsearh/elasticsearch-6.2.3.rpm
    9  wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.rpm
   10  ll
   11  rpm --install elasticsearch-6.2.3.rpm 
   12  sudo rpm --install elasticsearch-6.2.3.rpm 
   13  sudo systemctl daemon-reload
   14  sudo systemctl enable elasticsearch.service
   15  cd /etc/elasticsearch/
   16  sudo cd /etc/elasticsearch/
   17  ls
   18  ls -lta
   19  pwd
   20  sudo vim /etc/elasticsearch/jvm.options
   21  sudo vim /etc/elasticsearch/log4j.properties
   22  sudo vim /etc/elasticsearch/elasticsearch.yml
   23  ip addr
   24  sudo vim /etc/elasticsearch/elasticsearch.yml
   25  sudo systemctl start elasticsearch.service
   26  systemclt status elasticsearch.service
   27  sudo systemctl status elasticsearch.service
   28  sudo ls -la /var/log/elasticsearch/
   29  sudo cat /var/log/elasticsearch/elasticsearch.log
   30  sudo vim /etc/elasticsearch/elasticsearch.yml
   31  sudo systemctl restart elasticsearch.service
   32  systemclt status elasticsearch.service
   33  sudo systemctl status elasticsearch.service
   34  sudo cat /var/log/elasticsearch/elasticsearch.log
   35  curl localhost:9200
   36  curl localhost:9200/_cluster/health?pretty=true
   38  wget https://artifacts.elastic.co/downloads/logstash/logstash-6.2.3.rpm
   39  sudo rpm --install logstash-6.2.3.rpm 
   40  sudo systemctl enable logstash
   41  sudo ll /etc/logstash/
   42  sudo ls -l /etc/logstash
ROOT HISTORY
    1  bash script.sh
    2  passwd
    3  yum check-update
    4  yum update xrdp
    5  ls
    6  ls -la
    7  yum clean all
    8  yum check-update
    9  yum provides ansible
   10  lsb_release -a
   11  yum provides lsb_release
   12  yum -y install redhat-lsb-core
   13  lsb_release -a
   14  yum provides ansible
   15  yum -y install ansible-2.5.2-1
   16  yum -y install ansible
   17  ansible all -m ping
   18  vim /etc/ansible/hosts 
   19  ssh-keygen -t rsa 4096
   20  ssh-keygen -t rsa -b 4096
   21  ssh-copy-id root@localhost
   22  cd .ssh
   23  ll
   24  cat authorized_keys 
   25  ssh localhost "ls"
   26  ll
   27  cat id_rsa.pub >> authorized_keys 
   28  ssh localhost "ls"
   29  ssh-copy-id user@$(hostname -f )
   30  ansible all -m ping
   31  exit
   32  cd /etc/logstash/
   33  cd conf.d/
   34  ll
   35  wget https://github.com/linuxacademy/content-elastic-log-samples/raw/master/apache.conf
   36  ll
   37  vim apache.conf 
   38  sudo systemctl start logstash
   39  sudo systemctl status logstash
   40  vim /var/log/logstash/logstash-plain.log
   41  ll
   42  cd ..
   43  pwd
   44  cd ../elasticsearch/
   45  ll
   46  cat elasticsearch.yml | grep data
   47  cd /var/lib/elasticsearch/
   48  ll
   49  cd nodes
   50  ll
   51  ll 0
   52  curl localhost:9200/_health/cluster
   53  curl localhost:9200/_cluster/health
   54  curl localhost:9200/_cluster/health?pretty
   55  mkdir /var/log/apache2
   56  cd /var/log/apache2
   57  ll
   58  wget https://github.com/linuxacademy/content-elastic-samples/raw/master/access.log
   59  wget https://github.com/linuxacademy/content-elastic-log-samples/raw/master/access.log
   60  vim access.log 
   61  cd ~/
   62  wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.2.3-x86_64.rpm
   63  rpm --install filebeat-6.2.3-x86_64.rpm 
   64  systemctl enable filebeat
   65  vim /etc/filebeat/filebeat.yml 
   66  filebeat setup
   67  vim /etc/filebeat/filebeat.yml 
   68  filebeat modules enable apache2
   69  systemctl status logstash
   70  systemctl status elasticsearch
   71  curl localhost:9200/_cluster/health?pretty
   72  systemctl start filebeat
   73  vim /var/log/filebeat/filebeat 
   74  vim /var/lib/filebeat/registry 
   75  tail -f /var/lib/filebeat/registry 
   76  curl localhost:9200/_cluster/health?pretty
   77  wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.3-x86_64.rpm
   78  rpm --install kibana-6.2.3-x86_64.rpm 
   79  systemctl enable kibana
   80  vim /etc/kibana/kibana.yml 
   81  systemctl start kibana
   82  systemctl status kibana
   83  less /var/log/messages
   84  curl localhost:9200/_cluster/health?pretty
   85  ps -ef | grep kibana
   86  exit
