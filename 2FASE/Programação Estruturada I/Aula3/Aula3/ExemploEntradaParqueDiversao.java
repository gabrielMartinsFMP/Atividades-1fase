public class ExemploEntradaParqueDiversao
{
    public static void main(String[] args)
    {
        String seuNome = Teclado.leString("Nome do participante:  ");
        char primeiraLetraNome = Teclado.leChar("Primeira letra do nome");
        int idade = Teclado.leInt("Digite a idade: ");
        
        System.out.print("Olá");
        System.out.println(seuNome);
        System.out.printf("A primeira letra do seu nome é %c. \n", primeiraLetraNome);
        System.out.printf("Sua idade é: %d,", idade);
    }
}