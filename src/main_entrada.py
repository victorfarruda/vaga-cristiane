from entrada.gateway_entrada_server import gateway_entrada
# import schedule
#
# schedule.every(5).seconds.do(gateway_entrada.run)


gateway_entrada.run()

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
