public class TesteConvenio {
    public static void main(String[] args) {
        Convenio convenio = new Convenio("Top", "Muito topp");

        Paciente paciente = new Paciente("Gabriel", convenio, 2);

        paciente.exibirInformacoes();
    }
    
}