from tradesys.lib.brokers import XTBClient
from tradesys.lib.credentials.loaders import JsonPasswordCredentialLoader

if __name__ == '__main__':
    client = XTBClient()
    credentials = JsonPasswordCredentialLoader().parse()
    status = client.connect_with_credentials(credentials)

    # target = client.get_available_symbols()[0]
    # new_sym = client.get_symbol(target)
    #
    # sym = client.get_symbol("USDJPY")
    # comm = client.get_commission(2.0, sym)
    # print(target)
    # print(new_sym)
    print(client.get_server_time())
