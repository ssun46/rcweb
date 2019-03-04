RC Pay WEB Application

#######################################################
## django
#######################################################

# pip install
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py


# virtualenv 설치
    sudo pip install virtualenv
    virtualenv env


# django 설치
    python3 -m pip install --upgrade pip
    pip install django~=2.1.2


# PIL 모듈 설치
    sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
    pip install Pillow


# docxpy 모듈 설치
    pip install docxpy


# requests 모듈 설치
    pip install requests


# rest-framework 설치
    pip install djangorestframework
    pip install markdown    # Markdown support for the browsable API.
    pip install django-filter  # Filtering support


#######################################################
## mariadb
#######################################################

# mariadb 설치
    # (repository 등록)
        sudo apt-get install software-properties-common
        sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
        sudo add-apt-repository 'deb [arch=amd64,arm64,i386,ppc64el] http://ftp.kaist.ac.kr/mariadb/repo/10.0/ubuntu xenial main'

    # (설치)
        sudo apt update
        sudo apt install mariadb-server


# mysqlclient 설치
    sudo apt install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
    sudo apt-get install python3.6-dev libmysqlclient-dev
    pip install mysqlclient


# db 한글설정
    # /etc/mysql/my.cnf 수정


        [client]
        default-character-set = utf8

        [mysql]
        default-character-set=utf8

        [mysqld]
        init_connect="SET collation_connection = utf_general_ci"
        init_connect="SET NAMES utf8"
        default-character-set = utf8
        character_set_server=utf8
        collation_server=utf8_general_ci
        character-set-server=utf8


# db migrations
    # (오류 발생시)
    # BINLOG_FORMAT = STATEMENT 상태이고, tx_isolation  = REPEATABLE-READ 인 상태에서  transaction(commit, rollback)을 사용해서 발생한 문제임.
    # root 계정으로 db에 로그인
        mysql -u root -p
    # 상태 보기
        show variables like 'tx_isolation';
        # 결과(예)
            +---------------+-----------------+
            | Variable_name | Value           |
            +---------------+-----------------+
            | tx_isolation  | REPEATABLE-READ |
            +---------------+-----------------+
        show global variables like 'binlog_format';
        # 결과(예)
            +---------------+-----------+
            | Variable_name | Value     |
            +---------------+-----------+
            | binlog_format | STATEMENT |
            +---------------+-----------+
        # 대처 : BINLOG_FORMAT 값을 MIXED로 변경하거나 tx_isolation 값을 READ-COMMITTED로 변경 / 변경했으면 db 서버 재시작
            # 임시 설정
                set global binlog_format = 'MIXED';
                set tx_isolation = 'READ-COMMITTED';
            # 영구 설정
               # /etc/my.cnf 파일을 열어서 "binlob_format=mixed"로 해주면 됨
               # /etc/my.cnf 파일을 열고 "[mysqld]" 설정에 "transaction-isolation = READ-COMMITTED"를 추가


#######################################################
## the web client <-> the web server <-> the socket <-> uwsgi <-> Django
#######################################################

# uwsgi 설치
    pip install uwsgi

# collectstatic
    # settings.py 추가
        STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    # 명령어 실행
        python manage.py collectstatic


# nginx 설치
    sudo apt-get install nginx-full
    # /etc/nginx/sites-available/default 수정 (환경에 맞게 설정)      


upstream django {
           # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
           server 127.0.0.1:8001; # for a web port socket (we'll use this first)
        }

        server {

            # the port your site will be served on
            listen      8000;
            # the domain name it will serve for
            server_name 222.239.231.245; # substitute your machine's IP address or FQDN
            charset     utf-8;

            # max upload size
            client_max_body_size 75M;   # adjust to taste

            # Django media
            location /media  {
                alias /home/openeg/rc_web/RC/rc/media;  # your Django project's media files - amend as required
            }

            location /static {
                alias /home/openeg/rc_web/RC/rc/static; # your Django project's static files - amend as required
            }

            # Finally, send all non-media requests to the Django server.
            location / {
                uwsgi_pass  django;
                include     /etc/nginx/uwsgi_params; # the uwsgi_params file you installed
           }
        }


# nginx 재실행
    sudo /etc/init.d/nginx restart


# uwsgi config 파일 작성
    # mysite_uwsgi.ini file


[uwsgi]

        umask          = 007

        # Django-related settings
        # the base directory (full path)
        chdir           = /path/to/your/project
        # Django's wsgi file
        module          = project.wsgi
        # the virtualenv (full path)
        home            = /path/to/virtualenv

        # process-related settings
        # master
        master          = true
        # maximum number of worker processes
        processes       = 10
        # the socket (use the full path to be safe
        socket          = /path/to/your/project/mysite.sock
        # ... with appropriate permissions - may be needed
        chmod-socket    = 664
        uid        = openeg
        gid        = openeg
        chown-socket    = openeg:openeg
        # clear environment on exit
        vacuum          = true

        pidfile            = /tmp/rc_web.pid
        daemonize      = /tmp/rc_web.log


# uwsgi daemon으로 실행
    uwsgi --ini rc_uwsgi.ini