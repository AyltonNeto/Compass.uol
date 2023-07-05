# Estudo para a certificação AWS Cloud Practitioner CLF-C01

## Conceitos de Cloud e o Básico sobre AWS

### O que é "Cloud Computing?"
Utilização de estrutura de TI funcionando na nuvem com uso sob demanda. 

#### Vantagens do Cloud Computing
[x] - Velocidade -> Implementação de soluções mais rapidamente;
[x] - Updates -> Atualizações gerenciadas pela plataforma e sem interrupções;
[x] - Custo -> Custos mais baixos e com descontos a longo prazo;
[x] - Segurança -> Redundância e backups gerenciados pela plataforma;
[x] - Escalabilidade -> Escalabilidade pode ser automática ou modificada rapidamente.

#### Tipos de Serviços
[x] - IaaS (Infraestrutura como um Serviço) -> Gerencia: rede, armazenamento, servidores e virtualizações.
[x] - PaaS (Plataforma como um Serviço) -> Além dos anteriores, gerencia: sistema operacional, middleware e runtime.  
[x] - SaaS (Software como um Serviço) -> Além dos anteriores, gerencia: dados e aplicações.

#### Tipos de Nuvem
[x] - Public Cloud -> Quando uma provedora disponibiliza os serviços de nuvem ao público, sendo mais barata;
[x] - Hybrid Cloud -> Quando parte dos serviços utilizados estão na nuvem publica e parte na privada, preços combinados;
[x] - Private Cloud -> Quando uma provedora disponibiliza uma estrutura exclusiva para um cliente, sendo mais cara;

### Básico sobre AWS

#### Serviços da AWS
São as soluções oferecidos pela AWS. Atualmente existem mais de 200 serviços e são divididos em áreas, como computação, armazenamento, banco de dados, redes, análises, machine learning e segurança. 

#### Modelo de Responsabilidade Compartilhada
É a divisão das responsabilidades de segurança entre a AWS e o Cliente.
A AWS é responsável pela segurança *da* Nuvem, enquanto o Cliente é responsável pela segurança *na* nuvem. Ou seja, a estrutura física, os softwares e a manutenção da nuvem são de responsabilidade da AWS, mas o Cliente deve se responsabilizar pelos acessos e configurações utilizadas dentro da nuvem.

#### Forma de Acessar a AWS
Existem 3 formas: 
[x] - Console AWS (Interface amigável online)
[x] - CLI AWS (CLI instalável da AWS)
[x] - CloudShell (CLI Online da AWS)

## A Amazon AWS

### Infraestrutura Global da AWS
Existem as Regiões da AWS -> Zonas de Disponibilidade AWS -> Zonas Locais AWS -> Wavelenght AWS

#### Regiões da AWS
São localidades ao redor do mundo nas quais estão presentes as zonas de disponibilidade.

#### Zonas de Disponibilidade AWS
São os Data Centers que estão presentes nas Regiões da AWS e servem para gerar redundancia de dados. Ficam localizadas a quilometros de distância uma das outras (para que desastres não provoquem interrupções/perdas), mas dentro de um raio de 100km (para manter a latência baixa).

#### Zonas Locais AWS
São Data Centers menores, que estão localizadas mais proximas dos clientes para manter a latência baixa, o que possibilita serviços de streaming, por exemplo.

#### Wavelenght AWS
São estruturas da AWS localizadas nas provedoras de internet móvel, como a Claro. Possibilitam que dispositivos móveis se conectem com baixa latência aos serviços da AWS.

#### AWS Outspots
São estruturas da AWS localizadas em espaços de terceiros em regiões sem Zonas Locais ou em instalações de grandes clientes.

## IAM - Identity and Access Management (Gerenciamento de Acesso e Identidade)
É um serviço da que ajuda você a controlar o acesso aos recursos da AWS de forma segura. Com o IAM, é possível gerenciar, de maneira centralizada, permissões que controlam quais recursos da AWS os usuários poderão acessar. Você usa o IAM para controlar quem é autenticado (fez login) e autorizado (tem permissões) a usar os recursos.

