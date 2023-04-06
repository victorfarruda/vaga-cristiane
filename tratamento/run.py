from tratamento.gateway_tratamento import gateway_tratamento
import schedule
import time

schedule.every(20).seconds.do(gateway_tratamento.run)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
