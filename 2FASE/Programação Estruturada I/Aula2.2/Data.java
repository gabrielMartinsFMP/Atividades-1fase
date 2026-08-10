
public class Data
{
    // Atributos
    private int dia;
    private int mes;
    private int ano;

    // Construtor para objetos da classe Pessoa
    public Data(int dia, int mes, int ano)
    {
        // inicializa variáveis de instância
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public void exibeData()
    {
        System.out.println("Dia de nascimento: " + dia);
        System.out.println("Mes de nascimento: " + mes);
        System.out.println("Ano de nascimento: " + ano);
    }
}