### Componestes do IAM
[x] - Usuários: Representam indivíduos e têm acesso aos serviços da AWS por meio de credenciais de acesso.

[x] - Grupos: São usados para gerenciar o acesso de um conjunto de usuários aos serviços da AWS.

[x] - Roles: São usadas para delegar permissões a serviços ou entidades confiáveis dentro da AWS. 
Uma role define quais ações podem ser executadas e quais recursos podem ser acessados por uma entidade que assume a função.

[x] - Policys: São usadas para definir regras de acesso aos serviços da AWS. 
As políticas podem ser anexadas a usuários, grupos ou roles e especificam quais ações são permitidas ou negadas em quais recursos.

_Chaves de Acesso:_ Access Key Id e Secret Access Key

## EC2 - Elastic Computing Cloud
Serviço de virtualização da AWS

### Virtualização
A virtualização é uma tecnologia que permite criar ambientes virtuais que simulam a execução de sistemas operacionais, aplicativos e recursos de hardware em um único servidor físico. Ela possibilita que várias máquinas virtuais (VMs) coexistam em um único hardware, o que traz benefícios como economia de espaço, energia e recursos.

### Instâncias 
São as maquinas virtuais (VMs) criadas no EC2.

### Vantagens
[x] - Controle;
[x] - Segurança;
[x] - Compatibilidade;
[x] - Baixo Custo;
[x] - Simples.

### AMI - Amazon Machine Image
São imagens de instâncias, possuem todas as configurações, aplicações e dados da instância. São usadas para permitir a criação de cópias de uma instância em outras Zona de Disponibilidade. As instâncias serão criadas a partir da imagem. As imagens podem ser públicas (disponível para todos os usuários da AWS) ou privadas (dispónivel para contas específicas).

## Storage S3
Serviços de armazenamento da AWS. 
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
[x] - HDD: Lento, para armazenamento (mais barato)
[x] - SSD: Rápido, para instâncias (mais caro)

##### Tipos de Volumes

###### Uso Geral (General Purpose)
São SSDs de baixo custo que possuem de 1GB a 16TB e IOPS máximo de 16000 por volume. 
Usados para desktops virtuais, instâncias únicas de databases (como Oracle e Microsoft SQL), aplicações interativas sensíveis à latência, volumes de inicialização e ambientes de desenvolvimento/teste. 

[x] - gp2: Cargas de trabalho com picos ocasionais de tráfego.
[x] - gp3: Desempenho consistente e melhor econômia de custos.

###### IOPS Provisionadas
São SSDs de alta performance e durabilidade, adequados para cargas de trabalho que exigem desempenho extremamente alto, latência baixa e consistência. Possuem volumes de 4GB até 16TB (com excessão do Block Express que chega a 64TB).

[x] - io2 Block Express: 
Volume SSD de maior performance criado para cargas de trabalho transacionais sensíveis à latência essenciais para os negócios.
Ideal para implantações de missão crítica maiores e mais intensivas em I/O de NoSQL e bancos de dados relacionais, como Oracle, SAP HANA, Microsoft SQL Server e SAS Analytics. 

[x] - io2: 
Volume SSD de alta performance e durabilidade criado para workloads transacionais que dependem da latência.
Bancos de dados NoSQL e relacionais com alto consumo de E/S.

[x] - io1: 
Volume SSD de alta performance criado para workloads transacionais sensíveis à latência.
Bancos de dados NoSQL e relacionais com alto consumo de E/S.

###### Otimizados para Taxa de Transferência
[x] - st1: HDD otimizada por taxa de transferência. Usado para Big data, Data warehouses e Processamento de logs. 
Tamanho de 125GB até 16TB

###### Cold HDD
[x] - sc1: Armazenamento orientado a throughput para dados acessados com pouca frequência. Possuem o menor custo.
Tamanho de 125GB até 16TB

##### Snapshot
Funcionam como backups, são utilizados para permitir que uma outra instância acesse o volume EBS.

