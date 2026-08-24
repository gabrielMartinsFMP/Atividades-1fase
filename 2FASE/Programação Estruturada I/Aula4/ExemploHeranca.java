public class ExemploHeranca
{
    public static void main(String args[]){
        // Correção de parênteses e uso de leTexto para Strings
        Usuario usuario = new Usuario(
            Teclado.leInt("Informe a matricula do usuario: "),
            Teclado.leString("Informe o nome do usuario: "),
            Teclado.leString("Informe o login do usuario: "),
            Teclado.leString("Informe a senha do usuario: ")
        );

        // Corrigido de leInt para leString no nome do professor
        Professor professor = new Professor(
            Teclado.leInt("Informe a matricula do professor: "),
            Teclado.leString("Informe o nome do professor: "),
            Teclado.leString("Informe o login do professor: "),
            Teclado.leString("Informe a senha do professor: ")
        );

        // Corrigido de le para leInt na matrícula do aluno
        Aluno aluno = new Aluno(
            Teclado.leInt("Informe a matricula do aluno: "),
            Teclado.leString("Informe o nome do aluno: "),
            Teclado.leString("Informe o login do aluno: "),
            Teclado.leString("Informe a senha do aluno: ")
        );

        System.out.println(" ");
        System.out.println("Matricula do usuario: " + usuario.getMatricula());
        System.out.println("Nome do usuario: "+ usuario.getNome());
        
        System.out.println(" ");
        System.out.println("Matricula do professor: " + professor.getMatricula());
        System.out.println("Area de atuaca: "+ professor.getAreaAtuacao());

        System.out.println(" ");
        System.out.println("Matricula do aluno: " + aluno.getMatricula());
        System.out.println("Nome do aluno: "+ aluno.getNome());

        usuario.exibeDados();
        professor.exibeDados();
        aluno.exibeDados();
        
    }
}
