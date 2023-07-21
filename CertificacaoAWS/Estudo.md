# Estudo para a certificação AWS Cloud Practitioner CLF-C01

## Conceitos de Cloud e o Básico sobre AWS

### O que é "Cloud Computing?"
Utilização de estrutura de TI funcionando na nuvem com uso sob demanda. 

#### Vantagens do Cloud Computing
- [x] Velocidade -> Implementação de soluções mais rapidamente;
- [x] Updates -> Atualizações gerenciadas pela plataforma e sem interrupções;
- [x] Custo -> Custos mais baixos e com descontos a longo prazo;
- [x] Segurança -> Redundância e backups gerenciados pela plataforma;
- [x] Escalabilidade -> Escalabilidade pode ser automática ou modificada rapidamente.

#### Tipos de Serviços
- [x] IaaS (Infraestrutura como um Serviço) -> Gerencia: rede, armazenamento, servidores e virtualizações.
- [x] PaaS (Plataforma como um Serviço) -> Além dos anteriores, gerencia: sistema operacional, middleware e runtime.  
- [x] SaaS (Software como um Serviço) -> Além dos anteriores, gerencia: dados e aplicações.

#### Tipos de Nuvem
- [x] Public Cloud -> Quando uma provedora disponibiliza os serviços de nuvem ao público, sendo mais barata;
- [x] Hybrid Cloud -> Quando parte dos serviços utilizados estão na nuvem publica e parte na privada, preços combinados;
- [x] Private Cloud -> Quando uma provedora disponibiliza uma estrutura exclusiva para um cliente, sendo mais cara;

## EC2 - Elastic Computing Cloud
Serviço de virtualização da AWS. Permite ativar e desativar dinamicamente servidores virtuais, chamadas Instâncias EC2.

### Virtualização
A virtualização é uma tecnologia que permite criar ambientes virtuais que simulam a execução de sistemas operacionais, aplicativos e recursos de hardware em um único servidor físico. Ela possibilita que várias máquinas virtuais (VMs) coexistam em um único hardware, o que traz benefícios como economia de espaço, energia e recursos.
Vantagens da Virtualização: Controle; Segurança; Compatibilidade; Baixo Custo; Simples.

### Tipos de Instâncias
- De Uso Geral: equilibram os recursos de computação, memória e rede, para diversas cagas de trabalho.
- Otimizada para Computação: para tarefas de computação intensivas, como serviço de jogos.
- Otimizada para Memória: para tarefas com uso intensivo de memória, grandes conjuntos de dados.
- Otimizada para Armazenamento: alta performance para cargas com muita leitura e gravação de dados armazenados localmente.
- Computação Acelerada: utilizam aceleradores de hardware, para cálculos de float e processamentos gráficos.

### EC2 Auto Scaling
Serviço que permite ajustar automaticamente a escalabilidade horizontal, adicionando/removendo instâncias do Amazon EC2 em resposta a demandas de tráfego.

#### Scaling - Escalabilidade
- [x] Scaling Up: Aumentar os recursos de uma instância (vertical)
- [x] Scaling Out: Aumentar a quantidade de um instâncias (horizontal)

#### Auto Scaling Group
Um Auto Scaling Group é um grupo lógico de instâncias do Amazon EC2 que são tratadas como uma única entidade pelo EC2 Auto Scaling. O grupo define a configuração da escala automática, como a quantidade mínima e máxima de instâncias que devem ser mantidas em execução. Ele também especifica as políticas de escalonamento que determinam quando e como as instâncias devem ser adicionadas ou removidas com base na demanda.

##### Launch Configuration
Define as configurações necessárias para criar novas instâncias quando o Auto Scaling Group precisa adicionar mais capacidade. Isso inclui informações como a AMI (Amazon Machine Image) usada para criar as instâncias, o tipo de instância, as configurações de armazenamento e as configurações de segurança.

#### ELB - Elastic Load Balancer
É um serviço de balanceamento de carga oferecido pela AWS que distribui automaticamente o tráfego de entrada entre várias instâncias do Amazon EC2 ou outros recursos da AWS, ajudando a garantir alta disponibilidade e escalabilidade para seus aplicativos.

##### Tipos de Load Balancers
- [x] ALB - Aplication Load Balancer: Layer 7 (OSI) + Routeamento baseado em paths e hosts. [Mais Detalhado]
- [x] NLB - Network Load Balancer: Layer 4 (OSI) + Roteamento baseado em endereços IP e TDP/UDP. [Mais Rápido]

#### Scaling Policies
- [x] Target Tracking - Menos sensível a grandes aumentos de demanda de tráfego. Modificação Gradual...
- [x] Step/Simple Scaling - Mais sensível a grandes aumentos de demanda de tráfego. Modificação Necessária...

### Opções de Pagamento
- [x] Sob Demanda: São ideais para cargas de trabalho irregulares de curto prazo que não podem ser interrompidas.;

- [x] Modelo Spot: São ideais para cargas de trabalho com horários de início e término flexíveis ou que toleram interrupções. Utiliza a capacidade computacional ociosa por um valor inferior; 

