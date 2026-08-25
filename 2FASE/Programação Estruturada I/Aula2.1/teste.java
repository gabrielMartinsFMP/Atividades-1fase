public class teste
{
    public static void main(String[] args)
    {
        Data dataNascimento = new Data (12, 5, 1998);
        Pessoa pessoa = new Pessoa("Gabriel", dataNascimento);
        pessoa.exibeInformacoes();
    }
}