public class main
{
    public static void main(String[] args)
    {
        Computador computador1 = new Computador("Dell", "Imprision", 8);
        //Computador computador2 = new Computador("HP", "Pavilion", 16);
        //Computador computador3 = new Computador("Apple", "McBook", 32);
        
        System.out.println("Antes da modificação: ");
        computador1.exibirDados();
        System.out.println("=======");
        computador1.setMemoria(32);
        computador1.setModelo("Legion");
        computador1.exibirDados();
        System.out.println("Fim do teste");

        Automovel automovel1 = new Automovel("Chevrolet", "Astra", 2007);

        System.out.println("Antes da modificação: ");
        automovel1.exibirDados();
        System.out.println("=======");
        automovel1.setMarca("Volvo");
        automovel1.setModelo("v2");
        automovel1.setAno(2023);
        automovel1.exibirDados();
        System.out.println("Fim do teste");
        
        Imovel imovel1 = new Imovel("Ap", "35m2", 4);

        System.out.println("Antes da modificação: ");
        imovel1.exibeDados();
        System.out.println("=======");
        imovel1.setTipo("Casa");
        imovel1.setArea("50m2");
        imovel1.setQuartos(5);
        imovel1.exibeDados();
        System.out.println("Fim do teste");
    }
}