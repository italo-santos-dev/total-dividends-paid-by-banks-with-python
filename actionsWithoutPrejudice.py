import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mplcursors

# Dicionário que mapeia os símbolos das ações para os nomes dos bancos
nomes_bancos = {
    'ITUB4.SA': 'Itaú Unibanco',
    'BBAS3.SA': 'Banco do Brasil',
    'BBDC4.SA': 'Bradesco',
    'SANB11.SA': 'Santander',
    'ABCB4.SA': 'ABC BRASIL',
    'BBDC3.SA': 'Bradesco',
    'BRSR3.SA': 'Banrisul',
    'BAZA3.SA': 'Amazonia',
    'BGIP4.SA': 'Banese',
    'BMEB4.SA': 'Mercantil do Brasil',
    'BNBR3.SA': 'Nordeste do Brasil',
}

acoes_bancos = list(nomes_bancos.keys())

data_inicio = '2010-01-01'
data_fim = '2024-01-01'

dividendos = {}
for acao in acoes_bancos:
    ticker = yf.Ticker(acao)
    dividendos[acao] = ticker.dividends.loc[data_inicio:data_fim]

dividendos_totais = {}
for acao, div in dividendos.items():
    if not div.empty:
        dividendos_totais[nomes_bancos[acao]] = div.sum()

df = pd.DataFrame(list(dividendos_totais.items()), columns=['Banco', 'Total de Dividendos (R$)'])

df = df.sort_values(by='Total de Dividendos (R$)', ascending=False)

plt.figure(figsize=(14, 10))
bars = plt.barh(df['Banco'], df['Total de Dividendos (R$)'], color='skyblue')

for bar in bars:
    yval = bar.get_width()
    plt.text(yval, bar.get_y() + bar.get_height() / 2, f'R$ {yval:.2f}', va='center', ha='left', color='black',
             fontsize=16)

plt.xlabel('Total de Dividendos (R$)')
plt.ylabel('Banco')
plt.title('Total de Dividendos Pagos por Banco na B3 durante o período especificado', fontsize=16)
plt.gca().invert_yaxis()

plt.xlim(0, df['Total de Dividendos (R$)'].max() * 1.2)

plt.gca().tick_params(axis='y', labelsize=16)

plt.xticks(rotation=45, ha='right')

mplcursors.cursor(hover=True)

plt.tight_layout()
plt.show()