- [x] Instâncias Reservadas: são um desconto de cobrança aplicado ao uso de instâncias sob demanda em sua conta. 
Tipos de Instâncias Reservadas:
Instâncias reservadas comuns -> compromisso de _uso de longo prazo_ em uma _instância EC2 específica_, _para o uso constante_.
Instâncias reservadas conversíveis -> têm _maior flexibilidade_ do que as Instâncias Reservadas Padrão.
Instâncias reservadas agendadas -> programação _recorrente previsível_ que exija apenas uma fração do dia, semana ou mês.

- [x] Savings Plans: permite reduzir os custos de computação ao haver o compromisso com uma quantidade consistente de uso de computação por um período de um ou três anos.

- [x] Hosts Dedicados: São servidores físicos com capacidade de instância do Amazon EC2 totalmente dedicada ao uso do cliente.

### Serviços de Mensageria

#### Amazon SQS - Simple Queue Service
Permite desacoplar componentes do sistema. As requisições permanessem em fila até que sejam concluídas ou excluídas.

#### Amazon SNS - Simple Notification Service
É utilizado para enviar mensagens para assinantes via e-mail, mensagem de texto, notificações push e endpoints http/https.

### Computação Serveless
Você não pode ver ou acessar a infraestrutura subjacente

#### Serviços de Computação Serveless

##### Lambda
É um serviço de computação sem servidor da Amazon Web Services (AWS) que permite executar código de forma escalável e sem a necessidade de provisionar ou gerenciar servidores. Ele permite que você se concentre no desenvolvimento do seu código, enquanto a AWS cuida da infraestrutura subjacente. Foi projetado para processamentos de até 15mim, ou seja, rápidos. Orientado a eventos, serviços e aplicações.

##### Serviços para a orquestração de containers do Docker
###### Amazon ECS - Elastic Container Service
É um serviço de orquestração de contêineres totalmente gerenciado que permite executar, escalar e gerenciar aplicativos em contêineres. Ele simplifica a implantação e a execução de aplicativos em contêineres, fornecendo um ambiente escalável e altamente disponível.

###### Amazon EKS - Elastic Kubernetes Service
É um serviço de orquestração de contêineres Kubernetes totalmente gerenciado. Ele fornece um ambiente escalável e altamente disponível para executar aplicativos em contêineres usando a plataforma Kubernetes.

##### AWS Fargate
É uma tecnologia da AWS que permite a _execução de contêineres de forma serverless_, ou seja, sem a necessidade de provisionar e gerenciar instâncias EC2 (Elastic Compute Cloud).

### AMI - Amazon Machine Image
São imagens de instâncias, possuem todas as configurações, aplicações e dados da instância. São usadas para permitir a criação de cópias de uma instância em outras Zona de Disponibilidade. As instâncias serão criadas a partir da imagem. As imagens podem ser públicas (disponível para todos os usuários da AWS) ou privadas (dispónivel para contas específicas).

## A Amazon AWS

### Infraestrutura Global da AWS
Existem as Regiões da AWS -> Zonas de Disponibilidade AWS -> Zonas Locais AWS -> Wavelenght AWS

#### Regiões da AWS
São localidades ao redor do mundo geograficamente isoladas nas quais estão presentes as zonas de disponibilidade.

##### Fatores para Determinar uma Região
[x] - Conformidade: Obdecer as exigencias de regulamento da empresa;
[x] - Proximidade: Deve estar próxima dos seus clientes, visando reduzir a latência;
[x] - Disponibilidade: As vezes, as regiões mais proximas podem não ter os recursos desejados;
[x] - Preço: Os custos podem variar entre as regiões, devido aos impostos, por exmplo.

#### Zonas de Disponibilidade AWS
São os Data Centers que estão presentes nas Regiões da AWS e servem para gerar redundancia de dados. Ficam localizadas a quilometros de distância uma das outras (para que desastres não provoquem interrupções/perdas), mas dentro de um raio de 100km (para manter a latência baixa).

#### EDGE Locations - Locais de Borda
São os pontos de presença (locais de borda) da AWS que executam o CloudFront.

##### Amazon CloudFront
É um serviço que ajuda a fornecer dados, vídeos, aplicações e apis para os cliente com baixa latência e alta velocidade de transferencia, através do armazenamento de cópias em cache. Utiliza os EDGE Locations (Pontos de Presença). Em resumo, é um serviço global de entrega de conteúdo.

#### AWS Outspots
São estruturas da AWS localizadas em espaços de terceiros em regiões sem Zonas Locais ou em instalações de grandes clientes.

#### Zonas Locais AWS
São Data Centers menores, que estão localizadas mais proximas dos clientes para manter a latência baixa, o que possibilita serviços de streaming, por exemplo.

#### Wavelenght AWS
São estruturas da AWS localizadas nas provedoras de internet móvel, como a Claro. Possibilitam que dispositivos móveis se conectem com baixa latência aos serviços da AWS.

### Básico sobre AWS

#### Serviços da AWS
São as soluções oferecidos pela AWS. Atualmente existem mais de 200 serviços e são divididos em áreas, como computação, armazenamento, banco de dados, redes, análises, machine learning e segurança. 

#### Modelo de Responsabilidade Compartilhada
É a divisão das responsabilidades de segurança entre a AWS e o Cliente.
A AWS é responsável pela segurança *da* Nuvem, enquanto o Cliente é responsável pela segurança *na* nuvem. Ou seja, a estrutura física, os softwares e a manutenção da nuvem são de responsabilidade da AWS, mas o Cliente deve se responsabilizar pelos acessos e configurações utilizadas dentro da nuvem.

