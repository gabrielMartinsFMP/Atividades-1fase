
public class Pessoa
{
    // Atributos
    private String nome;
    private Data dataNascimento;

    
    // Construtor para objetos da classe Pessoa
    
    public Pessoa(String nome, Data dataNascimento)
    {
        // inicializa variáveis de instância
        this.nome = nome;
        this.dataNascimento = dataNascimento;
    }

    public String getNome()
    {
        return nome;
    }

    public void setNome(String nome)
    {
        this.nome = nome;
    }

     public String getDataNascimento()
    {
        return nome;
    }

    public void setDataNascimento(Data dataNascimento)
    {
        this.dataNascimento = dataNascimento;
    }
    
    public void exibeInformacoes()
    {
        System.out.println("O nome da pessoa é " + nome);
        System.out.println("Data de nascimento: " + dataNascimento);
    }
}