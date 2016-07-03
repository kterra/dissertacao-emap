## Construção de um mapa de deslocamento multimodal relacionando preço e tempo do deslocamento entre pontos da cidade do Rio de Janeiro

#### Outputs do Trabalho
- Mapas Estáticos
- Classificação de bairros por disponibilidade de mobilidade
- Classificação de bairros por custo de mobilidade
- Mapas Interativos - Visualização Web

### Metodologia
1. Definir dados a serem encontrados ou capturados
 * Distâncias entre pontos pré-determinados
 * Tempo de deslocamento entre pontos pré-determinados
 * Custos de transporte entre pontos pré-determinados
 * Itinerários de ônibus (antes e depois da mudança de 2016)
 * Trajetos usualmente feitos por determinados grupos da sociedade
 * outros
2. Varredura de dados (objetivo: verificar e encontrar dados disponíveis)
 * Identificar possíveis fontes de dados: [Rio Ônibus](http://www.rioonibus.com/servicos/terminais/), [Data Rio](http://data.rio), Grupo Pensa, Lab.rio
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
