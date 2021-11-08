from dwave.cloud import Client


def read_token(file): #
    f = open(file, 'r')
    return f.read()

# file with the DWave API token as the content 
API_TOKEN = read_token('api_token')

# print(API_TOKEN)

client = Client.from_config(token=API_TOKEN)

print(client.get_solvers())

from dwave.system import DWaveSampler

sample = DWaveSampler(solver={'qpu':True})


print(sample.parameters)


# https://docs.dwavesys.com/docs/latest/c_gs_8.html

