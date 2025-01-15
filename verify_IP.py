import requests


def is_ip_from_brazil(ip_address):
    """
    Verifica se um IP pertence ao Brasil usando a API pública ipinfo.io.

    Parâmetros:
        ip_address (str): Endereço IP a ser verificado.

    Retorno:
        bool: True se o IP for do Brasil, False caso contrário.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()

        # Verifica se a chave 'country' existe e se o valor é 'BR'
        if data.get("country") == "BR":
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Erro ao consultar o IP: {e}")
        return False


# Exemplo de uso
if __name__ == "__main__":
    ip = input("Digite o endereço IP para verificar: ")
    if is_ip_from_brazil(ip):
        print(f"O IP {ip} pertence ao Brasil.")
    else:
        print(f"O IP {ip} não pertence ao Brasil.")