#### S3 - Simple Storage Service
Foi o primeiro serviço oferecido pela AWS. Não possuem tamanho máximo, porém existe um limite de 5TB para o upload de um arquivo. Possui durabilidade de 99,999999999% e disponibilidade de 99,95-99,99%.

[x] - Buckets: Devem ter nome único e universal. Local onde tudo será armazenado (pastas e arquivos)

##### ACL - Access Control List
São as listas de controle de acesso (ACLs) do Amazon S3, permitem o gerenciamento do acesso aos buckets e seus objetos.

##### Classes de Armazenamento

###### S3 Standard
É a classe de armazenamento padrão do S3, projetada para alta durabilidade, disponibilidade e desempenho. É ideal para acesso frequente aos dados e é recomendada para uma ampla gama de casos de uso. Mais Cara!

###### S3 Intelligent-Tiering
É uma classe de armazenamento que usa aprendizado de máquina para analisar padrões de acesso aos dados e mover automaticamente os objetos entre as camadas de armazenamento de baixo custo e alta frequência de acesso. Essa classe é útil quando você tem dados com padrões de acesso variáveis e não deseja gerenciar manualmente a movimentação dos objetos entre camadas.

###### S3 Standard-Infrequent Access 
É uma classe de armazenamento de baixo custo adequada para dados que são acessados com menos frequência, mas quando o acesso ocorre, é necessário um desempenho rápido. É uma opção recomendada para backups, arquivos de log e dados de arquivamento. Pa

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
Permite configurar períodos para que o arquivo seja movido para outra classe de armazenamento. Possui filtros para automatizar quais pastas ou arquivos serão movidos ou pode ser aplicada a todo bucket.

##### AWS Storage Gateway
O AWS Storage Gateway é um serviço de armazenamento na nuvem híbrida que oferece acesso on-premises a armazenamento na nuvem praticamente ilimitado. Os clientes usam o Storage Gateway para simplificar o gerenciamento de armazenamento e reduzir os custos de casos de uso de armazenamento na nuvem híbrida. Ele disponibiliza uma performance de baixa latência armazenando em cache dados acessados com frequência no local e, ao mesmo tempo, armazenando dados de modo seguro e resiliente nos serviços de armazenamento na nuvem da Amazon.

### DNS - Domain Name System
Sistema responsável por converter nomes de domínio legíveis por humanos (por exemplo, www.amazon.com) em endereços IP legíveis por máquina (por exemplo, 192.0.2.44).

#### Amazon Route 53
É um serviço DNS altamente escalável que permite registrar e gerenciar domínios e direcionar o tráfego da Internet para recursos da AWS. Permite que você crie registros DNS personalizados para direcionar o tráfego de acordo com suas necessidades através de policies.

### EC2 Auto Scaling
Serviço que permite ajustar automaticamente a capacidade das instâncias do Amazon EC2 em resposta a demandas de tráfego em seus aplicativos.

#### Scaling - Escalabilidade
[x] - Scaling Up: Aumentar os recursos de uma instância (vertical)
[x] - Scaling Out: Aumentar a quantidade de um instâncias (horizontal)

#### Auto Scaling Group
Um Auto Scaling Group é um grupo lógico de instâncias do Amazon EC2 que são tratadas como uma única entidade pelo EC2 Auto Scaling. O grupo define a configuração da escala automática, como a quantidade mínima e máxima de instâncias que devem ser mantidas em execução. Ele também especifica as políticas de escalonamento que determinam quando e como as instâncias devem ser adicionadas ou removidas com base na demanda.

##### Launch Configuration
Define as configurações necessárias para criar novas instâncias quando o Auto Scaling Group precisa adicionar mais capacidade. Isso inclui informações como a AMI (Amazon Machine Image) usada para criar as instâncias, o tipo de instância, as configurações de armazenamento e as configurações de segurança.

#### ELB - Elastic Load Balancer
É um serviço de balanceamento de carga oferecido pela AWS que distribui automaticamente o tráfego de entrada entre várias instâncias do Amazon EC2 ou outros recursos da AWS, ajudando a garantir alta disponibilidade e escalabilidade para seus aplicativos.

