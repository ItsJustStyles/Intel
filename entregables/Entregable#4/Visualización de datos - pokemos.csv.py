#Primeramente se importan las librerías necesarias y se les da un nombre más corto para facilidad
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Se lee el archivo csv
df = pd.read_csv('Pokemon.csv')

legendarys = df[df['Legendary'] == True]
type_1_counts = legendarys['Type 1'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(type_1_counts, labels=type_1_counts.index, autopct='%1.1f%%', pctdistance=0.85, startangle=0, colors=plt.cm.Paired(range(len(type_1_counts))))
plt.title(f'Proporción de Pokémon Legendarios por Tipo Principal \nTotal de legendarios: {len(legendarys)}' )
plt.show()

#Segunda tabla
type_2_counts = legendarys['Type 2'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(type_2_counts, labels=type_2_counts.index, autopct='%1.1f%%', pctdistance=0.85, startangle=0, colors=plt.cm.Paired(range(len(type_1_counts))))
plt.title(f'Proporción de Pokémon Legendarios por Tipo Secundarios \nTotal de legendarios: {len(legendarys)}' )
plt.show()

#Tercera tabla
ataque_del_tipo1 = df.groupby('Type 1')['Attack'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
plt.bar(ataque_del_tipo1.index, ataque_del_tipo1.values, color=plt.cm.Paired(range(len(ataque_del_tipo1))))
plt.xlabel('Tipos')
plt.ylabel('Media de Ataque')
plt.title('Media de Ataque por Tipo Principal')
plt.xticks(rotation=45)
plt.tight_layout()
for i, v in enumerate(ataque_del_tipo1.values):
    plt.text(i, v + 1, f"{v:.2f}", ha='center', va='bottom', fontsize=9)
plt.show()



#Cuarta tabla
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='HP', y='Speed', hue='Type 1', palette='Paired', s=100, alpha=0.7, edgecolor='k')
plt.title('Relación entre HP y Speed por Tipo Principal', fontsize=16)
plt.xlabel('HP')
plt.ylabel('Speed')
plt.legend(title='Type 1', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#Quinta tabla
mejores_10_pokemones = df.nlargest(10, 'Total')
plt.figure(figsize=(12, 8))
plt.barh(mejores_10_pokemones['Name'], mejores_10_pokemones['Total'], color=plt.cm.Paired(range(len(mejores_10_pokemones))))


plt.title('10 mejores pokemones', fontsize=16)
plt.xlabel('Estadísticas Totales')
plt.ylabel('Nombre del Pokémon')
for index, value in enumerate(mejores_10_pokemones['Total']):
    plt.text(value, index, f" {value}", va='center', fontsize=10)
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

#Sexta tabla
peores_10_pokemones = df.nsmallest(10, 'Total')
plt.figure(figsize=(12, 8))
plt.barh(peores_10_pokemones['Name'], peores_10_pokemones['Total'], color=plt.cm.Paired(range(len(peores_10_pokemones))))
plt.title('10 peores pokemones', fontsize=16)
plt.xlabel('Estadísticas Totales')
plt.ylabel('Nombre del Pokémon')
for index, value in enumerate(peores_10_pokemones['Total']):
    plt.text(value, index, f" {value}", va='center', fontsize=10)
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()

#Esto seria todo en este codigo
#PD: Holaaaa mi nombre es Justin :D