#### Forma de Acessar a AWS
Existem 3 formas: 
- [x] Console AWS (Interface amigável online)
- [x] CLI AWS (CLI instalável da AWS)
- [x] SDKs Kits de Desenvolvimento de Software (permite o desenvolvimento de aplicativos que utilizam os serviços)
- [x] CloudShell (CLI Online da AWS)

##### AWS Elastic Beanstalk
Através da definições de código e configuração, ele simplifica a implantação, o gerenciamento e a escalabilidade de aplicativos web, também oferece um ambiente para executar aplicativos web em várias linguagens de programação, como Java, .NET, Python, Node.js, entre outras.

##### AWS CloudFormation
Permite criar um ambiente escrevendo linhas de código em vez de usar o AWS Management Console para provisionar recursos individualmente. Com o CloudFormation, você pode definir sua infraestrutura como código em arquivos YAML ou JSON e provisionar, modificar e excluir recursos com facilidade.

## Network - Rede

### Amazon VPC - Virtual Private Cloud
Permite criar uma rede virtual isolada na nuvem AWS, na qual o cliente pode utilizar os recursos da AWS em uma rede virtual definida por ele. O VPC oferece controle total sobre a configuração de rede, como a criação de sub-redes, definição de tabelas de roteamento e configuração de gateways, permitindo que você crie uma infraestrutura de rede personalizada na AWS.

#### Internet Gateway
É um componente do VPC que permite que recursos na sua rede privada se conectem com a internet. É através do Internet Gateway que você pode fornecer acesso público aos recursos da sua VPC.

#### Virtual Private Gateway
É um componente do VPC que permite conexões seguras de rede entre a sua VPC e uma rede local ou outra VPC. É usado para criar conexões VPN (Virtual Private Network) seguras e _estabelecer comunicação entre redes privadas_.

#### AWS Direct Connect 
É um serviço que permite estabelecer conexões de rede dedicadas (física) entre a sua rede local e a AWS. Ele oferece uma conexão de rede privada, de alta velocidade e baixa latência, fornecendo uma alternativa à conexão via internet.

### Subnet - Sub-rede
São subdivisões da sua rede (VPC), também é o local onde se iniciam as instâncias EC2.

#### Sub-redes Públicas
São sub-redes dentro do Amazon VPC que têm uma rota configurada para o Internet Gateway. Isso permite que as instâncias na sub-rede se comuniquem com a internet diretamente. As sub-redes públicas geralmente são usadas para hospedar recursos que precisam de acesso público, como servidores web.

#### Sub-redes Privadas
São sub-redes dentro do Amazon VPC que não têm uma rota direta para o Internet Gateway. Isso significa que as instâncias nas sub-redes privadas não têm acesso direto à internet. As sub-redes privadas são comumente usadas para hospedar bancos de dados ou outros serviços que não precisam de acesso público.

#### NACL - Lista de Controle de Acesso (ALC de rede)
É uma camada adicional de segurança para controlar o tráfego de entrada e saída das sub-redes no Amazon VPC. Elas são definidas em nível de sub-rede e funcionam como firewalls virtuais. permitem definir regras de filtragem de pacotes, especificando quais tipos de tráfego são permitidos ou bloqueados em uma sub-rede. _Por padrão_, a ACL de rede comum da conta _permite todo o tráfego de entrada e saída_, mas você pode modificá-la adicionando suas próprias regras. _São Stateless_

##### Filtragem de Pacotes Stateless
Avaliam cada pacote de forma independente, sem levar em consideração a conexão anterior ou posterior. Isso permite uma filtragem de pacotes mais granular, mas também requer a configuração adequada das regras para permitir o tráfego bidirecional necessário.

#### Grupos de Segurança
São uma camada de segurança para controlar o tráfego de entrada e saída das instâncias EC2 dentro do Amazon VPC. Eles são definidos em nível de instância. Permitem definir regras de filtragem de pacotes, especificando quais tipos de tráfego são permitidos ou bloqueados em uma instância. _Por padrão_, os grupos de segurança _negam todo o tráfego de entrada_, mas você pode adicionar regras personalizadas para atender às suas necessidades operacionais e de segurança. _São Statefull_

##### Filtragem de Pacotes Statefull 
Rastreiam o estado das conexões, permitindo que as respostas aos pacotes de saída relacionados a uma solicitação de entrada sejam permitidas automaticamente, simplificando a configuração das regras.

### DNS - Domain Name System
Sistema responsável por converter nomes de domínio legíveis por humanos (por exemplo, www.amazon.com) em endereços IP legíveis por máquina (por exemplo, 192.0.2.44).

#### Amazon Route 53
É um serviço DNS altamente escalável que permite registrar e gerenciar domínios e direcionar o tráfego da Internet para recursos da AWS. Permite que você crie registros DNS personalizados para direcionar o tráfego de acordo com suas necessidades através de policies. _Permite a criação de domínios públicos_. As três principais funções do Route 53 são registrar nomes de domínio, rotear o tráfego da Internet para os recursos do domínio e conferir a integridade desses recursos.

## Serviços de armazenamento da AWS. 
Existem 8 serviços: S3, Glacier, EFS, EBS, Snowball, Cloudfront, Storage Gateway e Instance Store EC2

### Categorias

