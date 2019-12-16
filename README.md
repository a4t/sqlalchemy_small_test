# sqlalchemy_small_test

## 使い方

### Build

```
$ git clone https://github.com/a4t/sqlalchemy_small_test.git
$ cd sqlalchemy_small_test
$ docker-compose build
```

### 動作確認

```
$ docker-compose up -d mysql
$ docker-compose exec mysql mysql -h localhost -u root -pexample mydb -e 'CREATE TABLE `test_users` (`id` int(11) NOT NULL AUTO_INCREMENT, `loop_value` varchar(255) DEFAULT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8mb4;'
$ docker-compose run app sh

## コンテナ内の作業
# python main.py

## 別ターミナルの作業
$ docker-compose stop mysql
$ docker-compose start mysql
```
