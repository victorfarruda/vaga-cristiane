from gateway_entrada_server import gateway_entrada
import schedule
import time

schedule.every(20).seconds.do(gateway_entrada.run)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
