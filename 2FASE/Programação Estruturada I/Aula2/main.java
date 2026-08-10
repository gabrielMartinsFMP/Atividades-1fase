public class main
{
    public static void main(String[] args)
    {
        Computador computador1 = new Computador("Dell", "Imprision", 8);
        Computador computador2 = new Computador("HP", "Pavilion", 16);
        Computador computador3 = new Computador("Apple", "McBook", 32);
        
        System.out.println("Antes da modificação: ");
        computador1.exibirDados();
        System.out.println("=======");
        computador1.setMemoria(32);
        computador1.setModelo("Legion");
        computador1.exibirDados();
        System.out.println("Fim do teste");
        
    }
}