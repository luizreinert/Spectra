<picture>
<p align="center">
  <img src="readme_images\logo_spectra.png" width="1068" title="hover text">
</p>
</picture>

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
# Sobre o projeto

Este projeto faz parte do meu trabalho de conclusão de curso em Biomedicina, intitulado 
"Análise comparativa entre uso de reveladores oxirredutores e de leitura automatizada na determinação da concentração inibitória mínima em bactérias de importância médica".

Trata-se de uma interface gráfica construída em Python, e tem como objetivo otimizar os experimentos que visam a obtenção da porcentagem de inibição bacteriana e a Concentração Inibitória Mínima (CIM) em experimentos realizados em microplacas de 96 poços. Os dados obtidos são representados por meio de um gráfico, que pode ser personalizado e salvo em diferentes formatos.

<picture>
<p align="center">
  <img src="readme_images\gui_screenshot.png" width="1410" title="hover text">
</p>
</picture>
 
## Funcionalidades

- Cálculo da porcentagem de inibição bacteriana
- Geração de gráficos personalizáveis

# Como utilizar?

Esse projeto foi pensado conforme os experimentos realizados no trabalho, com as bactérias Staphylococcus aureus e Escherichia coli, onde cada corante ocupa duas linhas (duplicata) e os controles positivos e negativos ocupam as duas últimas colunas da microplaca. No entanto, é possível configurar a posição dos controles nas duas últimas colunas, a bacteria utilizada e a concentração de antibiótico correspondente ao experimento. 

- A aplicação opera com base em valores de absorbância, obtidos por meio da leitura espectrofotométrica da microplaca de 96 poços
- Após selecionar a bactéria utilizada no experimento, deve-se inserir os valores de absorbância na tabela disponível na interface (Não é necessário preencher toda a tabela, caso o experimento tenha sido realizado com menos corantes e duplicatas)
- Para cada duplicata, é necessário selecionar as duas linhas e pressionar o botão correspondente ao corante utilizado na duplicata. 
- Após concluir e clicar em "Gerar gráfico", o gráfico correspondente será automaticamente incluído na aba "Gráfico". O mesmo pode ser personalizado (Cores das linhas, título e eixos) e salvo.