#### Block Storage 
Arquivos em formato de blocos conectados a uma instância (para baixa latência), método semelhante aos discos ou HDs.

#### File Storage
Dados são armazenados para compartilhamento entre usuários.

#### Object Storage
Objetos possuem identificação unica com uma URL.

### Serviços de Armazenamento

#### EBS - Elastic Block Store
Usado em instâncias. Deve estar na mesma Zona de Disponibilidade que a instância EC2. Para que o EBS possa se conectar a mais de uma instância, é necessário utilizar uma configuração específica.

##### Tipos de EBS
- [x] HDD: Lento, para armazenamento (mais barato)
- [x] SSD: Rápido, para instâncias (mais caro)

##### Tipos de Volumes

###### Uso Geral (General Purpose)
São SSDs de baixo custo que possuem de 1GB a 16TB e IOPS máximo de 16000 por volume. 
Usados para desktops virtuais, instâncias únicas de databases (como Oracle e Microsoft SQL), aplicações interativas sensíveis à latência, volumes de inicialização e ambientes de desenvolvimento/teste. 

- [x] gp2: Cargas de trabalho com picos ocasionais de tráfego.
- [x] gp3: Desempenho consistente e melhor econômia de custos.

###### IOPS Provisionadas
São SSDs de alta performance e durabilidade, adequados para cargas de trabalho que exigem desempenho extremamente alto, latência baixa e consistência. Possuem volumes de 4GB até 16TB (com excessão do Block Express que chega a 64TB).

- [x] io2 Block Express: 
Volume SSD de maior performance criado para cargas de trabalho transacionais sensíveis à latência essenciais para os negócios.
Ideal para implantações de missão crítica maiores e mais intensivas em I/O de NoSQL e bancos de dados relacionais, como Oracle, SAP HANA, Microsoft SQL Server e SAS Analytics. 

- [x] io2: 
Volume SSD de alta performance e durabilidade criado para workloads transacionais que dependem da latência.
Bancos de dados NoSQL e relacionais com alto consumo de E/S.

- [x] io1: 
Volume SSD de alta performance criado para workloads transacionais sensíveis à latência.
Bancos de dados NoSQL e relacionais com alto consumo de E/S.

###### Otimizados para Taxa de Transferência
- [x] st1: HDD otimizada por taxa de transferência. Usado para Big data, Data warehouses e Processamento de logs. 
Tamanho de 125GB até 16TB

###### Cold HDD
- [x] sc1: Armazenamento orientado a throughput para dados acessados com pouca frequência. Possuem o menor custo.
Tamanho de 125GB até 16TB

##### Snapshot
É um backup incremental. Isso significa que o primeiro backup de um volume copia todos os dados. Nos backups subsequentes, somente os blocos de dados que foram alterados desde o snapshot mais recente são salvos. Também são utilizados para permitir que uma outra instância acesse o volume EBS.

#### S3 - Simple Storage Service
Foi o primeiro serviço oferecido pela AWS. Não possuem tamanho máximo, porém existe um limite de 5TB para o upload de um arquivo. Possui durabilidade de 99,999999999% e disponibilidade de 99,95-99,99%. Muito _utilizado para hospedagem de sites estáticos_.

- [x] Buckets: Devem ter nome único e universal. Local onde tudo será armazenado (pastas e arquivos)

##### ACL - Access Control List
São as listas de controle de acesso (ACLs) do Amazon S3, permitem o gerenciamento do acesso aos buckets e seus objetos.

##### Classes de Armazenamento

###### S3 Standard
É a classe de armazenamento padrão do S3, projetada para alta durabilidade, disponibilidade e desempenho. É ideal para acesso frequente aos dados e é recomendada para uma ampla gama de casos de uso. Mais Cara!

###### S3 Intelligent-Tiering
É uma classe de armazenamento que usa aprendizado de máquina para analisar padrões de acesso aos dados e mover automaticamente os objetos entre as camadas de armazenamento de baixo custo e alta frequência de acesso. Essa classe é útil quando você tem dados com padrões de acesso variáveis e não deseja gerenciar manualmente a movimentação dos objetos entre camadas.

###### S3 Standard-Infrequent Access 
É uma classe de armazenamento de baixo custo adequada para dados que são acessados com menos frequência, mas quando o acesso ocorre, é necessário um desempenho rápido. É uma opção recomendada para backups, arquivos de log e dados de arquivamento. 

###### S3 One Zone-Infrequent Access
É semelhante ao S3 Standard-IA, mas os objetos são armazenados em apenas uma zona de disponibilidade, em vez de múltiplas zonas. Essa classe é adequada para dados que podem ser facilmente recriados ou reproduzidos, caso ocorra uma perda.

###### S3 Glacier Instant Retrieval
É usada para arquivar dados que raramente são acessados, mas exigem recuperação em milissegundos.

###### S3 Glacier Flexible Retrieval
É usada para arquivos nos quais partes dos dados podem precisar ser recuperadas em minutos. Os dados armazenados nesta classe podem ser acessados em apenas 1 a 5 minutos usando a recuperação acelerada ou em até 5 a 12 horas usando recuperações em massa gratuitas

###### S3 Glacier Deep Archive
É usada para arquivar dados que raramente precisam ser acessados, com um tempo de recuperação padrão de 12 horas. Mais barata!

