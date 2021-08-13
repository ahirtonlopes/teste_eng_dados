# Teste - Engenharia de Dados (Short Track)

Teste técnico para posições em Engenharia de Dados (short track)

O seguinte teste tem por premissa ser um problema base (Ref. <a href="https://teaching.cornell.edu/teaching-resources/engaging-students/problem-based-learningproblem">problem based learning</a>) de modo que você pode usá-lo como achar adequado tendo em vista a demonstração de seus conhecimentos técnicos.

Queremos entender melhor seu jeito de atacar problemas desafiadores em amostras de mundo real, além de que, do modo que está estruturada, a entrega, apesar de rápida, nos permite verificar mais detalhes de seu perfil profissional tais como organização, pontualidade e percepção quanto a suas skills de data wrangling, validação e governança, programação Python e entendimento dos serviços AWS (em especial Aws Lambda, Athena e Amazon Redshift).

Recomendamos ainda que o teste seja feito em no máximo 6 horas (não se preocupe em respostas muito detalhadas ou em complexidades que simplesmente não funcionariam no mundo real!).

As entregas devem ser via envio de link para um github público (ou similar) o qual contenha sua solução para o cenário a seguir:

## Cenário

No seguinte cenário você é a pessoa engenheira de dados por trás do projeto de data ops junto a uma grande indústria norte-americana.

Os dados a serem ingeridos e analisados em nossa plataforma de Big Data são dados de compras (orders), pessoas (people) e devoluções (returns).

Sua primeira tarefa é escrever uma aplicação de integração de dados, de modo a assegurar os aspectos de integridade e escalabilidade da solução, garantindo que os dados vão ser importados de maneira adequada para as camadas de consumo.

## Entregáveis

O primeiro entregável desse cenário deve ser um relatório (de preferência um <a href="https://jupyter.org/">jupyter notebook</a> ou <a href="https://colab.research.google.com/">colab notebook</a> relatando algumas das anomalias encontradas e investigações possíveis (falamos que aqui encorajamos gente curiosa, certo?!)

O dataset a ser utilizado nesse cenário (.zip com arquivo CSV) você encontra <a href="https://drive.google.com/file/d/1a8UCbzXFbqTQi0x8tqCXPRTlB--E7o8I/view?usp=sharing">aqui</a>.

Temos um apreço muito grande por qualidade e disponibilidade. Sendo assim, é bom contarmos com métricas para nos previnir e alertar sobre quaisquer problemas bem como metrificar e monitorar as arquitetura proposta. Logo, apreciamos se você conseguir entregar testes que mensurem a qualidade dos dados junto à sua solução desse primeiro entregável. 

O segundo entregável consiste na transformação de dados disponíveis em <a href="https://drive.google.com/file/d/1IDCjpDZh5St97jw4K_bAewJ8hf-rax9C/view?usp=sharing">arquivo Json</a> para o formato de dataframe, algo comum no dia a dia da empresa. Após transformar esse Json em dataframe é possível perceber que a coluna "item_list" está como dicionário. Seu gestor pediu dois pontos de atenção nessa tarefa:

- Expandir a coluna num mesmo dataframe;
- Normalizar os itens dessa coluna de dicionário e dividí-los em dois dataframes separados, seguindo o modelo relacional.

Imagine que o Json das notas fiscais é disponibilizado em uma API. Como você utilizaria as tecnologias da AWS para ingerir, transformar e, eventualmente, carregar esses dados em um banco de dados Redshift? O terceiro entregável consiste na construção de uma arquitetura de ingestão dos dados de nota fiscal do entregável anterior (como visto <a href="https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2020/06/22/Screen-Shot-2020-06-19-at-15.00.38.png">aqui</a>), a qual deve atender aos seguintes pontos:

- Esquemas de fluxo de dados;
- Descrições de funcionamento (se necessário);
- Nomes de tecnologias em ecossistema AWS (serviços, conectores, bibliotecas e módulos).

Será apreciado como esforço extra se você conseguir avançar mais na aplicação além desse ponto.

Já o quarto entregável pode estar contido como comentários em suas soluções prévias, queremos entender melhor como foi seu processo de solução de problemas, quais as hipóteses levantadas e, se tivesse mais tempo, como você poderia melhorar a implementação proposta.

Ou seja, temos quatro entregáveis:

- Relatório com exemplos de anomalias encontradas e possibilidades dentro da sua experiência e com relação aos dados da base;
- Resolução de problema de transformação de dados (NF-e);
- Arquitetura exemplo da ingestão anterior (ecossistema AWS);
- Comentários a respeito da implementações propostas e melhorias (desenvolvimento incremental).

## Dados

| Table            | Total Rows | Total Columns                                              |
| -----------------|:--------:  | :---------------------------------------------------------:|
| Orders           | 9994       | 21                                                         |
| People           | 4          | 2                                                          |
| Returns          | 296        | 2                                                          |

## O que será avaliado?

1. Buscamos soluções bem definidas e baseadas em método: soube mostrar quais as hipóteses levantadas? Precisou ao menos de modo resumido o por que escolheu determinado caminho? Quais os prós e contras usados para se basear essa solução e quais os passos para implementá-la?
2. Qualidades dos entregáveis, tanto o report de anaomalias encontradas quanto a arquitetura proposta.
3. A eficiência do método utilizado para a verificação de anomalias.
4. Se tivesse mais tempo, o que você faria para melhorar a sua solução?

## 

“Perception is strong and sight weak. In strategy it is important to see distant things as if they were close and to take a distanced view of close things.”

Miyamoto Musashi. Japanese martial artist, philosopher, strategist, writer, artist (1584-1645).

がんばろう

