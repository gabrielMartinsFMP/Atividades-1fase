public class Paciente {
    private String nome;
    private Convenio convenio;
    private int leito;

    public Paciente(String nome, Convenio convenio, int leito)
    {
        this.nome = nome;
        this.convenio = convenio;
        this.leito = leito;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public Convenio getConvenio(){
        return convenio;
    }

    public void setConvenio(Convenio convenio){
        this.convenio = convenio;
    }

    public int getLeito(){
        return leito;
    }

    public void setLeito(int leito){
        this.leito = leito;
    }

    public void exibirInformacoes(){
        System.out.println("Nome: " + nome);

        if (this.convenio != null){
            this.convenio.exibirInformacoes();
        }   else {
            System.out.println("Sem convenio. ");
        }
        
    }
}   