###### OBS: Glacier 
S3 Object Lock e S3 Glacier Vault Lock -> São ferramentas que permitem determinar um tempo mínimo para recuperar um objeto.

###### S3 Outposts
É um serviço de armazenamento de objetos que permite criar buckets do S3 em seu Outpost, além de armazenar e recuperar objetos facilmente on-premises.

##### Versionamento
Salva versões diferentes de um mesmo arquivo. Ao habilitar essa função no bucket não é possível desabilita-la, mas é possível suspende-la. O valor cobrado será a soma do tamanho das versões. Cada versão possui um ID da Versão (menos a 1ª).

##### Ciclos de Vida
São políticas que permitem configurar períodos para que o arquivo seja movido para outra classe de armazenamento. Possui filtros para automatizar quais pastas ou arquivos serão movidos ou pode ser aplicada a todo bucket.

#### S3 x EBS
- [x] S3: Utilizado para objetos completos ou alterações esporádicas. _Objetos_
- [x] EBS: Utilizado para execução de funções complexas de leitura, correção e alteração. _Blocos/Discos_

#### Amazon EFS - Elastic File System
É um sistema de armazenamento de arquivo compartilhado e gerenciado. Permite o acesso de varias instâncias aos arquivos de forma _simultânia_. É um sistema de arquivos pra _Linux_ e _Regional (em várias EZs)_. _Escala automaticamente_ a medida que são adicionados mais dados.

#### Migração de DB Lift-and-Shift
Migrar o banco de dados para ser executado no EC2. Permitindo o controle sobre as mesmas variáveis do ambiente on premises, como sistema operacional, memória, CPU, capacidade de armazenamento... 

#### Amazon RDS - Relation Database Service
É um serviço de banco de dados relacional _gerenciado_ oferecido pela AWS, ele fica responsável por manter o DB, como patches automatizados, backups, redundância, failover e recuperação de desastres. Ele permite que você configure, opere e escale facilmente bancos de dados relacionais na nuvem. Suporta uma variedade de bancos de dados relacionais populares, como MySQL, PostgreSQL, Oracle, SQL Server e MariaDB. Permite criar _réplicas de leitura entre regiões_.

#### Amazon Aurora
É um mecanismo de banco de dados relacional compatível com MySQL e PostgreSQL, mas projetado para oferecer desempenho, disponibilidade e escalabilidade aprimorados. Ele é um serviço _totalmente gerenciado pela AWS_. É compatível com a maioria das ferramentas e aplicativos existentes do MySQL e do PostgreSQL. Ele é _barato_, possui _dados replicados_ e realiza _backups contínuos para o S3_, além de _pontos de recuperação_.

#### DynamoDB
É um banco de dados _noSQL e serveless_, ou seja, o cliente não precisa gerenciar as instâncias ou sua infraestrutura. Ele é totalmente gerenciado e altamente escalável. Utiliza o _modelo de chave-valor_, os dados são organizados em itens (chaves) e cada item tem um atributo (valores). Para _trilhões de solicitações por dia_.

#### Tabelas Globais do Amazon DynamoDB
São um banco de dados totalmente gerenciado, com tecnologia sem servidor, multirregional e multiativo.

#### RDS x DynamoDB
- [X] RDS: Para análises de negócio, usado para unificar tabelas relacionais complexas.
- [x] DynamoDB: Usado quando não há a necessidade de relacionamento, eliminando as sobrecargas.

#### Amazon Redshift
É um data warehouse usado para análise de big data. Ele oferece a capacidade de coletar dados de muitas fontes além de ajudar a entender relações e tendências em todos os seus dados.

#### AWS DMS - Database Migration Service
Permite migrar bancos de dados relacionais e não relacionais e outros tipos de armazenamentos de dados. Os bancos de dados de origem e de destino _podem ser do mesmo tipo ou de tipos diferentes_. Durante a migração, o banco de dados de origem _permanece operacional_, reduzindo o tempo de inatividade em qualquer aplicativo que dependa do banco de dados. 

#### Outros Serviços de Banco de Dados
##### Banco de Dados
- [x] Amazon DocumentDB: é um serviço de banco de dados de documentos compatível com cargas de trabalho do MongoDB.
- [x] Amazon Neptune: é um serviço de _banco de dados de grafo_. 
- [x] Amazon Managed Blockchain: é um serviço para criar e gerenciar redes de blockchain com estruturas de código aberto.
- [x] Amazon QLDB - Quantum Ledger Database: é um serviço de banco de dados ledger.

OBS: O Neptune e o DocumentDB possuem replicação em várias AZs por padrão.

##### Aceleradores
- [x] Amazon ElastiCache: é um serviço que adiciona camadas de cache para ajudar a melhorar os tempos de leitura.
- [x] Amazon DAX - DynamoDB Acelerator: é um cache em memória para o DynamoDB.

##### AWS Storage Gateway
O AWS Storage Gateway _é um serviço de armazenamento na nuvem híbrida_ que oferece _acesso on-premises a armazenamento na nuvem praticamente ilimitado_. Os clientes usam o Storage Gateway para simplificar o gerenciamento de armazenamento e reduzir os custos de casos de uso de armazenamento na nuvem híbrida. Ele disponibiliza uma performance de baixa latência armazenando em cache dados acessados com frequência no local e, ao mesmo tempo, armazenando dados de modo seguro e resiliente nos serviços de armazenamento na nuvem da Amazon.

