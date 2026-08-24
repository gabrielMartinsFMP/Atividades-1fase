
/**
 * Escreva uma descrição da classe Computador aqui.
 * 
 * @author (seu nome) 
 * @version (um número da versão ou uma data)
 */
public class Automovel
{
    // variáveis de instância - substitua o exemplo abaixo pelo seu próprio
    private String marca;
    private String modelo;
    private int ano;

    //Construtor para objetos da classe Computador
    public Automovel(String marca, String modelo, int ano)
    {
        // inicializa variáveis de instância
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }
    
    //getters setters
    public String getMarca()
    {
        // escreva seu código aqui
        return marca;
    }
    
    public void setMarca(String marca)
    {
        this.marca = marca;
    }
    
    public String getModelo()
    {
        return modelo;
    }
    
    public void setModelo(String modelo)
    {
        this.modelo = modelo;
    }
    
    public int getAno()
    {
       return ano; 
    }
    
    public void setAno(int ano)
    {
        this.ano = ano;
    }
    
    public void exibirDados()
    {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
    }
}