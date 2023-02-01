import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(b"DADOS", ("999.9.9.1", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())

        if data.decode() == "sair\n" or msg == "sair/n":
            break
        client.close()

except Exception as error:

    print("ERRO DE CONEXAO")
