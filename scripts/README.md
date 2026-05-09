# Criação do Repositório no Kali Linux

## Criando diretório do projeto

```bash
mkdir desafio-bruteforce-medusa
```

## Entrando no diretório

```bash
cd desafio-bruteforce-medusa
```

## Inicializando repositório Git

```bash
git init
```

## Criando README principal

```bash
touch README.md
```

# Criação da Estrutura do Projeto

## Criando as pastas principais

```bash
mkdir images
mkdir wordlists
mkdir comandos
mkdir scripts
```

ou

## Criando todos os diretórios de uma vez

```bash
mkdir images wordlists comandos scripts
```

## Verificando a estrutura criada

```bash
ls
```

## Criando arquivos README.md dentro das pastas

```bash
touch images/README.md
touch wordlists/README.md
touch comandos/README.md
touch scripts/README.md
```

## Criando arquivos adicionais do projeto

### Wordlists

```bash
touch wordlists/users.txt
touch wordlists/passwords.txt
```

### Arquivo de comandos utilizados

```bash
touch comandos/comandos-utilizados.txt
```

### Script auxiliar

```bash
touch scripts/gerar_wordlist.py
```

## Verificando toda a estrutura

```bash
tree
```

## Caso o comando tree não exista

Instalar:

```bash
sudo apt install tree -y
```

## Exemplo da estrutura final

```text
desafio-bruteforce-medusa/
│
├── README.md
│
├── images/
│   └── README.md
│
├── wordlists/
│   ├── README.md
│   ├── users.txt
│   └── passwords.txt
│
├── comandos/
│   ├── README.md
│   └── comandos-utilizados.txt
│
└── scripts/
    ├── README.md
    └── gerar_wordlist.py
```

## Conectando ao GitHub

```bash
git remote add origin https://github.com/SEU-USUARIO/desafio-bruteforce-medusa.git
```

## Primeiro envio para o GitHub

```bash
git add .
git commit -m "Projeto inicial"
git push -u origin main
```

# Instalação do Ambiente do Laboratório

Este guia documenta o processo completo de preparação do ambiente utilizado no desafio de força bruta com Medusa.

O laboratório será composto por:

* Kali Linux
* Metasploitable 2
* VirtualBox

---

# Objetivo do Ambiente

O objetivo deste laboratório é criar um ambiente controlado para:

* realizar testes de força bruta;
* utilizar ferramentas de auditoria de segurança;
* praticar enumeração de serviços;
* compreender vulnerabilidades comuns em FTP, HTTP e SMB.

---

# Instalação do VirtualBox

## Download do VirtualBox

Acesse o site oficial:

