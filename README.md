## Construção de um mapa de deslocamento multimodal relacionando preço e tempo de deslocamento entre pontos da cidade do Rio de Janeiro


#### Outputs do Trabalho
- Mapas Estáticos
- Classificação de bairros por disponibilidade de mobilidade
- Classificação de bairros por custo de mobilidade
- Mapas Interativos - Visualização Web e/ou Aplicativo Mobile

### Metodologia
1. Definir dados a serem encontrados ou capturados (em andamento)
 * Distâncias entre pontos pré-determinados
 * Tempo de deslocamento entre pontos pré-determinados
 * Custos de deslocamento (tempo x dinheiro) entre pontos pré-determinados
 * Itinerários de ônibus (antes e depois da mudança de 2016)
 * Trajetos usualmente feitos por determinados grupos da sociedade
 * outros
2. Varredura de dados (em andamento)

  Objetivo: verificar e encontrar dados disponíveis
 * Identificar possíveis fontes de dados: [Rio Ônibus](http://www.rioonibus.com/servicos/terminais/), [Data Rio](http://data.rio), [Google Directions API](https://developers.google.com/maps/documentation/directions/?hl=pt-br),[Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/?hl=pt-br), [Google Maps Android API](https://developers.google.com/maps/documentation/android-api/?hl=pt-br), [Armazém de Dados](http://www.armazemdedados.rio.rj.gov.br/), Grupo Pensa, Lab.rio,

3. Captura das informações e construção de uma base
4. Escolha e justificativa do reticulado (considerar estações de transporte)
5. Construção de um modelo que relacione os custos de deslocamento
 * Considerar ocorrencias de transito no modelo?
6.  Visualização dos Dados

### Considerações sobre Dados

#### Modos de transporte
1. Disponíveis no site data.rio (pontos de parada, pontos de percurso, estações, tarifas):
  - Ônibus
  - Metrô
  - Trem
  - Barcas
  - Vlt
  - Bicicleta (Bike Rio) (apenas pontos de estações)
2. Disponíveis via Google Maps (site ou API: tempo, custo)
 - Táxi
 - Uber
 - Carro
 - Deslocamento a pé

#### Trajetos
- Consultar Grupo Pensa
- Considerar elaborar questionários


Ideias extras:
Analisar a dinamica de tempo/custo de deslocamento a partir de pontos que idealmente deveriam ter um fácil acesso, pois recebem uma grande quantidade de pessoas todos os dias

- Construir um reticulado baseado na localização de escolas públicas do Rio e um outro de escolas privadas e comparar. Pode também ser relacionada com a dinâmica imobiliária da cidade. Escolas técnicas do Rio. Pegar dados do ENEM.

- Construir um reticulado baseado na localização de hospitais do Rio. Cruzar com dados da Saúde. Pessoas são atendidad por hospitais específicos conforme seu local de moradia, mas será que conseguem chegar neles facilmente?
Possivel problema: Pessoal é atendida por hospital A, mas tem mais mobilidade para chegar ao hospital B.
