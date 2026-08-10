
/**
 * Escreva uma descrição da classe Computador aqui.
 * 
 * @author (seu nome) 
 * @version (um número da versão ou uma data)
 */
public class Imovel
{
    // variáveis de instância - substitua o exemplo abaixo pelo seu próprio
    private String tipo;
    private String area;
    private int quartos;

    //Construtor para objetos da classe Computador
    public Imovel(String tipo, String area, int quartos)
    {
        // inicializa variáveis de instância
        this.tipo = tipo;
        this.area = area;
        this.quartos = quartos;
    }
    
    //getters setters
    public String getTipo()
    {
        // escreva seu código aqui
        return tipo;
    }
    
    public void setTipo(String tipo)
    {
        this.tipo = tipo;
    }
    
    public String getArea()
    {
        return area;
    }
    
    public void setArea(String area)
    {
        this.area = area;
    }
    
    public int getQuartos()
    {
       return quartos; 
    }
    
    public void setQuartos(int quartos)
    {
        this.quartos = quartos;
    }
    
    public void exibeDados()
    {
        System.out.println("Tipo: " + tipo);
        System.out.println("Area: " + area);
        System.out.println("Quartos: " + quartos);
    }
}