[https://www.virtualbox.org/](https://www.virtualbox.org/)

## Download para Linux

Na página inicial:

1. Clique em Downloads;
2. Escolha a versão compatível com seu sistema operacional;
3. Baixe o pacote correspondente.

---

# Instalação do VirtualBox no Linux

## Debian/Ubuntu/Kali

Após baixar o arquivo:

```bash
sudo dpkg -i virtualbox-*.deb
```

## Corrigindo dependências

```bash
sudo apt --fix-broken install -y
```

## Verificando instalação

```bash
virtualbox
```

---

# Download do Kali Linux para VirtualBox

## Site oficial

[https://www.kali.org/get-kali/](https://www.kali.org/get-kali/)

## Escolhendo imagem pronta para VirtualBox

1. Acesse:

```text
Virtual Machines
```

2. Baixe:

```text
Kali Linux VirtualBox Image
```

O arquivo geralmente vem compactado em:

```text
.7z
```

---

# Extraindo o Kali Linux

## Instalando o 7zip

```bash
sudo apt install p7zip-full -y
```

## Extraindo arquivo

```bash
7z x kali-linux-*.7z
```

---

# Importando Kali Linux no VirtualBox

## Abrindo VirtualBox

```bash
virtualbox
```

## Adicionando máquina virtual

1. Clique em:

```text
Machine → Add
```

2. Selecione o arquivo:

```text
.vbox
```

3. Clique em:

```text
Open
```

A máquina Kali Linux aparecerá automaticamente.

---

# Iniciando Kali Linux

1. Selecione a VM;
2. Clique em Start.

## Credenciais padrão

```text
Usuário: kali
Senha: kali
```

---

# Atualizando Kali Linux (Opcional)

Após iniciar:

```bash
sudo apt update && sudo apt upgrade -y
```

---

# Instalação das Ferramentas do Laboratório 

Obs.: O kali ja vem com essas ferramentas em suas distibuição, entretanto esta exposto para informação

## Instalando Medusa, Nmap e SMBClient

```bash
sudo apt install medusa nmap ftp smbclient tree -y
```

## Verificando Medusa

```bash
medusa -h
```

---

# Download do Metasploitable 2

## Site oficial

[https://sourceforge.net/projects/metasploitable/](https://sourceforge.net/projects/metasploitable/)

## Arquivo esperado

```text
metasploitable-linux-2.0.0.zip
```

---

# Extraindo Metasploitable 2

## Instalando unzip

```bash
sudo apt install unzip -y
```

## Extraindo arquivo

```bash
unzip metasploitable-linux-2.0.0.zip
```

---

# Criando VM do Metasploitable 2 no VirtualBox

## Abrindo VirtualBox

```bash
virtualbox
```

## Criando nova máquina

1. Clique em:

```text
New
```

2. Nome:

```text
Metasploitable2
```

3. Tipo:

```text
Linux
```

4. Versão:

```text
Ubuntu (32-bit)
```

---

# Configuração de Memória

Recomendado:

```text
512 MB ou 1024 MB
```

Depois clique em:

```text
Create
```

---

# Configuração do Disco

## Utilizar disco existente

# Abrir Configurações da VM

1. Selecione a máquina virtual:

```text
Metasploitable2
```

2. Clique em:

```text
Settings
```

---

# Acessar Storage

No menu lateral:

```text
Storage
```

Você verá algo parecido com:

```text
Controller IDE
```

ou

```text
Controller SATA
```

---

# Adicionar Disco Virtual

1. Clique no ícone de HD:

```text
Add Hard Disk
```

2. Depois clique em:

```text
Choose Existing Disk
```

3. Selecione o arquivo:

```text
Metasploitable.vmdk
```

Esse arquivo está dentro da pasta extraída do Metasploitable 2.

---

# Confirmar Configuração

Clique em:

```text
OK
```

---

# Iniciar Máquina Virtual

Agora a VM deverá iniciar corretamente.

---

# Credenciais Padrão

```text
Usuário: msfadmin
Senha: msfadmin
```

---

# Verificando IP da Máquina

Após iniciar o sistema:

```bash
ifconfig
```

ou

```bash
ip a
```

Exemplo de IP:

```text
192.168.56.102
```

---

# Configuração de Rede das Máquinas

## Objetivo

Permitir comunicação entre:

* Kali Linux;
* Metasploitable 2.

---

# Configurando Rede no VirtualBox

## Em ambas as VMs

1. Clique em:

```text
Settings → Network
```

2. Em Adapter 1:

Escolha:

```text
Host-Only Adapter
```

---

# Iniciando Metasploitable 2

1. Selecione VM;
2. Clique em Start.

---

# Login no Metasploitable 2

## Credenciais padrão

```text
Usuário: msfadmin
Senha: msfadmin
```

---

# Descobrindo IP do Metasploitable

No terminal:

```bash
ifconfig
```

ou

```bash
ip a
```

Exemplo:

```text
192.168.56.102
```

---

# Testando Comunicação

No Kali Linux:

```bash
ping -c 3 192.168.56.102
```

# Descobrindo Serviços Ativos

## Scan com Nmap

```bash
nmap -sV 192.168.56.102
```

## Resultado esperado

```text
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
445/tcp open  microsoft-ds
```

---

# Considerações Éticas

Todos os testes deste laboratório devem ser realizados apenas em ambientes controlados e autorizados para fins educacionais.

