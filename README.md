# Scrapy Study

Scrapy Study é um repositório de estudo que contém algumas spiders para demonstração de web crawling e scraping com
[Scrapy](https://scrapy.org/) e [Scrapy Cloud](https://scrapinghub.com/).

## Índice
1. [Pré-Requisitos](#pré-requisitos)
2. [Para começar](#para-começar)
3. [Pastas](#pastas)
4. [Executando uma spider](#executando-uma-spider)

### Pré-Requisitos 

Ferramentas usadas nesse repositório:
- [Python](https://www.python.org/downloads/) = 2.7.15
- [Scrapy](https://scrapy.org/) >= 1.5

### Para começar

- Clone o repositório:
`git clone git@github.com:anacls/scrapy-study.git`

- Vá para o diretório principal:
`cd scrapy-study`

### Pastas 

* #### tdc_examples
  A pasta `tdc_examples` é um projeto com spiders utilizadas numa [apresentação](https://speakerdeck.com/anacls/web-crawling-e-scraping-tdc) realizada no TDC. 

  **Spiders** 
    * [books.py](https://github.com/anacls/scrapy-study/blob/master/tdc_examples/scrapy_study/spiders/books.py): faz raspagem no site books.toscrape.com, extrai e imprime **título**, **nome do autor** e **link** dos itens do catálogo.

    * [quotes.py](https://github.com/anacls/scrapy-study/blob/master/tdc_examples/scrapy_study/spiders/quotes.py): faz raspagem em duas páginas do site quotes.toscrape.com e para cada página extrai todo o **html** e salva em um novo arquivo .html.

    * [top_series_week.py](https://github.com/anacls/scrapy-study/blob/master/tdc_examples/scrapy_study/spiders/top_series_week.py): faz raspagem na sessão de séries do adorocinema.com extraindo e imprimindo **título**, **descrição**, **quantidade de temporadas**, de **episódios** e algumas outras informações sobre as séries.

    * [trains_situation.py](https://github.com/anacls/scrapy-study/blob/master/tdc_examples/scrapy_study/spiders/trains_situation.py): faz raspagem no site da CPTM e retorna a **situação atualizada** das linhas. 

    * [trilhas_tdc.py](https://github.com/anacls/scrapy-study/blob/master/tdc_examples/scrapy_study/spiders/trilhas_tdc.py): faz raspagem na sessão de **trilhas** do site do TDC 2018, extrai e retorna algumas informações sobre as trilhas. 

* #### tripadvisor 
  A pasta `tripadvisor` é um projeto que contém uma [única spider](https://github.com/anacls/scrapy-study/blob/master/tripadvisor/tripadvisor/spiders/tripadvisor.py). Essa spider faz raspagem na página de restaurantes de Indaiatuba no site do tripadvisor e retorna **nome**, **nota**, **endereço** e **link** do item. 

### Executando uma spider

#### Para executar uma spider na sua máquina local:
Vá até a pasta do projeto onde a spider se encontra e execute o comando `scrapy crawl <spider_name>`

Eg.: `cd tripadvisor && scrapy crawl tripadvisor` 

*OBS: O nome da spider nem sempre é igual ao nome do arquivo, esse nome é definido na váriavel `name` dentro do arquivo da spider.*

#### Para executar uma spider no ScrapingHub:

- Crie uma conta no [Scrapinghub](https://scrapinghub.com/)

- Crie um projeto selecionando `Scrapy` como a opção para fazer deploy das suas spiders

- Siga o passo a passo da aba `Code & Deploys`

- Vá para a sua dashboard e clique no botão `RUN`

- No campo `Spiders` digite o nome da spider que deseja executar