## Security

### Modelo de Responsabilidade Compartilhada
- [x] Deveres do Usuário -> Responsável pela segurança na nuvem: seus dados, aplicações, plataforma, identificação, acessos, rede, configurações (sistema operacional, rede e firework), autenticação e encriptação.

- [x] Deveres da AWS -> Responsável pela segurança da nuvem: Hardware (Toda a estrutura Global desde Regiões até Zonas)
                                                             Software (Computação, armazenamento, banco de dados e rede)

### MFA Autenticação Multifator

## IAM - Identity and Access Management (Gerenciamento de Acesso e Identidade)
É um serviço da que ajuda você a controlar o acesso aos recursos da AWS de forma segura. Com o IAM, é possível gerenciar, de maneira centralizada, permissões que controlam quais recursos da AWS os usuários poderão acessar. Você usa o IAM para controlar quem é autenticado (fez login) e autorizado (tem permissões) a usar os recursos.

### Componestes do IAM
- [x] Usuario Root (raiz): Possui acesso completo.

- [x] Usuários: Representam indivíduos e têm acesso aos serviços da AWS por meio de credenciais de acesso 
(por padrão não tem permissões).

- [x] Group (grupo): São usados para gerenciar o acesso de um conjunto de usuários aos serviços da AWS.

- [x] Roles (funções): São identidades que podem ser assumidas para obter acesso temporário às permissões.
Permitem o acesso entre aplicações e/ou serviços.

- [x] Policys (políticas): São documentos JSON que concedem ou negam permissões para serviços e recursos AWS.

_Chaves de Acesso:_ Access Key Id e Secret Access Key

### AWS Organizations
- [x] Gerenciamento Centralizado: permite gerenciar todos os usuários.
- [x] Faturamento Consolidado: Permite verificar e pagar as contas dos usuários, além de possibilitar descontos em massa.
- [x] Agrupamento Hierárquico: Agrupar usuários para atender requisitos de segurança ou necessidades orçamentárias. 
- [x] SCPs - Políticas de Controle de Serviço: Define quais serviços e recursos podem ser acessados individualmente ou não.

Usuário Root >>> Organizations Units (OU) >> AWS Account > AWS Resources

### AWS Artifact
Permite análisar, aceitar e gerenciar seus contratos com a AWS e acessar relatórios de conformidade da AWS sob demanda.

### WAF x Shield

#### WAF - Web Application Firewall 
É um serviço de firewall de aplicativos da web que ajuda a proteger aplicativos da web contra ataques comuns, como injeção de SQL, cross-site scripting (XSS) e ataques de força bruta.
 
#### Shield
 É um serviço de proteção contra DDoS (Distributed Denial of Service) que ajuda a proteger aplicações e infraestruturas contra ataques volumétricos, de camada de transporte e de camada de aplicativo.

- [x] Standard: protege automaticamente todos os clientes AWS sem nenhum custo.
- [x] Advanced: é pago, fornece diagnósticos detalhados de ataques, com capacidade de detectar e mitigar ataques elaborados.

### Security Services

### AWS KMS - Key Managemant Service
É um serviço de gerenciamento de chaves criptográficas. Ele permite criar e controlar de maneira centralizada as chaves de criptografia usadas para proteger dados confidenciais e outros recursos na nuvem.

#### AWS Inspector
É um serviço de segurança automatizado da AWS que ajuda a _identificar e corrigir vulnerabilidades_ de segurança em instâncias do Amazon EC2 e em aplicativos em execução na nuvem. _Gera relatórios de avaliação de segurança automatizados_.

#### Amazon GuardDuty
é um serviço que fornece detecção inteligente de ameaças para sua infraestrutura e seus recursos AWS. Ele identifica ameaças monitorando continuamente a atividade da rede e o comportamento da conta no seu ambiente AWS. 

### AWS Macie
Realiza a descoberta de dados confidenciais usando machine learning e correspondência de padrões, fornece visibilidade dos riscos de segurança de dados e habilita proteção automatizada contra esses riscos.

### Amazon Cognito 
Fornece um serviço gerenciado que pode oferecer suporte a recursos de _login/cadastro_ ou atuar como um _provedor de identidade_ (IdP) em um cenário de identidade federada.

### AWS KMS - Key Management Service
É um serviço de gerenciamento de chaves criptográficas usado para proteger dados e recursos armazenados e transmitidos dentro da plataforma AWS. O KMS ajuda a criar, controlar, gerenciar e auditar o uso de chaves de criptografia.

## Monitoramento e Análise

### CloudWatch
Permite que você _monitore sua infraestrutura da AWS e as aplicações que você executa_ na AWS _em tempo real_. Acesso a todas as _métricas e logs_ de forma centralizada na forma de painéis. Você pode monitorar suas cobranças estimadas da AWS usando o CloudWatch. Quando você ativa o monitoramento de cobranças estimadas em sua conta da AWS, elas são calculadas e enviadas várias vezes ao dia para o CloudWatch como dados de métrica. 

Alarme do CloudWatch* -> alertas gerados de acordo com alguma métrica definida pelo usuário, podem vir acompanhados de ações.

