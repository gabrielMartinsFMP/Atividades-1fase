
/**
 * Escreva uma descrição da classe Pessoa aqui.
 * 
 * @author (seu nome) 
 * @version (um número da versão ou uma data)
 */
public class Pessoa
{
    // Atributos
    private String nome;
    private int idade;

    
    // Construtor para objetos da classe Pessoa
    
    public Pessoa(String nome, int idade)
    {
        // inicializa variáveis de instância
        this.nome = nome;
        this.idade = idade;
    }

    
    public void fazAniversario()
    {
        // escreva seu código aqui
        this.idade = this.idade + 1;
    }
    
    public void exibirDados()
    {
        System.out.println("O nome da pessoa é " + nome);
        System.out.println("A idade da pessoa é " + idade);
    }
}