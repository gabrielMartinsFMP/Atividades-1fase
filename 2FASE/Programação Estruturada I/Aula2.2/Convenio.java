public class Convenio {
    private String nome;
    private String tipo;

    public Convenio(String nome, String tipo){
        this.nome = nome;
        this.tipo = tipo;
    }

    public String getNome(){
        return nome;
    }

    public void setTipo(String tipo){
        this.tipo = tipo;
    }


    public void exibirInformacoes(){
        System.out.println("Nome do convenio: " + this.nome);
        System.out.println("Tipo do convenio: " + this.tipo);
    }
}
