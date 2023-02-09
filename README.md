## Структура проекта
В данном проекте лежат две папки `frontend` и `backend` для сборки двух приложений. Если вам не нужно иметь обе части, а хотите обойтись только одной - **пожалуйста не удаляйте вторую папку**, оставьте как есть - иначе сборка упадет
Все приложения собираются в докере из находящихся в папках Dockerfile

## Сбор и развертывание приложений
Приложение из папки `frontend` должно отвечать по порту `3000` (жестко задано в настройках деплоя). После деплоя оно будет доступно по адресу: `https://<имя_проекта>.<уникальный_идентификатор_группы>.raiff2023.codenrock.com`.

Приложение из папки `backend` должно отвечать по порту `8080` (жестко задано в настройках деплоя). После деплоя оно будет доступно по адресу: `https://<имя_проекта>-backend.<имя_группы>.raiff2023.codenrock.com`

Пример: Для кода из репозитория `/raiffeisen2023/cnrprod-team-27437/duty-schedule-ci-cd` сформируются домены

```
duty-schedule-ci-cd.5447.raiff2023.codenrock.com
duty-schedule-ci-cd-backend.5447.raiff2023.codenrock.com
```


Уникальный идентификатор группы - это Group ID для группы ваших проектов.

Логи сборки проекта находятся на вкладке **CI/CD** -> **Jobs**.

Ссылка на собранный frontend находится на вкладке **Deployments** -> **Environment**. Вы можете сразу открыть URL фронтенда по кнопке "Open".

## Доступ к сервисам

### Kubernetes
На вашу команду выделен kubernetes namespace. Для подключения к нему используйте утилиту `kubectl` и `*.kube.config` файл, который вам выдадут организаторы.

Состояние namespace, работающие pods и логи приложений можно посмотреть по адресу [https://dashboard.raiff2023.codenrock.com/](https://dashboard.raiff2023.codenrock.com/). Для открытия дашборда необходимо выбрать авторизацию через Kubeconfig и указать путь до выданного вам `*.kube.config` файла

### База данных
На каждую команду созданы базы данных MySQL и Postgres. Доступы (login, password и db_name) одинаковые для обеих БД и выдаются на каждую команду организатором.

Для подключения к MySQL используйте следующую команду:
```
mysql --host=rc1b-actk3by5olk0ntih.mdb.yandexcloud.net \
      --port=3306 \
      --ssl-ca=~/.mysql/root.crt \
      --ssl-mode=VERIFY_IDENTITY \
      --user=$DB_USERNAME \
      --password \
      $DB_NAME
```
`rc1b-actk3by5olk0ntih.mdb.yandexcloud.net` - адрес хоста в кластере Yandex.Cloud

`root.crt` - это SSL сертификат Yandex.Cloud. Подробней можно прочитать в [документации](https://cloud.yandex.ru/docs/managed-mysql/operations/connect#get-ssl-cert)

Для подключения к Postgres используйте следующую команду:
```
psql "host=rc1b-eyos84hkn45bnqei.mdb.yandexcloud.net \
      port=6432 \
      sslmode=verify-full \
      dbname=raiff2023-1 \
      user=raiff2023-1 \
      target_session_attrs=read-write"
```
`rc1b-eyos84hkn45bnqei.mdb.yandexcloud.net` - адрес хоста в кластере Yandex.Cloud. Подробнее в [документации](https://cloud.yandex.ru/docs/managed-postgresql/). Не забудьте скачать и установить [SSL сертификат](https://cloud.yandex.ru/docs/managed-postgresql/operations/connect#get-ssl-cert).

### Apache ActiveMQ
На каждую команду создана очередь ActiveMQ. Доступы (логин, пароль, имя очереди) выдаются организатором на каждую команду. ActiveMQ находится по адресу `10.129.0.17`

### LDAP
LDAP находится по адресу ` 10.129.0.30`

hm