### Cloud Trail
É um serviço de _auditoria e rastreamento que registra as atividades_ realizadas em sua conta da AWS. Ele fornece informações detalhadas sobre ações realizadas pelos usuários, serviços e recursos da AWS, ajudando a auditar, monitorar e solucionar problemas de segurança e conformidade. Os _logs podem ser salvos por tempo indeterminado_. É possível identificar "o que aconteceu", "quem fez a solicitação", "quando ocorreu" e "como a solicitação foi feita".

#### AWS Trusted Advisor
 É um serviço que oferece _recomendações em tempo real_ para otimizar sua infraestrutura e aumentar a eficiência operacional. Ele analisa sua conta e fornece conselhos personalizados em várias áreas, como segurança, desempenho, custos e tolerância a falhas.

Utiliza os 5 Pilares para a Análise: Otimização de Custos, Performance, Segurança, Tolerância a Falhas e Limites de Serviço.

## Definição de Preço e Suporte

### Nível Gratuito
você começa a usar determinados serviços sem ter que se preocupar em incorrer em custos durante o período especificado. 
Três tipos de ofertas estão disponíveis: Sempre gratuito, 12 meses gratuitos e Versão de teste

### Filosofia AWS
- [x] Pay as You Use - Você paga de acordo com o que você usa!
- [x] Pay Less and You Use More - Você paga menos se você usar mais!
- [x] Pay Iven Less if You Reserved - Você paga muito menos se você reservar! 

### AWS Cost Calculator
É uma ferramenta online fornecida pela AWS que permite estimar os custos dos serviços da AWS com base nos recursos que você planeja usar.

### Budget x Cost Explorer
- [x] Budget: Orçamento -> Alerta/avisos antes que chegue a determinado valor.
- [x] Cost Explorer -> Visualização dos gastos e relatório de contas. 

### AWS Suport Plans

#### Basic 
- [x] Trusted Advisor: verificações básicas
- [x] AWS Personal Health Dashboard 
- [x] Suporte: Atendimento ao cliente 24/7
- [x] Acesso a whitepapers, documentação e comunidades de suporte

#### Developer
- [x] Suporte Básico: acesso ao Cloud Support pela Web em _horário comercial_
- [x] Acesso ao suporte por e-mail

#### Business
- [x] Trusted Advisor: verificações completas
- [x] Suporte Técnico: Acesso aos engenheiros de suporte de nuvem por telefone

#### Enterprise 
- [x] Inclui suporte dedicado de um gerente de contas (_TAM - Technical Account Management_)
- [x] Suporte Técnico: Acesso aos _engenheiros de suporte de nuvem 24h/7_
- [x] Assistencia a Conta: Equipe de _suporte do Concierge_
- [x] SLA de 15mim para cargas de trabalho críticas.


*Somente os planos Business e Enterprise possuem acesso completo ao Trusted Advisor.

TAM: Oferece o conhecimento especializado em toda a gama de serviços AWS. Ele ajuda você a projetar soluções que usam vários serviços combinados de forma eficiente por uma abordagem integrada.

### AWS Marketplace
É um catálogo digital com milhares de ofertas de fornecedores independentes de software. Você pode usar o AWS Marketplace para encontrar, testar e comprar software que pode ser executado na AWS. _Serviços prontos para uso_

### CAPEX x OPEX
- [x] CAPEX - Capital Expenditure: Pagamento estipulado previamente
- [x] OPEX - Operational Expenditure: Pagamento de acordo com o uso

## Migração e Inovação

### AWS CAF - Cloud Adoption Framework
Existe para _fornecer aconselhamento_ a empresa para habilitar uma migração rápida e tranquila.
Organiza orientações em _seis áreas de foco chamadas perspectivas_. Cada perspectiva aborda responsabilidades distintas. O processo de planejamento ajuda as pessoas certas em toda a organização a se prepararem para as mudanças futuras.

Capacidades Comerciais:
- [x] Perspectiva de negócio -> garante que a TI esteja alinhada às necessidades de negócio e foco nos resultados.
- [x] Perspectiva de pessoas -> promove o desenvolvimento de uma estratégia de gerenciamento de alterações na organização.
- [x] Perspectiva de governança -> concentra-se nas habilidades e nos processos para alinhar as estratégias de TI e negócios.

Capacidades Técnicas:
- [x] Perspectiva de plataforma -> inclui princípios e padrões para implementação de novas soluções na nuvem.
- [x] Perspectiva de segurança -> garante que a organização atenda aos objetivos de segurança.
- [x] Perspectiva de operações -> ajuda você a controlar as cargas de trabalho de TI para o nível definido na empresa.

#### Action Plan
Um plano de ação que ajuda a orientar sua organização para a migração na nuvem.

### Estratégias de Migração (6Rs)
- [x] Rehospedar: envolve a movimentação de aplicativos sem alterações. 
- [x] Replataformar: envolve fazer algumas otimizações na nuvem para obter um benefício tangível.
- [x] Retirar: é o processo de remoção de aplicativos que não são mais necessários.
- [x] Retenção: consiste em manter os aplicativos essenciais para a empresa no ambiente de origem.
- [x] Recompra: envolve a mudança de uma licença tradicional para um modelo de software como serviço.
- [x] Refatoração/rearquitetura: envolve reimaginar como um aplicativo é arquitetado e desenvolvido usando recursos da nuvem.

### AWS DataSync 
É um serviço da AWS que ajuda na transferência rápida e segura de grandes quantidades de dados entre diferentes locais. Ele é útil em várias situações, especialmente quando você precisa mover grandes volumes de dados de forma eficiente e confiável.

