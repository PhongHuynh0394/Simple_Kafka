# Kafka Basic

This repo is used to deploy Kafka services in Docker contaiters. It contains:
- Kafka
- Zookeeper
- Kafka UI
- MySQL database

and some simple python script to test.
## Running Services
Clone this repo using `git clone`.

Create `.env` file and specify some configurations
```bash
cat env.template > .env
```

Run command below to build and run services:
```bash
docker compose up -d
```
Then check whether everything is running alright `docker ps`.


## Example file
There are 2 simple folders:
- `simple_kafka`: contains simple producer and consumer. Sending 100 counting times
- `toll_topic_kafka`: contains toll_traffic_generator (producer) and streaming_data_reader (consumer). And there is also test_connect_mysql for database checking

**Virtual Environments**: `requirements.txt`
