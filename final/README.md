# Projeto Final PDI

## Como Rodar

Para rodar o projeto é necessário utilizar o `Docker`.

### Docker - Como Instalar

```bash
curl https://get.docker.com | bash
```

#### Pos-instalação

```
sudo usermod -aG docker $USER
```

Teste sua instalação:

```bash
# Se o comando a seguir não funcionar, reinicie o seu PC e tente novamente. Se mesmo assim não funcionar, entre em contato com um manteiner do projeto
docker run hello-world
```

### Projeto

- Clone o repositório:

```bash
git clone https://github.com/bmviniciuss/pdi-2019-1
```

- Entre na pasta `final`

```bash
cd pdi-2019-1/final
```

- Dê build na imagem do `docker`

```bash
docker buill -t pdi/final .
```

- Inicie o container:

```bash
docker run -it -v $PWD:/tf/notebooks -p 8888:8888 -t pdi/final
```

- Acesse o link que está no termial utilizando o `token` de acesso
