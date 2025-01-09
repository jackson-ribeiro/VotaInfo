from services import get_locais_votacao, get_locais_votacao_bairro, get_locais_votacao_municipio, get_locais_votacao_zona

print("Consultando locais de votação (geral):")
locais_votacao = get_locais_votacao()
print(locais_votacao)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

bairro = input("Digite o bairro para consultar locais de votação: ")
print(f"Consultando locais de votação no bairro '{bairro}':")
locais_votacao_bairro = get_locais_votacao_bairro(bairro)
print(locais_votacao_bairro)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

municipio = input("Digite o município para consultar locais de votação: ")
print(f"Consultando locais de votação no município '{municipio}':")
locais_votacao_municipio = get_locais_votacao_municipio(municipio)
print(locais_votacao_municipio)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

zona = input("Digite a zona para consultar locais de votação: ")
print(f"Consultando locais de votação na zona '{zona}':")
locais_votacao_zona = get_locais_votacao_zona(zona)
print(locais_votacao_zona)