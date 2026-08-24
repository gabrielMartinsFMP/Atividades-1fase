public class Usuario
{
    private int matricula;
    private String nome;
    private String login;
    private String senha;

    public Usuario(int mat, String nome, String log, String sen) {
        this.matricula = mat;
        this.nome = nome;
        this.login = log;
        this.senha = sen;
    }

    public int getMatricula() {
        return this.matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getLogin() {
        return this.login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getSenha() {
        return this.senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public void exibeDados(){
        System.out.println(" ");
        System.out.println("Matricula: " + matricula);
        System.out.println("Nome: "+ nome);
        System.out.println("Login: "+ login);
    }

}