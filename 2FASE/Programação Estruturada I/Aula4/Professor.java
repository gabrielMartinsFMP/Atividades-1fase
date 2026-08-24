public class Professor extends Usuario
{
    private String areaAtuacao;

    public  Professor(int mat, String nome, String log, String sen)
    {
        super(mat, nome, log, sen);
    }

    public String getAreaAtuacao(){
        return areaAtuacao;
    }

    public void setAreaAtuacao(String areaAtuacao)
    {
        this.areaAtuacao = areaAtuacao;
    }

    @Override
    public void exibeDados()
    {
        System.out.println(" ");
        System.out.println("Dados do professor: ");
        super.exibeDados();

        if(areaAtuacao !=null && !areaAtuacao.isEmpty())
            System.out.println("Area de atuacao: " + areaAtuacao);

    }
}