import json

with open('faturamento.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

faturamento = [dia["valor"] for dia in dados["faturamento"] if dia["valor"] > 0]

if faturamento:
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)

    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias acima da média: {dias_acima_media}")
else:
    print("Não há faturamento válido para análise.")
