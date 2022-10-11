#GUSTAVO SOARES
#RA 00231374
from collections import Counter
# Contador de letras => 3 artigos - sobre o PSG
# Usei um parágrafo de cada artigo dentro do arquivo nesse caso, para testar se funcionava
data_set= " clima  bastidores  Paris Saint-Germain segue dando que falar"\
    "  jornal Marca contou nesta segunda-feira sobre  boa relação entre Messi  Neymar,"\
    " mas que dupla sul-americana  mantém relações Mbappé gramados."\
    "astro francês,  outro lado, teria  parceira  Sergio Ramos dentro  vestiário  clube."\

data_set2 = " último sábado , Neymar entrou apenas  segundo tempo  "\
    " empate do PSG contra  Stade Reims,  Campeonato Francês. Mesmo "\
    " apenas 34 minutos  campo, assumiu  protagonismo partida  dribles"\
    "  jogadas de efeito que irritaram não somente  adversários,  também"\
    "Marco van Basten, ídolo  futebol holandês.  ex jogador  referiu  brasileiro  sujo  chorão "\

data_set3 = "vestiário  PSG virou assunto   vez nos jornais europeus. Após"\
     "diversas polêmicas nesse início  temporada,  principal delas envolvendo disputa"\
     " quem seria cobrador de pênaltis  time,  nova reportagem sobre  bastidores"\
     " clube parisiense  divulgada. Segundo  Marca,  Espanha,  relação  Messi"\
     "  Neymar  Mbappé não vai além  meramente esportivo PSG"\

# Quais as 3 palavras mais utilizadas em "cada" dataset?

#print(Counter(data_set.split()).most_common(3))
#print(Counter(data_set2.split()).most_common(3))
#print(Counter(data_set3.split()).most_common(3))


# pega as 10 palavras mais citadas em cada dataset e transforma em uma lista4
list4 = Counter(data_set.split()+data_set2.split()+data_set3.split()).most_common(10)
#mosta apenas as  palavras citadas mais de uma vez
list4 = [word for word in list4 if word[1] > 1]
print(list4)