### Snow Familly
É uma coleção de dispositivos físicos para transporte físico de até exabytes de dados para dentro e para fora da AWS. 

#### AWS Snowcone
É um dispositivo pequeno, robusto e seguro para transferência de dados e computação de borda.
Ele tem 2 CPUs, 4 GB de memória e 8 TB de armazenamento utilizável.

#### AWS Snowball
Normalmente utilizados em locais remotos, onde é mais complicado ter poder de computação.

##### Snowball Edge Otimizados para Armazenamento 
São ideais para migrações de dados de grande escala e fluxos de trabalho de transferência recorrentes, em além da computação local com necessidades maiores de capacidade. _Fornece 80 TB de armazenamento de HDD utilizável_.

##### Snowball Edge Otimizado para Computação 
Fornece recursos de computação poderosos para casos de uso, como machine learning, análise de vídeo em movimento completo, análise e pilhas de computação locais.  _Fornece 40 TB de armazenamento de HDD utilizável_

#### AWS Snowmobile.
É um serviço de transferência dados na escala de exabytes usado para mover grandes quantidades de dados para a nuvem AWS.
Você pode transferir _até 100 petabytes por Snowmobile_, um contêiner de transporte reforçado com 13,71 metros de comprimento puxado por um caminhão semirreboque. _Contém diversos métodos de segurança_, desde monitoramento até resistencia a fogo.

### Inovação com AWS
#### Serviços de Migração de VM
- [x] VMWare Cloud on AWS

#### Serviços de Machine Learning
- [x] Amazon SageMaker: Permite que você crie, treine e implemente modelos de machine learning de forma rápida.
- [x] Amazon Augmented AI (Amazon A2i): Permite a utilização de machine learning para a criação de soluções. 
- [x] AWS DeepRacer: é um carro de corrida autônomo de escala 1/18 para testar modelos de aprendizado por reforço.
- [x] Amazon Rekognition: Automatize e reduza o custo de seu reconhecimento de imagem e análise de vídeo com machine learning.
- [x] Amazon Transcribe: Converte automaticamente a fala em texto

### AWS Cost Anomaly Detection 
Aproveita tecnologias avançadas de _machine learning para identificar gastos anômalos_ e suas causas-raiz para que você possa tomar medidas rapidamente. 

### Amazon EMR
É a solução de big data em nuvem líder do setor para processamento de dados, análise interativa e machine learning que usa estruturas de código aberto, como Apache Spark, Apache Hive e Presto.

#### Serviços de Inteligencia Artificial
- [x] Amazon Lex: é um serviço para criação de interfaces de conversação usando voz e texto.
- [x] Amazon Textract: Permite a extração de textos e dados de documentos, tornando-os utilizáveis. 

#### Serviços de Internet das Coisas
- [x] AWS Ground Station: Espaço sei lá o que...

## Jornada para a Nuvem

### AWS Well-Architected Framework
Ferramenta que permite avaliar suas arquiteturas de acordo com 5 pilares: 
Excelência Operacional, Segurança, Confiabilidade, Eficiência de Performance e Otimização de Custo.

_SEx CEO_
Segurança - capacidade de _proteger_ informações, sistemas e ativos e, ao mesmo tempo, entregar valor comercial
Exelência Operacional - capacidade de _executar e monitorar_ sistemas para entregar valor comercial
Confiabilidade - capacidade de um sistema se recuperar, escalar e reduzir interrupções. _Funcionar Corretamente_
Eficiência de Performance - capacidade de _usar recursos computacionais com eficiência_ para cumprir requisitos do sistema
Otimização de Custos - capacidade de executar sistemas para entregar valor comercial com o _menor preço_.

### Os 6 Benefícios da Nuvem
- [x] Trocar despesas fixas por despesas variáveis. Pague pelo que usar e reduza despesas com facilidade.
- [x] Benefício de economia de escala massiva. Pague menos se usar mais.
- [x] Pare de tentar adivinhar a capacidade. Escalabilidade automática evitando ociosidade ou sobrecarga.
- [x] Aumente a velocidade e a agilidade. Facilita a experimentação e testes com custos mais baixos e com maior rapidez.
- [x] Pare de gastar com a construção e manutenção de DBs. A AWS pode gereciar e manter os DBs.
- [x] Ter alcance global em minutos. Utilizar a plataforma da AWS para aumentar a disponibilidade globalmente.

______________________________________________________________________________________________________________________________

## Serviços Aprendidos na Revisão

### AWS Config
O AWS Config avalia, audita e avalia continuamente as configurações e os relacionamentos de seus recursos.

### Lightsail

### Amazon WorkSpaces
São áreas de trabalho virtuais totalmente gerenciados, seguros e confiáveis para cada workload.

### AWS Compliance Program
Ele detalha a postura de conformidade da AWS em relação a várias regulamentações e frameworks. Determinando os serviços que atendem aos requisitos regulatórios regionais.

### AWS Audit Manager
Audite continuamente o uso da AWS para simplificar a avaliação de risco e conformidade

### Amazon Pinpoint

### Amazon Connect

### AWS Director Service



As chaves gerenci

### AWS Certificate Manager

### AWS Quick Start

### AWS COdePipeline

### AWS Batch

### AWS Migration Hub

### AWS CodeStar